<script setup lang="ts">
import { computed, ref } from 'vue'
import { onSlideLeave } from '@slidev/client'
const props = withDefaults(defineProps<{ words?: boolean }>(), { words: false })
const round = ref(0)
const phase = ref(0)
const running = ref(false)
let timer: ReturnType<typeof setInterval> | undefined
const tokens = ['我', '是', '模型', '助手', '。', '<EOS>']
const ids = [201,202,203,204,205,0]
const generated = ref<string[]>([])
const finished = ref(false)
const labels = ['计算概率分布','选择下一个 Token','检查结束标记','追加到 output','追加到 input']
const lines = ['const output = [];', 'while (true) {', '  const prob = raw_model(input);', '  const token = pickToken(prob);', '  if (isOver(token)) break;', '  output.push(token);', '  input.push(token);', '}']
const activeLine = computed(() => finished.value ? 4 : phase.value+2)
const inputWords = computed(() => ['你', '是', '谁', ...generated.value.slice(0, round.value)])
const showToken = (token: string) => props.words ? token : `${ids[tokens.indexOf(token)]} · ${token}`
function pause() { clearInterval(timer); timer = undefined; running.value = false }
function next() {
  if (finished.value) return
  if (phase.value === 2 && tokens[round.value] === '<EOS>') { finished.value = true; pause(); return }
  if (phase.value === 3) generated.value.push(tokens[round.value]!)
  if (phase.value === 4) { round.value++; phase.value = 0 } else phase.value++
}
function play() { if (running.value) return pause(); if (finished.value) return; running.value = true; timer = setInterval(next, 850) }
function reset() { pause(); round.value = 0; phase.value = 0; generated.value = []; finished.value = false }
onSlideLeave(pause)
</script>
<template>
  <div class="lab autoreg" @click.stop @keydown.stop>
    <div class="lab-head"><span class="tag">教学模型 · 固定示例</span><span>第 {{ round+1 }} 次预测 · {{ finished ? '遇到 EOS，退出循环' : labels[phase] }}</span><span class="spacer" /><button :disabled="finished" @click="next">单步</button><button class="secondary" :disabled="finished" @click="play">{{ running ? '暂停' : '播放' }}</button><button class="quiet" @click="reset">重置</button></div>
    <div class="autoreg-grid">
      <div class="code-trace"><div v-for="(line,i) in lines" :key="i" :class="{ active: activeLine === i }"><span>{{ i+1 }}</span><code>{{ line }}</code></div><p class="micro">高亮行表示下一步将执行的操作。固定选择只用于解释循环。</p></div>
      <div class="token-state">
        <label>input <small>原输入 + 已反馈的输出</small></label>
        <div class="chips"><span v-for="(token,i) in inputWords" :key="i" :class="{ generated: i>2 }">{{ token }}</span></div>
        <div class="prediction"><span>raw_model</span><svg viewBox="0 0 110 28" aria-hidden="true"><path d="M2 14 H100 M90 5 L100 14 L90 23" fill="none" stroke="currentColor" stroke-width="2" /></svg><b>{{ tokens[round] }}：0.70</b><span>其他：0.30</span></div>
        <div class="picked">{{ phase >= 2 || finished ? `选中 ${showToken(tokens[round]!)}` : '等待选择…' }}</div>
        <label>output <small>只收集生成结果</small></label>
        <div class="chips output"><span v-for="(token,i) in generated" :key="i" class="generated">{{ showToken(token) }}</span><span v-if="!generated.length" class="placeholder">空数组</span></div>
        <p class="micro">{{ finished ? 'EOS 不加入 output，也不追加到 input。' : phase === 4 ? 'output 已追加；下一步把同一个 Token 反馈到 input。' : '每轮依赖更新后的上下文；实际推理可通过 KV cache 复用计算。' }}</p>
      </div>
    </div>
  </div>
</template>
