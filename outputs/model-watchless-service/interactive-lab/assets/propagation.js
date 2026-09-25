// @ts-check
"use strict";
const NetworkView = (() => {
  const sampled = [165, 350, 535, 720, 905, 1090, 1275, 1460];
  const xs = [250, 490, 730, 970],
    counts = [8, 16, 16, 10];
  /** @param {number} l @param {number} j */
  function py(l, j) {
    return 390 + (j - (counts[l] - 1) / 2) * 39;
  }
  /** @param {NNModel} model @param {NNTrace} trace @param {number} step @param {boolean} backward @param {NNGradient|null} gradient @param {number} label */
  function svg(model, trace, step, backward, gradient, label) {
    const visible = backward
      ? [step >= 5, step >= 5, step >= 3, true]
      : [true, step >= 1, step >= 2, step >= 3];
    let s = `<svg class="network-svg" viewBox="0 0 1180 780" aria-label="${backward ? "反向" : "前向"}传播神经网络"><defs><filter id="nodeGlow"><feGaussianBlur stdDeviation="4"/></filter></defs>`;
    for (let l = 1; l < 4; l++)
      if (visible[l] && visible[l - 1]) {
        for (let j = 0; j < counts[l]; j++)
          for (let i = 0; i < counts[l - 1]; i++) {
            const actual = l === 1 ? sampled[i] : i,
              v = trace.a[l - 1][actual];
            s += `<line x1="${xs[l - 1]}" y1="${py(l - 1, i)}" x2="${xs[l]}" y2="${py(l, j)}" stroke="${backward ? "#658478" : "#d9e6ee"}" stroke-opacity="${backward ? 0.12 : 0.035 + 0.32 * v}" stroke-width="${backward ? 0.6 : 0.8}"/>`;
            if (!backward && l === step && j < 3 && i < 4)
              s += `<line class="flow-wire" pathLength="1" x1="${xs[l - 1]}" y1="${py(l - 1, i)}" x2="${xs[l]}" y2="${py(l, j)}" stroke="#8fffe0" stroke-width="1.5" style="animation-delay:${j * 0.09}s"/>`;
          }
      }
    for (let l = 0; l < 4; l++) {
      s += `<text x="${xs[l]}" y="746" text-anchor="middle" fill="#82949f" font-size="13">${["输入层", "隐藏层 1", "隐藏层 2", "输出层"][l]}</text>`;
      s += `<text x="${xs[l]}" y="766" text-anchor="middle" fill="#4f6572" font-size="10">${["抽样 8 / 1600", "16 neurons", "16 neurons", "0—9 · Softmax"][l]}</text>`;
      for (let j = 0; j < counts[l]; j++) {
        const actual = l === 0 ? sampled[j] : j,
          value = trace.a[l][actual];
        const shade = Math.round(
          47 +
            Math.min(1, l === 3 ? value / Math.max(...trace.a[3]) : value) *
              196,
        );
        const active = visible[l],
          text = l === 3 ? j : j + 1;
        s += `<g class="node" tabindex="0" role="button" aria-label="${["输入像素", "隐藏层一节点", "隐藏层二节点", "输出类别"][l]} ${l === 0 ? actual : text}，${active ? UI.fmt(value) : "尚未展示"}" data-layer="${l}" data-node="${actual}" opacity="${active ? 1 : 0.16}">`;
        if (active && value > 0.5)
          s += `<circle cx="${xs[l]}" cy="${py(l, j)}" r="18" fill="#ddfff0" opacity="${value * 0.23}" filter="url(#nodeGlow)"/>`;
        s += `<circle cx="${xs[l]}" cy="${py(l, j)}" r="14" fill="${active ? `rgb(${shade},${shade + 3},${shade + 7})` : "#25313b"}" stroke="#52636d" stroke-width=".6"/><text x="${xs[l]}" y="${py(l, j) + 4}" font-size="11" text-anchor="middle" fill="${active && shade > 160 ? "#15212a" : "#cbd6df"}">${text}</text></g>`;
        if (l === 3 && active) {
          s += `<text x="${xs[l] + 24}" y="${py(l, j) + 4}" fill="${j === NN.argmax(trace.a[3]) ? "#f4ffff" : "#a7bdca"}" font-size="${j === NN.argmax(trace.a[3]) ? 14 : 11}">${(value * 100).toFixed(1)}%</text>`;
          if (backward && step >= 1)
            s += `<circle cx="1080" cy="${py(l, j)}" r="13" fill="${j === label ? "#d6f4e9" : "#283640"}"/><text x="1080" y="${py(l, j) + 4}" text-anchor="middle" font-size="11" fill="${j === label ? "#183c30" : "#7f919f"}">${Number(j === label)}</text>`;
        }
        if (backward && gradient && l > 0 && active) {
          if (l === 3 && step >= 2)
            s += arrow(xs[l] - 34, py(l, j), gradient.desires[2][j], 2);
          if (l === 2 && step >= 3) {
            if (step === 3) {
              const c = model.weights[2].map(
                (row, k) => -row[j] * gradient.delta[2][k],
              );
              s += contributions(xs[l] - 35, py(l, j), c);
            } else
              s += arrow(
                xs[l] - 34,
                py(l, j),
                gradient.desires[1][j],
                Math.max(0.001, ...gradient.desires[1].map(Math.abs)),
              );
          }
          if (l === 1 && step >= 5) {
            if (step === 5) {
              const c = model.weights[1].map(
                (row, k) => -row[j] * gradient.delta[1][k],
              );
              s += contributions(xs[l] - 35, py(l, j), c);
            } else
              s += arrow(
                xs[l] - 34,
                py(l, j),
                gradient.desires[0][j],
                Math.max(0.001, ...gradient.desires[0].map(Math.abs)),
              );
          }
        }
      }
    }
    if (backward && step >= 1)
      s += `<text x="1080" y="746" text-anchor="middle" fill="#82949f" font-size="13">标签</text>`;
    return s + "</svg>";
  }
  /** @param {number} x @param {number} y @param {number} v @param {number} max */
  function arrow(x, y, v, max) {
    const len = 3 + Math.min(1, Math.abs(v) / (max || 1)) * 20,
      color = v >= 0 ? "#50dcba" : "#edac69",
      end = y + (v >= 0 ? -len / 2 : len / 2),
      start = y + (v >= 0 ? len / 2 : -len / 2),
      d = v >= 0 ? 1 : -1;
    if (Math.abs(v) < 1e-12)
      return `<circle cx="${x}" cy="${y}" r="2" fill="#506774"/>`;
    return `<path d="M${x},${start} L${x},${end} M${x - 3},${end + 4 * d} L${x},${end} L${x + 3},${end + 4 * d}" fill="none" stroke="${color}" stroke-width="2" stroke-linecap="round"><title>−∂L/∂a = ${v}</title></path>`;
  }
  /** @param {number} x @param {number} y @param {number[]} values */
  function contributions(x, y, values) {
    const max = Math.max(0.0001, ...values.map(Math.abs));
    return (
      values
        .slice(0, 3)
        .map((v, i) => arrow(x - i * 11, y, v, max))
        .join("") +
      `<text x="${x - 40}" y="${y + 4}" font-size="10" fill="#82949f">…</text>`
    );
  }
  /** @param {NNGradient} gradient @param {number} rate */
  function updateCards(gradient, rate) {
    return `<div class="update-grid">${gradient.dw
      .map((w, l) => {
        // 背景像素梯度常为零，摘要选幅度最大的三列，避免把稀疏性误看成未更新。
        const columns = w[0]
          .map((_, i) => i)
          .sort((a, b) =>
            w
              .slice(0, 3)
              .reduce((s, row) => s + Math.abs(row[b]) - Math.abs(row[a]), 0),
          )
          .slice(0, 3)
          .sort((a, b) => a - b);
        return `<div class="update-card"><h4>${["隐藏层 1", "隐藏层 2", "输出层"][l]} 参数调整</h4><small>ΔW · 前 3 行 / 抽样列 ${columns.join(",")}</small><div class="update-values">${w
          .slice(0, 3)
          .flatMap((row) => columns.map((i) => row[i]))
          .map((v) => delta(-rate * v))
          .join(
            "",
          )}</div><small>偏置调整 Δb · 前 3 项</small><div class="update-values bias-values">${gradient.db[
          l
        ]
          .slice(0, 3)
          .map((v) => delta(-rate * v))
          .join("")}</div></div>`;
      })
      .join("")}</div>`;
  }
  /** @param {number} v */
  function delta(v) {
    return `<span class="delta ${v >= 0 ? "up" : "down"}">${UI.signed(v)} ${v >= 0 ? "▴" : "▾"}</span>`;
  }
  return { svg, updateCards, sampled };
})();

