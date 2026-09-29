<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import ProbabilityBars from './ProbabilityBars.vue'
import { decoderLayer, targetWords, words } from '../lib/model'
const row=ref(2), head=ref(0)
const decoder = decoderLayer()
const result = computed(()=>decoder.cross.heads[head.value])
function reset(){row.value=2;head.value=0}
</script>
<template>
  <LabShell :steps="['Q 来自目标侧','K/V 来自源句','跨序列匹配','融合源句内容']" @reset="reset" v-slot="{ step }">
    <div class="controls"><label>目标输入 <select v-model.number="row"><option v-for="(w,i) in targetWords" :key="w" :value="i">{{ w }}</option></select></label><label>头 <select v-model.number="head"><option :value="0">头 1</option><option :value="1">头 2</option></select></label></div>
    <div class="matrix-row" v-if="step < 2"><MatrixView :values="[result.Q[row]]" label="Q · 目标侧投影" tone="q"/><span class="math-sign">→</span><MatrixView v-if="step > 0" :values="result.K" label="K · 编码器输出投影" tone="k" :rows="words"/><MatrixView v-if="step > 0" :values="result.V" label="V · 编码器输出投影" tone="v" :rows="words"/></div>
    <div class="lab-columns" v-else><MatrixView :values="result.weights" label="跨序列权重 · 7×3" :selected-row="row" heat/><div><ProbabilityBars :values="result.weights[row]" :labels="words"/><MatrixView v-if="step > 2" :values="[result.output[row]]" label="当前头的输出 · 2 维"/></div></div>
    <div class="insight">源句已完整给出，可关注全部中文位置。这里的热力图由未训练的教学矩阵算出，不代表真实翻译对齐。</div>
  </LabShell>
</template>
