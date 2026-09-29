<script setup lang="ts">
import { computed, ref } from 'vue'
const props = withDefaults(defineProps<{ rounds?: boolean }>(), { rounds: false })
const input = ref(1000)
const output = ref(props.rounds ? 10 : 500)
const inputCost = computed(() => input.value / 1e6 * 2.5)
const outputCost = computed(() => output.value / 1e6 * 15)
</script>
<template>
  <div class="lab cost-lab" @click.stop @keydown.stop>
    <div class="lab-head"><span class="tag">{{ rounds ? '教学循环 · 每步生成一个 Token' : '历史示例单价 · 不代表百炼现价' }}</span></div>
    <div v-if="!rounds" class="slider-line"><label for="input-count">输入 <strong>{{ input }}</strong></label><input id="input-count" v-model.number="input" type="range" min="0" max="10000" step="100" /></div>
    <div class="slider-line"><label :for="rounds ? 'round-output' : 'cost-output'">输出 <strong>{{ output }}</strong></label><input :id="rounds ? 'round-output' : 'cost-output'" v-model.number="output" type="range" min="0" max="2000" :step="rounds ? 1 : 50" /></div>
    <div v-if="rounds" class="big-equation"><strong>{{ output }}</strong><span>个输出 Token</span><span>≈</span><strong>{{ output }}</strong><span>次生成步骤</span></div>
    <div v-else class="cost-cards"><div><label>输入 $2.50 / 1M Token</label><strong>${{ inputCost.toFixed(5) }}</strong></div><div><label>输出 $15.00 / 1M Token</label><strong>${{ outputCost.toFixed(5) }}</strong></div><div><label>合计</label><strong>${{ (inputCost+outputCost).toFixed(5) }}</strong></div></div>
    <p class="micro">{{ rounds ? '不计额外的结束判断步骤。此图解释顺序依赖；真实推理有 prefill、KV cache、批处理等优化，不能据此推算 GPU 调用次数或实际价格。' : '费用 = 输入 Token × 输入单价 / 1,000,000 + 输出 Token × 输出单价 / 1,000,000。缓存等计费项未纳入本示例。' }}</p>
  </div>
</template>
