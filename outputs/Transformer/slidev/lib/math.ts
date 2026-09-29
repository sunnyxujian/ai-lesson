export type Matrix = number[][]
export const clone = (x: Matrix): Matrix => x.map(row => [...row])
export const fmt = (x: number, digits = 2) => x === -Infinity ? '−∞' : Number.isFinite(x) ? Number(x.toFixed(digits)).toString() : '—'
export function shape(x: Matrix): [number, number] {
  if (!x.length || !x[0].length || x.some(r => r.length !== x[0].length)) throw new Error('矩阵必须非空且各行等长')
  return [x.length, x[0].length]
}
export function transpose(x: Matrix): Matrix {
  const [, cols] = shape(x)
  return Array.from({ length: cols }, (_, j) => x.map(r => r[j]))
}
export function dot(a: number[], b: number[]): number {
  if (a.length !== b.length) throw new Error('点积维度不匹配')
  return a.reduce((sum, v, i) => sum + v * b[i], 0)
}
export function matmul(a: Matrix, b: Matrix): Matrix {
  if (shape(a)[1] !== shape(b)[0]) throw new Error('矩阵乘法维度不匹配')
  const columns = transpose(b)
  return a.map(row => columns.map(col => dot(row, col)))
}
export function add(a: Matrix, b: Matrix): Matrix {
  if (shape(a).join() !== shape(b).join()) throw new Error('残差相加要求相同形状')
  return a.map((r, i) => r.map((v, j) => v + b[i][j]))
}
export function softmax(row: number[]): number[] {
  if (!row.length || row.some(x => Number.isNaN(x) || x === Infinity)) throw new Error('Softmax 输入无效')
  const max = Math.max(...row)
  if (max === -Infinity) throw new Error('至少保留一个未被屏蔽的位置')
  const exp = row.map(x => x === -Infinity ? 0 : Math.exp(x - max))
  const sum = exp.reduce((a, b) => a + b, 0)
  return exp.map(x => x / sum)
}
export interface AttentionResult {
  raw: Matrix
  scores: Matrix
  weights: Matrix
  output: Matrix
  dk: number
}
export function attention(q: Matrix, k: Matrix, v: Matrix, scaled = true, causal = false): AttentionResult {
  const [n, dk] = shape(q)
  if (shape(k)[1] !== dk || shape(k)[0] !== shape(v)[0]) throw new Error('Q/K/V 维度不匹配')
  if (causal && n !== k.length) throw new Error('本演示的因果自注意力使用等长 Q/K')
  const raw = matmul(q, transpose(k))
  // 先屏蔽未来位置，再按行计算 Softmax；不能在 Softmax 后直接截断。
  const scores = raw.map((r, i) => r.map((x, j) => causal && j > i ? -Infinity : x / (scaled ? Math.sqrt(dk) : 1)))
  const weights = scores.map(softmax)
  return { raw, scores, weights, output: matmul(weights, v), dk }
}
export function layerNorm(row: number[], gamma = 1, beta = 0) {
  const mean = row.reduce((s, x) => s + x, 0) / row.length
  const variance = row.reduce((s, x) => s + (x - mean) ** 2, 0) / row.length
  const z = row.map(x => (x - mean) / Math.sqrt(variance + 1e-5))
  return { mean, variance, z, output: z.map(x => gamma * x + beta) }
}
export function positionEncoding(position: number, dimensions = 4): number[] {
  return Array.from({ length: dimensions }, (_, i) => {
    const angle = position / 10000 ** (2 * Math.floor(i / 2) / dimensions)
    return i % 2 === 0 ? Math.sin(angle) : Math.cos(angle)
  })
}
