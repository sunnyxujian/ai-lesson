---
theme: default
title: 认识模型服务接口 · 交互演示
info: |
  基于第三课完整教程与重点演示稿重制。含百炼真实请求和本地教学计算。
author: AI 学习空间
layout: default
source: 1
aspectRatio: 16/9
canvasWidth: 1200
colorSchema: light
fonts:
  provider: none
  sans: PingFang SC
  mono: SFMono-Regular
monaco: false
mdc: false
highlighter: shiki
lineNumbers: true
transition: fade
presenter: true
drawings:
  enabled: true
  persist: false
download: false
htmlAttrs:
  lang: zh-CN
---

<div class="eyebrow">从接口到生成机制</div>
<h1 class="hero-title">认识模型<br /><span>服务接口</span></h1>
<p class="hero-sub">发送一条消息之后，<br />模型服务究竟做了什么？</p>
<div class="hero-tags"><span>真实请求 · 百炼</span><span>逐步执行 · 自回归</span><span>可操作 · 采样实验</span></div>
<div class="hero-orbit" aria-hidden="true">f(x)</div>

<!--
开场：本课承接裸模型，向上看服务如何封装模型能力。
面向懂 HTTP 和 JavaScript 的开发者。先从真实请求进入，再拆开流程，最后回到参数对照。
说明两种标记：绿色是真实 API；蓝色是教学模拟或本地计算。教学数据不能用于推测百炼内部实现。
讲前在 .env.local 配置 key 和模型名称并重启；未配置仍可讲全部概念。
来源：完整教程第 1 节。
-->

---
source: 1
---

# 从模型计算，到服务接口
<p class="subtitle">同一个 AI 产品，可以从三个层次观察。</p>

<div class="stack-card" v-click><strong>AI App</strong><span>用户界面、业务流程、会话管理</span></div>
<div class="stack-card core" v-click><strong>Model Service</strong><span>接收消息，通过 HTTP 返回回复</span></div>
<div class="stack-card" v-click><strong>Raw Model</strong><span>Token 序列 → 下一个 Token 的概率分布</span></div>
<div class="callout" v-click>一次服务请求，内部通常包含许多次生成步骤。</div>

<!--
依次展开三层。强调应用、模型服务、裸模型不是同一个函数。
[click] App 把能力放到具体业务里。
[click] 本课研究 Model Service。
[click] 裸模型的抽象只负责算分布。
[click] 为后面的自回归做铺垫。真实工程有路由、缓存和优化，图只划分职责。
来源：完整教程第 1 节。
-->

---
source: 2
---

# 接口规格决定“怎样发请求”
<p class="subtitle">路径、鉴权方式、请求字段、响应结构，都属于接口协议。</p>

<div class="three-column">
<div class="card" v-click><h3>OpenAI 风格</h3><p>区分 Chat Completions<br />与 Responses</p><p class="detail">兼容其中一个端点，不代表兼容全部 API。</p></div>
<div class="card" v-click><h3>Anthropic 风格</h3><p>读取对应的消息结构<br />与鉴权约定</p><p class="detail">不能只换域名，就假定字段一致。</p></div>
<div class="card" v-click><h3>Gemini 风格</h3><p>读取对应的内容结构<br />与生成配置</p><p class="detail">接口相似不意味着模型能力相同。</p></div>
</div>
<div class="callout" v-click>本次实操：百炼的 OpenAI 兼容 Chat Completions 接口。</div>

<!--
原课用三种接口体系说明为什么要读服务商文档。本页不评价厂商排名，也不承诺所有厂商完全兼容。
本课的真实实验统一使用 Chat Completions，便于参数对照。原课录制时展示的是 Responses；下一页到第五页明确区分。
来源：完整教程第 2 节。
-->

---
source: 2
---

# 一条消息，发出一次真实请求
<p class="subtitle">POST /chat/completions · JSON 请求体 · Bearer 鉴权由本地服务端补入</p>

<LiveRequest />

