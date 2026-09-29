<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import { input, multiHead, outputProjection, words } from '../lib/model'
const selected = ref(0), query = ref(1), gain = ref(1)
const result = computed(() => multiHead(input.map((r,i) => r.map(v => v*(i === query.value ? gain.value : 1)))))
function reset() { selected.value=0; query.value=1; gain.value=1 }
</script>
<template>
  <LabShell :steps="['独立投影','不同权重','各头输出','拼接','输出投影']" @reset="reset" v-slot="{ step }">
    <div class="controls"><label>头 <select v-model.number="selected"><option :value="0">头 1</option><option :value="1">头 2</option></select></label><label>词块 <select v-model.number="query"><option v-for="(w,i) in words" :key="w" :value="i">{{ w }}</option></select></label><label>该词输入倍率 <input v-model.number="gain" type="range" min="0.2" max="2" step="0.1">{{ gain.toFixed(1) }}</label></div>
    <div class="matrix-row" v-if="step === 0"><MatrixView :values="result.heads[selected].Q" label="Q · 3×2" tone="q" :selected-row="query"/><MatrixView :values="result.heads[selected].K" label="K · 3×2" tone="k"/><MatrixView :values="result.heads[selected].V" label="V · 3×2" tone="v"/></div>
    <div class="matrix-row" v-else-if="step === 1"><MatrixView v-for="(h,i) in result.heads" :key="i" :values="h.weights" :label="`头 ${i+1} 的注意力`" :selected-row="query" heat/></div>
    <div class="matrix-row" v-else-if="step === 2"><MatrixView v-for="(h,i) in result.heads" :key="i" :values="h.output" :label="`头 ${i+1} · 3×2 输出`" :selected-row="query"/></div>
    <div class="matrix-row" v-else-if="step === 3"><MatrixView :values="[result.heads[0].output[query]]" label="头 1"/><span class="math-sign">⊕</span><MatrixView :values="[result.heads[1].output[query]]" label="头 2"/><span class="math-sign">→</span><MatrixView :values="[result.concat[query]]" label="Concat · 4 维"/></div>
    <div class="matrix-row" v-else><MatrixView :values="result.concat" label="Concat" :selected-row="query"/><span class="math-sign">×</span><MatrixView :values="outputProjection" label="Wᴼ · 4×4"/><span class="math-sign">=</span><MatrixView :values="result.output" label="MHA 输出" :selected-row="query"/></div>
    <div class="insight">每头使用自己的 WQ、WK、WV；头的关注模式由参数决定，不预设固定的“语法头”或“语义头”。</div>
  </LabShell>
</template>
