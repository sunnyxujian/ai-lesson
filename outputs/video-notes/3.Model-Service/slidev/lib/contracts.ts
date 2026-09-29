export interface ChatInput {
  system: string
  prompt: string
  temperature?: number
  top_p?: number
}
export interface ChatResult {
  text: string
  model: string
  elapsedMs: number
  usage?: { prompt_tokens?: number; completion_tokens?: number; total_tokens?: number }
  finishReason?: string
}
export interface ModelConfig {
  ready: boolean
  missing: string[]
  baseURL: string
  model: string
}