<!--
配置完成后，点击发送。未配置时解释环境变量即可，不用模拟回答假装调用成功。
切换“查看请求快照”，逐项讲 model、messages 和 stream:false。实际路径是配置中的 /compatible-mode/v1 加 /chat/completions。
说明浏览器调用本机代理，代理再访问百炼，API key 留在服务端。页面中的耗时包含网络和服务处理，不能当成纯模型计算时间。
用量仅显示服务商实际返回值；没有返回就显示未提供。
来源：完整教程第 2 节；百炼接入为本演示新增实操。
-->

---
source: 3
---

# SDK 把 HTTP 请求封装起来
<p class="subtitle">点击切换代码：请求表达方式改变，消息的含义保持一致。</p>

````md magic-move
```http {1-2|3-4|6-9}
POST /compatible-mode/v1/chat/completions HTTP/1.1
Host: <你的百炼服务域名>
Authorization: Bearer <服务端环境变量>
Content-Type: application/json

{
  "model": "<MODEL_NAME>",
  "messages": [{ "role": "user", "content": "你是谁？" }]
}
```
```ts
// 服务端 SDK 写法示意
const client = new OpenAI({
  baseURL: process.env.MODEL_BASE_URL,
  apiKey: process.env.MODEL_API_KEY,
});
const result = await client.chat.completions.create({
  model: process.env.MODEL_NAME,
  messages: [{ role: 'user', content: '你是谁？' }],
});
console.log(result.choices[0].message.content);
```
````

<p class="small-note">原课的 /v1/responses 使用 input；这里的 Chat Completions 使用 messages，不能直接混用。</p>

<!--
逐步说明请求行、请求头、请求体。点击变换为 SDK 代码，指出 client 封装 HTTP，并没有运行一个本地大模型。
这是服务端 SDK 写法的示意，省略 import。实际项目代理使用 fetch 以便直接处理超时与取消，不要求观众在浏览器执行这段代码。
来源：完整教程第 2–3 节。
-->

---
source: 3
---

# 换服务商，先核对三个配置
<p class="subtitle">切换示例，观察请求基地址、凭据和模型名称。</p>

<ConfigSwitcher />

<!--
点击百炼和 OpenAI 切换，强调只是配置展示，不发送请求。
原课用 Kimi 讲兼容 SDK 的例子；这里用本次指定的百炼地址实际落地。原则相同：读兼容说明，检查基地址、key、model。
不要把模型名称留成另一家名称，也不要混用密钥。提供商支持的具体模型应从自己的服务配置中获取。
来源：完整教程第 3 节。
-->

---
source: 4
---

# 一个服务，也可以提供多套规格
<p class="subtitle">兼容关系属于端点，SDK 必须与该端点对应。</p>

<table class="protocol-table">
<thead><tr><th>服务商文档说明</th><th>选择</th><th>继续核对</th></tr></thead>
<tbody>
<tr v-click><td>端点 A 兼容 OpenAI 消息接口</td><td>对应的 OpenAI SDK 方法</td><td>字段与模型支持范围</td></tr>
<tr v-click><td>端点 B 兼容 Anthropic 消息接口</td><td>对应的 Anthropic SDK 方法</td><td>基地址与鉴权方式</td></tr>
</tbody>
</table>
<div class="callout" v-click>“能用同一个 SDK”描述接入方式，不代表服务的所有功能都相同。</div>
<p class="small-note">原课以 Kimi 的多协议接入举例；本页不承诺当前百炼端点支持另一套协议。</p>

<!--
沿用原课“同一服务兼容多套规格”的思路。不要把 /anthropic 后缀类比追加到本次百炼地址。
讲清楚 SDK 是请求格式的封装，底层仍需对应具体端点。
来源：完整教程第 4 节。
-->

---
source: 5
---

# 变化很多，先抓住共同核心
<p class="subtitle">接口会增加功能；先理解消息怎样变成回复。</p>

