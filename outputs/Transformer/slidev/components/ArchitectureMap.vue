<script setup lang="ts">
import { useId } from 'vue'
const arrowId = `arrow-${useId().replace(/:/g, '')}`
withDefaults(defineProps<{ active?: number; compact?: boolean }>(), { active: -1, compact: false })
const encoder = ['输入嵌入 + 位置', '多头自注意力', 'Add & Norm', 'FFN → Add & Norm', '编码器输出']
const decoder = ['右移目标 + 位置', '带掩码自注意力', 'Add & Norm', '交叉注意力 + Add & Norm', 'FFN + Add & Norm', 'Linear → Softmax']
</script>
<template>
  <svg :class="['architecture', { compact }]" viewBox="0 0 880 370" role="img" aria-label="经典 Transformer：编码器输出向解码器交叉注意力提供 K/V，目标侧提供 Q">
    <defs><marker :id="arrowId" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="none" stroke="currentColor" stroke-width="1.5"/></marker></defs>
    <text x="165" y="25" class="arch-title">编码器 · 源句</text><text x="635" y="25" class="arch-title">解码器 · 已知目标前缀</text>
    <g v-for="(label,i) in encoder" :key="`e${i}`" :class="{ lit: active === i || (active === 8 && i === 4) }">
      <rect x="40" :y="44+i*57" width="250" height="40" rx="8"/>
      <text x="165" :y="69+i*57">{{ label }}</text>
      <path v-if="i < 4" :d="`M165 ${86+i*57} v12`" :marker-end="`url(#${arrowId})`"/>
    </g>
    <g v-for="(label,i) in decoder" :key="`d${i}`" :class="{ lit: active === 5+i }">
      <rect x="510" :y="44+i*51" width="300" height="38" rx="8"/>
      <text x="660" :y="68+i*51">{{ label }}</text>
      <path v-if="i < 5" :d="`M660 ${84+i*51} v10`" :marker-end="`url(#${arrowId})`"/>
    </g>
    <path d="M292 292 H414 V216 H507" class="cross-wire" :class="{ energized: active === 8 }" :marker-end="`url(#${arrowId})`"/>
    <text x="397" y="276" class="wire-label">K / V</text><text x="687" y="191" class="wire-label">Q</text>
    <text x="165" y="352" class="arch-note">中间编码层重复 N 次</text><text x="660" y="363" class="arch-note">中间解码层重复 N 次</text>
  </svg>
</template>
