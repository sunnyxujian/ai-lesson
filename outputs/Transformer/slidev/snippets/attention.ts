import { matmul, softmax, transpose, type Matrix } from '../lib/math'

export function scaledAttention(Q: Matrix, K: Matrix, V: Matrix) {
  const dk = Q[0].length
  const scores = matmul(Q, transpose(K))
  const scaled = scores.map(row => row.map(x => x / Math.sqrt(dk)))
  const weights = scaled.map(softmax)
  return matmul(weights, V)
}
