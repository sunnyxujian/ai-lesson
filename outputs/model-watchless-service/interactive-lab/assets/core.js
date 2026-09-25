// @ts-check
"use strict";

/** @typedef {{sizes:number[], weights:number[][][], biases:number[][], seed:number}} NNModel */
/** @typedef {{a:number[][], z:number[][]}} NNTrace */
/** @typedef {{dw:number[][][], db:number[][], delta:number[][], desires:number[][]}} NNGradient */
/** @typedef {{pixels:number[], label:number, id:string}} NNSample */

const NN = (() => {
  const SIZES = [1600, 16, 16, 10];
  const PREPROCESS = "gray40-foreground-one-v1";
  /** @param {number} seed */
  function random(seed) {
    let state = seed >>> 0;
    return () => {
      state += 0x6d2b79f5;
      let t = state;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  /** @param {number} [seed] @returns {NNModel} */
  function create(seed = 42) {
    const rand = random(seed);
    const weights = SIZES.slice(1).map((size, l) => {
      const limit = Math.sqrt(6 / (SIZES[l] + size));
      return Array.from({ length: size }, () =>
        Array.from({ length: SIZES[l] }, () => (rand() * 2 - 1) * limit),
      );
    });
    return {
      sizes: SIZES.slice(),
      weights,
      biases: SIZES.slice(1).map((n) => Array(n).fill(0)),
      seed,
    };
  }
  /** @param {NNModel} m @returns {NNModel} */
  function clone(m) {
    return {
      sizes: m.sizes.slice(),
      seed: m.seed,
      weights: m.weights.map((w) => w.map((row) => row.slice())),
      biases: m.biases.map((b) => b.slice()),
    };
  }
  /** @param {number} x */
  function sigmoid(x) {
    return x >= 0 ? 1 / (1 + Math.exp(-x)) : Math.exp(x) / (1 + Math.exp(x));
  }
  /** @param {number[]} values */
  function softmax(values) {
    const max = Math.max(...values);
    const e = values.map((x) => Math.exp(x - max));
    const sum = e.reduce((s, x) => s + x, 0);
    return e.map((x) => x / sum);
  }
  /** @param {NNModel} model @param {number[]} input @returns {NNTrace} */
  function forward(model, input) {
    const a = [input];
    const z = [];
    for (let l = 0; l < model.weights.length; l++) {
      const prev = a[l];
      const values = model.weights[l].map((row, j) => {
        let sum = model.biases[l][j];
        for (let i = 0; i < row.length; i++) sum += row[i] * prev[i];
        return sum;
      });
      z.push(values);
      a.push(
        l === model.weights.length - 1 ? softmax(values) : values.map(sigmoid),
      );
    }
    return { a, z };
  }
  /** @param {number[]} prediction @param {number} label */
  function loss(prediction, label) {
    return prediction.reduce(
      (s, p, i) => s + (p - Number(i === label)) ** 2,
      0,
    );
  }
  /** @param {number[]} values */
  function argmax(values) {
    return values.indexOf(Math.max(...values));
  }
  /** @param {NNModel} model @returns {NNGradient} */
  function zeros(model) {
    return {
      dw: model.weights.map((w) => w.map((row) => row.map(() => 0))),
      db: model.biases.map((b) => b.map(() => 0)),
      delta: [],
      desires: [],
    };
  }
  /** @param {NNModel} model @param {NNTrace} trace @param {number} label @returns {NNGradient} */
  function backward(model, trace, label) {
    const g = zeros(model);
    const last = model.weights.length - 1;
    const p = trace.a[last + 1];
    const dp = p.map((x, i) => 2 * (x - Number(i === label)));
    const dot = dp.reduce((s, x, i) => s + x * p[i], 0);
    // Softmax 有类别间耦合，必须使用完整的雅可比乘积。
    g.delta[last] = p.map((x, i) => x * (dp[i] - dot));
    g.desires[last] = dp.map((x) => -x);
    for (let l = last; l >= 0; l--) {
      if (l < last) {
        const da = model.biases[l].map((_, j) =>
          model.weights[l + 1].reduce(
            (s, row, k) => s + row[j] * g.delta[l + 1][k],
            0,
          ),
        );
        g.desires[l] = da.map((x) => -x);
        g.delta[l] = da.map(
          (d, j) => d * trace.a[l + 1][j] * (1 - trace.a[l + 1][j]),
        );
      }
      g.db[l] = g.delta[l].slice();
      g.dw[l] = g.delta[l].map((d) => trace.a[l].map((x) => d * x));
    }
    return g;
  }
  /** @param {NNGradient} target @param {NNGradient} source @param {number} [scale] */
  function addGradient(target, source, scale = 1) {
    target.dw.forEach((matrix, l) =>
      matrix.forEach((row, j) => {
        target.db[l][j] += source.db[l][j] * scale;
        row.forEach((_, i) => {
          row[i] += source.dw[l][j][i] * scale;
        });
      }),
    );
  }
  /** @param {NNModel} model @param {NNGradient} g @param {number} rate */
  function apply(model, g, rate) {
    // 先完整校验，再统一提交，防止出现只更新一半的网络。
    const next = clone(model);
    next.weights.forEach((matrix, l) =>
      matrix.forEach((row, j) => {
        next.biases[l][j] -= rate * g.db[l][j];
        row.forEach((_, i) => {
          row[i] -= rate * g.dw[l][j][i];
        });
      }),
    );
    if (
      next.weights.some((w) =>
        w.some((row) => row.some((x) => !Number.isFinite(x))),
      ) ||
      next.biases.some((b) => b.some((x) => !Number.isFinite(x)))
    )
      throw new Error("参数超出有限数值范围，请减小学习率后重置。");
    model.weights = next.weights;
    model.biases = next.biases;
  }
  /** @param {NNModel} model */
  function serialize(model) {
    return JSON.stringify(
      {
        version: 1,
        architecture: "dense",
        hiddenActivation: "sigmoid",
        outputActivation: "softmax",
        loss: "sum-squared-error",
        preprocessing: PREPROCESS,
        ...model,
      },
      null,
      2,
    );
  }
  /** @param {string} text @returns {NNModel} */
  function deserialize(text) {
    const d = JSON.parse(text);
    if (
      d.version !== 1 ||
      d.architecture !== "dense" ||
      d.hiddenActivation !== "sigmoid" ||
      d.outputActivation !== "softmax" ||
      d.loss !== "sum-squared-error" ||
      d.preprocessing !== PREPROCESS
    )
      throw new Error("模型版本、激活函数或预处理规则与本实验不兼容。");
    if (
      !Array.isArray(d.sizes) ||
      JSON.stringify(d.sizes) !== JSON.stringify(SIZES) ||
      !Number.isInteger(d.seed)
    )
      throw new Error("网络结构必须为 1600 → 16 → 16 → 10，并包含整数种子。");
    if (
      !Array.isArray(d.weights) ||
      d.weights.length !== 3 ||
      !Array.isArray(d.biases) ||
      d.biases.length !== 3
    )
      throw new Error("缺少有效的权重或偏置。");
    for (let l = 0; l < 3; l++) {
      if (
        !Array.isArray(d.weights[l]) ||
        d.weights[l].length !== SIZES[l + 1] ||
        !Array.isArray(d.biases[l]) ||
        d.biases[l].length !== SIZES[l + 1]
      )
        throw new Error("参数层尺寸不匹配。");
      for (const row of d.weights[l])
        if (
          !Array.isArray(row) ||
          row.length !== SIZES[l] ||
          row.some(
            (x) =>
              typeof x !== "number" || !Number.isFinite(x) || Math.abs(x) > 1e6,
          )
        )
          throw new Error("权重行尺寸错误，或存在无效、过大的数值。");
      if (
        d.biases[l].some(
          (x) =>
            typeof x !== "number" || !Number.isFinite(x) || Math.abs(x) > 1e6,
        )
      )
        throw new Error("偏置包含无效、过大的数值。");
    }
    return clone(d);
  }
  return {
    SIZES,
    PREPROCESS,
    random,
    create,
    clone,
    sigmoid,
    softmax,
    forward,
    loss,
    argmax,
    zeros,
    backward,
    addGradient,
    apply,
    serialize,
    deserialize,
  };
})();
