// @ts-check
"use strict";
const TrainingPage = (() => {
  /** @param {HTMLElement} host */
  function mount(host) {
    let model = NN.create(42),
      mode = "mini",
      batchSize = 16,
      rate = 0.3,
      shuffle = true,
      subset = "all",
      inference = false;
    let updates = 0,
      epoch = 0,
      cursor = 0,
      selected = 80,
      running = false,
      busy = false,
      generation = 0,
      disposed = false,
      timer = 0;
    /** @type {number[]} */ let order = [],
      losses = [],
      accuracies = [],
      active = [];
    /** @type {{index:number,gradient:NNGradient,loss:number}[]} */ let individual =
      [];
    /** @type {NNGradient|null} */ let average = null;
    /** @type {{loss:number,accuracy:number,perClass:number[]}|null} */
    let lastEvaluation = null;
    let lastBefore = 0,
      lastAfter = 0,
      lastRate = rate;
    let childDispose = () => {},
      tab = "batch";
    host.innerHTML =
      UI.heading(
        "TRAINING MODES · 训练模式",
        "把不同样本的意见，汇成一次更新",
        "同一个网络，同一份数据。改变的是：计算多少个样本之后，再更新参数。",
        "θ ← θ − η · mean(∇L₁, …, ∇Lᴮ)",
      ) +
      `<div class="subnav" id="training-tabs"><button data-tab="batch" class="active">批次与训练</button><button data-tab="tensor">张量组织</button><button data-tab="fitting">拟合与泛化</button></div><div id="training-extra" hidden></div><div id="training-content"><div class="lab-layout fade-in"><div class="training-main"><section class="board"><div class="board-toolbar"><span>训练集 <strong>200</strong> · 独立验证集 <strong>50</strong> · 固定合成笔画</span><span id="batch-position">等待第一次更新</span></div><div id="dataset-grid" class="data-grid"></div><div class="board-caption">青绿描边是最近一次更新使用的批次，蓝框是当前查看的样本。点击样本，只做推理查看预测。</div></section><section class="panel"><div class="panel-title"><i class="status-dot"></i>观察训练过程</div><div id="training-metrics" class="metric-grid"></div><div class="training-charts"><div><div class="chart-legend"><span>验证集平均损失</span></div><canvas id="training-loss" class="chart" aria-label="验证损失曲线"></canvas></div><div><div class="chart-legend"><span class="orange">验证集准确率</span></div><canvas id="training-accuracy" class="chart" aria-label="验证准确率曲线"></canvas></div></div><div id="class-accuracy" class="hint"></div></section><section class="panel" id="batch-inspector"></section><section class="panel"><div class="section-heading"><h2>同起点公平对比</h2><span class="chip">补充实验</span></div><p class="hint">三个独立网络都从种子 42 开始，以相同数据顺序各看完整的 200 个样本。这里只比较一轮；它们的更新次数不同，不预设哪种方式一定获胜。</p><div class="button-row"><button id="compare-modes">比较三种训练模式 · 各 1 epoch</button><button id="compare-order">比较打乱 / 按类别 · 各 1 epoch</button></div><p id="comparison-status" class="hint" role="status"></p><div id="comparison-table"></div></section><section class="panel"><div class="section-heading"><h2>先学会 0，再学习 1</h2><span class="chip">遗忘实验</span></div><p class="hint">阶段切换保留参数。观察右侧 0、1 验证准确率：学习新类别时，旧类别的能力可能改变。混合训练按钮从相同初始参数重新开始。</p><div class="button-row"><button id="forget-zero">阶段 1 · 只练 0</button><button id="forget-one">阶段 2 · 接着练 1</button><button id="forget-mixed">对照 · 混合 0 和 1</button></div><p id="forget-status" class="notice">当前使用全部 10 类。选定阶段后，可单批更新或连续训练。</p></section></div><aside class="lab-sidebar">` +
      UI.panel(
        "训练控制",
        `<div class="segmented"><button id="mode-train" class="active">训练</button><button id="mode-infer">仅推理</button></div><label class="field">更新方式<select id="training-mode" class="full"><option value="sgd">SGD · 每个样本更新</option><option value="mini" selected>小批量 · 每一批更新</option><option value="full">全批量 · 全部样本后更新</option></select></label><label class="field">小批量大小<input id="training-batch" type="number" min="1" max="200" step="1" value="16"></label><label class="field">学习率 η<input id="training-rate" type="number" min="0.0001" max="10" step="0.01" value="0.3"></label><label class="checkbox"><input id="training-shuffle" type="checkbox" checked>每轮随机打乱样本</label><div class="button-row"><button id="training-once">更新一批</button><button id="training-run" class="primary">连续训练</button></div><button id="training-reset" class="full">重置为相同起点</button><p class="hint">更改方式、批次、学习率或顺序，会重置为种子 42，便于比较。暂停会丢弃尚未提交的批次。</p><div id="training-status" class="error" role="status"></div>`,
      ) +
      UI.panel(
        "当前样本 · 推理",
        `<div class="sample-preview"><canvas id="training-sample"></canvas><div><h3 id="sample-title"></h3><div id="sample-result" class="hint"></div></div></div><div id="sample-bars" style="margin-top:17px"></div><p class="hint" id="inference-note">使用当前参数，只执行前向传播。</p>`,
      ) +
      UI.panel(
        "模型文件",
        `<div class="button-row"><button id="model-export">导出 JSON</button><button id="model-import">导入 JSON</button></div><input type="file" id="model-file" accept=".json,application/json" hidden><p class="hint">包含架构、预处理规则、权重与偏置。导入后自动进入推理模式。</p><div id="model-status" class="hint" role="status"></div><details><summary>网络架构与学习框架</summary><p>架构规定层数、连接和运算；框架负责执行运算与自动求导。本实验在浏览器中直接实现全连接网络的前向与反向计算。</p></details><details><summary>训练和推理的区别</summary><p>训练计算损失、梯度并更新参数。推理固定这些参数，只计算输入到输出；导入模型不会自动执行训练。</p></details><details><summary>为什么还需要配置文件</summary><p>只有一串权重数字无法重建网络，还需要层尺寸、激活函数和像素预处理。这里把这些配置与权重一起保存进 JSON。</p></details>`,
        "wide",
      ) +
      `</aside></div></div>`;

    /** @param {string} selection */
    function indices(selection) {
      return DigitData.train
        .map((_, i) => i)
        .filter(
          (i) =>
            selection === "all" ||
            (selection === "mixed" && DigitData.train[i].label < 2) ||
            String(DigitData.train[i].label) === selection,
        );
    }
    function makeOrder() {
      const items = indices(subset);
      order = shuffle ? DigitData.shuffle(items, 2026 + epoch) : items;
    }
    function stop() {
      generation++;
      clearTimeout(timer);
      running = false;
      busy = false;
      if (!disposed) {
        host
          .querySelectorAll(".sample-cell.pending")
          .forEach((el) => el.classList.remove("pending"));
        UI.button("#training-run").textContent = "连续训练";
        controls();
      }
    }
    /** @param {number} token */
    function check(token) {
      if (disposed || token !== generation) throw new Error("cancelled");
    }
    /** @param {number} token */
    async function yieldFrame(token) {
      await new Promise((resolve) => setTimeout(resolve, 0));
      check(token);
    }
    /** @param {NNModel} target @param {number} token */
    async function evaluate(target, token) {
      let total = 0,
        correct = 0;
      const perClass = Array(10).fill(0);
      for (let i = 0; i < DigitData.validation.length; i++) {
        check(token);
        const sample = DigitData.validation[i],
          p = NN.forward(target, sample.pixels).a[3];
        total += NN.loss(p, sample.label);
        if (NN.argmax(p) === sample.label) {
          correct++;
          perClass[sample.label]++;
        }
        if (i % 5 === 4) await yieldFrame(token);
      }
      return {
        loss: total / 50,
        accuracy: correct / 50,
        perClass: perClass.map((n) => n / 5),
      };
    }
    /** @param {NNModel} target @param {number[]} batch @param {number} token @param {boolean} [capture] */
    async function gradients(target, batch, token, capture = false) {
      const avg = NN.zeros(target),
        details = [];
      let loss = 0;
      for (let i = 0; i < batch.length; i++) {
        check(token);
        const index = batch[i],
          sample = DigitData.train[index],
          trace = NN.forward(target, sample.pixels),
          g = NN.backward(target, trace, sample.label),
          value = NN.loss(trace.a[3], sample.label);
        NN.addGradient(avg, g, 1 / batch.length);
        loss += value / batch.length;
        if (capture) details.push({ index, gradient: g, loss: value });
        if (i % 3 === 2) await yieldFrame(token);
      }
      return { avg, details, loss };
    }
    /** @param {NNModel} target @param {number[]} batch @param {number} token */
    async function batchLoss(target, batch, token) {
      let sum = 0;
      for (let i = 0; i < batch.length; i++) {
        check(token);
        const s = DigitData.train[batch[i]];
        sum += NN.loss(NN.forward(target, s.pixels).a[3], s.label);
        if (i % 5 === 4) await yieldFrame(token);
      }
      return sum / batch.length;
    }
    async function updateBatch() {
      if (inference || disposed) return;
      const token = generation;
      busy = true;
      controls();
      // 初始评估也可能被用户取消；第一次提交前补齐起点，避免错位的曲线。
      const initial = losses.length ? null : await evaluate(model, token);
      const size =
          mode === "sgd" ? 1 : mode === "full" ? order.length : batchSize,
        batch = order.slice(cursor, cursor + size);
      UI.$("#training-status").textContent =
        `正在累积 ${batch.length} 个样本的梯度…`;
      host
        .querySelectorAll("[data-sample]")
        .forEach((el) =>
          el.classList.toggle(
            "pending",
            batch.includes(Number(el.getAttribute("data-sample"))),
          ),
        );
      const result = await gradients(model, batch, token, true);
      // 在副本上更新并完成评估后才提交，取消操作不会留下半个批次。
      const candidate = NN.clone(model);
      NN.apply(candidate, result.avg, rate);
      const afterLoss = await batchLoss(candidate, batch, token),
        evaluation = await evaluate(candidate, token);
      check(token);
      model = candidate;
      average = result.avg;
      individual = result.details;
      lastBefore = result.loss;
      lastAfter = afterLoss;
      lastRate = rate;
      active = batch;
      updates++;
      cursor += batch.length;
      if (cursor >= order.length) {
        epoch++;
        cursor = 0;
        makeOrder();
      }
      if (initial) {
        losses = [initial.loss];
        accuracies = [initial.accuracy];
      }
      losses.push(evaluation.loss);
      accuracies.push(evaluation.accuracy);
      busy = false;
      UI.$("#training-status").textContent =
        `已更新第 ${updates} 批 · ${batch.length} 个样本平均后更新`;
      renderMetrics(evaluation);
      renderGrid();
      renderInspector();
      renderPrediction();
      controls();
    }
    /** @param {unknown} error */
    function failure(error) {
      if (error instanceof Error && error.message === "cancelled") return;
      stop();
      if (!disposed)
        UI.$("#training-status").textContent =
          error instanceof Error ? error.message : String(error);
    }
    async function loop() {
      if (!running || disposed || inference) return;
      try {
        await updateBatch();
        if (running) timer = window.setTimeout(loop, 20);
      } catch (e) {
        failure(e);
      }
    }
    /** @param {{loss:number,accuracy:number,perClass:number[]}} evaluation */
    function renderMetrics(evaluation) {
      lastEvaluation = evaluation;
      UI.$("#training-metrics").innerHTML =
        UI.metric("完成 epoch / 更新次数", `${epoch} / ${updates}`) +
        UI.metric("验证损失", UI.fmt(evaluation.loss)) +
        UI.metric("验证准确率", `${(evaluation.accuracy * 100).toFixed(0)}%`);
      UI.$("#class-accuracy").textContent =
        `验证类别 0：${(evaluation.perClass[0] * 100).toFixed(0)}%　类别 1：${(evaluation.perClass[1] * 100).toFixed(0)}%　· 每类 5 个独立样本，适合观察变化，不代表真实应用准确率。`;
      plots();
    }
    function plots() {
      if (tab !== "batch") return;
      UI.plot(UI.canvas("#training-loss"), [
        { values: losses, color: "#50dcba" },
      ]);
      UI.plot(UI.canvas("#training-accuracy"), [
        { values: accuracies, color: "#edac69" },
      ]);
    }
    function renderGrid() {
      // 网格顺序与本轮的数据顺序一致，末轮批次仍保留高亮。
      const allowed = new Set(order),
        display = [
          ...order,
          ...DigitData.train.map((_, i) => i).filter((i) => !allowed.has(i)),
        ];
      UI.$("#dataset-grid").innerHTML = display
        .map(
          (i) =>
            `<button class="sample-cell ${active.includes(i) ? "current" : ""} ${i === selected ? "selected" : ""} ${!allowed.has(i) ? "faint" : ""}" data-sample="${i}" aria-label="数字 ${DigitData.train[i].label}，样本 ${i}"><canvas></canvas><small>${DigitData.train[i].label}</small></button>`,
        )
        .join("");
      host.querySelectorAll("[data-sample]").forEach((el) => {
        const i = Number(el.getAttribute("data-sample"));
        DigitData.draw(
          /** @type {HTMLCanvasElement} */ (el.querySelector("canvas")),
          DigitData.train[i],
        );
        el.addEventListener("click", () => {
          stop();
          selected = i;
          renderGrid();
          renderPrediction();
        });
      });
      UI.$("#batch-position").textContent =
        `第 ${epoch + 1} 轮 · ${cursor} / ${order.length} · 最近批次 ${active.length}`;
    }
    function renderPrediction() {
      const sample = DigitData.train[selected],
        p = NN.forward(model, sample.pixels).a[3];
      DigitData.draw(UI.canvas("#training-sample"), sample);
      UI.$("#sample-title").textContent =
        `标签 ${sample.label} → 预测 ${NN.argmax(p)}`;
      UI.$("#sample-result").textContent =
        `平方和损失 ${UI.fmt(NN.loss(p, sample.label))}`;
      UI.$("#sample-bars").innerHTML = UI.bars(p);
    }
    function renderInspector() {
      const el = UI.$("#batch-inspector");
      if (!average || !individual.length) {
        el.innerHTML = `<div class="panel-title"><i class="status-dot"></i>从每个样本的梯度，到平均梯度</div><p class="hint">执行一次更新后，这里将列出每个样本对同一个参数的梯度、求平均的过程，以及该批次更新前后的损失。</p><div class="notice mono">ḡ = (g₁ + g₂ + … + gᴮ) / B<br>Δθ = −η · ḡ</div>`;
        return;
      }
      el.innerHTML = `<div class="panel-title"><i class="status-dot"></i>最近一批 · ${individual.length} 个样本 → 一次更新</div><div class="metric-grid">${UI.metric("批次更新前损失", UI.fmt(lastBefore))}${UI.metric("批次更新后损失", UI.fmt(lastAfter))}${UI.metric("实际批次大小", String(individual.length))}</div><div class="button-row" style="margin-top:18px"><label>查看参数所在层<select id="gradient-layer"><option value="0">隐藏层 1</option><option value="1">隐藏层 2</option><option value="2" selected>输出层</option></select></label><label>神经元（从 0 起）<input id="gradient-node" type="number" min="0" max="9" value="0"></label><label>参数<select id="gradient-kind"><option value="bias">偏置 b</option><option value="weight">权重 w</option></select></label><label>输入索引<input id="gradient-input" type="number" min="0" max="15" value="0" disabled></label></div><div id="gradient-breakdown"></div><details><summary>查看三个层的参数更新摘要</summary><div style="margin-top:15px">${NetworkView.updateCards(average, lastRate)}</div></details>`;
      function breakdown() {
        const l = Number(UI.select("#gradient-layer").value),
          isWeight = UI.select("#gradient-kind").value === "weight";
        UI.input("#gradient-node").max = String(NN.SIZES[l + 1] - 1);
        UI.input("#gradient-input").max = String(NN.SIZES[l] - 1);
        UI.input("#gradient-input").disabled = !isWeight;
        const j = Math.floor(UI.number(UI.input("#gradient-node"), 0)),
          i = Math.floor(UI.number(UI.input("#gradient-input"), 0));
        const get = (g) => (isWeight ? g.dw[l][j][i] : g.db[l][j]),
          mean = get(average);
        UI.$("#gradient-breakdown").innerHTML =
          `<div class="detail-grid"><div class="table-scroll"><table class="detail-table"><thead><tr><th>样本 / 标签</th><th>更新前损失</th><th>∂L/∂θ</th></tr></thead><tbody>${individual.map((item) => `<tr><td>${item.index} / ${DigitData.train[item.index].label}</td><td>${UI.fmt(item.loss)}</td><td class="${get(item.gradient) >= 0 ? "down" : "up"}">${UI.signed(get(item.gradient))}</td></tr>`).join("")}</tbody></table></div><div><div class="notice mono">梯度求和 = ${UI.signed(mean * individual.length)}<br>除以批次大小 ${individual.length}<br>平均梯度 = ${UI.signed(mean)}<br>Δθ = −${lastRate} × ḡ<br>= ${UI.signed(-lastRate * mean)}</div><p class="hint">正梯度意味着参数需要减小；青绿表示参数增加，橙色表示参数减少。所有样本都在更新前的同一组参数上计算。</p></div></div>`;
      }
      for (const id of ["#gradient-layer", "#gradient-kind"])
        UI.select(id).onchange = breakdown;
      UI.input("#gradient-node").onchange = breakdown;
      UI.input("#gradient-input").onchange = breakdown;
      breakdown();
    }
    function controls() {
      UI.button("#mode-train").classList.toggle("active", !inference);
      UI.button("#mode-infer").classList.toggle("active", inference);
      for (const id of [
        "#training-once",
        "#compare-modes",
        "#compare-order",
        "#forget-zero",
        "#forget-one",
        "#forget-mixed",
      ])
        UI.button(id).disabled = inference || busy || running;
      UI.button("#training-run").disabled = inference || (busy && !running);
      UI.button("#training-run").textContent = running
        ? "暂停训练"
        : "连续训练";
      UI.input("#training-batch").disabled = inference || mode !== "mini";
      UI.input("#training-rate").disabled = inference;
      UI.input("#training-shuffle").disabled = inference;
      UI.select("#training-mode").disabled = inference;
      UI.$("#inference-note").textContent = inference
        ? "当前为仅推理模式，所有训练更新已停用。"
        : "查看样本只执行前向传播，不会更新参数。";
    }
    async function baseline() {
      const token = generation;
      losses = [];
      accuracies = [];
      lastEvaluation = null;
      UI.$("#training-metrics").innerHTML =
        UI.metric("完成 epoch / 更新次数", `${epoch} / ${updates}`) +
        UI.metric("验证损失", "待计算") +
        UI.metric("验证准确率", "待计算");
      UI.$("#class-accuracy").textContent = "验证指标尚未计算完成。";
      plots();
      busy = true;
      controls();
      try {
        const e = await evaluate(model, token);
        check(token);
        losses = [e.loss];
        accuracies = [e.accuracy];
        busy = false;
        renderMetrics(e);
        controls();
      } catch (e) {
        failure(e);
      }
    }
    function reset() {
      stop();
      model = NN.create(42);
      updates = 0;
      epoch = 0;
      cursor = 0;
      subset = "all";
      active = [];
      individual = [];
      average = null;
      makeOrder();
      UI.$("#training-status").textContent = "正在计算初始验证指标…";
      UI.$("#forget-status").textContent =
        "当前使用全部 10 类。选定阶段后，可单批更新或连续训练。";
      renderGrid();
      renderPrediction();
      renderInspector();
      const token = generation;
      baseline().then(() => {
        if (!disposed && !busy && token === generation)
          UI.$("#training-status").textContent = "已恢复相同起点 · 种子 42";
      });
    }
    async function compare(kind) {
      stop();
      busy = true;
      controls();
      const token = generation;
      UI.$("#comparison-table").innerHTML = "";
      const records = [];
      const variants =
        kind === "modes"
          ? [
              { name: "SGD", size: 1, shuffled: shuffle },
              {
                name: `Mini-Batch (${batchSize})`,
                size: batchSize,
                shuffled: shuffle,
              },
              { name: "Full Batch", size: 200, shuffled: shuffle },
            ]
          : [
              { name: "小批量 · 按类别", size: batchSize, shuffled: false },
              { name: "小批量 · 打乱", size: batchSize, shuffled: true },
            ];
      try {
        const initial = await evaluate(NN.create(42), token);
        for (const variant of variants) {
          const target = NN.create(42),
            items = variant.shuffled
              ? DigitData.shuffle(indices("all"), 2026)
              : indices("all");
          let count = 0;
          for (let start = 0; start < items.length; start += variant.size) {
            check(token);
            UI.$("#comparison-status").textContent =
              `${variant.name} · 已处理 ${start} / 200 个样本（可用重置或切页取消）`;
            const r = await gradients(
              target,
              items.slice(start, start + variant.size),
              token,
            );
            NN.apply(target, r.avg, rate);
            count++;
            await yieldFrame(token);
          }
          const e = await evaluate(target, token);
          records.push({
            name: variant.name,
            count,
            loss: e.loss,
            accuracy: e.accuracy,
          });
          UI.$("#comparison-table").innerHTML =
            `<div class="table-scroll"><table class="detail-table"><thead><tr><th>模式</th><th>样本数</th><th>更新次数</th><th>初始验证损失</th><th>最终验证损失</th><th>验证准确率</th></tr></thead><tbody>${records.map((r) => `<tr><td>${r.name}</td><td>200</td><td>${r.count}</td><td>${UI.fmt(initial.loss)}</td><td>${UI.fmt(r.loss)}</td><td>${(r.accuracy * 100).toFixed(0)}%</td></tr>`).join("")}</tbody></table></div>`;
        }
        check(token);
        UI.$("#comparison-status").textContent =
          `对比完成 · 学习率 ${rate} · 各自独立计算，未修改上方网络参数。`;
        busy = false;
        controls();
      } catch (e) {
        if (e instanceof Error && e.message === "cancelled") {
          if (!disposed)
            UI.$("#comparison-status").textContent =
              "对比已取消，已完成的结果保留。";
        } else failure(e);
      }
    }
    /** @param {string} phase */
    function setPhase(phase) {
      stop();
      if (phase === "mixed") {
        model = NN.create(42);
        updates = 0;
        losses = [];
        accuracies = [];
      }
      subset = phase;
      epoch = 0;
      cursor = 0;
      active = [];
      individual = [];
      average = null;
      makeOrder();
      UI.$("#forget-status").textContent =
        phase === "0"
          ? "阶段 1：只使用 20 张数字 0；保留当前参数。请开始训练，并观察类别 0 和 1 的验证结果。"
          : phase === "1"
            ? "阶段 2：切换为 20 张数字 1；保留已学到的参数。继续训练，观察原来的数字 0 是否受影响。"
            : "混合对照：从种子 42 重新开始，使用 40 张数字 0 和 1。当前批次顺序由“随机打乱”控制。";
      renderGrid();
      renderPrediction();
      renderInspector();
      controls();
      if (phase === "mixed") baseline();
      else if (lastEvaluation) renderMetrics(lastEvaluation);
    }
    UI.select("#training-mode").onchange = () => {
      mode = UI.select("#training-mode").value;
      reset();
    };
    UI.input("#training-batch").onchange = () => {
      batchSize = Math.floor(UI.number(UI.input("#training-batch"), 16));
      UI.input("#training-batch").value = String(batchSize);
      reset();
    };
    UI.input("#training-rate").onchange = () => {
      rate = UI.number(UI.input("#training-rate"), rate);
      reset();
    };
    UI.input("#training-shuffle").onchange = () => {
      shuffle = UI.input("#training-shuffle").checked;
      reset();
    };
    UI.button("#training-once").onclick = () => {
      if (busy || inference) return;
      stop();
      updateBatch().catch(failure);
    };
    UI.button("#training-run").onclick = () => {
      if (running) {
        stop();
        UI.$("#training-status").textContent = "已暂停；未提交的批次已取消。";
        return;
      }
      if (busy || inference) return;
      running = true;
      controls();
      loop();
    };
    UI.button("#training-reset").onclick = reset;
    UI.button("#mode-train").onclick = () => {
      stop();
      inference = false;
      controls();
    };
    UI.button("#mode-infer").onclick = () => {
      stop();
      inference = true;
      UI.$("#training-status").textContent = "仅推理：参数保持固定";
      controls();
    };
    UI.button("#compare-modes").onclick = () => compare("modes");
    UI.button("#compare-order").onclick = () => compare("order");
    UI.button("#forget-zero").onclick = () => setPhase("0");
    UI.button("#forget-one").onclick = () => setPhase("1");
    UI.button("#forget-mixed").onclick = () => setPhase("mixed");
    UI.button("#model-export").onclick = () => {
      stop();
      UI.download("neural-lab-model.json", NN.serialize(model));
      UI.$("#model-status").textContent = "已导出当前参数与网络配置。";
    };
    UI.button("#model-import").onclick = () => {
      stop();
      UI.input("#model-file").click();
    };
    UI.input("#model-file").onchange = async () => {
      const file = UI.input("#model-file").files?.[0];
      if (!file) return;
      stop();
      const token = generation;
      try {
        if (file.size > 5 * 1024 * 1024)
          throw new Error(
            "模型文件过大，请选择本实验导出的 JSON（不超过 5 MB）。",
          );
        const data = await file.text();
        check(token);
        const next = NN.deserialize(data);
        model = next;
        inference = true;
        updates = 0;
        epoch = 0;
        cursor = 0;
        subset = "all";
        active = [];
        individual = [];
        average = null;
        makeOrder();
        UI.$("#model-status").textContent = "导入成功，已切换为仅推理模式。";
        renderGrid();
        renderPrediction();
        renderInspector();
        controls();
        await baseline();
      } catch (e) {
        if (!disposed && !(e instanceof Error && e.message === "cancelled"))
          UI.$("#model-status").textContent =
            e instanceof Error ? e.message : String(e);
      } finally {
        if (!disposed) UI.input("#model-file").value = "";
      }
    };
    host.querySelectorAll("#training-tabs button").forEach((el) =>
      el.addEventListener("click", () => {
        stop();
        childDispose();
        tab = el.getAttribute("data-tab") || "batch";
        host
          .querySelectorAll("#training-tabs button")
          .forEach((b) => b.classList.toggle("active", b === el));
        UI.$("#training-content").hidden = tab !== "batch";
        UI.$("#training-extra").hidden = tab === "batch";
        childDispose =
          tab === "tensor"
            ? Experiments.tensor(UI.$("#training-extra"))
            : tab === "fitting"
              ? Experiments.fitting(UI.$("#training-extra"))
              : () => {};
        if (tab === "batch") plots();
      }),
    );
    window.addEventListener("resize", plots);
    makeOrder();
    renderGrid();
    renderPrediction();
    renderInspector();
    baseline();
    controls();
    return () => {
      stop();
      disposed = true;
      childDispose();
      window.removeEventListener("resize", plots);
    };
  }
  return { mount };
})();
