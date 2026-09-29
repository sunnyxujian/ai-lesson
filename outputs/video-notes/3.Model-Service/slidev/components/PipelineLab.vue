<script setup lang="ts">
import { computed, ref } from 'vue'
import { onSlideLeave } from '@slidev/client'
const props = withDefaults(defineProps<{ mode?: 'overview' | 'auth' | 'post' }>(), { mode: 'overview' })
const stage = ref(0)
const running = ref(false)
const scenario = ref('通过')
let timer: ReturnType<typeof setInterval> | undefined
const labels = computed(() => props.mode === 'post' ? ['输出 Token','Detokenization','输出检查','自然语言回复'] : ['用户消息','前处理','自回归','后处理','回复'])
const detail = computed(() => {
  if (props.mode === 'post') return ['[201, 202, 203, 204, 205]', '我 / 是 / 模型 / 助手 / 。', scenario.value === '通过' ? '示例规则检查通过' : '示例规则未通过：本次不交付输出', '我是模型助手。'][stage.value]
  if (stage.value === 1 && scenario.value !== '通过') return `${scenario.value}：在此停止，不进入模型计算。`
  return ['user: 你是谁？','校验访问权限 → 组装消息 → Tokenization','概率分布 → 选择 Token → 追加上下文 → 下一轮','将 Token 还原为文本，按服务规则处理输出','assistant: 我是模型助手。'][stage.value]
})
const stopped = computed(() => scenario.value !== '通过' && stage.value === (props.mode === 'post' ? 2 : 1))
function pause() { clearInterval(timer); timer = undefined; running.value = false }
function step() { if (stopped.value || stage.value >= labels.value.length-1) return pause(); stage.value++; if (stopped.value || stage.value >= labels.value.length-1) pause() }
function play() { if (running.value) return pause(); running.value = true; timer = setInterval(step, 1100) }
function reset() { pause(); stage.value = 0 }
onSlideLeave(pause)
</script>
<template>
  <div class="lab flow-lab" @click.stop @keydown.stop>
    <div class="lab-head"><span class="tag">教学流程 · 不代表服务商内部实现</span><span class="spacer" /><select v-if="mode !== 'overview'" v-model="scenario" aria-label="流程情境" @change="reset"><option>通过</option><template v-if="mode === 'auth'"><option>密钥无效</option><option>模型无权限</option><option>余额不足</option></template><option v-else>检查未通过</option></select><button @click="step" :disabled="stopped || stage === labels.length-1">下一步</button><button class="secondary" @click="play" :disabled="stopped || stage === labels.length-1">{{ running ? '暂停' : '播放' }}</button><button class="quiet" @click="reset">重置</button></div>
    <svg viewBox="0 0 1000 170" role="img" aria-label="请求处理阶段">
      <g v-for="(label,i) in labels" :key="label" :transform="`translate(${20+i*(960/labels.length)},42)`">
        <path v-if="i < labels.length-1" :d="`M${960/labels.length-35} 42 h34 l-9 -7 m9 7 l-9 7`" stroke="#becadd" fill="none" stroke-width="2" />
        <rect :width="960/labels.length-36" height="84" rx="14" :fill="i === stage ? stopped ? '#fff1f0' : '#edf2ff' : '#ffffff'" :stroke="i === stage ? stopped ? '#d14b50' : '#3868f5' : '#dce4ef'" stroke-width="2" />
        <text :x="(960/labels.length-36)/2" y="48" text-anchor="middle" class="svg-token">{{ label }}</text>
        <circle v-if="i === stage" :cx="(960/labels.length-36)/2" cy="-19" r="6" :fill="stopped ? '#d14b50' : '#3868f5'" />
      </g>
    </svg>
    <div class="flow-detail" :class="{ error: stopped }">{{ detail }}</div>
    <p class="micro">{{ mode === 'post' ? '检查未通过后的拒绝、修订或重新生成由服务规则决定；这里仅展示一种停止交付的情境。' : '一条消息穿过服务层，内部可能包含更多路由、缓存和检查。' }}</p>
  </div>
</template>