const PropagationPage = (() => {
  let sharedModel = NN.create(42);
  /** @param {HTMLElement} host @param {boolean} backward */
  function mount(host, backward = false) {
    let step = 0,
      sampleIndex = backward ? 20 : 80,
      rate = 0.3,
      applied = false,
      timer = 0,
      playing = false,
      training = false,
      rounds = 0,
      selectedLayer = 1,
      selectedNode = 0,
      offset = 0,
      disposed = false;
    let base = NN.clone(sharedModel),
      trace = NN.forward(base, DigitData.train[sampleIndex].pixels),
      gradient = NN.backward(base, trace, DigitData.train[sampleIndex].label),
      after = trace;
    let history = [NN.loss(trace.a[3], DigitData.train[sampleIndex].label)];
    const names = backward
      ? [
          "① 前向计算，得到预测",
          "② 对照标签，计算损失",
          "③ 对输出层的调整方向",
          "④ 隐藏层 2 接收各项贡献",
          "⑤ 隐藏层 2 汇总贡献",
          "⑥ 隐藏层 1 接收各项贡献",
          "⑦ 隐藏层 1 汇总贡献",
          "⑧ 更新所有参数",
        ]
      : [
          "① 输入像素，点亮输入层",
          "② 计算并点亮隐藏层 1",
          "③ 计算并点亮隐藏层 2",
          "④ 输出层点亮，得到概率",
        ];
    host.innerHTML =
      UI.heading(
        backward
          ? "BACK PROPAGATION · 反向传播"
          : "FORWARD PROPAGATION · 前向传播",
        backward
          ? "全连接神经网络 — 误差向后流动"
          : "全连接神经网络 — 信号向前流动",
        backward
          ? "把误差逐层传回去，再沿负梯度方向调整每一个参数。"
          : "一张图片，26,058 个参数，一次从左到右的计算。",
        backward
          ? "θ ← θ − η∇L · L = Σ (pᵢ − yᵢ)²"
          : "a⁽ˡ⁾ = σ(W⁽ˡ⁾a⁽ˡ⁻¹⁾ + b⁽ˡ⁾)",
      ) +
      (backward
        ? `<div class="subnav" id="backward-tabs"><button class="active" data-tab="network">网络反向传播</button><button data-tab="landscape">二维 / 三维下山 <span class="chip">补充实验</span></button></div><div id="landscape-host" hidden></div>`
        : "") +
      `<div id="prop-content"><div class="lab-layout fade-in"><div><section class="board"><div class="board-toolbar"><span>1600 → 16 → 16 → 10</span><strong>${backward ? "GRADIENT FLOW" : "SIGNAL FLOW"}</strong></div><div style="position:relative"><div id="network-diagram"></div><div class="sample-anchor"><canvas id="prop-sample" aria-label="输入数字样本"></canvas>输入样本</div><div id="update-overlay" class="update-overlay" hidden></div></div><div class="board-caption" id="prop-caption"></div></section><section id="node-inspector" class="panel detail-panel"></section></div><aside class="lab-sidebar">` +
      UI.panel(
        "操作区",
        `<div id="prop-steps"></div><div class="button-row"><button id="prop-prev">上一步</button><button id="prop-next" class="primary">下一步</button></div><div class="button-row"><button id="prop-play">自动播放</button><button id="prop-reset">重置</button></div>`,
      ) +
      UI.panel(
        "输入与参数",
        `<label class="field">选择数字样本<select id="prop-digit" class="full">${Array.from({ length: 10 }, (_, i) => `<option value="${i}">${i} · 合成手写数字</option>`).join("")}</select></label><div class="button-row"><button id="prop-variant">换一种写法</button><button id="prop-random">重新随机参数</button></div><div class="hint" id="prop-seed"></div>`,
      ) +
      (backward
        ? UI.panel(
            "训练控制",
            `<label class="field">学习率 η<input id="prop-rate" type="number" min="0.0001" max="10" step="0.01" value="0.3"></label><div class="button-row"><button id="prop-once">训练一轮</button><button id="prop-train" class="primary">连续训练</button></div><div id="prop-metrics"></div><div class="error" id="prop-error" role="status"></div><canvas class="chart" id="prop-history" aria-label="同一样本损失随更新次数的变化"></canvas><p class="hint">同一样本的平方和损失。高学习率可能使损失上升；不强制生成下降曲线。</p>`,
            "wide",
          )
        : UI.panel(
            "网络参数",
            `<table class="detail-table"><tbody><tr><td>隐藏层 1</td><td>1600×16+16</td></tr><tr><td>隐藏层 2</td><td>16×16+16</td></tr><tr><td>输出层</td><td>16×10+10</td></tr><tr><td>总参数</td><td class="up">26,058</td></tr></tbody></table><p class="hint" style="margin-top:14px">初始参数来自固定随机种子，尚未经过训练。输出概率最高不代表识别正确。</p>`,
          )) +
      `</aside></div></div>`;
    UI.select("#prop-digit").value = String(DigitData.train[sampleIndex].label);
    let landscapeDispose = () => {};
    function stop() {
      clearTimeout(timer);
      playing = false;
      training = false;
      if (!disposed) {
        UI.button("#prop-play").textContent = "自动播放";
        if (backward) UI.button("#prop-train").textContent = "连续训练";
      }
    }
    function snapshot() {
      base = NN.clone(sharedModel);
      trace = NN.forward(base, DigitData.train[sampleIndex].pixels);
      gradient = NN.backward(base, trace, DigitData.train[sampleIndex].label);
      after = trace;
      applied = false;
    }
    function commit() {
      if (applied) return;
      NN.apply(sharedModel, gradient, rate);
      applied = true;
      rounds++;
      after = NN.forward(sharedModel, DigitData.train[sampleIndex].pixels);
      history.push(NN.loss(after.a[3], DigitData.train[sampleIndex].label));
    }
    function render() {
      const sample = DigitData.train[sampleIndex];
      UI.$("#network-diagram").innerHTML = NetworkView.svg(
        base,
        trace,
        step,
        backward,
        gradient,
        sample.label,
      );
      DigitData.draw(UI.canvas("#prop-sample"), sample);
      UI.$("#prop-steps").innerHTML = UI.steps(step, names);
      UI.button("#prop-prev").disabled = step === 0;
      UI.button("#prop-next").disabled = step === names.length - 1;
      UI.$("#prop-seed").textContent =
        `种子 ${sharedModel.seed} · 样本 ${sample.id} · Sigmoid → Softmax`;
      UI.$("#prop-caption").textContent = backward
        ? "箭头表示 −∂L/∂a：青绿向上，橙色向下。多箭头展示前 3 项贡献，汇总使用全部贡献；显示长度按当前组缩放。"
        : "输入图为 40×40；为便于阅读，连线只展示 8 个抽样像素，实际计算使用全部 1600 个输入。点击任意节点查看数值。";
      const overlay = UI.$("#update-overlay");
      overlay.hidden = !(backward && step === 7);
      if (backward) {
        const beforeLoss = NN.loss(trace.a[3], sample.label),
          afterLoss = NN.loss(after.a[3], sample.label);
        overlay.innerHTML = `<h3>参数已按负梯度更新 · η = ${rate}</h3>${NetworkView.updateCards(gradient, rate)}<p class="hint" style="text-align:center;margin:20px 0 0">损失 ${UI.fmt(beforeLoss)} → ${UI.fmt(afterLoss)} · 预测 ${NN.argmax(trace.a[3])} → ${NN.argmax(after.a[3])}</p>`;
        UI.$("#prop-metrics").innerHTML =
          `<div class="metric-grid">${UI.metric("更新次数", String(rounds))}${UI.metric("更新前损失", UI.fmt(beforeLoss))}${UI.metric("当前损失", UI.fmt(afterLoss))}</div>`;
        UI.plot(UI.canvas("#prop-history"), [
          { values: history, color: "#50dcba" },
        ]);
      }
      host.querySelectorAll(".node").forEach((el) => {
        const choose = () => {
          selectedLayer = Number(el.getAttribute("data-layer"));
          selectedNode = Number(el.getAttribute("data-node"));
          offset = 0;
          inspect();
        };
        el.addEventListener("click", choose);
        el.addEventListener("keydown", (e) => {
          const event = /** @type {KeyboardEvent} */ (e);
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            choose();
          }
        });
      });
      inspect();
    }
    function inspect() {
      const panel = UI.$("#node-inspector"),
        l = selectedLayer,
        j = selectedNode;
      if (l === 0) {
        panel.innerHTML = `<div class="panel-title"><i class="status-dot"></i>输入像素 ${j} · 行 ${Math.floor(j / 40) + 1} / 列 ${(j % 40) + 1}</div><div class="notice">前景强度 ${UI.fmt(trace.a[0][j])}。输入是数据，不带可训练权重与偏置。</div>`;
        return;
      }
      const weights = base.weights[l - 1][j],
        prev = trace.a[l - 1],
        g = gradient;
      const rows = weights
        .slice(offset, offset + 16)
        .map((w, k) => {
          const i = offset + k;
          return `<tr><td>${i}</td><td>${UI.fmt(prev[i])}</td><td>${UI.fmt(w)}</td><td>${UI.fmt(w * prev[i])}</td>${backward ? `<td>${UI.signed(-rate * g.dw[l - 1][j][i])}</td>` : ""}</tr>`;
        })
        .join("");
      const sum = trace.z[l - 1][j],
        a = trace.a[l][j],
        bias = base.biases[l - 1][j];
      panel.innerHTML = `<div class="panel-title"><i class="status-dot"></i>${l === 3 ? "输出类别 " + j : "隐藏层 " + l + " · 神经元 " + (j + 1)}<span class="chip">计算快照 · 更新前</span></div><div class="metric-grid">${UI.metric("偏置 b", UI.fmt(bias))}${UI.metric("加权和 + 偏置 z", UI.fmt(sum))}${UI.metric(l === 3 ? "Softmax 概率" : "Sigmoid 激活", UI.fmt(a))}</div><div class="detail-grid" style="margin-top:20px"><div><h3>输入逐项展开</h3><div class="button-row"><button id="terms-prev" ${offset === 0 ? "disabled" : ""}>← 前 16 项</button><button id="terms-next" ${offset + 16 >= weights.length ? "disabled" : ""}>后 16 项 →</button></div><div class="table-scroll"><table class="detail-table"><thead><tr><th>i</th><th>aᵢ</th><th>wᵢ</th><th>wᵢaᵢ</th>${backward ? "<th>Δwᵢ</th>" : ""}</tr></thead><tbody>${rows}</tbody></table></div><p class="hint">当前 ${offset + 1}—${Math.min(offset + 16, weights.length)} / ${weights.length} 项。完整求和使用所有项。</p></div><div><h3>整层矩阵运算</h3><p class="mono hint">W [${base.sizes[l]} × ${base.sizes[l - 1]}] × a [${base.sizes[l - 1]} × 1] + b [${base.sizes[l]} × 1]</p><div class="button-row"><label class="field">矩阵行起点<input id="matrix-row" type="number" min="1" max="${base.sizes[l]}" value="1"></label><label class="field">矩阵列起点<input id="matrix-col" type="number" min="1" max="${base.sizes[l - 1]}" value="${offset + 1}"></label></div><div class="matrix-wrap" id="layer-matrix">${UI.matrix(base.weights[l - 1].map((row) => row.slice(offset, offset + 8)))}</div><p class="hint">显示最多 8 行 × 8 列，可调整行列起点浏览所有参数。${l === 3 ? "输出使用同层所有 logits 共同计算 Softmax。" : "每一行对应一个神经元。"}</p>${backward ? `<p class="notice mono">∂L/∂z = ${UI.fmt(g.delta[l - 1][j])}<br>Δb = ${UI.signed(-rate * g.db[l - 1][j])}<br>−∂L/∂a = ${UI.fmt(g.desires[l - 1][j])}</p>` : ""}</div></div>`;
      UI.button("#terms-prev").onclick = () => {
        offset = Math.max(0, offset - 16);
        inspect();
      };
      UI.button("#terms-next").onclick = () => {
        offset = Math.min(weights.length - 1, offset + 16);
        inspect();
      };
      function matrixWindow() {
        const start = Math.floor(UI.number(UI.input("#matrix-row"), 1)) - 1,
          col = Math.floor(UI.number(UI.input("#matrix-col"), 1)) - 1;
        UI.$("#layer-matrix").innerHTML = UI.matrix(
          base.weights[l - 1]
            .slice(start, start + 8)
            .map((row) => row.slice(col, col + 8)),
        );
      }
      UI.input("#matrix-row").onchange = matrixWindow;
      UI.input("#matrix-col").onchange = matrixWindow;
    }
    function advance() {
      if (step < names.length - 1) {
        step++;
        if (backward && step === 7) commit();
        render();
      }
    }
    /** @param {()=>void} action */
    function safe(action) {
      try {
        action();
      } catch (e) {
        stop();
        if (backward)
          UI.$("#prop-error").textContent =
            e instanceof Error ? e.message : String(e);
      }
    }
    function tick() {
      if (disposed || !playing) return;
      safe(() => {
        advance();
        if (step < names.length - 1) timer = window.setTimeout(tick, 1000);
        else stop();
      });
    }
    function trainingTick() {
      if (disposed || !training) return;
      safe(() => {
        snapshot();
        commit();
        step = 7;
        render();
        timer = window.setTimeout(trainingTick, 120);
      });
    }
    function changed() {
      stop();
      step = 0;
      snapshot();
      history = [NN.loss(trace.a[3], DigitData.train[sampleIndex].label)];
      rounds = 0;
      if (backward) UI.$("#prop-error").textContent = "";
      render();
    }
    UI.button("#prop-next").onclick = () => {
      stop();
      safe(advance);
    };
    UI.button("#prop-prev").onclick = () => {
      stop();
      step = Math.max(0, step - 1);
      render();
    };
    UI.button("#prop-play").onclick = () => {
      if (playing) {
        stop();
        return;
      }
      stop();
      if (step === names.length - 1) {
        if (backward) snapshot();
        step = 0;
        render();
      }
      playing = true;
      UI.button("#prop-play").textContent = "暂停播放";
      timer = window.setTimeout(tick, 800);
    };
    UI.button("#prop-reset").onclick = () => {
      sharedModel = NN.create(42);
      sampleIndex = backward ? 20 : 80;
      rate = 0.3;
      UI.select("#prop-digit").value = String(
        DigitData.train[sampleIndex].label,
      );
      if (backward) UI.input("#prop-rate").value = "0.3";
      changed();
    };
    UI.button("#prop-random").onclick = () => {
      sharedModel = NN.create(sharedModel.seed + 1);
      changed();
    };
    UI.select("#prop-digit").onchange = () => {
      sampleIndex = Number(UI.select("#prop-digit").value) * 20;
      changed();
    };
    UI.button("#prop-variant").onclick = () => {
      sampleIndex =
        Math.floor(sampleIndex / 20) * 20 + (((sampleIndex % 20) + 1) % 20);
      changed();
    };
    if (backward) {
      UI.input("#prop-rate").onchange = () => {
        rate = UI.number(UI.input("#prop-rate"), rate);
        stop();
        step = 0;
        snapshot();
        render();
      };
      UI.button("#prop-once").onclick = () => {
        stop();
        safe(() => {
          if (applied) snapshot();
          commit();
          step = 7;
          render();
        });
      };
      UI.button("#prop-train").onclick = () => {
        if (training) {
          stop();
          return;
        }
        stop();
        training = true;
        UI.button("#prop-train").textContent = "暂停训练";
        trainingTick();
      };
      host.querySelectorAll("#backward-tabs button").forEach((el) =>
        el.addEventListener("click", () => {
          stop();
          landscapeDispose();
          const landscape = el.getAttribute("data-tab") === "landscape";
          UI.$("#prop-content").hidden = landscape;
          UI.$("#landscape-host").hidden = !landscape;
          host
            .querySelectorAll("#backward-tabs button")
            .forEach((b) => b.classList.toggle("active", b === el));
          if (landscape)
            landscapeDispose = Experiments.landscape(UI.$("#landscape-host"));
          else {
            landscapeDispose = () => {};
            render();
          }
        }),
      );
    }
    const resize = () => {
      if (backward && !UI.$("#prop-content").hidden)
        UI.plot(UI.canvas("#prop-history"), [
          { values: history, color: "#50dcba" },
        ]);
    };
    window.addEventListener("resize", resize);
    render();
    return () => {
      stop();
      disposed = true;
      landscapeDispose();
      window.removeEventListener("resize", resize);
    };
  }
  return { mount };
})();
