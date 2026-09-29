<script setup lang="ts">
defineProps<{ labels: string[]; values: number[]; highlight?: number }>()
</script>
<template>
  <div class="probabilities" role="img" :aria-label="labels.map((l,i) => `${l}: ${(values[i]*100).toFixed(1)}%`).join('；')">
    <div v-for="(value, i) in values" :key="i" class="prob-row" :class="{ chosen: highlight === i }">
      <span>{{ labels[i] }}</span><div class="track"><div class="fill" :style="{ width: `${Math.max(0, value) * 100}%` }"></div></div><b>{{ (value * 100).toFixed(1) }}%</b>
    </div>
  </div>
</template>
