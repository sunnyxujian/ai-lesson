<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import ProbabilityBars from './ProbabilityBars.vue'
import { attention, fmt, matmul } from '../lib/math'
import { input, projections, words } from '../lib/model'
withDefaults(defineProps<{ start?: number }>(), { start: 0 })
const initial = () => ({ Q: matmul(input, projections.Q), K: matmul(input, projections.K), V: matmul(input, projections.V) })
const matrices = ref(initial()), kind = ref<'Q'|'K'|'V'>('Q'), query = ref(1), row = ref(1), col = ref(0), scaled = ref(true)
const a = computed(() => attention(matrices.value.Q, matrices.value.K, matrices.value.V, scaled.value))
const value = computed({ get: () => matrices.value[kind.value][row.value][col.value], set: v => { if (Number.isFinite(v)) matrices.value[kind.value][row.value][col.value] = v } })
const parts = computed(() => matrices.value.V.map((r,j) => r.map(x => x*a.value.weights[query.value][j])))
const exponentials = computed(() => { const r=a.value.scores[query.value], max=Math.max(...r); return r.map(v => Math.exp(v-max)) })
function reset() { matrices.value=initial(); kind.value='Q'; query.value=1; row.value=1; col.value=0; scaled.value=true }
</script>
<template>
  <LabShell :steps="['点积分数','缩放','Softmax','加权 V','输出向量']" :start="start" label="真实计算 · 单头 dₖ = dᵥ = 4" @reset="reset" v-slot="{ step }">
    <div class="controls"><label>查询 <select v-model.number="query"><option v-for="(w,i) in words" :key="w" :value="i">{{ w }}</option></select></label><label>编辑 <select v-model="kind"><option>Q</option><option>K</option><option>V</option></select></label><label><input v-model="scaled" type="checkbox"> ÷ √4</label><label>选中值 <input v-model.number="value" type="range" min="-5" max="5" step="0.1"><output>{{ fmt(value) }}</output></label></div>
    <div class="lab-columns"><div><MatrixView :values="matrices[kind]" :label="`${kind} · 点击数值后拖动滑块`" :tone="kind.toLowerCase()" :selected-row="row" :selected-col="col" selectable @select="(i,j) => {row=i; col=j}"/><p class="micro">编辑行 {{ row+1 }}，列 {{ col+1 }}；查询高亮行独立选择。</p></div>
      <div class="result-panel" :key="step">
        <MatrixView v-if="step === 0" :values="a.raw" label="QKᵀ" :rows="words" :cols="words" :selected-row="query"/>
        <template v-else-if="step === 1"><MatrixView :values="[a.raw[query], a.scores[query]]" label="分数缩放对照" :rows="['原始','缩放后']" :cols="words"/><p class="micro">当前除数 {{ scaled ? '√4 = 2' : '1（关闭标准缩放）' }}</p></template>
        <template v-else-if="step === 2"><ProbabilityBars :labels="words" :values="a.weights[query]"/><p class="micro">exp(s − max) = [{{ exponentials.map(x=>fmt(x,4)).join(', ') }}]</p><p class="micro">权重和 = {{ a.weights[query].reduce((s,v)=>s+v,0).toFixed(6) }}</p></template>
        <MatrixView v-else-if="step === 3" :values="parts" label="每一行：aⱼ × Vⱼ" :rows="words"/>
        <template v-else><MatrixView :values="a.output" label="H = AV" :rows="words" :selected-row="query"/><p class="micro">H{{ query+1 }} = 各个加权 V 的逐维和</p></template>
      </div>
    </div>
    <div class="insight">{{ step < 2 ? '每一行是一个查询，每一列是一个被参考的位置。改变 Q/K 会改变匹配分数。' : step === 2 ? 'Softmax 沿行归一化。缩放用于控制分数尺度，不会改变该行分数的排序。' : '试着只改 V：权重保持不变，但输出变化。注意力分配与提取内容是两件事。' }}</div>
  </LabShell>
</template>
