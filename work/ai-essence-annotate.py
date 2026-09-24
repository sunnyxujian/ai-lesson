from pathlib import Path
import json,re
p=Path('outputs/video-notes/4.AI-本质');w=p/'work'
notes=json.loads((w/'notes-data.json').read_text(encoding='utf-8'))
visuals=[
'画面列出 AI Application、Model Service、Raw Model 三层，后两层已经打勾；背景是模型服务的前处理、自回归和后处理示意图。',
'画面同时展示 OpenAI 文档页面与三层笔记，Skills 被用作功能从应用层进入服务层的例子。这是课堂录制时的接口示例，正文保留讲者的概括，不作为当前所有 API 的能力说明。',
'Raw Model 图中，Token List 指向模型，再输出概率分布；权重矩阵通过 GPU 与模型相连，下方有“训练/微调”箭头。便签比较 GPT-3.5、微调后的矩阵与 GPT-4。微调是否划算、所需两三个月或半年，是本课举例与讲者判断。',
'便签把应用层分为“应用开发 / 工具使用”，并列出 LangChain、LangGraph、DeepAgent。开发框架名称根据画面校正。',
'画面展示课程目录以及高薪课、架构课、兴趣课和福利课程的介绍。正文保留原课的课程介绍与薪资表述，不将其改写为效果保证。',
'画面显示应用开发与工具使用的分工，字幕明确列出 Claude Code、Codex、OpenCode。另一个工具在音频中被识别成 OpenCL / Open Cloud，正文暂作 OpenClaw 并保留存疑标记。',
'便签写出两个问题：“1. 输入什么给模型？2. 如何处理模型的输出？”与这两个问题无关的 ASR 异常尾句已经通过同一时段的局部音频重识别排除，原始块仍保留供核查。',
'红框圈出模型服务的前处理、自回归和后处理；用户消息与 AI 回复位于两侧。这里展示的核心关系是：应用把消息交给服务，再接收返回内容。',
'便签记录 skill、协议缓存、大文件上传、单点登录这些例子。原画面使用“协议缓存”的写法，正文照录；OAuth 的音频辨识不够清楚，已保留术语存疑标记。',
'便签中的链路是“用户 ↔ Claude Code（skill）↔ 代理服务器 ↔ 模型服务”。后续代码工程名为 proxy-server，源码入口为 index.js。',
'''日志画面列出请求方法、地址、请求头、请求体，以及响应状态和响应头等信息。配置画面显示如下测试值：

```dotenv
TARGET_URL=https://www.baidu.com
PORT=3000
LOG_LEVEL=debug
```

启动命令经音频局部复核为 `npm run dev`；终端测试命令为 `curl http://localhost:3000/`。这些是课堂现有代理项目的操作，不包含该项目的完整源码。''',
'CC Switch 中选中了 Kimi-Proxy。应用端的请求地址应指向本地代理，代理的 TARGET_URL 应指向实际模型服务；百度地址仅用于前一步测试。选用的截图展示配置列表，未采用含凭据的配置展开画面。',
'请求 JSON 的 tools 列表中有 name 为 Skill 的条目，description 说明技能的使用时机、技能名称和可选参数。这里的 Skill 是工具名，技能清单则在后续提示词里列出。',
'请求标明 model 为 kimi-for-coding；system-reminder 列出 docker-compose、skill-create、web-design-guidelines 及各自描述。另一个画面显示 CLAUDE.md 文本被送进上下文；画面中的路径属于用户级全局规则，讲解中也提到工程规则。这里记录本次演示实际观察到的请求，不推断所有版本或所有请求都相同。',
'终端实际输入是 `review UX`，不是转写里的“review邮箱”。返回显示 Skill(web-design-guidelines) 和 Successfully loaded skill，随后要求用户指定文件路径、文件模式，或审查整个项目中的特定类型文件。',
'SSE 中反复出现 event: content_block_delta；data 对象的 delta.type 为 input_json_delta，partial_json 逐段出现 web、-design、-guid、elines 等片段。片段拼接后形成技能名称。这些事件名与字段名来自所选画面。',
'便签按顺序补出用户输入、Claude Code 添加提示词、模型判断使用技能、返回 JSON（技能调用），再交给 Claude Code 的链路。',
'红框分别标出给模型输入与处理模型输出的位置。补充日志画面能看到 tool_use、Skill、input.skill、tool_result，以及 Web Interface Guidelines 文档正文；这是第二轮请求包含技能内容的直接证据。',
'画面保留完整调用链与 AI 应用层笔记。讲者在这一段再次说明，Skills 是用来展示分析方法的例子，随后会在工具课程中继续讲解具体概念。',
'课程介绍叠放在完整流程笔记上，结尾区分 AI 应用开发与 AI 工具使用两条学习路线。课程获取方式保留原课语境。'
]
for n,v in zip(notes,visuals):
 n['visual']=v
 n['body']=n['body'].replace('测试的赋','测试字符').replace('说技能是不是','所以技能是不是').replace('所以说，我知道了吧','所以说，知道了吧').replace('为提示词','喂提示词')
 n['body']=re.sub(r'(?<=[，：])\n\n','',n['body'])
 # No paragraph is allowed to end in an ASR sentence fragment.
 n['body']=n['body'].replace('这节课的内容呢，只要AI存在一天，\n\n','这节课的内容呢，只要 AI 存在一天，')
 (w/'codex-notes'/f'scene_{n["id"]:03}.md').write_text(f'## 标题\n{n["title"]}\n\n## Light-plus\n{n["body"]}\n\n## Visual explainer\n{v}\n',encoding='utf-8')
(w/'notes-data.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((w/'scene-manifest.json').read_text(encoding='utf-8'))
coverage={'source_chunks':70,'ordered_scenes':len(notes),'body_characters':sum(len(n['body']) for n in notes),'method':'Every raw chunk assigned in order. Bodies retain near-verbatim speech; explicit join edits documented separately. This is a mapping and editorial review, not a word-level accuracy guarantee.','chapters':[{'id':n['id'],'title':n['title'],'source_start_sec':s['start_sec'],'source_end_sec':s['end_sec'],'body_characters':len(n['body'])} for n,s in zip(notes,manifest['scenes'])]}
(w/'content-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
print('Wrote',len(notes),'reviewed scene notes')