<div class="inline-flow">
<div class="card" v-click><h3>用户消息</h3><p>自然语言</p></div><span class="arrow">→</span>
<div class="card" v-click><h3>模型服务</h3><p>封装模型能力</p></div><span class="arrow">→</span>
<div class="card" v-click><h3>AI 回复</h3><p>自然语言</p></div>
</div>
<div class="callout" v-click>我们要打开中间这层，观察输入准备、生成和结果处理。</div>
<p class="small-note">文件、工具等扩展能力，按实际需要阅读对应文档。</p>

<!--
原课用服务能力交集解释学习策略。本课范围仍限定在文本消息生成，不扩展为工具调用、RAG 或 Agent 课程。
先让听众描述目前知道的：发 HTTP 请求、得到 JSON。下一步解释 JSON 背后的流程。
来源：完整教程第 5 节。
-->

---
source: 6
---

# 输入与输出，通常分别计费
<p class="subtitle">相同 Token 数量，使用不同单价，得到不同费用。</p>

<CostLab />

<!--
拖动输入、输出滑杆，观察金额线性变化。这里使用原课录制时的 $2.50/$15.00 每百万 Token，不是百炼报价。
解释 1M=1,000,000。缓存输入、推理 Token、套餐等可能另有规则，费用面板不覆盖这些差异。
原课也谈包月时间窗、降级和排队：具体约束应看购买方案，不能用本教学公式推断全部账单。
来源：完整教程第 6 节。
-->

---
source: 7
---

# 服务内部，可以先看三个阶段
<p class="subtitle">前处理准备输入，自回归产生 Token，后处理组织输出。</p>

<PipelineLab />

<!--
单步演示或播放。黄色或红色错误不是本页重点，先建立主流程。
前处理、自回归、后处理是教学分层，不是对百炼真实内部架构的抓包结论。
来源：完整教程第 7 节。
-->

---
source: 8
---

# 先确认身份与调用权限
<p class="subtitle">请求可能在进入模型计算前就被拒绝。</p>

<PipelineLab mode="auth" />

<!--
选择密钥无效或模型无权限，点击下一步，观察停在前处理；再选通过并重置演示完整路径。
这些是本地教学情境，不发送无效 key 到真实平台。真实接口错误在第 4 页按实际响应呈现。
余额和权限检查的具体顺序取决于服务，不把此示意当成统一实现。
来源：完整教程第 8 节。
-->

---
source: 9
---

# 系统消息与用户消息一起组成输入
<p class="subtitle">改变系统提示，模型看到的上下文也随之改变。</p>

<TokenAssembly />

<!--
先看 system/user 两张消息卡片，再按下一步观察角色序列与示意 ID。切换猫咪角色，说明上下文会变化。
本例只展示开发者设置的 system，不声称能读取平台隐藏提示词。
原课称服务端补入提示为“提示词注入”；此处称消息组装，避免与恶意 prompt injection 攻击混淆。
不通过模型自称判断其真实来源，原课的换牌推测不作为已证实事实传播。
来源：完整教程第 9 节。
-->

---
source: 10
---

# 都是 Token，也有角色约定
<p class="subtitle">输入最终变成数字，角色与指令仍然有语义。</p>

<TokenAssembly mode="roles" />

<!--
展示角色标记也进入序列。用户请求扮演猫与要求忽略更高优先级规则不能混为一谈。
不承诺每个模型都会按同样的优先级处理；这是训练和服务协议共同影响的行为。
来源：完整教程第 10 节。
-->

---
source: 11
---

# Tokenization：把文本变为模型输入
<p class="subtitle">从文本片段到词表 ID，保持可对应的序列。</p>

<TokenAssembly mode="tokens" />

<!--
点击两次下一步进入 ID 视图，悬停或聚焦查看双向映射。这里的中文切分与 ID 都是教学定义。
说明真实 tokenizer 可将一个词拆成多个片段，也可能合并空格、标点和字符，不能按字数直接当 Token 数。
界面显示的特殊角色文本是示意，不声称某个真实模型使用这些字面标记。
来源：完整教程第 11 节。
-->

---
source: 12
---

