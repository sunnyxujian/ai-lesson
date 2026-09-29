<script setup lang="ts">
import { fmt, type Matrix } from '../lib/math'
withDefaults(defineProps<{ values: Matrix; label: string; rows?: string[]; cols?: string[]; selectedRow?: number; selectedCol?: number; heat?: boolean; tone?: string; selectable?: boolean }>(), { selectedRow: -1, selectedCol: -1, tone: '' })
const emit = defineEmits<{ select: [row: number, col: number] }>()
</script>
<template>
  <figure class="matrix-view" :class="[tone, { dense: values.length > 4 }]">
    <figcaption>{{ label }} <small>{{ values.length }} × {{ values[0]?.length }}</small></figcaption>
    <table :aria-label="label">
      <thead v-if="cols"><tr><th></th><th v-for="(col, j) in cols" :key="j">{{ col }}</th></tr></thead>
      <tbody><tr v-for="(row, i) in values" :key="i">
        <th v-if="rows" scope="row">{{ rows[i] }}</th>
        <td v-for="(value, j) in row" :key="j" :class="{ selected: (selectedRow === i && (selectedCol < 0 || selectedCol === j)), masked: value === -Infinity }" :style="heat && Number.isFinite(value) ? { backgroundColor: `rgba(20,119,107,${0.06 + value * 0.7})`, color: value > .65 ? 'white' : '#143e39' } : {}">
          <button v-if="selectable" @click="emit('select', i, j)" :aria-label="`${label} 第 ${i+1} 行第 ${j+1} 列，${fmt(value)}`">{{ fmt(value) }}</button>
          <span v-else>{{ fmt(value) }}</span>
        </td>
      </tr></tbody>
    </table>
  </figure>
</template>
