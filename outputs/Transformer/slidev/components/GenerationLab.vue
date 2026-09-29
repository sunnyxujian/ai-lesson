<script setup lang="ts">
import LabShell from './LabShell.vue'
import ProbabilityBars from './ProbabilityBars.vue'
import ArchitectureMap from './ArchitectureMap.vue'
import { generationScript, vocabulary } from '../lib/model'
import { softmax } from '../lib/math'
const phases=['读取前缀','解码器加工','词表概率','选择并追加']
const steps=generationScript.flatMap(s=>phases.map(p=>`${p} · ${s.token}`))
const index=(s:number)=>Math.floor(s/4)
const prefix=(s:number)=>['BOS',...generationScript.slice(0,index(s)+(s%4===3?1:0)).map(x=>x.token)]
</script>
<template>
  <LabShell :steps="steps" label="教学脚本 · 预设 logits → 真实 Softmax" v-slot="{ step }">
    <div class="token-strip generation"><span v-for="(word,i) in prefix(step)" :key="i" :class="{ active: i === prefix(step).length-1 }">{{ word }}</span></div>
    <div class="lab-columns generation-columns"><ArchitectureMap :active="[5,8,10,10][step%4]" compact/><div v-if="step%4 >= 2"><ProbabilityBars :labels="vocabulary" :values="softmax(generationScript[index(step)].logits)" :highlight="step%4 === 3 ? index(step) : -1"/></div><div v-else class="generation-caption"><p>{{ step%4 === 0 ? '已有前缀作为输入' : '带掩码自注意力 → 交叉注意力 → FFN' }}</p><small>流程高亮仅说明机制；下面的语言路径来自教学脚本。</small></div></div>
    <div class="insight">{{ step === steps.length-1 ? '生成 EOS，序列结束。这里使用贪心选择；真实任务还可采用其他解码策略。' : step%4 === 3 ? `选中 ${generationScript[index(step)].token} 并追加；下一轮以前缀的新状态继续。` : '预设路径：Can Huolala carry a Labrador?；此页不使用未训练小模型的 logits。' }}</div>
  </LabShell>
</template>
