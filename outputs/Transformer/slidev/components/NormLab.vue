<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import { encoder, input, words } from '../lib/model'
import { fmt, layerNorm } from '../lib/math'
const props = withDefaults(defineProps<{ start?: number }>(), { start: 0 })
const row=ref(1), gain=ref(1), gamma=ref(1), beta=ref(0)
const sub = computed(() => encoder.att.output[row.value].map(v=>v*gain.value))
const sum = computed(() => input[row.value].map((v,j)=>v+sub.value[j]))
const norm = computed(() => layerNorm(sum.value,gamma.value,beta.value))
function reset() { row.value=1; gain.value=1; gamma.value=1; beta.value=0 }
</script>
<template>
  <LabShell :steps="['输入与子层输出','残差相加','按特征标准化','可学习缩放与平移']" :start="props.start" @reset="reset" v-slot="{ step }">
    <div class="controls"><label>词块 <select v-model.number="row"><option v-for="(w,i) in words" :key="w" :value="i">{{ w }}</option></select></label><label>子层倍率 <input v-model.number="gain" type="range" min="0" max="2" step="0.1">{{ gain.toFixed(1) }}</label><label>γ <input v-model.number="gamma" type="range" min="0" max="2" step="0.1">{{ gamma.toFixed(1) }}</label><label>β <input v-model.number="beta" type="range" min="-1" max="1" step="0.1">{{ beta.toFixed(1) }}</label></div>
    <div class="matrix-row"><MatrixView :values="[input[row]]" label="X"/><span class="math-sign">+</span><MatrixView :values="[sub]" label="子层输出"/><template v-if="step > 0"><span class="math-sign">=</span><MatrixView :values="[sum]" label="残差和 R"/></template></div>
    <div class="matrix-row" v-if="step > 1"><div class="stats"><span>μ = {{ fmt(norm.mean,3) }}</span><span>σ² = {{ fmt(norm.variance,3) }}</span></div><MatrixView :values="[norm.z]" label="z = (R − μ) / √(σ² + ε)"/><MatrixView v-if="step > 2" :values="[norm.output]" label="γz + β"/></div>
    <div class="insight">{{ step < 2 ? '残差让原始表示直接进入下一步；将子层倍率设为 0，观察相加结果。' : 'LayerNorm 对一个 Token 的所有特征求均值与方差，不跨 Token；结果可以为负，也可以大于 1。' }}</div>
    <p class="micro" v-if="step > 2">此处用标量 γ/β 同时控制四维；真实 LayerNorm 通常为每个特征学习独立 γ/β。</p>
  </LabShell>
</template>
