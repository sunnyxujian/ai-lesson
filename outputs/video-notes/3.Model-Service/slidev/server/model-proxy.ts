import type { Plugin } from 'vite'
import type { IncomingMessage, ServerResponse } from 'node:http'
import type { ChatInput, ChatResult } from '../lib/contracts'

function json(res: ServerResponse, status: number, body: unknown) {
  if (res.destroyed || res.writableEnded) return
  res.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' })
  res.end(JSON.stringify(body))
}

async function readBody(req: IncomingMessage): Promise<ChatInput> {
  let size = 0
  const parts: Buffer[] = []
  for await (const chunk of req) {
    const part = Buffer.from(chunk)
    size += part.length
    if (size > 16384) throw new Error('请求过大，请缩短提示词（最多 16 KB）。')
    parts.push(part)
  }
  const value: unknown = JSON.parse(Buffer.concat(parts).toString('utf8'))
  if (!value || typeof value !== 'object') throw new Error('请求内容必须是对象。')
  const input = value as Record<string, unknown>
  if (typeof input.prompt !== 'string' || !input.prompt.trim() || input.prompt.length > 6000)
    throw new Error('用户消息需为 1–6000 个字符。')
  if (typeof input.system !== 'string' || input.system.length > 2000)
    throw new Error('系统消息最多 2000 个字符。')
  for (const [key, max] of [['temperature', 2], ['top_p', 1]] as const) {
    const v = input[key]
    if (v !== undefined && (typeof v !== 'number' || !Number.isFinite(v) || v < 0 || v > max || (key === 'top_p' && v === 0)))
      throw new Error(`${key} 参数超出本演示允许的范围。`)
  }
  return { system: input.system, prompt: input.prompt, temperature: input.temperature as number | undefined, top_p: input.top_p as number | undefined }
}

export function modelProxy(env: Record<string, string>): Plugin {
  const baseURL = env.MODEL_BASE_URL?.trim().replace(/\/+$/, '') ?? ''
  const key = env.MODEL_API_KEY?.trim() ?? ''
  const model = env.MODEL_NAME?.trim() ?? ''
  const missing = ['MODEL_BASE_URL', 'MODEL_API_KEY', 'MODEL_NAME'].filter(name => !env[name]?.trim())
  let busy = false
  // 只在服务端保存凭据；错误信息也需要移除上游可能回显的凭据。
  const redact = (value: string) => (key ? value.split(key).join('[REDACTED]') : value).replace(/Bearer\s+[^\s"']+/gi, 'Bearer [REDACTED]').slice(0, 600)
  return {
    name: 'model-service-local-proxy',
    configureServer(server) {
      server.middlewares.use(async (req, res, next) => {
        const path = req.url?.split('?')[0]
        if (path !== '/api/demo/config' && path !== '/api/demo/chat') return next()
        // 仅允许本机同源访问，防止其他网页借本地代理发出付费请求。
        const host = req.headers.host ?? ''
        if (!/^(127\.0\.0\.1|localhost)(:\d+)?$/.test(host)) return json(res, 403, { error: '仅支持本机访问。' })
        if (req.headers.origin && req.headers.origin !== `http://${host}`) return json(res, 403, { error: '仅支持同源访问。' })
        if (req.headers['sec-fetch-site'] === 'cross-site') return json(res, 403, { error: '仅支持同源访问。' })
        if (path === '/api/demo/config') {
          if (req.method !== 'GET') return json(res, 405, { error: '请使用 GET。' })
          return json(res, 200, { ready: missing.length === 0, missing, baseURL, model })
        }
        if (req.method !== 'POST') return json(res, 405, { error: '请使用 POST。' })
        if (!req.headers['content-type']?.startsWith('application/json')) return json(res, 415, { error: '请发送 JSON。' })
        if (missing.length) return json(res, 503, { error: `配置未完成：${missing.join('、')}。填写 .env.local 后重启 pnpm dev。` })
        if (busy) return json(res, 409, { error: '已有请求正在执行，请等待或取消。' })
        let input: ChatInput
        try { input = await readBody(req) }
        catch (error) { return json(res, 400, { error: error instanceof SyntaxError ? 'JSON 格式错误。' : (error as Error).message }) }
        if (busy) return json(res, 409, { error: '已有请求正在执行。' })
        busy = true
        const controller = new AbortController()
        let timedOut = false
        const timeout = setTimeout(() => { timedOut = true; controller.abort() }, 60000)
        const cancel = () => controller.abort()
        res.on('close', cancel)
        const start = performance.now()
        try {
          const endpoint = new URL(`${baseURL}/chat/completions`)
          if (endpoint.protocol !== 'https:' || endpoint.username || endpoint.password) throw new Error('invalid-config')
          const messages = [
            ...(input.system.trim() ? [{ role: 'system', content: input.system }] : []),
            { role: 'user', content: input.prompt },
          ]
          const upstream = await fetch(endpoint, {
            method: 'POST', redirect: 'error', signal: controller.signal,
            headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
            body: JSON.stringify({ model, messages, stream: false, ...(input.temperature !== undefined ? { temperature: input.temperature } : {}), ...(input.top_p !== undefined ? { top_p: input.top_p } : {}) }),
          })
          const data = await upstream.json().catch(() => null)
          if (!upstream.ok) {
            const message = typeof data?.error?.message === 'string' ? redact(data.error.message) : '上游请求失败，请检查服务配置与参数支持情况。'
            return json(res, upstream.status, { error: `百炼 HTTP ${upstream.status}：${message}` })
          }
          const choice = data?.choices?.[0]
          if (typeof choice?.message?.content !== 'string') return json(res, 502, { error: '接口未返回可显示的文本 content；请检查模型是否支持当前文本对话格式。' })
          const usage = data?.usage
          const number = (value: unknown) => typeof value === 'number' && Number.isFinite(value) && value >= 0 ? value : undefined
          const result: ChatResult = {
            text: choice.message.content,
            model: typeof data.model === 'string' ? data.model : model,
            elapsedMs: Math.round(performance.now() - start),
            finishReason: typeof choice.finish_reason === 'string' ? choice.finish_reason : undefined,
            usage: usage ? { prompt_tokens: number(usage.prompt_tokens), completion_tokens: number(usage.completion_tokens), total_tokens: number(usage.total_tokens) } : undefined,
          }
          json(res, 200, result)
        }
        catch {
          json(res, timedOut ? 504 : 502, { error: timedOut ? '请求超过 60 秒，已中止本地等待。' : controller.signal.aborted ? '请求已取消。' : '连接或响应解析失败，请检查服务地址、模型名称及网络。' })
        }
        finally {
          clearTimeout(timeout)
          res.off('close', cancel)
          busy = false
        }
      })
    },
  }
}
