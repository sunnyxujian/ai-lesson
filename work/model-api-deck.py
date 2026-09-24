from pathlib import Path
import json,html
p=Path(__file__).resolve().parents[1]/'outputs/video-notes/3.认识模型服务接口'
s=[]
def add(title,body,scene,hint,kind=''):s.append(dict(title=title,body=body,scene=scene,hint=hint,kind=kind))
def steps(items):return '<div class="steps">'+ '<b>→</b>'.join('<div data-edit>'+a+'<small>'+b+'</small></div>' for a,b in items)+'</div>'
def points(items):return '<ul class="pointlist">'+''.join('<li data-edit>'+x+'</li>' for x in items)+'</ul>'
def fine(x):return '<p class="fine" data-edit>'+x+'</p>'
def take(x):return '<p class="takeaway" data-edit>'+x+'</p>'
def code(x):return '<pre class="code" data-edit>'+html.escape(x)+'</pre>'
def photo(n,caption):return '<figure><img src="{{image:'+str(n)+'}}" alt="'+caption+'"><figcaption>'+caption+'</figcaption></figure>'
add('认识模型服务接口','<div class="title-line"></div><p class="subtitle" data-edit>从自然语言，到模型计算，再回到自然语言。</p><div class="title-meta">Model Service / API / 自回归</div>',1,'承接上一课的裸模型：输入Token列表，得到下一个Token概率分布。本课向上走一层，观察模型服务怎样对外提供能力。','title')
add('从模型计算，到服务接口','<div class="comparison"><div><em>Raw Model</em><p data-edit>Token → 概率分布</p><strong data-edit>底层计算的抽象</strong></div><div><em>Model Service</em><p data-edit>消息 → 回复</p><strong data-edit>通过 API 提供能力</strong></div></div>'+take('通过 HTTP 连接模型服务。'),1,'保留谷歌Gemini对外发布的例子。强调模型服务是上一层封装，不能把它和底层模型函数直接等同。')
add('先确认接口规格',steps([('OpenAI','课堂称为事实标准'),('Anthropic','Claude 的接口规格'),('Gemini','谷歌的接口规格')])+take('查看服务商文档：兼容哪一套？'),2,'原课区分三大类规格，说明很多提供商兼容OpenAI；并保留Claude页面地区受限的操作插曲。兼容性需以所用端点的文档为前提。')
add('一次请求，一次回复',code('POST /v1/responses\nContent-Type: application/json\nAuthorization: Bearer $OPENAI_API_KEY\n\n{ "model": "gpt-5.4", "input": "…" }')+fine('课堂 HTTP 示例：先看懂请求行、请求头、请求体与响应体。'),2,'按原课解释发送自然语言、得到回复。这里是录制时展示的OpenAI接口例子，不是新接入项目的当前配置承诺。响应行和响应头概念也要掌握。')
add('SDK 把网络请求封装起来',steps([('创建 client','设置 API key'),('指定模型','传入提示与消息'),('读取响应','得到模型回复')])+fine('语言与网络基础，决定你能否看懂这层封装。'),4,'回顾原课的new OpenAI、创建client、选择模型、输入提示与消息、取回响应的步骤。对应的网络基础要求保存在完整教程第三节。')
add('兼容接口，主要更换三项',points(['<b>基地址</b>：改为服务商提供的地址','<b>API key</b>：使用该服务商的凭据','<b>模型名称</b>：查阅它的模型列表'])+fine('课堂例子：通过 OpenAI SDK 请求 Kimi。'),4,'按原课提问：不是OpenAI的模型，能不能用OpenAI SDK？在兼容前提下可以。不要把模型名称留成原提供商的名称，也不要把密钥混用。')
add('同一服务，也能兼容多套规格','<div class="split"><div><p class="lead" data-edit>Kimi</p><p data-edit>一个地址兼容 OpenAI</p><p data-edit>另一个地址兼容 Anthropic</p><p class="fine" data-edit>据兼容规格选择对应 SDK。</p></div>'+photo(5,'课堂文档：不同基地址的配置')+'</div>',5,'原课查看K2编程工具配置，地址后缀包含anthropic。解释Claude Sonnet和Opus同属这里讨论的Anthropic接口体系，不把兼容范围扩大为所有功能。')
add('变化很多，先看交集','<div class="quote" data-edit>先抓各家共同提供的<br>模型能力。</div>'+steps([('用户消息','自然语言输入'),('模型服务','封装底层模型'),('AI 回复','自然语言输出')]),6,'先讲上传文件、Skill、Tool等接口功能变化很快，再沿原课的三个相交圆说明为何先看交集。具体功能需要时查文档。')
add('输入和输出，分别计费','<div class="big-stats"><div><em>$2.50</em><p>输入 / 每 1M Token</p><strong data-edit>课堂展示价格</strong></div><div><em>$15.00</em><p>输出 / 每 1M Token</p><strong data-edit>课堂展示价格</strong></div></div>'+fine('录制时示例；不同服务商和计费方案不同。缓存输入另有一项。'),7,'完整解释原课输入、输出Token分开计费；包月仍可能有时间窗限制、降级或排队。这里的美元数字来自视频，不用于当前价格比较。')
add('服务内部的三个阶段',steps([('前处理','认证 · 提示 · Token 化'),('自回归','调用模型 · 选择 · 追加'),('后处理','还原语言 · 检查输出')])+take('把后续每个概念，放回这条流程。'),8,'保持原课三步顺序。此处先展示结构，后面逐一讲解，不把图理解为所有服务内部实现完全一致。')
add('先确认身份与权限',points(['API key 是否有效','余额是否足够','是否有权调用接口或模型'])+fine('不同付费方式，可能对应不同的模型权限。'),8,'认证属于服务层。按原课解释key、余额和调用权限，之后再进入提示词注入。')
add('系统提示词随输入一起进入模型','<div class="band" data-edit>system：当用户询问你是什么模型时，<br>你是阿里的大模型千问……</div><div class="band" data-edit>user：你是什么模型？</div>'+fine('课堂示意：服务端补入系统提示词。'),9,'说明这里的提示词注入指服务端加入系统提示，与攻击语境不同。原课关于使用他人模型再加提示词的内容明确是猜测，不据此指认任何服务商。')
add('都是 Token，也有角色约定','<div class="comparison"><div><em>用户提示词</em><p data-edit>提问前的要求</p><strong data-edit>“你要说是 Kimi。”</strong></div><div><em>系统提示词</em><p data-edit>服务层的约束</p><strong data-edit>训练时学习角色规则</strong></div></div>'+fine('原课同时讲输入的数字抽象与 system / user 的角色含义。'),10,'复述月之暗面的Kimi例子和扮演猫例子。冲突如何处理，原课归于模型训练和规则重要性；“都是Token”不意味着角色标记不存在。')
add('Tokenization：准备模型输入',steps([('自然语言','系统提示 + 用户消息'),('分词','Tokenization'),('Token 列表','数字数组')])+take('这就是传给 raw_model 的 input。'),11,'回扣上一课。提示词和用户消息都需转成Token表示；本课没有展开分词算法细节。')
add('模型返回的是概率分布','<div class="split"><div>'+code('const prob = raw_model(input);')+'<p style="margin-top:40px" data-edit>某个 Token：0.3<br>另一个 Token：0.2<br>……</p></div>'+photo(12,'课堂：将 output 改名为 prob')+'</div>',12,'讲者现场把变量名output改成prob，强调还没有选出Token。概率分布是下一步pickToken的输入。')
add('自回归：生成，再追加',code('const output = [];\nwhile (1) {\n  const prob = raw_model(input);\n  const token = pickToken(prob, options);\n  if (isOver(token)) break;\n  output.push(token);\n  input.push(token);\n}')+fine('课堂伪代码：结束 Token 触发退出。'),13,'解释每一行。output只收集生成结果，input不断加入新Token。raw_model、pickToken、isOver和options是示意接口，不是完整可运行代码。')
add('“你是谁”怎样接成回答？',steps([('你是谁','初始输入'),('你是谁 + 我','第一次追加'),('你是谁 + 我 + 是','第二次追加')])+take('继续循环，直到选到结束 Token。'),13,'保持原课的“我”“是”例子。这里展示自然语言直觉，实际传入仍是Token数组。强调每轮以更新后的输入继续预测。')
add('输出越长，生成轮次越多','<div class="large-number">1,000 Token</div><div class="result-line">↓<p data-edit>约 1,000 次逐 Token 生成</p></div>'+take('原课以循环次数解释输出成本。')+fine('这是教学简化；课程没有展开缓存等推理优化。'),14,'先保留十个、几百、上千个Token的例子，再解释原输入与已有输出参与后续生成。亏损与市场集中的行业判断放在完整备注，保持其观点性质。')
add('采样发生在 pickToken 这一步',code('const token = pickToken(prob, options);')+steps([('temperature','调节选择随机性'),('top_k','按数量限制候选'),('top_p','按累计概率限制候选')])+fine('由用户随 API 请求传入配置；具体支持项取决于接口。'),15,'说明原始概率分布与服务侧采样的区别。原课列出这三个参数，后面现场也发现所查看接口不提供top_k。')
add('temperature 调节随机性','<div class="comparison"><div><em>较低温度</em><p data-edit>选择更集中</p><strong data-edit>课堂例子：0、0.1、0.2</strong></div><div><em>较高温度</em><p data-edit>选择更多样</p><strong data-edit>课堂例子：1 以上</strong></div></div>'+fine('原课文档展示 0–2 的范围；精确行为依具体模型与实现。'),15,'完整备注保留原课0和2的极端口语说明，并说明这不是严格公式。不要把温度2讲成所有Token等概率，也不保证温度0跨运行绝对一致。')
add('确定的答案，也可能确定地错','<div class="quote" data-edit>设为 0，<br>不等于结果正确。</div>'+points(['代码、科研：原课建议偏低','创意写作：可以调高','普通应用：可从默认值开始']),16,'原课指出一错到底或循环的问题。错误时可改变提示词，input变化也会使分布变化。保留0.7经验值和按模型测试的限定，避免将其作为普适最优值。')
add('top_k：保留概率最高的 K 个','<div class="large-number">K = 10</div>'+steps([('100 个候选','按概率降序'),('前 10 个','进入选择范围'),('其余候选','本轮排除')])+fine('所展示 OpenAI 接口未提供 top_k；课堂仍解释了其概念。'),17,'在保留集合内再选择，按原课的教学顺序解释。强调截断按数量，不是累计到某个概率。')
add('top_p：达到累计概率阈值','<div class="band" data-edit>0.30 → 0.55 → 0.75 → <b>0.90</b></div><div class="large-number" style="font-size:82px;margin-top:55px">top_p = 0.80</div>'+take('前三项不够，加入第四项；保留前四个。')+fine('原课概率：0.30、0.25、0.20、0.15、0.10。'),18,'逐项相加，说明不能因为0.75接近0.8就只保留三个。第四项加入后是0.9，首次达到阈值。再在保留候选中进行选择。')
add('后处理：把 Token 还原成回复',steps([('输出 Token 列表','自回归的结果'),('Detokenization','恢复自然语言'),('输出检查','按服务规则处理')])+fine('原课例子：发现输出问题后，补充问题并重新生成、检查。'),19,'保持原课对合规性检查的说明。不同产品严格程度是讲者判断；重新生成是一种举例，不是所有服务的固定机制。')
add('把新功能放回这张图',steps([('前处理','输入怎样准备'),('自回归','Token 怎样产生'),('后处理','结果怎样交付')])+'<div class="pullquote" data-edit>抓住核心，<br>新增能力再查文档。</div>',20,'收束原课：接口快速变化并不可怕，先判断新功能位于哪一层。预告后续模型服务扩展，但不补讲视频中没有出现的专题。')
for i in [2,18]:s[i]['body']=s[i]['body'].replace('<b>→</b>','')
(p/'work/deck-data.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(s),'slides')
