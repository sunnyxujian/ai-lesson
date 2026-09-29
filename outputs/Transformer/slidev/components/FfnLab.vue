<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import { encoder, ffn, words } from '../lib/model'
const row=ref(1), activate=ref(true)
const result = computed(()=>ffn(encoder.norm1,activate.value))
function reset(){row.value=1;activate.value=true}
</script>
<template>
  <LabShell :steps="['输入 4 维','线性扩张 4→8','ReLU','投影回 4 维']" @reset="reset" v-slot="{ step }">
    <div class="controls"><label>词块 <select v-model.number="row"><option v-for="(w,i) in words" :key="w" :value="i">{{ w }}</option></select></label><label><input v-model="activate" type="checkbox"> 启用 ReLU</label><span>同一组 W₁、b₁、W₂、b₂ 处理所有位置</span></div>
    <MatrixView :values="[encoder.norm1[row]]" label="输入 x · 4 维"/>
    <MatrixView v-if="step > 0" :values="[result.hidden[row], ...(step > 1 ? [result.activated[row]] : [])]" label="隐层 · 8 维" :rows="step > 1 ? ['xW₁+b₁',activate ? 'ReLU' : '恒等映射'] : ['xW₁+b₁']"/>
    <MatrixView v-if="step > 2" :values="[result.output[row]]" label="FFN 输出 · 4 维"/>
    <div class="insight">FFN 在每个位置内部加工特征；跨位置的信息交换发生在注意力中。ReLU 将负值截为 0。</div>
  </LabShell>
</template>