# 模型返回的是概率分布
<p class="subtitle">计算出候选概率，还需要选择才能得到下一个 Token。</p>

```ts {1|2|all}
const input = [101, 102, 103];  // 示意：你是谁
const prob = raw_model(input); // 返回分布，不是整句回复
```

<div class="three-column" style="margin-top:25px">
<div class="card" v-click><h3>候选「我」</h3><p style="font-size:42px">0.30</p><p class="detail">只是其中一种可能</p></div>
<div class="card" v-click><h3>候选「你」</h3><p style="font-size:42px">0.25</p><p class="detail">还没有执行选择</p></div>
<div class="card" v-click><h3>其余候选</h3><p style="font-size:42px">0.45</p><p class="detail">总概率加起来为 1</p></div>
</div>
<p class="small-note">数值为教学示意。固定权重、固定输入下，用确定的分布计算抽象理解模型。</p>

<!--
原课把变量 output 改名 prob，以避免误会。本页保留这一关键区别。
抽象函数输出分布，采样才引入这里讨论的随机选择。实际数值计算和部署细节会影响可复现性。
来源：完整教程第 12 节。
-->

---
source: 13
---

# 自回归：生成，再追加到输入
<p class="subtitle">盯住两次 push：一次收集答案，一次准备下一轮。</p>

<AutoregressionLab />

<!--
先单步：计算分布、选择、检查、追加 output、追加 input。高亮行是下一步将执行的行。
在 output 已追加、input 尚未追加的时刻停住，让听众解释差别。然后继续，input 变长，下一轮开始。
播放至 EOS，说明结束 Token 不进入正文；教学词表、概率和选择固定，以便重复讲解。
来源：完整教程第 13 节。
-->

---
source: 13
---

# “你是谁”怎样接成一段回答？
<p class="subtitle">每次预测，都以原消息和已经生成的内容作为上下文。</p>

<AutoregressionLab words />

<!--
用文字视图再看同一个循环。原课先生成“我”，再生成“是”；本演示扩展为“我是模型助手。”后遇到 EOS。
可以停在中间问：如果不把生成 Token 加入 input，下一轮会看到什么？
input 上的文字只是为了可读，模型实际使用的仍是 Token 序列。
来源：完整教程第 13 节。
-->

---
source: 14
---

# 输出越长，顺序生成的步骤越多
<p class="subtitle">用逐 Token 循环理解成本直觉，再区分真实工程优化。</p>

<CostLab rounds />

<!--
调到 1000，观察约 1000 个单 Token 生成步骤。此处不计最终 EOS 等额外步骤。
明确：逻辑上依赖完整上下文，不等于每次都从头计算全部输入。KV cache 等优化会复用先前计算，投机解码等也使实际执行更复杂。
价格不只由这条简化循环决定。原课关于普遍亏损、市场集中与涨价的内容属于讲者判断，不作为当前事实讲解。
来源：完整教程第 14 节。
-->

---
source: 15
---

# 采样发生在 pickToken 这一步
<p class="subtitle">分布由模型计算，选择策略决定下一步拿哪个候选。</p>

```ts {1|2|all}
const prob = raw_model(input);
const token = pickToken(prob, options);
```

<div class="three-column" style="margin-top:24px">
<div class="card" v-click><h3>temperature</h3><p>调整分布的集中程度</p><p class="detail">低温更集中，高温更平缓</p></div>
<div class="card" v-click><h3>top_k</h3><p>限制候选数量</p><p class="detail">按概率排序后保留 K 个</p></div>
<div class="card" v-click><h3>top_p</h3><p>限制累计概率范围</p><p class="detail">保留首次达到阈值的前缀</p></div>
</div>
<p class="small-note">各页独立展示参数作用；实际支持项与组合处理顺序，依模型和实现而定。</p>

<!--
不要把所有参数都写到每个 API 请求里。原课现场就发现所展示接口没有 top_k。
本项目真实调用只提供 temperature 与 top_p 可选项，且默认省略；本地教学实验包含 top_k。
来源：完整教程第 15 节。
-->

