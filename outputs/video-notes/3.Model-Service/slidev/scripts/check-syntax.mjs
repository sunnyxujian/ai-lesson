import { readFileSync, readdirSync, existsSync } from 'node:fs'
import { resolve, dirname } from 'node:path'
import { parse as parseDeck } from '@slidev/parser'
import { parse, compileScript, compileTemplate } from '@vue/compiler-sfc'
import MarkdownIt from 'markdown-it'
import ts from 'typescript'
import postcss from 'postcss'

const problems = []
const fail = (where, errors) => errors.forEach(error => problems.push(`${where}: ${typeof error === 'string' ? error : error.message}`))
const markdown = readFileSync('slides.md', 'utf8')
const deck = await parseDeck(markdown, resolve('slides.md'))
const md = new MarkdownIt({ html: true })
if (deck.slides.length !== 25) problems.push(`应有 25 页，实际 ${deck.slides.length} 页`)
const reference = readFileSync('public/reference/完整教程.html', 'utf8')
let notes = 0
for (const [i, slide] of deck.slides.entries()) {
  if (slide.note?.trim()) notes++
  else problems.push(`第 ${i+1} 页缺少讲者备注`)
  if (!reference.includes(`id="section-${String(slide.frontmatter.source).padStart(2, '0')}"`)) problems.push(`第 ${i+1} 页教程章节不存在`)
  // Markdown 转为 Vue 模板后只做语法检查，不启动服务或生成站点。
  const html = md.render(slide.content)
  fail(`第 ${i+1} 页模板`, compileTemplate({ source: html, filename: `slide-${i+1}.vue`, id: `slide-${i+1}` }).errors)
}
let count = 0
for (const directory of ['components', 'layouts']) {
  for (const name of readdirSync(directory).filter(name => name.endsWith('.vue'))) {
    const filename = `${directory}/${name}`
    const { descriptor, errors } = parse(readFileSync(filename, 'utf8'), { filename })
    fail(filename, errors)
    const script = descriptor.scriptSetup ? compileScript(descriptor, { id: filename }) : undefined
    if (descriptor.template) fail(filename, compileTemplate({ source: descriptor.template.content, filename, id: filename, compilerOptions: { bindingMetadata: script?.bindings } }).errors)
    count++
  }
}
for (const match of markdown.matchAll(/^```(?:ts|js)[^\n]*\n([\s\S]*?)^```\s*$/gm)) {
  const result = ts.transpileModule(match[1], { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.ESNext }, reportDiagnostics: true })
  for (const diagnostic of result.diagnostics ?? []) problems.push(ts.flattenDiagnosticMessageText(diagnostic.messageText, '\n'))
}
postcss.parse(readFileSync('styles/theme.css', 'utf8'), { from: 'styles/theme.css' })
// 核对教程本地资源；外链和 data URL 不作为文件路径。
for (const match of reference.matchAll(/(?:src|href)=["']([^"']+)["']/g)) {
  const url = match[1]
  if (/^(?:[a-z]+:|#|\/)/i.test(url)) continue
  const target = resolve(dirname('public/reference/完整教程.html'), decodeURIComponent(url.split('#')[0]))
  if (!existsSync(target)) problems.push(`教程本地资源缺失：${url}`)
}
if (problems.length) { console.error(problems.join('\n')); process.exitCode = 1 }
else console.log(`语法检查通过：${deck.slides.length} 页、${notes} 份备注、${count} 个 Vue 文件、TS 片段、CSS 和教程资源。未运行构建或浏览器。`)
