---
theme: default
title: Transformer · 从注意力计算到完整架构
author: 原材料内容与图示：小白debug；Slidev 交互重编
info: |
  32 页 / 45 分钟。面向具备编程基础的听众。
  固定教学参数，浏览器本地计算，不调用模型 API。
colorSchema: light
aspectRatio: 16/9
canvasWidth: 1200
fonts:
  sans: PingFang SC
  mono: SFMono-Regular
  provider: none
favicon: /favicon.svg
transition: fade
monaco: false
download: false
selectable: true
duration: 45min
htmlAttrs:
  lang: zh-CN
drawings:
  enabled: true
  persist: false
---

<div class="eyebrow">交互技术讲义 · 45 分钟</div>
<h1 class="hero-title">Transformer</h1>
<div class="hero-subtitle">从注意力计算到完整架构</div>
<div class="hero-line"></div>
<p class="lead">看懂信息如何流动，也看清每一步怎么算。</p>
<div class="meta">32 页 · 小矩阵真实计算 · 经典 Encoder–Decoder 架构</div>
<div class="source">基于小白debug的原材料重新编排；架构依据《Attention Is All You Need》</div>

<!--
用时 0:30。说明这是一份机制课，不训练模型，不调用线上 API。
预设的小矩阵会真的参与计算，但未经训练，不能展示真实语义能力。
内容来源：同目录 Transformer-图文文章.html 与 Transformer-演示文稿.html，原署名小白debug。
论文：https://arxiv.org/html/1706.03762v7
-->

---

# 学完后，能解释什么？

<div class="two-up">
<div>
<h2>算得清</h2>

- 追踪 Q、K、V 的来源和维度
- 手算一行注意力权重与输出
- 解释掩码为什么放在 Softmax 前

</div>
<div>
<h2>连得起来</h2>

- 组装编码层与解码层
- 区分训练中的并行与推理中的逐步生成
- 对比三类 Transformer 架构

</div>
</div>

<div class="insight">只需理解向量、矩阵乘法与函数；关键公式会逐步拆开。</div>

<!--
用时 0:45。先询问听众是否接触过矩阵乘法；提醒每行对应一个 Token。
讲解路径：表示 → 匹配与汇聚 → 子层 → 编码/解码 → 生成。
本课范围以经典 Transformer 为准，不展开 RoPE、KV Cache、RMSNorm。
-->

---

# 同一个“拉”，为什么不是同一个意思？

<div class="statement">货拉拉<span style="color:var(--teal)">拉不拉</span>拉布拉多</div>

<div class="pill-row"><span class="pill">货拉拉 · 平台名称</span><span class="pill">拉不拉 · 动作</span><span class="pill">拉布拉多 · 犬种</span></div>

<div class="two-up"><div><h2>carry / drag / pull？</h2><p>词的解释依赖前后信息。</p></div><div><h2>Can Huolala carry a Labrador?</h2><p>翻译需要表示、关联和生成。</p></div></div>

<div class="insight">本课使用三个教学词块；真实 Token 边界由分词器决定。</div>

<!--
用时 1:15。让听众判断 carry 与 drag 的差别，再指出上下文的作用。
不要把分词示例当成某款 tokenizer 的实际输出。
后面一直沿用三词块，降低理解每个新模块时的额外负担。
来源：原材料“从翻译问题说起”。
-->

---

# 经典 Transformer 的两条信息流

<ArchitectureMap />

<!--
用时 1:30。左边读取完整中文，右边读取已经知道的英文前缀。
强调横向连线：编码器输出向每个解码层的交叉注意力提供 K/V。
图中编码层和解码层均可重复 N 次。为了看清机制，后续演示采用缩小维度。
此图将 FFN 与后面的 Add & Norm 合并显示，不改变顺序。
来源：论文 §3.1、图 1，https://arxiv.org/html/1706.03762v7
-->

---

# Token ID 是索引，Embedding 是参数

