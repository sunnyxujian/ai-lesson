// @ts-check
"use strict";
const UI = (() => {
  /** @param {string} s @param {ParentNode} [root] @returns {HTMLElement} */
  function $(s, root = document) {
    const el = root.querySelector(s);
    if (!(el instanceof HTMLElement)) throw new Error(`找不到元素 ${s}`);
    return el;
  }
  /** @param {string} s @returns {HTMLInputElement} */
  function input(s) {
    return /** @type {HTMLInputElement} */ ($(s));
  }
  /** @param {string} s @returns {HTMLSelectElement} */
  function select(s) {
    return /** @type {HTMLSelectElement} */ ($(s));
  }
  /** @param {string} s @returns {HTMLCanvasElement} */
  function canvas(s) {
    return /** @type {HTMLCanvasElement} */ ($(s));
  }
  /** @param {string} s @returns {HTMLButtonElement} */
  function button(s) {
    return /** @type {HTMLButtonElement} */ ($(s));
  }
  /** @param {unknown} s */
  function escape(s) {
    return String(s).replace(
      /[&<>"']/g,
      (c) =>
        ({
          "&": "&amp;",
          "<": "&lt;",
          ">": "&gt;",
          '"': "&quot;",
          "'": "&#39;",
        })[c] || c,
    );
  }
  /** @param {number} n @param {number} [digits] */
  function fmt(n, digits = 4) {
    return Number.isFinite(n)
      ? Math.abs(n) < 10 ** -digits && n !== 0
        ? n.toExponential(2)
        : n.toFixed(digits)
      : "—";
  }
  /** @param {number} n */
  function signed(n) {
    return `${n >= 0 ? "+" : ""}${fmt(n, 3)}`;
  }
  /** @param {number} n @param {number} min @param {number} max */
  function clamp(n, min, max) {
    return Math.max(min, Math.min(max, n));
  }
  /** @param {HTMLInputElement} el @param {number} fallback */
  function number(el, fallback) {
    const n = el.valueAsNumber;
    const v = Number.isFinite(n)
      ? clamp(
          n,
          el.min === "" ? -Infinity : Number(el.min),
          el.max === "" ? Infinity : Number(el.max),
        )
      : fallback;
    el.value = String(v);
    return v;
  }
  /** @param {string} eyebrow @param {string} title @param {string} subtitle @param {string} formula */
  function heading(eyebrow, title, subtitle, formula) {
    return `<div class="page-heading"><div><div class="eyebrow">${eyebrow}</div><h1>${title}</h1><p class="page-subtitle">${subtitle}</p></div><div class="formula-tag">${formula}</div></div>`;
  }
  /** @param {string} title @param {string} content @param {string} [extra] */
  function panel(title, content, extra = "") {
    return `<section class="panel ${extra}"><div class="panel-title"><i class="status-dot"></i>${title}</div>${content}</section>`;
  }
  /** @param {number} step @param {string[]} names */
  function steps(step, names) {
    return `<div class="step-label">STEP ${step + 1} / ${names.length}</div><div class="step-title">${names[step]}</div><div class="progress">${names.map((_, i) => `<span class="${i <= step ? "on" : ""}"></span>`).join("")}</div>`;
  }
  /** @param {string} key @param {string} value */
  function metric(key, value) {
    return `<div class="metric"><div class="key">${key}</div><div class="value">${value}</div></div>`;
  }
  /** @param {number[]} values */
  function bars(values) {
    return values
      .map(
        (p, i) =>
          `<div class="bar-row"><span>${i}</span><div class="bar-track"><i style="width:${p * 100}%"></i></div><output>${(p * 100).toFixed(1)}%</output></div>`,
      )
      .join("");
  }
  /** @param {HTMLCanvasElement} c */
  function context(c) {
    const rect = c.getBoundingClientRect();
    const w = Math.max(240, rect.width),
      h = Math.max(120, rect.height),
      dpr = Math.min(devicePixelRatio || 1, 2);
    c.width = Math.round(w * dpr);
    c.height = Math.round(h * dpr);
    const ctx = c.getContext("2d");
    if (!ctx) throw new Error("浏览器不支持 Canvas 2D");
    ctx.scale(dpr, dpr);
    return { ctx, w, h };
  }
  /** @param {HTMLCanvasElement} c @param {{values:number[],color:string,label?:string}[]} series @param {string} [xlabel] */
  function plot(c, series, xlabel = "参数更新次数") {
    const { ctx, w, h } = context(c),
      left = 45,
      top = 15,
      right = w - 16,
      bottom = h - 29;
    const all = series.flatMap((s) => s.values).filter(Number.isFinite);
    const max = Math.max(0.01, ...all) * 1.1;
    const count = Math.max(2, ...series.map((s) => s.values.length));
    ctx.font = "10px monospace";
    ctx.lineWidth = 1;
    for (let i = 0; i <= 4; i++) {
      const y = top + ((bottom - top) * i) / 4;
      ctx.strokeStyle = "#22313b";
      ctx.beginPath();
      ctx.moveTo(left, y);
      ctx.lineTo(right, y);
      ctx.stroke();
      ctx.fillStyle = "#718692";
      ctx.fillText((max * (1 - i / 4)).toFixed(2), 3, y + 4);
    }
    for (const s of series) {
      ctx.strokeStyle = s.color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      s.values.forEach((v, i) => {
        const x = left + ((right - left) * i) / (count - 1),
          y = bottom - (v / max) * (bottom - top);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      });
      ctx.stroke();
      if (s.values.length === 1) {
        ctx.fillStyle = s.color;
        ctx.beginPath();
        ctx.arc(
          left,
          bottom - (s.values[0] / max) * (bottom - top),
          3,
          0,
          Math.PI * 2,
        );
        ctx.fill();
      }
    }
    ctx.fillStyle = "#718692";
    ctx.textAlign = "center";
    ctx.fillText(xlabel, (left + right) / 2, h - 5);
    ctx.textAlign = "right";
    ctx.fillText(String(Math.max(0, count - 1)), right, bottom + 14);
    ctx.textAlign = "left";
  }
  /** @param {string} filename @param {string} contents */
  function download(filename, contents) {
    const url = URL.createObjectURL(
      new Blob([contents], { type: "application/json" }),
    );
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  /** @param {number[][]} values @param {number} [rows] @param {number} [cols] */
  function matrix(values, rows = 8, cols = 8) {
    return `<div class="matrix" style="grid-template-columns:repeat(${Math.min(cols, values[0]?.length || 1)},1fr)">${values
      .slice(0, rows)
      .map((row) =>
        row
          .slice(0, cols)
          .map(
            (v) =>
              `<span style="color:${v >= 0 ? "#73dec1" : "#efb47d"};background:${v >= 0 ? "#245345" : "#573d27"}${Math.round(
                25 + clamp(Math.abs(v), 0, 1) * 80,
              )
                .toString(16)
                .padStart(2, "0")}">${fmt(v, 3)}</span>`,
          )
          .join(""),
      )
      .join("")}</div>`;
  }
  return {
    $,
    input,
    select,
    canvas,
    button,
    escape,
    fmt,
    signed,
    clamp,
    number,
    heading,
    panel,
    steps,
    metric,
    bars,
    context,
    plot,
    download,
    matrix,
  };
})();
