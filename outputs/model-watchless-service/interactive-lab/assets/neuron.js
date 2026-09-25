// @ts-check
"use strict";
const NeuronPage = (() => {
  /** @param {HTMLElement} host */
  function mount(host) {
    let inputs = [30, 750, 30],
      params = [0.9, 0.8, -0.55, 1.05];
    const names = ["收入", "信用分", "负债率"],
      units = ["万/年", "分", "%"];
    const ranges = [
      [0, 100, 1],
      [300, 950, 10],
      [0, 100, 1],
    ];
    host.innerHTML =
      UI.heading(
        "SINGLE NEURON · 感知机",
        "单个神经元 — 贷款审批决策",
        "改变一个输入，或转动一个旋钮，观察这个神经元如何响应。",
        "z = Σ wᵢxᵢ + b → y = ReLU(z) → 亮度 tanh(y)",
      ) +
      `<div class="lab-layout fade-in"><div><section class="board"><div class="board-toolbar"><span>三个输入 · 一个输出</span><strong>LIVE COMPUTATION</strong></div><div id="neuron-diagram"></div><div id="neuron-calcs" class="calc-strip"></div><div class="board-caption">输出 y 为教学示例中的数值，不是经过验证的贷款审批概率。节点亮度经过 tanh 映射，不改变 y。</div></section>${UI.panel("逐项计算", `<div id="neuron-equation" class="mono notice"></div><div class="table-scroll"><table class="detail-table"><thead><tr><th>特征</th><th>原始输入</th><th>归一化 x</th><th>权重 w</th><th>w × x</th></tr></thead><tbody id="neuron-terms"></tbody></table></div><p class="hint" style="margin:14px 0 0">收入 / 100；信用分 (分数 − 300) / 650；负债率 / 100。三个输入都映射到 [0, 1]。</p>`, "detail-panel")}</div><aside class="lab-sidebar">` +
      UI.panel(
        "输入特征 X",
        names
          .map(
            (name, i) =>
              `<label class="field"><span class="field-title"><span>X${i + 1} · ${name}</span><small id="contribution-${i}"></small></span><span class="input-stepper"><button type="button" data-input="${i}" data-direction="-1" aria-label="减少${name}">−</button><input id="feature-${i}" type="number" min="${ranges[i][0]}" max="${ranges[i][1]}" step="${ranges[i][2]}" value="${inputs[i]}" aria-label="${name}"><span class="unit">${units[i]}</span><button type="button" data-input="${i}" data-direction="1" aria-label="增加${name}">＋</button></span></label>`,
          )
          .join(""),
      ) +
      UI.panel(
        "权重 & 偏置",
        `<div class="knob-grid">${params.map((p, i) => `<div><button class="knob" id="knob-${i}" role="slider" aria-label="${i === 3 ? "偏置 b" : "权重 w" + (i + 1)}" aria-valuemin="-3" aria-valuemax="3" aria-valuenow="${p}"></button><div class="knob-caption">${i === 3 ? "b" : "w" + ["₁", "₂", "₃"][i]}</div><input class="knob-number" id="param-${i}" type="number" min="-3" max="3" step="0.01" value="${p}" aria-label="${i === 3 ? "偏置" : "权重" + (i + 1)}精确值"></div>`).join("")}</div><p class="hint" style="margin:16px 0 0">上下拖动旋钮 · 方向键微调 · 下方可直接输入</p>`,
      ) +
      UI.panel(
        "复现课堂场景",
        `<div class="button-row"><button id="preset-a">30 / 750 / 30</button><button id="preset-b">35 / 350 / 30</button></div><p class="hint">换输入，保留当前权重与偏置。对一个样本合适的参数，不一定适合另一个样本。</p><button class="full" id="neuron-reset">恢复全部初始值</button>`,
      ) +
      `</aside></div>`;

    function render() {
      const x = [inputs[0] / 100, (inputs[1] - 300) / 650, inputs[2] / 100];
      const terms = x.map((v, i) => v * params[i]),
        sum = terms.reduce((s, v) => s + v, 0),
        z = sum + params[3],
        y = Math.max(0, z),
        intensity = Math.tanh(y);
      const gray = Math.round(45 + intensity * 205);
      UI.$("#neuron-diagram").innerHTML =
        `<svg class="neuron-svg" viewBox="0 0 1100 620" role="img" aria-label="三个输入经权重汇入神经元，输出 ${UI.fmt(y)}"><defs><radialGradient id="neuron-glow"><stop stop-color="#c1ffe6" stop-opacity="${intensity * 0.22}"/><stop offset="1" stop-color="#50dcba" stop-opacity="0"/></radialGradient><marker id="neuron-tip" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#667882"/></marker></defs><circle cx="565" cy="310" r="180" fill="url(#neuron-glow)"/>${inputs
          .map((v, i) => {
            const py = 130 + i * 180,
              color = params[i] >= 0 ? "#70baa7" : "#c78169";
            return `<text x="135" y="${py + 8}" text-anchor="end" fill="#e4edf3" font-size="23">X${i + 1} = ${v}</text><line x1="154" y1="${py}" x2="478" y2="310" stroke="${color}" stroke-width="${1.5 + Math.abs(params[i])}"/><rect x="270" y="${(py + 310) / 2 - 17}" width="115" height="34" rx="17" fill="#101f24" stroke="${color}"/><text x="327" y="${(py + 310) / 2 + 6}" text-anchor="middle" fill="${color}" font-size="16">w${i + 1}=${params[i].toFixed(2)}</text>`;
          })
          .join(
            "",
          )}<circle cx="565" cy="310" r="90" fill="rgb(${gray},${gray + Math.round((255 - gray) * 0.03)},${gray + Math.round((255 - gray) * 0.05)})" stroke="#70818e" stroke-width="2"/><text x="565" y="305" text-anchor="middle" fill="${intensity > 0.45 ? "#31424c" : "#b5c8d1"}" font-size="13">${y > 0 ? "已激活" : "未激活"}</text><text x="565" y="331" text-anchor="middle" fill="${intensity > 0.45 ? "#31424c" : "#b5c8d1"}" font-size="11">ReLU</text><line x1="667" y1="310" x2="867" y2="310" stroke="#667882" stroke-width="3" marker-end="url(#neuron-tip)"/><text x="895" y="320" fill="#f0f7fa" font-size="27">y = ${y.toFixed(2)}</text><text x="565" y="440" fill="#9caaad" font-size="14" text-anchor="middle">b = ${UI.signed(params[3])}</text></svg>`;
      UI.$("#neuron-calcs").innerHTML = [
        ["加权和 Σwx", sum],
        ["加偏置 z", z],
        ["ReLU 输出 y", y],
        ["亮度 tanh(y)", intensity],
      ]
        .map(
          ([label, v]) =>
            `<div><div class="key">${label}</div><div class="value">${UI.fmt(Number(v), 3)}</div></div>`,
        )
        .join("");
      UI.$("#neuron-equation").textContent =
        `y = max(0, ${terms.map((v) => UI.fmt(v, 3)).join(" + ")} + (${UI.fmt(params[3], 2)})) = ${UI.fmt(y)}`;
      UI.$("#neuron-terms").innerHTML = names
        .map(
          (name, i) =>
            `<tr><td>${name}</td><td>${inputs[i]}</td><td>${UI.fmt(x[i])}</td><td>${UI.fmt(params[i], 2)}</td><td>${UI.signed(terms[i])}</td></tr>`,
        )
        .join("");
      params.forEach((p, i) => {
        const knob = UI.$(`#knob-${i}`),
          color = i === 3 ? "#edac69" : "#50dcba";
        knob.setAttribute("aria-valuenow", String(p));
        knob.innerHTML = `<svg viewBox="0 0 80 80" aria-hidden="true"><circle cx="40" cy="40" r="29" fill="none" stroke="#27363f" stroke-width="6" stroke-dasharray="137 183" transform="rotate(135 40 40)"/><circle cx="40" cy="40" r="29" fill="none" stroke="${color}" stroke-width="6" stroke-dasharray="${((p + 3) / 6) * 137} 183" transform="rotate(135 40 40)"/><text x="40" y="45" text-anchor="middle" fill="#e2edf1" font-family="monospace" font-size="12">${p.toFixed(2)}</text></svg>`;
        if (document.activeElement !== UI.input(`#param-${i}`))
          UI.input(`#param-${i}`).value = String(p);
      });
      inputs.forEach((v, i) => {
        if (document.activeElement !== UI.input(`#feature-${i}`))
          UI.input(`#feature-${i}`).value = String(v);
        UI.$(`#contribution-${i}`).textContent = `w·x = ${UI.signed(terms[i])}`;
      });
    }
    inputs.forEach((_, i) => {
      UI.input(`#feature-${i}`).addEventListener("input", () => {
        const el = UI.input(`#feature-${i}`);
        if (Number.isFinite(el.valueAsNumber)) {
          inputs[i] = UI.clamp(el.valueAsNumber, ranges[i][0], ranges[i][1]);
          render();
        }
      });
      UI.input(`#feature-${i}`).addEventListener("change", () => {
        inputs[i] = UI.number(UI.input(`#feature-${i}`), inputs[i]);
        render();
      });
    });
    host.querySelectorAll("[data-input]").forEach((el) =>
      el.addEventListener("click", () => {
        const b = /** @type {HTMLElement} */ (el),
          i = Number(b.dataset.input);
        inputs[i] = UI.clamp(
          inputs[i] + Number(b.dataset.direction) * ranges[i][2],
          ranges[i][0],
          ranges[i][1],
        );
        render();
      }),
    );
    params.forEach((_, i) => {
      const knob = UI.button(`#knob-${i}`);
      let startY = 0,
        startValue = 0,
        dragging = false;
      /** @param {number} v */
      function set(v) {
        params[i] = Math.round(UI.clamp(v, -3, 3) * 100) / 100;
        render();
      }
      knob.addEventListener("pointerdown", (e) => {
        dragging = true;
        startY = e.clientY;
        startValue = params[i];
        knob.setPointerCapture(e.pointerId);
      });
      knob.addEventListener("pointermove", (e) => {
        if (dragging) set(startValue + (startY - e.clientY) * 0.02);
      });
      knob.addEventListener("pointerup", () => {
        dragging = false;
      });
      knob.addEventListener("pointercancel", () => {
        dragging = false;
      });
      knob.addEventListener("lostpointercapture", () => {
        dragging = false;
      });
      knob.addEventListener("keydown", (e) => {
        if (
          [
            "ArrowUp",
            "ArrowRight",
            "ArrowDown",
            "ArrowLeft",
            "Home",
            "End",
          ].includes(e.key)
        ) {
          e.preventDefault();
          set(
            e.key === "Home"
              ? -3
              : e.key === "End"
                ? 3
                : params[i] +
                  (["ArrowUp", "ArrowRight"].includes(e.key) ? 1 : -1) *
                    (e.shiftKey ? 0.1 : 0.01),
          );
        }
      });
      UI.input(`#param-${i}`).addEventListener("change", () =>
        set(UI.number(UI.input(`#param-${i}`), params[i])),
      );
    });
    UI.button("#preset-a").onclick = () => {
      inputs = [30, 750, 30];
      render();
    };
    UI.button("#preset-b").onclick = () => {
      inputs = [35, 350, 30];
      render();
    };
    UI.button("#neuron-reset").onclick = () => {
      inputs = [30, 750, 30];
      params = [0.9, 0.8, -0.55, 1.05];
      render();
    };
    render();
    return () => {};
  }
  return { mount };
})();
