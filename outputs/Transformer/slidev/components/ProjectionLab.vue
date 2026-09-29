<script setup lang="ts">
import { computed, ref } from 'vue'
import LabShell from './LabShell.vue'
import MatrixView from './MatrixView.vue'
import { input, projections, words } from '../lib/model'
import { fmt, matmul } from '../lib/math'
const row = ref(1), col = ref(0), weightRow = ref(0), kind = ref<'Q'|'K'|'V'>('Q')
const result = computed(() => matmul(input, projections[kind.value]))
function reset() { row.value=1; col.value=0; weightRow.value=0; kind.value='Q' }
</script>
<template>
  <LabShell :steps="['选择投影','逐项相乘','累加为一维','得到完整矩阵']" @reset="reset" v-slot="{ step }">
    <div class="controls"><label>词块 <select v-model.number="row"><option v-for="(w,i) in words" :key="w" :value="i">{{ w }}</option></select></label><label>角色 <select v-model="kind"><option>Q</option><option>K</option><option>V</option></select></label><span>点击 W 的单元格，选择输出列</span></div>
    <div class="matrix-row"><MatrixView :values="input" label="X" :rows="words" :selected-row="row"/><span class="math-sign">×</span><MatrixView :values="projections[kind]" :label="`W${kind}`" :tone="kind.toLowerCase()" :selected-row="weightRow" :selected-col="col" selectable @select="(i,j) => { weightRow=i; col=j }"/><span class="math-sign">=</span><MatrixView :values="result" :label="kind" :tone="kind.toLowerCase()" :selected-row="row" :selected-col="step === 3 ? -1 : col"/></div>
    <div class="equation" v-if="step > 0"><span v-for="(v,i) in input[row]" :key="i" :class="{ emphasis: i === weightRow }">{{ i ? ' + ' : '' }}{{ fmt(v) }} × {{ fmt(projections[kind][i][col]) }}</span><b v-if="step > 1"> = {{ fmt(result[row][col]) }}</b></div>
    <div class="insight">同一个 X 经三套可学习参数投影。Q / K 用来匹配，V 提供被加权的内容。</div>
  </LabShell>
</template>
