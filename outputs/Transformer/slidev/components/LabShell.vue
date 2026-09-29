<script setup lang="ts">
import { ref, watch, onScopeDispose } from 'vue'
import { useIsSlideActive, onSlideEnter, onSlideLeave } from '@slidev/client'
const props = withDefaults(defineProps<{ steps: string[]; start?: number; label?: string }>(), { start: 0, label: '交互实验' })
const emit = defineEmits<{ reset: [] }>()
const step = ref(props.start), playing = ref(false)
const active = useIsSlideActive()
let timer: ReturnType<typeof setInterval> | undefined
function pause() { if (timer) clearInterval(timer); timer = undefined; playing.value = false }
function reset() { pause(); step.value = props.start; emit('reset') }
function move(n: number) { pause(); step.value = Math.max(0, Math.min(props.steps.length - 1, step.value + n)) }
function toggle() {
  if (playing.value) return pause()
  if (step.value === props.steps.length - 1) step.value = 0
  playing.value = true
  timer = setInterval(() => { if (step.value < props.steps.length - 1) step.value++; else pause() }, 2200)
}
// Slidev 会保留离场页面实例；只依赖组件卸载不能停止计时器。
onSlideEnter(reset)
onSlideLeave(pause)
watch(active, value => { if (!value) pause() })
onScopeDispose(pause)
</script>
<template>
  <section class="lab" @click.stop @pointerdown.stop @keydown.stop>
    <div class="lab-top"><span class="eyebrow">{{ label }}</span><span class="lab-stage" aria-live="polite">{{ step + 1 }} / {{ steps.length }} · {{ steps[step] }}</span></div>
    <div class="lab-content"><slot :step="step" /></div>
    <div class="lab-bottom">
      <div class="step-buttons"><button @click="move(-1)" :disabled="step === 0">← 上一步</button><button class="primary" @click="toggle" :aria-pressed="playing">{{ playing ? '暂停' : '播放' }}</button><button @click="move(1)" :disabled="step === steps.length-1">下一步 →</button><button @click="reset">重置</button></div>
      <span class="step-dots" aria-hidden="true"><i v-for="(_, i) in steps" :key="i" :class="{ active: i === step }"></i></span>
    </div>
  </section>
</template>
