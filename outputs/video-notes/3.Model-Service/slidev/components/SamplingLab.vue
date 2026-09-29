<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { baseProbabilities as base, candidates, normalize, retainedIndices, sample, temperatureDistribution } from '../lib/sampling'
const props = defineProps<{ mode: 'temperature' | 'top_k' | 'top_p' }>()
const value = ref(props.mode === 'temperature' ? 1 : props.mode === 'top_k' ? 3 : 0.8)
const counts = ref([0,0,0,0,0])
const chosen = ref(-1)
const kept = computed(() => props.mode === 'temperature' ? [0,1,2,3,4] : retainedIndices(base, props.mode, value.value))
const probabilities = computed(() => props.mode === 'temperature' ? temperatureDistribution(base, value.value) : normalize(base.map((v, i) => kept.value.includes(i) ? v : 0)))
const total = computed(() => counts.value.reduce((a,b) => a+b,0))
const cumulative = base.map((_, i) => base.slice(0, i+1).reduce((a,b) => a+b,0))
function reset() { counts.value = [0,0,0,0,0]; chosen.value = -1 }
watch(value, reset)
function draw(n: number) { for (let i=0;i<n;i++) { chosen.value = sample(probabilities.value); counts.value[chosen.value]!++ } }
const percent = (v: number) => `${(v*100).toFixed(1)}%`
</script>
<template>
  <div class="lab sampling-lab" @click.stop @keydown.stop>
    <div class="lab-head"><span class="tag">教学计算 · 非模型内部数据</span><span class="muted">原始分布：0.30 / 0.25 / 0.20 / 0.15 / 0.10</span></div>
    <div class="slider-line"><label :for="`sampling-${mode}`">{{ mode }} <strong>{{ value.toFixed(mode === 'top_k' ? 0 : 2) }}</strong></label><input :id="`sampling-${mode}`" v-model.number="value" type="range" :min="mode === 'top_k' ? 1 : mode === 'top_p' ? 0.05 : 0" :max="mode === 'top_k' ? 5 : mode === 'top_p' ? 1 : 2" :step="mode === 'top_k' ? 1 : 0.05" /><button class="secondary" @click="value = mode === 'temperature' ? 1 : mode === 'top_k' ? 3 : 0.8; reset()">重置</button></div>
    <div class="distribution">
      <svg viewBox="0 0 560 260" role="img" :aria-label="`${mode} 调整后的候选分布`">
        <text x="85" y="20" class="svg-label">灰色：原始概率　蓝色：最终抽样概率</text>
        <g v-for="(token, i) in candidates" :key="token" :transform="`translate(0,${40+i*42})`" :opacity="kept.includes(i) ? 1 : 0.3">
          <text x="20" y="22" class="svg-token">{{ token }}</text>
          <rect x="85" y="1" :width="base[i]! * 320" height="10" rx="4" fill="#ccd5e4" />
          <rect x="85" y="15" :width="probabilities[i]! * 320" height="15" rx="4" :fill="chosen === i ? '#8b5cf6' : '#3868f5'" class="prob-bar" />
          <text x="420" y="24" class="svg-value">{{ percent(probabilities[i]!) }}</text>
          <text v-if="mode === 'top_p'" x="490" y="24" class="svg-label">Σ {{ cumulative[i]!.toFixed(2) }}</text>
        </g>
      </svg>
      <div class="sampling-explain">
        <template v-if="mode === 'temperature'"><h3>{{ value === 0 ? '贪心选择' : value < 1 ? '概率更集中' : value === 1 ? '保持原分布' : '概率更平缓' }}</h3><p class="formula">qᵢ = pᵢ<sup>1/T</sup> / Σ pⱼ<sup>1/T</sup></p><p class="micro">T=0 单独取最大概率项。T=2 仍保留概率差异，不能理解为等概率。</p></template>
        <template v-else><h3>保留 {{ kept.length }} 个候选</h3><p v-if="mode === 'top_p'">累计 {{ percent(kept.reduce((sum,i) => sum+base[i]!,0)) }}，首次达到阈值。</p><p v-else>按概率降序保留前 K 个。</p><p class="micro">排除项概率归零；保留项重新归一化后抽样。本页独立展示截断，不叠加温度。</p></template>
        <div class="row"><button @click="draw(1)">抽取 1 次</button><button class="secondary" @click="draw(200)">抽取 200 次</button></div>
        <p class="micro">本地抽样 {{ total }} 次；参数变化后清空统计。</p>
        <div class="histogram"><span v-for="(n,i) in counts" :key="i">{{ candidates[i] }} <b>{{ n }}</b></span></div>
      </div>
    </div>
  </div>
</template>
