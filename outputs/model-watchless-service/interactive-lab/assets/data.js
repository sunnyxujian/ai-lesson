// @ts-check
"use strict";
const DigitData = (() => {
  /** @type {number[][][][]} */
  const strokes = [
    [
      [
        [0.53, 0.1],
        [0.32, 0.13],
        [0.23, 0.3],
        [0.2, 0.65],
        [0.31, 0.86],
        [0.54, 0.88],
        [0.72, 0.7],
        [0.76, 0.35],
        [0.66, 0.14],
        [0.53, 0.1],
      ],
    ],
    [
      [
        [0.32, 0.3],
        [0.55, 0.12],
        [0.49, 0.87],
      ],
      [
        [0.29, 0.88],
        [0.7, 0.88],
      ],
    ],
    [
      [
        [0.24, 0.3],
        [0.35, 0.13],
        [0.61, 0.12],
        [0.75, 0.27],
        [0.69, 0.44],
        [0.25, 0.85],
        [0.76, 0.85],
      ],
    ],
    [
      [
        [0.25, 0.18],
        [0.65, 0.13],
        [0.73, 0.29],
        [0.49, 0.46],
        [0.67, 0.51],
        [0.76, 0.7],
        [0.61, 0.87],
        [0.29, 0.82],
      ],
    ],
    [
      [
        [0.61, 0.12],
        [0.24, 0.58],
        [0.78, 0.57],
      ],
      [
        [0.65, 0.32],
        [0.59, 0.9],
      ],
    ],
    [
      [
        [0.75, 0.14],
        [0.31, 0.14],
        [0.28, 0.46],
        [0.59, 0.44],
        [0.74, 0.6],
        [0.67, 0.8],
        [0.44, 0.89],
        [0.23, 0.78],
      ],
    ],
    [
      [
        [0.69, 0.15],
        [0.45, 0.17],
        [0.26, 0.46],
        [0.25, 0.75],
        [0.42, 0.88],
        [0.64, 0.82],
        [0.72, 0.64],
        [0.58, 0.49],
        [0.28, 0.52],
      ],
    ],
    [
      [
        [0.23, 0.16],
        [0.78, 0.15],
        [0.51, 0.52],
        [0.36, 0.9],
      ],
    ],
    [
      [
        [0.49, 0.12],
        [0.28, 0.2],
        [0.3, 0.37],
        [0.67, 0.59],
        [0.72, 0.76],
        [0.56, 0.89],
        [0.32, 0.84],
        [0.24, 0.65],
        [0.58, 0.39],
        [0.71, 0.23],
        [0.61, 0.12],
        [0.49, 0.12],
      ],
    ],
    [
      [
        [0.71, 0.46],
        [0.45, 0.53],
        [0.26, 0.4],
        [0.29, 0.19],
        [0.53, 0.12],
        [0.73, 0.28],
        [0.64, 0.65],
        [0.44, 0.89],
      ],
    ],
  ];
  /** @param {number} label @param {number} seed @param {string} id @returns {NNSample} */
  function make(label, seed, id) {
    const rand = NN.random(seed);
    const angle = (rand() - 0.5) * 0.35,
      sx = 0.85 + rand() * 0.27,
      sy = 0.88 + rand() * 0.2;
    const dx = (rand() - 0.5) * 3,
      dy = (rand() - 0.5) * 3,
      width = 1 + rand() * 0.65;
    const pixels = Array(1600).fill(0);
    const paths = strokes[label].map((path) =>
      path.map(([x, y]) => {
        const u = (x - 0.5) * 34 * sx,
          v = (y - 0.5) * 34 * sy;
        return [
          20 + u * Math.cos(angle) - v * Math.sin(angle) + dx + (rand() - 0.5),
          20 + u * Math.sin(angle) + v * Math.cos(angle) + dy + (rand() - 0.5),
        ];
      }),
    );
    for (const path of paths)
      for (let k = 1; k < path.length; k++) {
        const [ax, ay] = path[k - 1],
          [bx, by] = path[k];
        const vx = bx - ax,
          vy = by - ay,
          len = vx * vx + vy * vy;
        for (
          let y = Math.max(0, Math.floor(Math.min(ay, by) - 4));
          y <= Math.min(39, Math.ceil(Math.max(ay, by) + 4));
          y++
        ) {
          for (
            let x = Math.max(0, Math.floor(Math.min(ax, bx) - 4));
            x <= Math.min(39, Math.ceil(Math.max(ax, bx) + 4));
            x++
          ) {
            const t = Math.max(
              0,
              Math.min(1, ((x - ax) * vx + (y - ay) * vy) / (len || 1)),
            );
            const distance = Math.hypot(x - ax - t * vx, y - ay - t * vy);
            pixels[y * 40 + x] = Math.max(
              pixels[y * 40 + x],
              Math.exp((-distance * distance) / (width * width)),
            );
          }
        }
      }
    return { pixels, label, id };
  }
  /** @type {NNSample[]} */
  const train = [],
    validation = [];
  for (let digit = 0; digit < 10; digit++) {
    for (let i = 0; i < 20; i++)
      train.push(make(digit, 1000 + digit * 100 + i, `train-${digit}-${i}`));
    for (let i = 0; i < 5; i++)
      validation.push(
        make(digit, 90000 + digit * 100 + i, `validation-${digit}-${i}`),
      );
  }
  /** @param {HTMLCanvasElement} canvas @param {NNSample} sample */
  function draw(canvas, sample) {
    canvas.width = canvas.height = 40;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    const im = ctx.createImageData(40, 40);
    sample.pixels.forEach((p, i) => {
      const v = Math.round(255 * (1 - p));
      im.data.set([v, v, v, 255], i * 4);
    });
    ctx.putImageData(im, 0, 0);
  }
  /** @param {number[]} values @param {number} seed */
  function shuffle(values, seed) {
    const arr = values.slice(),
      rand = NN.random(seed);
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(rand() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }
  return { train, validation, make, draw, shuffle };
})();