<div class="flow-row"><div class="flow-box">文本<small>货拉拉／拉不拉／拉布拉多</small></div><span>→</span><div class="flow-box">Token ID<small>在词表中的离散索引</small></div><span>→</span><div class="flow-box">Embedding<small>查表得到连续向量</small></div></div>

$$
E_{\mathrm{table}}\in\mathbb{R}^{|V|\times d_{\mathrm{model}}},\qquad e_i=E_{\mathrm{table}}[\mathrm{id}_i]
$$

<div class="two-up"><div><h2>编号的距离没有语义保证</h2><p>ID 相邻，不代表含义相近。</p></div><div><h2>向量随训练变化</h2><p>每个维度通常没有固定的人类语义标签。</p></div></div>

<!--
用时 1:00。用数组查表解释 embedding，比“把编号变大”更准确。
指出 embedding 表是模型参数，而句子中的向量是查表结果。
来源：论文 §3.4；原材料 Token 与向量章节。
-->

---

# 位置编码让顺序进入表示

<EmbeddingLab />

<!--
用时 2:00。先看三行词向量，再点击下一步显示位置编码。
选择中间词块，交换首尾，说明词向量跟着词走，位置向量固定在位置上。
关闭位置编码作对照。即使中间 Token 的初始向量不变，后续上下文表示也可能变化。
经典输入为 sqrt(d_model) E + PE；这里使用 4 维正弦编码。
来源：论文 §3.4–3.5，https://arxiv.org/html/1706.03762v7
-->

---

# 位置编码是同维相加

$$
\begin{aligned}
\mathrm{PE}(p,2i)&=\sin\left(p/10000^{2i/d_{\mathrm{model}}}\right)\\
\mathrm{PE}(p,2i+1)&=\cos\left(p/10000^{2i/d_{\mathrm{model}}}\right)\\
X_p&=\sqrt{d_{\mathrm{model}}}\,E_p+\mathrm{PE}_p
\end{aligned}
$$

<div class="two-up"><div><h2>不同频率，描述位置</h2><p>每一对维度用一组正弦 / 余弦。</p></div><div><h2>维度保持不变</h2><p>4 维词嵌入 + 4 维位置编码 → 4 维输入。</p></div></div>

<div class="insight">图里可以把词义与位置分开画；经典模型实际执行向量相加。</div>

<!--
用时 1:30。不用推导所有三角恒等式；只解释 p 是位置、i 是频率索引。
位置编码可有多种方案，这页只介绍经典论文的正弦形式。
原始词嵌入缩放因子不要误写为注意力中的 1/sqrt(dk)，两者作用位置不同。
来源：论文 §3.5。
-->

---

# 全程使用同一套维度约定

| 对象 | 本课示例 | 含义 |
|---|---|---|
| 输入 X | 3 × 4 | 3 个词块，每个 4 维 |
| 单头 Q、K、V | 3 × 4 | 单头计算页中 dₖ = dᵥ = 4 |
| 多头中的 Q、K、V | 每头 3 × 2 | 两个头，每头 dₖ = dᵥ = 2 |
| 注意力矩阵 A | 3 × 3 | 行是查询，列是被参考位置 |
| FFN 中间表示 | 3 × 8 | 每个 Token 的特征扩张 |

<div class="insight">先看形状，再看数值；交叉注意力中，目标长度与源句长度可以不同。</div>

<!--
用时 1:30。让听众用矩阵乘法规则预测 QK 转置和 AV 的尺寸。
此页只定义教学配置；原论文 base 模型 d_model=512、8 个头、每头 64 维。
无需记住 512，关注行和列分别代表什么。
来源：论文 §3.2.2、§3.3。
-->

---

# Q、K、V：同一输入的三个投影

<ProjectionLab />

<!--
用时 1:45。先选“拉不拉”的 Q，再点 W 的某一列，逐项演示乘法和求和。
切换 K/V：相同 X 经不同权重变成不同角色。
Q 想匹配什么、K 如何被匹配、V 提供哪些内容，是类比，不是固定语义字段。
来源：论文 §3.2.2。权重采用固定教学参数。
-->

