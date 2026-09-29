# Transformer · Slidev 交互技术讲义

32 页，约 45 分钟。适合具备编程基础、希望理解 Transformer 计算与信息流的听众。采用浅色 16:9 版式，包含逐页讲者备注和可操作的小矩阵演示。

## 本地启动

需要 Node.js **22.12.0 或更高版本**、pnpm。此工程锁定 pnpm 11.9.0 与 Slidev 53.0.0。

```sh
cd '/Users/Admin/Documents/学习空间/ai-lesson/outputs/Transformer/slidev'
pnpm install --frozen-lockfile
pnpm dev
```

浏览器访问终端显示的本地地址，默认是 `http://localhost:3030`。只绑定本机回环地址。如端口被占用，可运行 `pnpm dev --port 3031`。

这是需要启动本地服务的 Slidev 项目，不能通过双击 `slides.md` 演示。首次安装依赖需要联网；课程内容、字体、SVG 和数学计算不使用远程 API 或 CDN。参考资料链接需联网打开。未配置网站发布、PDF/PPTX 导出。

## 演示操作

- 页面空白处使用方向键前后导航；第 15 页代码和第 32 页答案有逐步高亮/揭示。
- 交互区使用“上一步 / 下一步 / 播放 / 暂停 / 重置”。自动播放每 2.2 秒推进一个阶段，结束后停止。
- 点击矩阵单元格选择待编辑数值，再拖动滑块；注意“编辑行”与“查询行”是独立选择。
- 控件内的按键保留给表单操作，不触发全局翻页。离开交互区后可正常使用导航键。
- 离开页面暂停，重新进入恢复该页初始示例；各页面的参数互不污染。
- Slidev 演讲者模式显示讲者备注与计时。打开 `/presenter/1` 可进入讲者视图。交互参数在各浏览器窗口内独立保存；使用双屏时，请在投影的演示窗口操作交互控件，讲者窗口用于查看备注。
- 系统启用“减少动态效果”时，取消补间和流动动画；手动分步和数值计算仍可使用。

## 课程结构

| 页码 | 内容 | 建议时长 |
|---|---|---|
| 1–4 | 问题、目标、架构导航 | 4 分钟 |
| 5–8 | Token、Embedding、位置与维度 | 6 分钟 |
| 9–16 | 注意力完整计算与多头 | 13 分钟 |
| 17–22 | 残差、LayerNorm、FFN、编码器 | 7 分钟 |
| 23–29 | 右移、掩码、交叉注意力、解码生成 | 11 分钟 |
| 30–32 | 架构对比、回顾与理解检查 | 4 分钟 |

## 源码入口

- `slides.md`：32 页正文、公式、组件引用、逐页讲者备注。
- `components/`：交互实验及共享矩阵、条形图、步骤控制和 SVG 架构图。
- `lib/math.ts`：矩阵运算、稳定 Softmax、注意力、LayerNorm 和位置编码。
- `lib/model.ts`：固定教学参数、两头注意力、编码层、解码层和生成脚本。
- `snippets/attention.ts`：第 15 页导入的真实 TypeScript 代码片段。
- `styles/index.css`：统一视觉样式，Slidev 自动加载。

## 数学与教学边界

矩阵统一采用行表示 Token：`d_model=4`，两头各 `d_k=d_v=2`，FFN `4→8→4`。单头注意力页单独使用 `d_k=d_v=4`。所有中间数值来自本地运算，界面仅在显示时舍入，内部运算保留精度。

经典结构使用 Post-LN。输入是 `sqrt(d_model) × Embedding + PE`；演示省略 Dropout。LayerNorm 的 ε 为 `1e-5`，交互以共享标量 γ/β 控制四维，实际模型通常逐特征学习。编码器演示算两层，为减少教学参数复用相同权重；标准堆叠通常各层独立。解码器演示计算一层。

所有参数都未经训练，词块划分是教学示意。注意力热力图不代表真实翻译对齐。第 27 页 logits 来自小模型的实际输出投影；第 28 页使用**独立预设 logits** 展示 `Can Huolala carry a Labrador?` 的可读生成路径，Softmax 仍真实计算，使用贪心选择并在 EOS 停止。它不是真实模型现场翻译。

## 检查与验收

```sh
pnpm check
```

仅检查 Markdown/frontmatter、公式、Vue SFC、CSS、TypeScript 语法及类型，核对 32 页、讲者备注、组件引用和本地资源路径。不运行构建、浏览器、导出或部署。静态检查不能证明布局和交互已经通过浏览器验收。

首次演示前建议人工确认：

- 修改 Q/K 后权重更新；只改 V 时权重不变、输出变化。
- Softmax 各行权重和为 1；未来位置的掩码权重为 0。
- 多头输出是 `3×2 + 3×2 → 3×4 → 3×4`，与残差维度匹配。
- LayerNorm 按单个 Token 的特征维计算；FFN 对各位置使用同一组参数。
- 上一步、暂停、重置、切页停止和重新进入复位正常；生成 EOS 后不继续追加。
- 矩阵与公式在投影尺寸下没有溢出或遮挡；键盘焦点清晰可见。

## 来源与署名

原材料内容与图示署名：**小白debug**。本稿依据上级目录的《Transformer-图文文章.html》《Transformer-演示文稿.html》重编，参考同目录交互示例的计算组织方式，并将图表重绘为 Vue/SVG。原文件保持原样。

- [Attention Is All You Need](https://arxiv.org/html/1706.03762v7)
- [Layer Normalization](https://arxiv.org/abs/1607.06450)
- [BERT](https://arxiv.org/abs/1810.04805)
- [GPT: Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- [Slidev 组件文档](https://sli.dev/guide/component)
