<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import ProbabilityBars from './ProbabilityBars.vue'
import { multiHead, targetInput, targetWords } from '../lib/model'
const row=ref(2), masked=ref(true)
const result=computed(()=>multiHead(targetInput,targetInput,masked.value).heads[0])
function reset(){row.value=2;masked.value=true}
</script>
<template>
  <LabShell :steps="['右移输入','屏蔽未来分数','Softmax 权重']" @reset="reset" v-slot="{ step }">
    <div class="controls"><label>输入位置 <select v-model.number="row"><option v-for="(w,i) in targetWords" :key="w" :value="i">{{ i }} · {{ w }}</option></select></label><label><input v-model="masked" type="checkbox"> 因果掩码</label><strong>这个位置预测：{{ [...targetWords.slice(1),'EOS'][row] }}</strong></div>
    <div v-if="step === 0"><div class="token-strip"><span v-for="(w,i) in targetWords" :key="w" :class="{ active: i === row, future: masked && i > row }">{{ w }}<small>输入位置 {{ i }}</small></span></div><div class="insight">输入 BOS, Can, Huolala… 对应标签 Can, Huolala, carry…；允许看当前位置，因为它已经是已知输入。</div></div>
    <div class="lab-columns" v-else><MatrixView :values="step === 1 ? result.scores : result.weights" :label="step === 1 ? '掩码后的分数 · 上三角为 −∞' : 'Softmax · 每行和为 1'" :selected-row="row" :heat="step === 2"/><div><ProbabilityBars :labels="targetWords" :values="result.weights[row]"/><p class="micro">选中查询行 {{ row }} 的分布；未来位置的权重为 0。</p></div></div>
    <div class="insight" v-if="step > 0">{{ masked ? '先将未来位置设为 −∞，再 Softmax；不是把已算出的概率简单抹掉。' : '对照实验：关闭掩码后，训练中的当前位置能偷看未来输入，造成信息泄漏。' }}</div>
  </LabShell>
</template>
