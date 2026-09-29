<script setup lang="ts">
import { computed, ref } from 'vue'
const provider = ref('百炼')
const fields = computed(() => provider.value === '百炼' ? { baseURL: 'https://llm-u0vlqrit84y13fo8.cn-beijing.maas.aliyuncs.com/compatible-mode/v1', apiKey: 'process.env.MODEL_API_KEY', model: 'process.env.MODEL_NAME' } : { baseURL: 'https://api.openai.com/v1', apiKey: 'process.env.OPENAI_API_KEY', model: '"<可用的 OpenAI 模型>"' })
</script>
<template>
  <div class="lab" @click.stop @keydown.stop>
    <div class="lab-head"><span class="tag">配置示意 · 切换不会发送请求</span><span class="spacer" /><button v-for="name in ['百炼','OpenAI']" :key="name" :class="provider === name ? '' : 'secondary'" @click="provider = name">{{ name }}</button></div>
    <div class="config-grid"><div><div v-for="(value,key) in fields" :key="key" class="config-field"><label>{{ key }}</label><code>{{ value }}</code></div></div><pre class="demo-code">const client = new OpenAI({
  baseURL,
  apiKey,
});

const result = await client
  .chat.completions.create({
    model,
    messages,
  });</pre></div>
    <p class="micro">更换服务商必须同时核对地址、凭据、模型与端点支持。兼容 Chat Completions 不自动意味着兼容 Responses。</p>
  </div>
</template>
