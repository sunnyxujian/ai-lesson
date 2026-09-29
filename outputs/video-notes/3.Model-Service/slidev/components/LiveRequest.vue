<script setup lang="ts">
import { computed, ref } from 'vue'
import { onSlideEnter, onSlideLeave } from '@slidev/client'
import { liveBusy, liveState } from '../lib/live-session'
import type { ChatInput, ChatResult, ModelConfig } from '../lib/contracts'
const props = withDefaults(defineProps<{ compare?: boolean }>(), { compare: false })
const config = ref<ModelConfig>({ ready: false, missing: [], baseURL: '', model: '' })
const status = ref('进入本页后读取本地配置。')
const enabled = ref(false)
const parameter = ref<'temperature' | 'top_p'>('temperature')
const a = ref(0.2)
const b = ref(1.2)
const ownBusy = ref(false)
const selected = ref('A')
const view = ref<'response' | 'request'>('response')
let controller: AbortController | undefined
let configController: AbortController | undefined
const recordKey = (slot: string) => props.compare ? slot : 'single'
const record = computed(() => liveState.records[recordKey(selected.value)])
const differentMessages = computed(() => {
  const a = liveState.records.A?.request
  const b = liveState.records.B?.request
  return props.compare && a && b && (a.system !== b.system || a.prompt !== b.prompt)
})
const input = (slot: string): ChatInput => ({
  system: liveState.system, prompt: liveState.prompt,
  ...(enabled.value ? { [parameter.value]: slot === 'A' ? a.value : b.value } : {}),
})
const preview = computed(() => {
  const snapshot = record.value?.request ?? input(selected.value)
  return JSON.stringify({
    model: record.value?.model || config.value.model || '<MODEL_NAME>',
    messages: [...(snapshot.system.trim() ? [{ role: 'system', content: snapshot.system }] : []), { role: 'user', content: snapshot.prompt }],
    stream: false,
    ...(snapshot.temperature !== undefined ? { temperature: snapshot.temperature } : {}),
    ...(snapshot.top_p !== undefined ? { top_p: snapshot.top_p } : {}),
  }, null, 2)
})
async function refresh() {
  configController?.abort()
  configController = new AbortController()
  try {
    const response = await fetch('/api/demo/config', { signal: configController.signal })
    if (!response.ok) throw new Error()
    config.value = await response.json()
    status.value = config.value.ready ? `已配置：${config.value.model}` : `待填写：${config.value.missing.join('、')}；保存后重启 pnpm dev。`
  } catch { status.value = '无法读取本地代理配置，请通过 pnpm dev 打开演示稿。' }
}
onSlideEnter(refresh)
function cancel() { controller?.abort() }
onSlideLeave(() => { cancel(); configController?.abort() })
async function send(slot: string) {
  if (liveBusy.value || !config.value.ready || !liveState.prompt.trim()) return
  selected.value = slot
  view.value = 'response'
  const snapshot = { ...input(slot) }
  const run = { request: snapshot, at: new Date().toLocaleTimeString(), model: config.value.model }
  const key = recordKey(slot)
  liveState.records[key] = run
  liveBusy.value = true
  ownBusy.value = true
  controller = new AbortController()
  let timeout = false
  const timer = setTimeout(() => { timeout = true; controller?.abort() }, 65000)
  try {
    const response = await fetch('/api/demo/chat', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(snapshot), signal: controller.signal })
    const data = await response.json()
    if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`)
    liveState.records[key] = { ...run, result: data as ChatResult }
  } catch (error) {
    liveState.records[key] = { ...run, error: controller.signal.aborted ? timeout ? '请求超时。' : '已取消本地请求；上游可能已产生用量。' : error instanceof Error ? error.message : '请求失败。' }
  } finally { clearTimeout(timer); liveBusy.value = false; ownBusy.value = false; controller = undefined }
}
function switchParameter() {
  a.value = parameter.value === 'temperature' ? 0.2 : 0.5
  b.value = parameter.value === 'temperature' ? 1.2 : 0.95
}
</script>

<template>
  <div class="lab live-lab" @click.stop @keydown.stop>
    <div class="lab-head"><span class="tag real">真实 API · 百炼</span><span class="muted status">{{ status }}</span><button class="quiet" :disabled="liveBusy" @click="refresh">刷新配置</button></div>
    <p v-if="differentMessages" class="micro comparison-note">A / B 的消息内容不同，请检查快照；当前记录不能只归因于参数差异。</p>
    <div class="live-grid">
      <div>
        <label>system<textarea v-model="liveState.system" rows="1" maxlength="2000" :disabled="liveBusy" aria-label="系统消息" /></label>
        <label>user<textarea v-model="liveState.prompt" rows="3" maxlength="6000" :disabled="liveBusy" aria-label="用户消息" /></label>
        <div class="row"><label class="inline"><input v-model="enabled" type="checkbox" :disabled="liveBusy" />显式传入采样参数</label></div>
        <div v-if="enabled" class="row parameters">
          <select v-model="parameter" :disabled="liveBusy" aria-label="对照参数" @change="switchParameter"><option>temperature</option><option>top_p</option></select>
          <label class="inline">A <input v-model.number="a" type="number" :min="parameter === 'top_p' ? 0.01 : 0" :max="parameter === 'top_p' ? 1 : 2" step="0.05" :disabled="liveBusy" /></label>
          <label v-if="compare" class="inline">B <input v-model.number="b" type="number" :min="parameter === 'top_p' ? 0.01 : 0" :max="parameter === 'top_p' ? 1 : 2" step="0.05" :disabled="liveBusy" /></label>
        </div>
        <p v-else class="micro">参数省略：使用服务商默认值。</p>
        <div class="row">
          <button :disabled="!config.ready || liveBusy || !liveState.prompt.trim()" @click="send('A')">{{ compare ? '发送 A' : '发送请求' }}</button>
          <button v-if="compare" :disabled="!config.ready || liveBusy || !liveState.prompt.trim()" @click="send('B')">发送 B</button>
          <button v-if="ownBusy" class="secondary" @click="cancel">取消</button>
        </div>
        <p class="micro">手动发送才调用模型。参数支持范围以所选模型为准。</p>
      </div>
      <div class="result-pane">
        <div class="row tabs">
          <template v-if="compare"><button v-for="slot in ['A','B']" :key="slot" :disabled="ownBusy" :class="selected === slot ? '' : 'secondary'" @click="selected = slot">记录 {{ slot }}</button></template>
          <button class="quiet" @click="view = view === 'response' ? 'request' : 'response'">{{ view === 'response' ? '查看请求快照' : '查看回复' }}</button>
        </div>
        <template v-if="view === 'request'"><p class="micro">{{ record ? '已发送快照' : '待发送预览' }} · Authorization: Bearer [服务端凭据]</p><pre class="response-code">{{ preview }}</pre></template>
        <template v-else>
          <div v-if="ownBusy && !record?.result && !record?.error" class="waiting">请求中，等待真实模型回复…</div>
          <p v-else-if="record?.error" role="alert" class="error">{{ record.error }}</p>
          <div v-else-if="record?.result" class="response-text">{{ record.result.text }}</div>
          <div v-else class="empty">{{ compare ? '使用相同消息，分别发送 A / B，再切换记录比较。' : '填写本地环境变量后，点击发送查看真实回复。' }}<br />这里不会用模拟回复替代真实结果。</div>
          <div v-if="record?.result" class="metrics"><span>{{ record.result.elapsedMs }} ms</span><span>输入 {{ record.result.usage?.prompt_tokens ?? '未提供' }}</span><span>输出 {{ record.result.usage?.completion_tokens ?? '未提供' }}</span><span>总计 {{ record.result.usage?.total_tokens ?? '未提供' }}</span></div>
          <p v-if="record" class="micro">{{ record.at }} · {{ record.model }} · {{ record.request.temperature !== undefined ? `temperature=${record.request.temperature}` : record.request.top_p !== undefined ? `top_p=${record.request.top_p}` : '默认参数' }}</p>
        </template>
      </div>
    </div>
  </div>
</template>
