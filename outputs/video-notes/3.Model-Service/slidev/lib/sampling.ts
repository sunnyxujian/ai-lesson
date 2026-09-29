// 教学分布来自原课；这些数值不是百炼模型返回的概率。
export const candidates = ['我', '你', '它', '这', '嗯']
export const baseProbabilities = [0.30, 0.25, 0.20, 0.15, 0.10]
export function normalize(values: number[]): number[] {
  const sum = values.reduce((a, b) => a + b, 0)
  return sum > 0 ? values.map(v => v / sum) : values.map(() => 0)
}
export function temperatureDistribution(probabilities: number[], temperature: number): number[] {
  if (temperature === 0) {
    const winner = probabilities.indexOf(Math.max(...probabilities))
    return probabilities.map((_, i) => i === winner ? 1 : 0)
  }
  // 减去最大 log 值，避免小温度时数值下溢。
  const logits = probabilities.map(p => Math.log(p) / temperature)
  const max = Math.max(...logits)
  return normalize(logits.map(v => Math.exp(v - max)))
}
export function retainedIndices(probabilities: number[], mode: 'top_k' | 'top_p', threshold: number): number[] {
  const sorted = probabilities.map((p, index) => ({ p, index })).sort((a, b) => b.p - a.p)
  if (mode === 'top_k') return sorted.slice(0, threshold).map(v => v.index)
  let sum = 0
  const indices: number[] = []
  for (const entry of sorted) {
    indices.push(entry.index)
    sum += entry.p
    if (sum + 1e-12 >= threshold) break
  }
  return indices
}
export function sample(probabilities: number[]): number {
  const draw = Math.random()
  let cumulative = 0
  for (let i = 0; i < probabilities.length; i++) {
    cumulative += probabilities[i]!
    if (draw < cumulative) return i
  }
  return probabilities.length - 1
}
