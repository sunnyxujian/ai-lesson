<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import ProbabilityBars from './ProbabilityBars.vue'
import { fmt } from '../lib/math'
import { targetWords, vocabulary, vocabularyOutput } from '../lib/model'
const row=ref(2), result=computed(()=>vocabularyOutput(row.value))
</script>
<template><LabShell :steps="['隐藏表示','词表投影','概率分布']" @reset="row=2" v-slot="{ step }">
  <div class="controls"><label>目标输入位置 <select v-model.number="row"><option v-for="(w,i) in targetWords" :key="w" :value="i">{{ w }}</option></select></label><span>教学词表大小 |V| = 9</span></div>
  <div class="lab-columns"><div><MatrixView :values="[result.hidden]" label="解码器输出 h · 1×4"/><p class="equation" v-if="step > 0">h × W_vocab → logits<br>1×4 · 4×9 → 1×9</p><p class="micro">未训练的固定参数：此处最高概率词未必是正确译文。</p></div><ProbabilityBars v-if="step === 2" :labels="vocabulary" :values="result.probabilities"/><div v-else-if="step === 1" class="logit-grid"><div v-for="(token,i) in vocabulary" :key="token"><span>{{ token }}</span><b>{{ fmt(result.logits[i],3) }}</b></div></div></div>
</LabShell></template>