---
source: 15
---

# temperature 改变选择的集中程度
<p class="subtitle">拖动滑杆，再抽样观察理论分布与有限次数统计的差别。</p>

<SamplingLab mode="temperature" />

<!--
先从 T=1 开始，观察原分布。降低到 0.2 后集中，再设 0 演示贪心最大项，最后调到 2。
T=2 仍不是等概率。反复抽样是浏览器本地数学计算，不调用模型。有限样本频率不需要精确等于理论概率。
温度公式是为原课增加的严谨解释，不重复原课“2 完全随机”的口语化结论。
来源：完整教程第 15 节。
-->

---
source: 16
---

# 更确定，不等于更正确
<p class="subtitle">同一提示词，只改变一项参数；用真实回复判断任务效果。</p>

<LiveRequest compare />

<!--
先勾选显式参数，选择 temperature；A=0.2，B=1.2，分别手动发送，再切换记录查看差异。
如模型不支持该参数，直接讲错误并取消勾选，不声称参数起效。也可选择 top_p 单独对照。
A/B 只有消息完全相同时才适合做参数比较；请求快照可核对。每组一次结果仅是观察，不足以证明统计结论。
确定性不保证正确。实际服务的 T=0 也不保证跨运行绝对一致。原课场景温度经验值不作为本项目默认最优值。
来源：完整教程第 16 节。
-->

---
source: 17
---

# top_k：保留概率最高的 K 个
<p class="subtitle">截断按数量，排除项本轮不再参与选择。</p>

<SamplingLab mode="top_k" />

<!--
原课用 100 个候选取前 10 个；这里缩成 5 个候选便于观察。拖到 K=1，只有“我”；拖到 K=5，全部保留。
观察灰色原始概率与蓝色归一化概率。排除项即使原始概率非零，抽样频数也为零。
本页不调用百炼，也不假定所选模型暴露 top_k 参数。
来源：完整教程第 17 节。
-->

---
source: 18
---

# top_p：保留累计概率达到阈值的候选
<p class="subtitle">0.30 + 0.25 + 0.20 = 0.75，还没有达到 0.80。</p>

<SamplingLab mode="top_p" />

<!--
默认阈值 0.8，保留前四项，累计 0.9；第五项排除。强调不能因为 0.75 接近就停在第三项。
调到 0.75 观察恰好三项；调到 1 保留所有候选。截断后需归一化，再在保留集合内抽取。
本页与温度独立，避免把一种采样运算顺序当成所有提供商的固定实现。
来源：完整教程第 18 节。
-->

---
source: 19
---

# 后处理：把 Token 还原成回复
<p class="subtitle">先恢复文本，再按服务规则组织最终输出。</p>

<PipelineLab mode="post" />

<!--
单步展示 ID 到文字，再通过示例检查。切换“检查未通过”，说明服务可能拒绝、修订或重新生成。
本例只选择停止交付，原课的重新生成再检查是另一种举例，不代表所有服务固定采用。
不将不同厂商检查严格程度的主观比较当成事实。本页也不声称看到了百炼的内部审核结果。
来源：完整教程第 19 节。
-->

---
source: 20
---

# 把新能力，放回这张流程图
<p class="subtitle">读一份新接口文档时，先判断它改变了哪个环节。</p>

<PipelineLab />

<div class="review-list" style="margin-top:16px">
<div class="card"><b>前处理</b><br />输入如何组织？</div>
<div class="card"><b>自回归</b><br />下一步如何产生？</div>
<div class="card"><b>后处理</b><br />结果如何交付？</div>
</div>

<!--
最后播放完整流程，让听众将 API key、system、Tokenization、pickToken、Detokenization 放回位置。
回顾：服务接口封装能力；自回归将生成内容反馈为输入；参数改变选择行为但不能保证正确性。
可以回到第 4 页看请求快照，或第 21 页继续参数实验。完整课程链接保留在每页页脚。
来源：完整教程第 20 节。
-->
