<script setup lang="ts">
import { computed, ref } from 'vue'
withDefaults(defineProps<{ mode?: 'assembly' | 'roles' | 'tokens' }>(), { mode: 'assembly' })
const phase = ref(0)
const role = ref('简洁助手')
const active = ref(-1)
const system = computed(() => role.value === '简洁助手' ? '请简洁回答。' : '请用猫的口吻回答。')
const pieces = computed(() => ['<system>', ... (role.value === '简洁助手' ? ['请','简洁','回答','。'] : ['请','用','猫','的','口吻','回答','。']), '<user>','你','是','谁','？','<assistant>'])
const vocab: Record<string, number> = { '<system>':1,'<user>':2,'<assistant>':3,'请':10,'简洁':11,'回答':12,'。':13,'用':14,'猫':15,'的':16,'口吻':17,'你':101,'是':102,'谁':103,'？':104 }
</script>
<template>
  <div class="lab assembly-lab" @click.stop @keydown.stop>
    <div class="lab-head"><span class="tag">教学词表 · Token ID 为示意</span><span class="spacer" /><select v-model="role" aria-label="系统提示示例" @change="active = -1"><option>简洁助手</option><option>猫咪角色</option></select><button @click="phase = (phase+1)%3">{{ phase === 2 ? '从头演示' : '下一步' }}</button></div>
    <div class="assembly-grid">
      <div class="message-stack"><div class="message system"><label>system</label>{{ system }}</div><div class="message"><label>user</label>你是谁？</div><p class="micro">切换系统消息，观察输入如何变化。这里展示开发者提供的 system，不推测平台隐藏提示词。</p></div>
      <div>
        <template v-if="phase === 0"><div class="empty">第一步：分别组织 system 和 user 消息。<br />点击“下一步”查看角色序列。</div></template>
        <template v-else><label>{{ phase === 1 ? '角色与文本序列' : '示意 Token ID' }}</label><div class="chips token-map"><button v-for="(piece,i) in pieces" :key="i" :class="{ role: piece.startsWith('<'), selected: active === i }" @mouseenter="active = i" @focus="active = i">{{ phase === 1 ? piece : vocab[piece] }}</button></div><div class="mapping-detail">{{ active < 0 ? '悬停或聚焦任意块，查看文字与 ID 的映射。' : `${pieces[active]} ↔ ${vocab[pieces[active]!]}` }}</div><p class="micro">真实切分由 tokenizer 决定，不保证一字一个 Token；角色可通过模板、特殊标记等方式编码。</p></template>
      </div>
    </div>
    <p v-if="mode === 'roles'" class="callout small">都变成数字，不等于角色没有意义。模型会通过训练学习角色和指令约定。</p>
  </div>
</template>