---

# 注意力的核心：匹配权重，再汇聚内容

$$
\underbrace{QK^\top}_{\text{匹配分数}}
\quad\longrightarrow\quad
\underbrace{\operatorname{softmax}(QK^\top/\sqrt{d_k})}_{\text{按行分配权重 }A}
\quad\longrightarrow\quad
\underbrace{AV}_{\text{融合内容}}
$$

<div class="flow-row"><div class="flow-box q"><span class="role-label">Q · 查询</span><small>每行提出一个匹配需求</small></div><div class="flow-box k"><span class="role-label">K · 键</span><small>与查询计算匹配分数</small></div><div class="flow-box v"><span class="role-label">V · 值</span><small>按权重参与输出</small></div></div>

<div class="insight">注意力输出是一个向量，不是直接选出某个词，也不是最终词表概率。</div>

<!--
用时 1:15。提前展示完整公式，然后在下一页拆解。
区分注意力权重和下一词概率：前者定义在上下文位置上，后者定义在词表上。
来源：论文 §3.2.1。
-->

---

# 点积：一行 Q 与所有 K 比较

<AttentionLab :start="0" />

<!--
用时 2:00。从第一步停留，选择“拉不拉”作为查询。
编辑 Q 的一个值，观察它只直接改变对应查询行的分数；编辑 K 则可影响多个查询。
每个分数都是对应分量乘积之和。点积受方向与长度共同影响，不等同于余弦相似度。
后续步骤可以点击探索，课堂主线先在这页聚焦原始点积分数。
来源：论文 §3.2.1。
-->

---

# 缩放：控制进入 Softmax 的数值尺度

<AttentionLab :start="1" />

<!--
用时 1:30。开关除以 sqrt(4)，再进入 Softmax 对比分布集中程度。
这是单头 4 维示例，不把缩放除数误用为序列长度。
在独立、均值 0、方差 1 的分量假设下，点积方差随 dk 增长，缩放控制方差。
不要说缩放必然让排序变化；同一正除数不会改变一行的大小顺序。
来源：论文 §3.2.1 脚注 1。
-->

---

# Softmax：把整行分数变成权重

<AttentionLab :start="2" />

<!--
用时 1:30。看权重和为 1，以及 exp(s-max) 的中间值。
说明减去最大值不会改变归一化结果，只改善数值稳定性。
改动一个分数会影响分母，因此通常会改变整行的多个权重。
不能将原稿近似权重与不匹配的分数直接配对；本演示全部现场计算。
来源：论文注意力公式；稳定 Softmax 为代数等价实现。
-->

---

# 加权 V：把参考内容混合成新表示

<AttentionLab :start="3" />

<!--
用时 1:45。把编辑矩阵切到 V，改一个值，然后回到 Softmax 步骤观察权重不变。
回到加权 V 和输出步骤，观察输出对应维度改变。
同一个位置的标量权重乘到 V 的全部特征，最后逐维相加。
四页交互相互独立，避免上一页参数修改污染后续示例。
来源：论文 §3.2.1。
-->

---

# 将公式对应到代码

<<< @/snippets/attention.ts {4-5|6|7|8|all}

<div class="insight">矩阵运算批量执行所有查询；教学组件用同样的计算步骤显示中间结果。</div>

<!--
用时 1:15。按翻页键逐行高亮，依次指向 dk、点积、缩放、Softmax 和输出。
此函数展示无掩码单头；带掩码版本稍后在 Softmax 前加入屏蔽。
softmax 是共享模块中的稳定实现，函数可以跳转源码查看。
代码为本项目实际可类型检查的片段，不是接入模型的 API。
-->

---

# 多头注意力：独立投影，拼接后再投影

<MultiHeadLab />

<!--
用时 2:00。切换两个头，看各自 2 维的 Q/K/V 和 3×3 权重。
观察 2 + 2 拼接成 4 维，然后通过 4×4 的 W_O。
多个头不等于简单复制同一次计算，也不人为指定固定语义职责。
完整公式：Concat(head1, head2) W_O。
来源：论文 §3.2.2。
-->

