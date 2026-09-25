// @ts-check
"use strict";
const Experiments = (() => {
  /** @param {number} x */
  const f = (x) => 0.09 * (x + 0.8) ** 2 + 0.55 * Math.cos(1.7 * x) + 0.65;
  /** @param {number} x */
  const df = (x) => 0.18 * (x + 0.8) - 0.935 * Math.sin(1.7 * x);
  /** @param {number} x @param {number} y */
  const surface = (x, y) => f(x) + f(y);
  /** @param {HTMLElement} host */
  function landscape(host) {
    let dimension = 2,
      x = 3.9,
      y = 2.8,
      rate = 0.15,
      angle = -0.7,
      tilt = 0.65,
      running = false,
      timer = 0,
      disposed = false;
    /** @type {number[][]} */
    let path = [[x, y]];
    /** @type {{x:number,y:number,u:number,v:number}[]} */
    let projected = [];
    host.innerHTML = `<div class="lab-layout fade-in"><div class="board"><div class="board-toolbar"><span id="surface-title">二维曲线 · 一个参数</span><strong>LOSS LANDSCAPE</strong></div><canvas class="chart large" id="landscape-canvas" aria-label="可拖动起点的损失曲线或可旋转损失曲面"></canvas><div class="board-caption" id="landscape-tip"></div><div id="landscape-metrics" class="calc-strip"></div></div><aside class="lab-sidebar">${UI.panel("下山实验", `<div class="segmented"><button id="dimension-2" class="active">二维曲线</button><button id="dimension-3">三维曲面</button></div><label class="field">学习率 η<input id="landscape-rate" type="number" min="0.001" max="4" step="0.05" value="0.15"></label><label class="field">起点 / 当前位置 x<input id="landscape-x" type="range" min="-6" max="6" step="0.01" value="3.9"></label><label class="field" id="landscape-y-field" hidden>起点 / 当前位置 y<input id="landscape-y" type="range" min="-6" max="6" step="0.01" value="2.8"></label><div class="button-row"><button id="landscape-step">下降一步</button><button id="landscape-play" class="primary">自动下山</button></div><button class="full" id="landscape-reset">恢复起点与视角</button><p class="error" id="landscape-error" role="status"></p>`)}${UI.panel("读懂当前方向", `<div id="landscape-gradient" class="notice mono"></div><p class="hint">青绿是下降轨迹，橙色是切线或负梯度。改变学习率就改变每次走多远；大步可能越过谷底，局部下降也不保证到达全局最低点。</p><details open><summary>本实验的教学函数</summary><p class="mono">f(x) = 0.09(x+0.8)² + 0.55cos(1.7x) + 0.65<br>二维损失 C(x) = f(x)<br>三维损失 C(x,y) = f(x) + f(y)</p><p>这是用于展示局部极小值的解析函数，不是手写数字网络的实际损失切片。</p></details>`)}</aside></div>`;
    const canvas = UI.canvas("#landscape-canvas");
    function stop() {
      running = false;
      clearTimeout(timer);
      if (!disposed) UI.button("#landscape-play").textContent = "自动下山";
    }
    function resetPath() {
      stop();
      path = [[x, y]];
      UI.$("#landscape-error").textContent = "";
      draw();
    }
    function draw() {
      const { ctx, w, h } = UI.context(canvas);
      const left = 48,
        right = w - 25,
        top = 25,
        bottom = h - 35;
      ctx.font = "11px monospace";
      projected = [];
      if (dimension === 2) {
        const mapX = (v) => left + ((v + 6) / 12) * (right - left),
          mapY = (v) => bottom - (v / 5.5) * (bottom - top);
        ctx.strokeStyle = "#243640";
        ctx.fillStyle = "#7b919e";
        ctx.lineWidth = 1;
        for (let i = 0; i <= 5; i++) {
          const sy = mapY(i);
          ctx.beginPath();
          ctx.moveTo(left, sy);
          ctx.lineTo(right, sy);
          ctx.stroke();
          ctx.fillText(String(i), 20, sy + 4);
        }
        for (let i = -6; i <= 6; i += 2) {
          const sx = mapX(i);
          ctx.beginPath();
          ctx.moveTo(sx, top);
          ctx.lineTo(sx, bottom);
          ctx.stroke();
          ctx.fillText(String(i), sx - 6, bottom + 20);
        }
        ctx.strokeStyle = "#93a8b3";
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i <= 400; i++) {
          const u = -6 + (i * 12) / 400;
          i === 0
            ? ctx.moveTo(mapX(u), mapY(f(u)))
            : ctx.lineTo(mapX(u), mapY(f(u)));
        }
        ctx.stroke();
        // 谷底位置直接从同一条函数采样，不用固定的“正确终点”。
        const valleys = [];
        for (let i = 1; i < 600; i++) {
          const u = -6 + i * 0.02;
          if (f(u) < f(u - 0.02) && f(u) < f(u + 0.02)) valleys.push(u);
        }
        const min = Math.min(...valleys.map(f));
        valleys.forEach((u) => {
          const global = f(u) <= min + 0.001;
          ctx.fillStyle = global ? "#50dcba" : "#657b89";
          ctx.beginPath();
          ctx.arc(mapX(u), mapY(f(u)), 4, 0, Math.PI * 2);
          ctx.fill();
          ctx.fillText(
            global ? "最低谷" : "局部谷",
            mapX(u) - 20,
            mapY(f(u)) + 22,
          );
        });
        ctx.setLineDash([5, 5]);
        ctx.strokeStyle = "#edac69";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(mapX(x - 1), mapY(f(x) - df(x)));
        ctx.lineTo(mapX(x + 1), mapY(f(x) + df(x)));
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.strokeStyle = "#50dcba";
        ctx.lineWidth = 2;
        ctx.beginPath();
        path.forEach((p, i) => {
          const sx = mapX(p[0]),
            sy = mapY(f(p[0]));
          if (i === 0) ctx.moveTo(sx, sy);
          else ctx.lineTo(sx, sy);
        });
        ctx.stroke();
        path.forEach((p) => {
          ctx.fillStyle = "#50dcba80";
          ctx.beginPath();
          ctx.arc(mapX(p[0]), mapY(f(p[0])), 2, 0, Math.PI * 2);
          ctx.fill();
        });
        ctx.shadowColor = "#50dcba";
        ctx.shadowBlur = 18;
        ctx.fillStyle = "#8fffdc";
        ctx.beginPath();
        ctx.arc(mapX(x), mapY(f(x)), 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
        ctx.fillStyle = "#8ba2ad";
        ctx.fillText("损失 C", left, 15);
        ctx.fillText("参数 x", right - 38, h - 8);
      } else {
        const scale = Math.min(w / 17, h / 12);
        const project = (u, v, z) => {
          const a = u * Math.cos(angle) - v * Math.sin(angle),
            b = u * Math.sin(angle) + v * Math.cos(angle);
          return [
            w / 2 + a * scale,
            h * 0.7 + b * scale * Math.sin(tilt) - z * scale * Math.cos(tilt),
            b,
          ];
        };
        /** @type {{points:number[][],depth:number,z:number}[]} */
        const faces = [];
        for (let u = -5; u < 5; u += 0.5)
          for (let v = -5; v < 5; v += 0.5) {
            const points = [
              [u, v],
              [u + 0.5, v],
              [u + 0.5, v + 0.5],
              [u, v + 0.5],
            ].map(([a, b]) => project(a, b, surface(a, b)));
            faces.push({
              points,
              depth: points.reduce((s, p) => s + p[2], 0) / 4,
              z: surface(u, v),
            });
          }
        faces.sort((a, b) => a.depth - b.depth);
        for (const face of faces) {
          const color = UI.clamp(face.z / 8, 0, 1);
          ctx.fillStyle = `hsl(${155 - color * 40} 34% ${15 + color * 20}%)`;
          ctx.strokeStyle = "#47826770";
          ctx.lineWidth = 0.5;
          ctx.beginPath();
          face.points.forEach((p, i) =>
            i === 0 ? ctx.moveTo(p[0], p[1]) : ctx.lineTo(p[0], p[1]),
          );
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
        }
        for (let u = -5; u <= 5; u += 0.25)
          for (let v = -5; v <= 5; v += 0.25) {
            const p = project(u, v, surface(u, v));
            projected.push({ x: p[0], y: p[1], u, v });
          }
        const axis = (end, label, color) => {
          const a = project(0, 0, 0),
            b = project(...end);
          ctx.strokeStyle = color;
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.moveTo(a[0], a[1]);
          ctx.lineTo(b[0], b[1]);
          ctx.stroke();
          ctx.fillStyle = color;
          ctx.fillText(label, b[0] + 5, b[1]);
        };
        axis([6, 0, 0], "x 参数 1", "#a7c1cc");
        axis([0, 6, 0], "y 参数 2", "#a7c1cc");
        axis([0, 0, 7], "损失 C", "#c7d9e0");
        ctx.strokeStyle = "#80ffcf";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        path.forEach((p, i) => {
          const q = project(p[0], p[1], surface(p[0], p[1]) + 0.06);
          i === 0 ? ctx.moveTo(q[0], q[1]) : ctx.lineTo(q[0], q[1]);
        });
        ctx.stroke();
        const p = project(x, y, surface(x, y) + 0.07),
          end = project(
            x - rate * df(x),
            y - rate * df(y),
            surface(x, y) + 0.07,
          ),
          ex = project(x - rate * df(x), y, surface(x, y) + 0.07);
        ctx.setLineDash([4, 4]);
        ctx.strokeStyle = "#7bb7fa";
        ctx.beginPath();
        ctx.moveTo(p[0], p[1]);
        ctx.lineTo(ex[0], ex[1]);
        ctx.lineTo(end[0], end[1]);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.strokeStyle = "#edac69";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(p[0], p[1]);
        ctx.lineTo(end[0], end[1]);
        ctx.stroke();
        const ang = Math.atan2(end[1] - p[1], end[0] - p[0]);
        ctx.beginPath();
        ctx.moveTo(
          end[0] - 7 * Math.cos(ang - 0.5),
          end[1] - 7 * Math.sin(ang - 0.5),
        );
        ctx.lineTo(end[0], end[1]);
        ctx.lineTo(
          end[0] - 7 * Math.cos(ang + 0.5),
          end[1] - 7 * Math.sin(ang + 0.5),
        );
        ctx.stroke();
        ctx.fillStyle = "#b8ffe4";
        ctx.shadowColor = "#50dcba";
        ctx.shadowBlur = 15;
        ctx.beginPath();
        ctx.arc(p[0], p[1], 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
      }
      UI.$("#surface-title").textContent =
        dimension === 2 ? "二维曲线 · 一个参数" : "三维曲面 · 两个参数";
      UI.$("#landscape-tip").textContent =
        dimension === 2
          ? "在图中横向拖动，选择新的起点。橙色虚线是当前位置的切线；谷底标记来自函数采样。"
          : "拖动旋转曲面；单击网格选择附近起点，也可使用右侧滑杆。橙色为负梯度步长，蓝色虚线为 x / y 分量。";
      UI.$("#landscape-metrics").innerHTML = [
        ["当前位置 x", UI.fmt(x, 3)],
        [
          dimension === 2 ? "切线斜率" : "当前位置 y",
          UI.fmt(dimension === 2 ? df(x) : y, 3),
        ],
        ["当前损失", UI.fmt(dimension === 2 ? f(x) : surface(x, y), 4)],
        ["已走步数", path.length - 1],
      ]
        .map(
          ([k, v]) =>
            `<div><div class="key">${k}</div><div class="value">${v}</div></div>`,
        )
        .join("");
      UI.$("#landscape-gradient").innerHTML =
        `∂C/∂x = ${UI.fmt(df(x))}<br>Δx = ${UI.signed(-rate * df(x))}${dimension === 3 ? `<br>∂C/∂y = ${UI.fmt(df(y))}<br>Δy = ${UI.signed(-rate * df(y))}` : ""}`;
      UI.input("#landscape-x").value = String(x);
      UI.input("#landscape-y").value = String(y);
    }
    function step() {
      const nx = x - rate * df(x),
        ny = dimension === 3 ? y - rate * df(y) : y;
      if (!Number.isFinite(nx + ny) || Math.abs(nx) > 6 || Math.abs(ny) > 6) {
        stop();
        UI.$("#landscape-error").textContent =
          "下一步将离开 [-6, 6] 展示范围，已暂停。减小学习率或重新选择起点。";
        return;
      }
      x = nx;
      y = ny;
      path.push([x, y]);
      if (path.length >= 1000) {
        stop();
        UI.$("#landscape-error").textContent =
          "已完成 999 步，可重选起点继续观察。";
      }
      draw();
    }
    function tick() {
      if (disposed || !running) return;
      step();
      if (Math.hypot(df(x), dimension === 3 ? df(y) : 0) < 1e-6) stop();
      if (running) timer = window.setTimeout(tick, 90);
    }
    for (const dim of [2, 3])
      UI.button(`#dimension-${dim}`).onclick = () => {
        stop();
        dimension = dim;
        UI.button("#dimension-2").classList.toggle("active", dim === 2);
        UI.button("#dimension-3").classList.toggle("active", dim === 3);
        UI.$("#landscape-y-field").hidden = dim === 2;
        resetPath();
      };
    UI.input("#landscape-rate").onchange = () => {
      stop();
      rate = UI.number(UI.input("#landscape-rate"), rate);
      draw();
    };
    UI.input("#landscape-x").oninput = () => {
      x = Number(UI.input("#landscape-x").value);
      resetPath();
    };
    UI.input("#landscape-y").oninput = () => {
      y = Number(UI.input("#landscape-y").value);
      resetPath();
    };
    UI.button("#landscape-step").onclick = () => {
      stop();
      step();
    };
    UI.button("#landscape-play").onclick = () => {
      if (running) {
        stop();
        return;
      }
      running = true;
      UI.button("#landscape-play").textContent = "暂停下山";
      tick();
    };
    UI.button("#landscape-reset").onclick = () => {
      x = 3.9;
      y = 2.8;
      rate = 0.15;
      angle = -0.7;
      tilt = 0.65;
      UI.input("#landscape-rate").value = "0.15";
      resetPath();
    };
    let dragging = false,
      startX = 0,
      startY = 0,
      moved = false;
    /** @param {PointerEvent} e */
    function choose2(e) {
      const r = canvas.getBoundingClientRect();
      x = UI.clamp(
        ((e.clientX - r.left - 48) / (r.width - 73)) * 12 - 6,
        -6,
        6,
      );
      resetPath();
    }
    canvas.onpointerdown = (e) => {
      stop();
      dragging = true;
      moved = false;
      startX = e.clientX;
      startY = e.clientY;
      canvas.setPointerCapture(e.pointerId);
      if (dimension === 2) choose2(e);
    };
    canvas.onpointermove = (e) => {
      if (!dragging) return;
      if (dimension === 2) choose2(e);
      else {
        const dx = e.clientX - startX,
          dy = e.clientY - startY;
        if (Math.abs(dx) + Math.abs(dy) > 2) moved = true;
        angle += dx * 0.01;
        tilt = UI.clamp(tilt + dy * 0.008, 0.2, 1.25);
        startX = e.clientX;
        startY = e.clientY;
        draw();
      }
    };
    canvas.onpointerup = (e) => {
      if (dragging && dimension === 3 && !moved) {
        const r = canvas.getBoundingClientRect();
        const px = e.clientX - r.left,
          py = e.clientY - r.top;
        const nearest = projected.reduce(
          (a, b) =>
            Math.hypot(a.x - px, a.y - py) < Math.hypot(b.x - px, b.y - py)
              ? a
              : b,
          projected[0],
        );
        if (nearest) {
          x = nearest.u;
          y = nearest.v;
          resetPath();
        }
      }
      dragging = false;
    };
    canvas.onpointercancel = () => {
      dragging = false;
    };
    canvas.onlostpointercapture = () => {
      dragging = false;
    };
    window.addEventListener("resize", draw);
    draw();
    return () => {
      stop();
      disposed = true;
      window.removeEventListener("resize", draw);
    };
  }

  /** @param {HTMLElement} host */
  function fitting(host) {
    let degree = 3,
      seed = 73;
    const truth = (x) => 0.45 * Math.sin(3 * x) + 0.2 * x;
    /** @type {number[][]} */ let points = [],
      validation = [];
    function makeData() {
      const r = NN.random(seed);
      points = Array.from({ length: 18 }, (_, i) => {
        const x = -1 + (2 * i) / 17;
        return [x, truth(x) + (r() - 0.5) * 0.36];
      });
      validation = Array.from({ length: 60 }, (_, i) => {
        const x = -1 + (2 * (i + 0.5)) / 60;
        return [x, truth(x) + (r() - 0.5) * 0.36];
      });
    }
    host.innerHTML = `<div class="lab-layout fade-in"><section class="board"><div class="board-toolbar"><span>拟合复杂度与泛化</span><strong>补充实验 · 真实最小二乘</strong></div><canvas id="fit-canvas" class="chart large" aria-label="训练数据、验证数据和多项式拟合曲线"></canvas><div class="board-caption">青绿为训练点，橙色为独立验证点，蓝线为拟合结果。提高复杂度不保证验证误差下降。</div></section><aside class="lab-sidebar">${UI.panel("模型复杂度", `<label class="field">多项式次数 <output id="fit-degree-label">3</output><input id="fit-degree" type="range" min="1" max="16" step="1" value="3"></label><div class="segmented"><button data-degree="1">低复杂度</button><button data-degree="3" class="active">适中</button><button data-degree="16">高复杂度</button></div><button id="fit-data" class="full">换一组带噪声数据</button><div id="fit-metrics" style="margin-top:18px"></div>`)}${UI.panel("泛化不等于记住训练数据", `<p class="hint">同一个函数生成 18 个训练点和 60 个独立验证点，各自叠加噪声。模型只读取训练点；验证误差独立计算。</p><p class="notice">低次数可能表达不了规律；高次数可能跟随训练噪声摆动。这里用多项式复杂度类比网络容量，不把某个固定次数硬标成必然过拟合。</p>`)}</aside></div>`;
    /** @param {number} x @param {number} n */
    function basis(x, n) {
      const out = [1];
      if (n > 0) out.push(x);
      for (let i = 2; i <= n; i++) out.push(2 * x * out[i - 1] - out[i - 2]);
      return out;
    }
    function solve() {
      // Chebyshev 基配合两次正交化，避免高阶普通幂基的严重病态。
      const n = degree + 1,
        m = points.length,
        cols = Array.from({ length: n }, (_, j) =>
          points.map((p) => basis(p[0], degree)[j]),
        );
      const q = [],
        r = Array.from({ length: n }, () => Array(n).fill(0));
      for (let j = 0; j < n; j++) {
        const v = cols[j].slice();
        for (let pass = 0; pass < 2; pass++)
          for (let k = 0; k < j; k++) {
            const dot = v.reduce((s, a, i) => s + a * q[k][i], 0);
            r[k][j] += dot;
            for (let i = 0; i < m; i++) v[i] -= dot * q[k][i];
          }
        r[j][j] = Math.max(1e-12, Math.hypot(...v));
        q.push(v.map((a) => a / r[j][j]));
      }
      const qty = q.map((col) =>
          col.reduce((s, v, i) => s + v * points[i][1], 0),
        ),
        c = Array(n).fill(0);
      for (let i = n - 1; i >= 0; i--) {
        let v = qty[i];
        for (let j = i + 1; j < n; j++) v -= r[i][j] * c[j];
        c[i] = v / r[i][i];
      }
      return c;
    }
    function draw() {
      const coeff = solve(),
        pred = (x) => basis(x, degree).reduce((s, v, i) => s + v * coeff[i], 0),
        mse = (data) =>
          data.reduce((s, p) => s + (pred(p[0]) - p[1]) ** 2, 0) / data.length;
      const { ctx, w, h } = UI.context(UI.canvas("#fit-canvas")),
        left = 45,
        right = w - 20,
        top = 25,
        bottom = h - 32,
        mapX = (x) => left + ((x + 1) / 2) * (right - left),
        mapY = (y) => bottom - ((y + 1.1) / 2.2) * (bottom - top);
      ctx.font = "10px monospace";
      ctx.strokeStyle = "#263640";
      ctx.fillStyle = "#7d929e";
      for (let i = -1; i <= 1; i += 0.5) {
        ctx.beginPath();
        ctx.moveTo(left, mapY(i));
        ctx.lineTo(right, mapY(i));
        ctx.stroke();
        ctx.fillText(i.toFixed(1), 10, mapY(i) + 3);
      }
      ctx.save();
      ctx.beginPath();
      ctx.rect(left, top, right - left, bottom - top);
      ctx.clip();
      ctx.setLineDash([4, 5]);
      ctx.strokeStyle = "#6a7d88";
      ctx.beginPath();
      for (let i = 0; i <= 300; i++) {
        const x = -1 + (2 * i) / 300;
        i === 0
          ? ctx.moveTo(mapX(x), mapY(truth(x)))
          : ctx.lineTo(mapX(x), mapY(truth(x)));
      }
      ctx.stroke();
      ctx.setLineDash([]);
      for (const [data, color] of [
        [validation, "#edac69"],
        [points, "#50dcba"],
      ]) {
        ctx.fillStyle = /** @type {string} */ (color);
        for (const p of /** @type {number[][]} */ (data)) {
          ctx.globalAlpha = data === points ? 1 : 0.6;
          ctx.beginPath();
          ctx.arc(
            mapX(p[0]),
            mapY(p[1]),
            data === points ? 4 : 2.5,
            0,
            Math.PI * 2,
          );
          ctx.fill();
        }
      }
      ctx.globalAlpha = 1;
      ctx.strokeStyle = "#7bb7fa";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let i = 0; i <= 500; i++) {
        const x = -1 + (2 * i) / 500,
          py = UI.clamp(mapY(pred(x)), -h * 10, h * 10);
        i === 0 ? ctx.moveTo(mapX(x), py) : ctx.lineTo(mapX(x), py);
      }
      ctx.stroke();
      ctx.restore();
      ctx.fillStyle = "#8398a4";
      ctx.fillText("x = −1", left, h - 9);
      ctx.fillText("x = 1", right - 35, h - 9);
      UI.$("#fit-degree-label").textContent = String(degree);
      UI.$("#fit-metrics").innerHTML =
        `<div class="metric-grid" style="grid-template-columns:1fr 1fr">${UI.metric("训练 MSE", UI.fmt(mse(points)))}${UI.metric("验证 MSE", UI.fmt(mse(validation)))}</div><p class="hint">参数 ${degree + 1} 个 · 固定纵轴 [-1.1, 1.1]，越界振荡被裁切。</p>`;
      host
        .querySelectorAll("[data-degree]")
        .forEach((el) =>
          el.classList.toggle(
            "active",
            Number(el.getAttribute("data-degree")) === degree,
          ),
        );
    }
    UI.input("#fit-degree").oninput = () => {
      degree = Number(UI.input("#fit-degree").value);
      draw();
    };
    host.querySelectorAll("[data-degree]").forEach((el) =>
      el.addEventListener("click", () => {
        degree = Number(el.getAttribute("data-degree"));
        UI.input("#fit-degree").value = String(degree);
        draw();
      }),
    );
    UI.button("#fit-data").onclick = () => {
      seed++;
      makeData();
      draw();
    };
    makeData();
    window.addEventListener("resize", draw);
    draw();
    return () => window.removeEventListener("resize", draw);
  }

  /** @param {HTMLElement} host */
  function tensor(host) {
    host.innerHTML = `<section class="panel fade-in"><div class="section-heading"><h2>从一个数字到一批图片</h2><span class="chip">补充实验</span></div><p class="hint">选择一个训练样本，观察同一组像素如何从矩阵展平为向量，再组织成批次张量。</p><div class="button-row" style="max-width:450px"><label class="field">数字<select id="tensor-digit">${Array.from({ length: 10 }, (_, i) => `<option>${i}</option>`).join("")}</select></label><label class="field">批次大小<select id="tensor-batch"><option>1</option><option selected>16</option><option>32</option><option>200</option></select></label></div><div class="tensor-grid"><div class="tensor-card"><h3>0 维 · 标量</h3><div class="tensor-shape">shape: []</div><div class="tensor-art" id="tensor-scalar"></div><p class="hint">一个像素的前景强度</p></div><div class="tensor-card"><h3>1 维 · 向量</h3><div class="tensor-shape">shape: [1600]</div><div class="tensor-art" id="tensor-vector" style="font-size:12px"></div><p class="hint">按行展开，与网络输入一致</p></div><div class="tensor-card"><h3>2 维 · 矩阵</h3><div class="tensor-shape">shape: [40, 40]</div><canvas id="tensor-image" style="width:120px;height:120px;image-rendering:pixelated"></canvas><p class="hint">单张灰度图片</p></div><div class="tensor-card"><h3>3 维 · 图片批次</h3><div class="tensor-shape" id="tensor-batch-shape"></div><div id="tensor-stack" style="height:115px;position:relative"></div><p class="hint" id="tensor-flat"></p></div></div><div class="notice" id="tensor-pipeline" style="margin-top:24px"></div><p class="hint">图片批次 [B,40,40] 在全连接网络中展平为 [B,1600]。本页用浏览器顺序累积梯度来展示批次语义，不声称在 GPU 上并行执行。</p></section>`;
    function render() {
      const digit = Number(UI.select("#tensor-digit").value),
        b = Number(UI.select("#tensor-batch").value),
        sample = DigitData.train[digit * 20],
        start = sample.pixels.findIndex((p) => p > 0.3);
      UI.$("#tensor-scalar").textContent = UI.fmt(sample.pixels[start], 3);
      UI.$("#tensor-vector").textContent = `…\n${sample.pixels
        .slice(start, start + 5)
        .map((v) => UI.fmt(v, 2))
        .join("  ")}\n…`;
      DigitData.draw(UI.canvas("#tensor-image"), sample);
      UI.$("#tensor-batch-shape").textContent = `shape: [${b}, 40, 40]`;
      UI.$("#tensor-stack").innerHTML = Array.from(
        { length: Math.min(5, b) },
        (_, i) =>
          `<div style="position:absolute;width:85px;height:78px;left:${i * 9}px;top:${i * 7}px;border:1px solid #50dcba80;background:#133b32ee;border-radius:5px;padding:10px;font:12px monospace">样本 ${i + 1}</div>`,
      ).join("");
      UI.$("#tensor-flat").textContent =
        `展平为 [${b}, 1600] · ${b * 1600} 个数`;
      UI.$("#tensor-pipeline").textContent =
        `[${b},1600] × W₁ᵀ → [${b},16] → [${b},16] → [${b},10] → ${b} 个样本损失 → 求平均 → 更新一次参数`;
    }
    UI.select("#tensor-digit").onchange = render;
    UI.select("#tensor-batch").onchange = render;
    render();
    return () => {};
  }
  return { landscape, fitting, tensor };
})();
