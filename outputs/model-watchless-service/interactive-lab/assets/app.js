// @ts-check
"use strict";
(() => {
  const host = UI.$("#app");
  let dispose = () => {};
  function route() {
    dispose();
    const path = location.hash.replace(/^#\//, "") || "neuron";
    const selected = ["neuron", "forward", "backward", "training"].includes(
      path,
    )
      ? path
      : "neuron";
    document.querySelectorAll("[data-route]").forEach((el) => {
      const active = el.getAttribute("data-route") === selected;
      el.classList.toggle("active", active);
      if (active) el.setAttribute("aria-current", "page");
      else el.removeAttribute("aria-current");
    });
    document.title =
      ({
        neuron: "单个神经元",
        forward: "前向传播",
        backward: "梯度下降与反向传播",
        training: "训练模式",
      }[selected] || "神经网络") + " · 交互实验室";
    dispose =
      selected === "neuron"
        ? NeuronPage.mount(host)
        : selected === "forward"
          ? PropagationPage.mount(host)
          : selected === "backward"
            ? PropagationPage.mount(host, true)
            : TrainingPage.mount(host);
    window.scrollTo(0, 0);
  }
  const help = /** @type {HTMLDialogElement} */ (UI.$("#help-dialog"));
  UI.button("#help-button").onclick = () => help.showModal();
  UI.button("#close-help").onclick = () => help.close();
  help.addEventListener("click", (e) => {
    if (e.target === help) {
      const r = help.getBoundingClientRect();
      if (
        e.clientX < r.left ||
        e.clientX > r.right ||
        e.clientY < r.top ||
        e.clientY > r.bottom
      )
        help.close();
    }
  });
  window.addEventListener("hashchange", route);
  window.addEventListener("pagehide", () => dispose());
  window.addEventListener("pageshow", (event) => {
    if (event.persisted) route();
  });
  route();
})();