---

# 残差连接：保留输入的直接路径

<NormLab :start="0" />

<!--
用时 1:15。把子层倍率降为 0，看到残差和退化为输入本身。
倍率是教学对照控件，不是原架构中的额外训练门控。
残差要求输入与子层输出形状一致，多头输出投影使维度与 d_model 对齐。
残差有利于信息与梯度传播，不等于“原始信息永远完整不变”。
来源：论文 §3.1。
-->

---

# LayerNorm：在每个 Token 内标准化

<NormLab :start="2" />

<!--
用时 1:30。解释均值与方差取自当前一行的四个特征。
下一步拖动 gamma/beta，强调输出没有 0 到 1 的范围限制。
实现使用 epsilon=1e-5 防止零方差除零；展示标准化结果的方差应接近而非严格等于 1。
交互采用共享标量 gamma/beta 方便操作，真实参数通常逐特征学习。
来源：论文 §3.1；Layer Normalization，https://arxiv.org/abs/1607.06450
-->

---

# FFN：每个位置独立加工特征

<FfnLab />

<!--
用时 1:45。按 4→8→ReLU→4 走完四步，切换词块说明各位置使用同一组参数。
关闭 ReLU 对照结果，指出激活前后负值的变化。
不能说注意力之前都是线性：Softmax 和 LayerNorm 本身已含非线性。
FFN 增加特征变换能力；跨 Token 交互仍由注意力提供。
来源：论文 §3.3。
-->

---

# 编码层：先交换信息，再加工特征

<div class="flow-row"><div class="flow-box">多头自注意力<small>跨 Token 汇聚</small></div><span>→</span><div class="flow-box">Add & Norm<small>残差后归一化</small></div><span>→</span><div class="flow-box">FFN<small>逐位置特征变换</small></div><span>→</span><div class="flow-box">Add & Norm<small>形状仍为 n × d_model</small></div></div>

$$
\begin{aligned}
U &= \operatorname{LN}\left(X+\operatorname{MHA}(X)\right)\\
H &= \operatorname{LN}\left(U+\operatorname{FFN}(U)\right)
\end{aligned}
$$

<div class="insight">这是经典 Post-LN 顺序；为看清主线，公式和演示省略 Dropout。</div>

<!--
用时 1:00。回顾前面三种组件，强调两条残差分别绕过不同子层。
经典论文在子层输出加到残差之前应用 Dropout；教学计算省略随机性。
不将此处 Post-LN 说成所有现代模型的通用顺序。
来源：论文 §3.1、§5.4。
-->

---

# 编码器堆叠：每层重新组织上下文表示

<div class="flow-row"><div class="flow-box">X<small>3 × 4</small></div><span>→</span><div class="flow-box">编码层 1<small>3 × 4</small></div><span>→</span><div class="flow-box">编码层 2<small>3 × 4</small></div><span>→</span><div class="flow-box">Memory<small>每个源 Token 的表示</small></div></div>

<div class="two-up"><div><h2>形状保持</h2><p>始终是一组向量，通常不压成单个“句子向量”。</p></div><div><h2>参数通常各层独立</h2><p>计算结构重复，不意味着共享同一套权重。</p></div></div>

<div class="source">经典论文使用 6 层；本课小模型计算两层，并为演示简洁复用固定参数。</div>

<!--
用时 0:45。不要承诺每层一定可解释为某种语法或语义层级。
教学实现复用 encoderLayer 权重以减少展示参数，不能据此认为标准 Transformer 层间共享权重。
输出仍有每个位置的表示，稍后全部作为交叉注意力的源信息。
来源：论文 §3.1。
-->

---

# 编码器输出，还不是译文

<div class="two-up"><div><h2>已经得到</h2><p class="statement">源句的上下文表示</p><p>Memory ∈ ℝ<sup>源长度 × d_model</sup></p></div><div><h2>接下来需要</h2><p class="statement">目标词的概率分布</p><p>先结合已知英文，再参考完整中文。</p></div></div>

