<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import { embedding, words } from '../lib/model'
import { positionEncoding } from '../lib/math'
const selected = ref(1), reversed = ref(false), positional = ref(true)
const order = computed(() => reversed.value ? [2,1,0] : [0,1,2])
const rows = computed(() => order.value.map(i => words[i]))
const e = computed(() => order.value.map(i => embedding[i]))
const p = [0,1,2].map(i => positionEncoding(i))
const x = computed(() => e.value.map((r,i) => r.map((v,j) => 2*v + (positional.value ? p[i][j] : 0))))
function reset() { selected.value=1; reversed.value=false; positional.value=true }
</script>
<template>
  <LabShell :steps="['查表取向量','注入顺序','交换词块，比较结果']" @reset="reset" v-slot="{ step }">
    <div class="controls"><label>观察位置 <select v-model.number="selected"><option v-for="(w,i) in rows" :value="i" :key="i">{{ i }} · {{ w }}</option></select></label><button @click="reversed = !reversed">交换首尾词块</button><label><input type="checkbox" v-model="positional"> 加位置编码</label></div>
    <div class="token-strip"><span v-for="(w,i) in rows" :key="w" :class="{ active: selected === i }">{{ w }} <small>位置 {{ i }}</small></span></div>
    <div class="matrix-row"><MatrixView :values="e" label="Embedding E" :rows="rows" :selected-row="selected"/><template v-if="step > 0"><span class="math-sign">×2 +</span><MatrixView :values="p" label="正弦位置编码 P" :selected-row="selected"/><span class="math-sign">=</span><MatrixView :values="x" label="输入 X" :selected-row="selected"/></template></div>
    <div class="insight">{{ step === 0 ? 'Token ID 只负责查表；表中的向量是模型参数。这里用固定教学值。' : step === 1 ? '经典论文：X = √d_model × E + P；这里 √4 = 2，同一位置相加的是同维向量。' : '交换词块后，词向量跟随词块移动，位置编码留在位置上。关掉位置编码观察差别。' }}</div>
  </LabShell>
</template>
