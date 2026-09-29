import { add, attention, layerNorm, matmul, positionEncoding, softmax, type Matrix } from './math'
export const words = ['货拉拉', '拉不拉', '拉布拉多']
export const embedding: Matrix = [[1, .2, .4, -.3], [.1, .8, -.2, .5], [-.2, .3, 1, .4]]
// 经典论文先将词嵌入乘 √d_model，再加同维度的位置编码。
export const input = embedding.map((r, i) => r.map((v, j) => v * 2 + positionEncoding(i)[j]))
export const projections: Record<'Q' | 'K' | 'V', Matrix> = {
  Q: [[1, 0, .5, 0], [0, 1, 0, -.5], [.5, 0, 1, 0], [0, .5, 0, 1]],
  K: [[.5, 0, 1, 0], [0, 1, 0, .5], [1, 0, -.5, 0], [0, .5, 0, 1]],
  V: [[1, .2, 0, 0], [0, .5, .2, 0], [0, 0, 1, .2], [.2, 0, 0, .5]],
}
export const headProjections = [
  { Q: [[1, 0], [0, 1], [.5, 0], [0, -.5]], K: [[.5, 0], [0, 1], [1, .5], [.2, 0]], V: [[1, 0], [0, .5], [.5, 1], [.2, -.2]] },
  { Q: [[0, 1], [1, 0], [0, -.5], [.5, .2]], K: [[1, .5], [0, -1], [.5, 1], [.2, .5]], V: [[0, 1], [1, .5], [.5, 0], [-.2, .5]] },
]
export const outputProjection: Matrix = [[.6, .1, 0, .2], [0, .7, .2, 0], [.3, 0, .6, .1], [.1, .2, 0, .7]]
export function multiHead(q: Matrix, kv: Matrix = q, causal = false) {
  const heads = headProjections.map(w => {
    const Q = matmul(q, w.Q), K = matmul(kv, w.K), V = matmul(kv, w.V)
    return { Q, K, V, ...attention(Q, K, V, true, causal) }
  })
  const concat = q.map((_, i) => heads.flatMap(h => h.output[i]))
  return { heads, concat, output: matmul(concat, outputProjection) }
}
// 固定、未训练的教学权重；同一层的各位置共享这组 FFN 参数。
export const W1: Matrix = [[1, -1, .5, 0, .3, -.5, .8, .2], [.5, 1, 0, -.5, 1, .2, -.3, .4], [0, .5, 1, 1, -.2, .8, .2, -.5], [.2, 0, -.5, .7, .5, -.3, 1, .2]]
export const W2: Matrix = [[.7, 0, .2, -.1], [0, .5, -.5, .2], [.4, .2, .3, 0], [-.2, .6, .4, .1], [.3, -.2, .1, .5], [.1, .4, -.3, .2], [.2, .1, .6, -.2], [-.1, .3, .2, .4]]
export const b1 = [.1, -.2, .3, 0, -.1, .2, 0, .1]
export const b2 = [.1, 0, -.1, .2]
export function ffn(x: Matrix, activate = true) {
  const hidden = matmul(x, W1).map(r => r.map((v, j) => v + b1[j]))
  const activated = hidden.map(r => r.map(v => activate ? Math.max(0, v) : v))
  const output = matmul(activated, W2).map(r => r.map((v, j) => v + b2[j]))
  return { hidden, activated, output }
}
export function encoderLayer(x: Matrix) {
  const att = multiHead(x)
  const residual1 = add(x, att.output), norm1 = residual1.map(r => layerNorm(r).output)
  const feedForward = ffn(norm1)
  const residual2 = add(norm1, feedForward.output), output = residual2.map(r => layerNorm(r).output)
  return { input: x, att, residual1, norm1, feedForward, residual2, output }
}
export const encoder = encoderLayer(input)
export const memory = encoderLayer(encoder.output).output
export const targetWords = ['BOS', 'Can', 'Huolala', 'carry', 'a', 'Labrador', '?']
export const targetInput: Matrix = targetWords.map((_, i) => [Math.sin(i + .2), Math.cos(i * .7), .2 * i, 1 - i * .15].map((v, j) => 2 * v + positionEncoding(i)[j]))
export function decoderLayer(x: Matrix = targetInput) {
  const self = multiHead(x, x, true)
  const norm1 = add(x, self.output).map(r => layerNorm(r).output)
  const cross = multiHead(norm1, memory)
  const norm2 = add(norm1, cross.output).map(r => layerNorm(r).output)
  const feedForward = ffn(norm2)
  const output = add(norm2, feedForward.output).map(r => layerNorm(r).output)
  return { self, norm1, cross, norm2, feedForward, output }
}
export const vocabulary = ['Can', 'Huolala', 'carry', 'a', 'Labrador', '?', 'EOS', 'drag', 'Does']
export const vocabularyProjection: Matrix = Array.from({ length: 4 }, (_, i) => vocabulary.map((_, j) => Math.sin((i + 1) * (j + 2)) * .7))
export function vocabularyOutput(position: number) {
  const hidden = decoderLayer().output[position]
  const logits = matmul([hidden], vocabularyProjection)[0]
  return { hidden, logits, probabilities: softmax(logits) }
}
// 语言路径是独立的教学预设，不把未训练小模型的输出冒充为翻译结果。
export const generationScript = vocabulary.slice(0, 7).map((token, i) => ({
  token,
  logits: vocabulary.map((_, j) => j === i ? 2.8 : -.4 + .35 * Math.sin(j + i)),
}))