<div class="insight">解码器同时处理两件事：目标侧的连续性，以及源句的信息。</div>

<!--
用时 0:45。用一句话过渡：左边算出的不是英文文本，而是供右边读取的向量。
问听众 K/V 应该来自哪里，为交叉注意力埋伏笔。
来源：论文 §3.1、§3.2.3。
-->

---

# 右移目标序列：用已知内容预测下一词

| 位置 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 解码输入 | BOS | Can | Huolala | carry | a | Labrador | ? |
| 预测标签 | Can | Huolala | carry | a | Labrador | ? | EOS |

<div class="two-up"><div><h2>训练：标签已知</h2><p>一次处理多个位置，同时阻止各位置偷看未来。</p></div><div><h2>推理：未来未知</h2><p>从 BOS 开始，把刚选出的词追加回输入。</p></div></div>

<div class="insight">当前位置的 Q 来自已知前缀的表示，不来自尚未生成的词。</div>

<!--
用时 1:30。指向输入 Huolala 与目标 carry，说明同一位置的输入与预测对象不同。
BOS/EOS 为开始/结束符号的教学记法，具体 tokenizer 的符号名称可能不同。
训练时目标来自真实数据，因此要掩码防止泄漏。
来源：论文 §3.1、§3.2.3。
-->

---

# 因果掩码：只允许看自己和过去

<MaskLab />

<!--
用时 2:00。选 Huolala 输入位置，说明它预测 carry。
切到分数矩阵，未来列显示负无穷；下一步看对应概率为 0。
取消掩码作对照，再恢复。完整目标序列只用于训练机制示意，推理时未来输入不存在。
这里展示第一头的真实小矩阵计算。
来源：论文 §3.2.3。
-->

---

# 交叉注意力：目标侧查询，源句提供内容

<CrossAttentionLab />

<!--
用时 2:00。Q 是解码器带掩码自注意力之后的表示的投影，K/V 是编码器最终输出的投影。
演示 7×3 权重矩阵，说明交叉注意力不是必须方阵。
所有中文已知，不需要用目标侧的因果三角掩码屏蔽中文。
不得把这组未训练权重解释为真实的中英文对齐结果。
来源：论文 §3.2.3。
-->

---

# 解码层：三段子层，三次残差归一化

$$
\begin{aligned}
U &= \operatorname{LN}\left(Y+\operatorname{MaskedMHA}(Y)\right)\\
Z &= \operatorname{LN}\left(U+\operatorname{CrossMHA}(U,M)\right)\\
H &= \operatorname{LN}\left(Z+\operatorname{FFN}(Z)\right)
\end{aligned}
$$

<div class="flow-row"><div class="flow-box">Masked self-attention<small>已知目标之间建立关系</small></div><div class="flow-box">Cross-attention<small>读取编码器 Memory M</small></div><div class="flow-box">FFN<small>每个位置加工特征</small></div></div>

<div class="insight">每个解码层都能读取同一份编码器最终输出，并使用自己的投影参数。</div>

<!--
用时 1:15。Y 是目标侧上一层输出；首层来自目标嵌入与位置编码。
CrossMHA(U,M) 表示 Q 来源是 U、K/V 来源是 M，不能遗漏交叉注意力后的 Add & Norm。
小模型演示一层解码器，经典论文是六层。
来源：论文 §3.1、§3.2.3。
-->

---

# 输出投影：隐藏向量变成词表概率

<VocabularyLab />

<!--
用时 1:15。按隐藏向量→词表 logits→Softmax 走三步。
该页 logits 确实来自小矩阵解码器的输出投影，但参数未经训练，最高项不保证正确。
输入维度 4 与词表大小 9 没有必须相等的要求。
下一页使用单独明确标注的预设 logits，以展示一条可读的生成路径。
来源：论文 §3.4。
-->

---

