import { reactive, ref } from 'vue'
import type { ChatInput, ChatResult } from './contracts'
export interface RunRecord { request: ChatInput; result?: ChatResult; error?: string; at: string; model: string }
// 同一浏览器中的各演示页共享记录和请求锁，防止翻页重复发送。
export const liveState = reactive({
  system: '你是一位简洁、严谨的技术讲师。',
  prompt: '用一个贴近开发者的比喻解释：模型服务与裸模型有什么区别？不超过100字。',
  records: {} as Record<string, RunRecord>,
})
export const liveBusy = ref(false)
