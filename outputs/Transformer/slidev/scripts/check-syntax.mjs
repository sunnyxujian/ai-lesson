import { readFile, readdir, access } from 'node:fs/promises'
import { dirname, join, resolve, extname } from 'node:path'
import { fileURLToPath } from 'node:url'
import { parseSync, resolveConfig } from '@slidev/parser'
import { parse, compileScript, compileTemplate, compileStyle } from '@vue/compiler-sfc'
import MarkdownIt from 'markdown-it'
import katex from 'katex'
import postcss from 'postcss'
import ts from 'typescript'

// 静态解析检查，不启动 Vite 服务，不运行构建，也不执行教学计算。
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const failures = []
const check = (condition, message) => { if (!condition) failures.push(message) }
const report = (label, errors) => errors.forEach(error => failures.push(`${label}: ${typeof error === 'string' ? error : error.message}`))
async function exists(path) { try { await access(path); return true } catch { return false } }
async function files(dir) {
  const result = []
  for (const entry of await readdir(join(root, dir), { withFileTypes: true })) {
    const path = join(dir, entry.name)
    if (entry.isDirectory()) result.push(...await files(path))
    else result.push(path)
  }
  return result
}
const vueFiles = [...await files('components'), 'global-bottom.vue'].filter(p => p.endsWith('.vue'))
const componentNames = new Set(vueFiles.map(p => p.split('/').at(-1).replace('.vue', '')))
const markdown = new MarkdownIt({ html: true })
let formulas = 0
function validateFormula(formula, label, displayMode) {
  try { katex.renderToString(formula, { throwOnError: true, displayMode }) }
  catch (error) { failures.push(`${label}: ${error.message}`) }
  formulas++
}
async function validateResource(href, label) {
  if (/^(https?:|data:|#|mailto:)/.test(href)) return
  const resource = href.split(/[?#]/)[0]
  const path = resource.startsWith('/') ? join(root, 'public', resource.slice(1)) : resolve(root, resource.replace(/^@\//, ''))
  check(await exists(path), `${label}: 本地引用不存在 ${href}`)
}
function checkTs(source, label) {
  const result = ts.transpileModule(source, { fileName: label, reportDiagnostics: true, compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext, isolatedModules: true } })
  for (const diagnostic of result.diagnostics ?? []) {
    if (diagnostic.category === ts.DiagnosticCategory.Error) failures.push(`${label}: ${ts.flattenDiagnosticMessageText(diagnostic.messageText, '\n')}`)
  }
}
function checkComponents(template, label) {
  for (const [, component] of template.matchAll(/<([A-Z][\w]*)\b/g)) check(componentNames.has(component), `${label}: 未找到自定义组件 ${component}`)
}
const content = await readFile(join(root, 'slides.md'), 'utf8')
const deck = parseSync(content, join(root, 'slides.md'))
check(deck.slides.length === 32, `预期 32 页，实际 ${deck.slides.length} 页`)
resolveConfig(deck.slides[0].frontmatter)
await validateResource(deck.slides[0].frontmatter.favicon, 'favicon')
for (const [index, slide] of deck.slides.entries()) {
  const label = `slides.md 第 ${index+1} 页`
  check(Boolean(slide.note?.trim()), `${label}: 缺少讲者备注`)
  let body = slide.content
  // 保留代码导入的路径检查，并将片段作为普通 fenced code 交给 Markdown 解析。
  for (const match of [...body.matchAll(/^<<<\s+(\S+)(?:[^\n]*)/gm)]) {
    const path = match[1]
    await validateResource(path, label)
    if (await exists(resolve(root, path.replace(/^@\//, '')))) {
      const snippet = await readFile(resolve(root, path.replace(/^@\//, '')), 'utf8')
      body = body.replace(match[0], `\n\`\`\`ts\n${snippet}\n\`\`\`\n`)
    }
  }
  body = body.replace(/\$\$([\s\S]*?)\$\$/g, (_, formula) => { validateFormula(formula, label, true); return '<div class="math-static-placeholder"></div>' })
  body = body.replace(/\$([^$\n]+)\$/g, (_, formula) => { validateFormula(formula, label, false); return '<span class="math-static-placeholder"></span>' })
  for (const [, href] of body.matchAll(/(?:src|href)="([^"]+)"/g)) await validateResource(href, label)
  for (const [, href] of body.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)) await validateResource(href, label)
  checkComponents(body, label)
  const html = markdown.render(body).replace(/<pre>/g, '<pre v-pre>')
  const parsed = compileTemplate({ source: `<div>${html}</div>`, filename: `${index+1}.vue`, id: `slide-${index+1}` })
  report(label, parsed.errors)
}
for (const path of vueFiles) {
  const source = await readFile(join(root, path), 'utf8')
  const { descriptor, errors } = parse(source, { filename: path })
  report(path, errors)
  let script
  if (descriptor.script || descriptor.scriptSetup) {
    try { script = compileScript(descriptor, { id: path }); checkTs(script.content, path+'.ts') }
    catch (error) { failures.push(`${path}: ${error.message}`) }
  }
  if (descriptor.template) {
    checkComponents(descriptor.template.content, path)
    report(path, compileTemplate({ source: descriptor.template.content, filename: path, id: path, compilerOptions: { bindingMetadata: script?.bindings } }).errors)
  }
  for (const style of descriptor.styles) report(path, compileStyle({ source: style.content, filename: path, id: path }).errors)
}
for (const path of [...await files('lib'), ...await files('snippets')]) if (extname(path) === '.ts') checkTs(await readFile(join(root, path), 'utf8'), path)
for (const path of await files('styles')) {
  if (extname(path) !== '.css') continue
  try { postcss.parse(await readFile(join(root, path), 'utf8'), { from: path }) }
  catch (error) { failures.push(`${path}: ${error.message}`) }
}
if (failures.length) { console.error(failures.join('\n')); process.exitCode=1 }
else console.log(`静态解析通过：${deck.slides.length} 页及讲者备注，${vueFiles.length} 个 Vue 文件，${formulas} 组公式；组件、代码与本地资源引用有效。`)