# 逐词生成：选择结果，再接回前缀

<GenerationLab />

<!--
用时 2:00。可以自动播放到第三个词，再暂停指出 Can Huolala carry 的前缀增长。
每个词分四步：读取前缀、解码器加工、候选概率、选择并追加。
此页 logits 为教学预设，Softmax 真实计算。不要称为模型现场翻译。
EOS 后停止。使用重置可回到 BOS；离场自动暂停，再进入回到初始状态。
机制来源：论文 §3.1；语言示例来自原材料。
-->

---

# 训练能并行，生成仍逐步进行

| | 训练 | 自回归推理 |
|---|---|---|
| 目标输入 | 右移的真实目标序列 | 当前已经生成的前缀 |
| 未来内容 | 数据中存在，必须掩码 | 尚未生成 |
| 计算 | 多个目标位置可并行 | 下一个词依赖之前的选择 |
| 目的 | 用损失更新参数 | 参数固定，选择下一词 |

<div class="insight">“并行处理序列”与“自回归生成”描述不同阶段，并不矛盾。</div>

<!--
用时 1:00。训练中通常对各位置的目标词计算交叉熵，再反向传播更新参数。
生成时不因为每次输出一个词就重新训练。
本课不展开缓存优化，也不展示参数学习过程。
来源：论文 §3.1、§4、§5。
-->

---

# 三类架构：保留哪些信息通路？

| 架构 | 主要注意力结构 | 典型用途 / 例子 |
|---|---|---|
| Encoder-only | 双向自注意力 | 表示学习、分类；BERT |
| Encoder–Decoder | 源句双向 + 目标因果 + 交叉注意力 | 序列到序列；经典翻译架构 |
| Decoder-only | 因果自注意力 | 自回归语言建模；GPT |

<div class="insight">常见 Decoder-only 同时移除了独立编码器和交叉注意力；不能只把左边框擦掉。</div>

<div class="source">这些是结构与常见用法的对照，不是任务能力的互斥划分。</div>

<!--
用时 1:30。避免把 encoder-only 等同于完全不能支持生成任务，或把 decoder-only 等同于不能做理解。
常见 GPT 类 decoder-only 不含经典 encoder-decoder attention；输入问题与回答在同一序列建模。
BERT：https://arxiv.org/abs/1810.04805
GPT：https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
经典架构：https://arxiv.org/html/1706.03762v7
-->

---

# 沿着信息流，再走一遍

<ArchitectureLab />

<!--
用时 1:30。让听众说出每次高亮模块需要读哪些信息。
从中文输入推进到编码器 Memory，再到目标前缀、自注意力、交叉注意力、词表分布。
问 K/V 横向连线在哪，问未来信息在哪里被挡住。
本图是结构说明，不用连线动画代替实际模型计算。
来源：论文 §3。
-->

---

# 三个问题，检查是否真正理解

<div class="two-up"><div>

1. 只修改 V，注意力权重会变吗？
2. 训练时已有完整目标，为什么还要掩码？
3. 交叉注意力为什么可以是 7 × 3？

</div><div>
<v-clicks>

- 不会；Q/K 不变时权重不变，输出可以改变。
- 防止当前位置读取未来答案，保持因果约束。
- 7 个目标查询，分别参考 3 个源位置。

</v-clicks>
</div></div>

<div class="source">
原材料：小白debug · Transformer 图文文章与演示文稿<br>
论文：<a href="https://arxiv.org/html/1706.03762v7">Attention Is All You Need</a> · <a href="https://arxiv.org/abs/1607.06450">Layer Normalization</a><br>
架构对照：<a href="https://arxiv.org/abs/1810.04805">BERT</a> · <a href="https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf">GPT</a>
</div>

<!--
用时 1:00。先让听众回答，再按键逐条揭示答案。
结束时再强调：参数来自训练；课堂的固定参数只用于理解数学与数据流。
完整阅读材料保留在上级目录。所有互动都可重置，便于课后探索。
来源见本页链接及各页讲者备注。
-->
