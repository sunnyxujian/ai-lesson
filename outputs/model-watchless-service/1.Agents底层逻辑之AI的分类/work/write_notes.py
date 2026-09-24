from pathlib import Path
import json,re
p=Path(__file__).resolve().parents[1];m=json.loads((p/'work/scene-manifest.json').read_text(encoding='utf-8'))
descriptions=[
('先认识概念，才能无障碍交流','思维导图以“人工智能 / Artificial Intelligence”为中心，列出哲学流派、要解决的问题、实现方法三个入口。'),
('没有代码的思考为什么仍然重要','便笺从“用户输入一句话，自动产生视频”，往上列出“计算机如何产生一个视频”和“如何生成图像”。这是讲解中从需求向前置问题追问的过程。'),
('从文生视频逐层追问到智能','便笺完整列出：用户输入一句话自动产生视频 → 计算机如何产生视频 → 如何生成图像 → 如何理解用户的话 → 如何让计算机理解语言 → 语言是什么 → 如何让计算机有智能 → 什么是智能。上方问题具有更高的抽象层次。'),
('如何理解人工智能与智能的共识','导图展开三大哲学流派：符号主义对应“智能=推理规则”，连接主义对应“智能=大脑结构”，行为主义对应“智能=环境互动”。口述先用聊天、NPC、自动泊车和排序举例，再引出这些方向。'),
('符号主义、连接主义与行为主义','画面保留三条并列关系：符号主义—推理规则；连接主义—大脑结构；行为主义—环境互动。它们在图中作为哲学流派并列，不是产品功能列表。'),
('分类角度可以不同，不能互相硬套','画面切换到“要解决的问题”分支，另两个入口仍是哲学流派和实现方法。口述通过性别、年龄、道德与职业说明不同划分角度。'),
('自然语言处理研究什么问题','自然语言处理（NLP）下有文本分类（情感分析、垃圾邮件识别）、机器翻译（中译英、英译中）、文本生成（写文章、写代码）及问答系统（智能客服、知识问答）。这些是问题类别。'),
('语音技术、Transformer与应用场景','语音技术（Speech）分支列出 ASR（语音转文字）、TTS（文字转语音）、语音唤醒（“Hey Siri”）和声纹识别（通过声音解锁）；下方可见计算机视觉分支。'),
('计算机视觉的常见任务','计算机视觉（CV）分支列出图像分类（猫或狗）、目标检测（框出行人）、语义分割（区分属于同类事物的像素区）、人脸识别（刷脸支付）、指纹识别（指纹解锁）和文字提取（提取图片文字）。'),
('用 Web API 类比业务领域与实现技术','便笺写有“web 应用 / API”与 Java、Go、Python、NodeJS。四种语言对应同一种应用需求，用来说明应用领域不限定实现技术。'),
('OCR与语音合成：场景仍在，手段可变','截图工具的 OCR 窗口显示识别出的中文条目，包括语义分割、人脸识别、指纹识别、文字提取；背景仍是业务问题导图。这是讲者现场演示文字提取的结果。'),
('实现智能的方法：知识工程、演化计算、机器学习','“实现方法”分支展开知识工程、演化计算和机器学习，其中机器学习使用黑色节点突出。'),
('机器学习的定义','导图定义为：对于一个计算机程序，如果它在任务 T 上的性能 P，随着经验 E 的增加而提升，那么我们就称这个程序为机器学习。下方指出关键是设计训练方法，让机器自主学习。'),
('任务、经验和性能，以及跨领域的智能','定义右边展开任务（T）：你要 AI 干什么；经验（E）：给 AI 喂什么；性能（P）：怎么衡量好坏。它们与左侧定义一一对应。'),
('用写文章与下棋理解 T、E、P','画面保留 T、E、P 的三个问题与机器学习定义。讲解以文章、棋谱和输赢结果逐一对应任务、经验和性能。'),
('关键是设计能够学习的训练方法','关键节点右边展开四类：监督学习—人类给答案；自监督学习—自己找答案；无监督学习—没有答案；强化学习—给奖惩。'),
('监督学习与数据标注','画面中监督学习对应“人类给答案”，下方红色方框示意标注区域。其他三类学习方式仍保留，便于比较。'),
('图像标注示例：车辆与目标框','旧课件展示一张街道图，车辆被绿色矩形框圈出，标签中可见 car 和 truck。它是人工提供目标位置与类别的标注例子。'),
('文本与音频的标注示例','本图由两个实际课件画面上下拼接：上图文本标注界面以不同颜色标记人物、地点、组织等实体；下图 ASR 标注界面包含 Speaker 1 Audio、Speaker 2 Audio 的波形以及一条 Speaker 2 的“Alright.”片段。这里的 Speaker 标签属于示例界面，不是给本课程讲者识别身份。'),
('理论方向与自监督学习的引入','画面突出“自监督学习—自己找答案”，并保留“监督学习—人类给答案”等并列节点。讲解强调方向与方法本身有作用，然后转入从现成数据寻找答案。'),
('自监督学习：遮住答案，再自己对答案','便笺写出“1+1=2”，其中“1+1”被选中。讲者用已知正确的式子说明只给前半部分，预测后半部分，再利用原有答案核对。'),
('无监督、强化学习与组合使用','导图将“无监督学习—没有答案”与“强化学习—给奖惩”并列。口述依次用螺丝良品/残次品、瓷器断代、围棋和格斗游戏解释，再强调实际训练可结合多种范式。'),
('机器学习怎样实现：从线性回归到神经网络','“如何实现？”分支列出线性回归、决策树、支持向量机和神经网络；神经网络进一步连接深度学习。这里是实现手段，与上方训练范式是不同分支。'),
('深度学习与强化学习属于不同分类角度','神经网络节点连到深度学习；强化学习则位于训练方法分支，对应“给奖惩”。两者不是同一层级的互斥选项。'),
('回顾：方向、问题、训练与实现逐步推进','画面同时保留任务/经验/性能、四种训练范式以及线性回归、决策树、支持向量机、神经网络和深度学习，展示这些术语的层级关系。'),
('从 Transformer 到工程落地，还要继续设计','便笺列出“功能”“需求分析 文档”“架构设计 图纸”；背景是机器学习、神经网络和深度学习导图。讲者用软件工程逐层设计的过程解释从理论到具体实现仍有步骤。'),
('理解关系，遇到术语就不慌','最后的画面突出“神经网络—深度学习”关系，同时保留机器学习定义、训练范式和其他实现手段。')]
replacements={
'A镜子':'Agents','A级的开发':'Agents 的开发','AI、量子开发':'AI、Agents 开发','A级产品开发':'Agents 产品开发',
'文声视频':'文生视频','纹身视频':'文生视频','纹身、视频':'文生视频','纹身图':'文生图','一真正的图像':'一帧帧的图像','方法沟通':'方法搞通',
'全是former':'Transformer','全是泡沫':'Transformer','全时方面':'Transformer','全闪方面':'Transformer','传输问题':'Transformer','全formal':'Transformer','全系统嘛':'Transformer','全系统过后':'Transformer 过后','全是模板':'Transformer',
'GPT六':'GPT Live','掐着D P T':'ChatGPT','敲GPT':'ChatGPT','chat GPT':'ChatGPT','G P T':'GPT','K P I':'KPI','M P C':'NPC','A P P':'APP','T T S':'TTS','A S R':'ASR',
'前段工程师':'前端工程师','后段工程师':'后端工程师','一代注入':'依赖注入','切分的头痕':'切分成 Token','换的头痕':'转换的 Token','他不认为你这个世界的规则':'他认为这个世界的规则',
'就像阿尔法狗':'就像 AlphaGo','经验意义':'经验 E','随着经验益':'随着经验 E','新媒体要关注什么事情':'性能 P 要关注什么事情','公知台':'控制台','复数':'负数','时间网络':'神经网络','时间手段':'实现手段','学习智能这件事儿':'实现智能这件事儿',
'人脸识别、声纹识别、文字提取':'人脸识别、指纹识别、文字提取','就声纹识别，通过声纹识别来识别':'就是文字识别，通过文字识别来识别','问 Dog':'问一个模型（此处名称识别不清）',
'加法里叫内设计':'Java 里叫类设计','内图设计，内设计':'类图设计、类设计','叫内图':'叫类图','得加入手机吧':'得架构设计吧','你三个手机有落地吗':'你做架构设计有落地吗',
'只是实现的时间途径':'只是实现途径','一读一的实现手段':'一堆一堆的实现手段',
}
fixes=[];coverage=[];c=0
for s,(title,visual) in zip(m['scenes'],descriptions):
    paragraphs=[];ids=[]
    for cue in s['source_cues']:
        c+=1;ids.append(c);text=cue['text']
        if '<|endoftext|>' in text:
            text,anomaly=text.split('<|endoftext|>',1)
            fixes.append({'cue':c,'kind':'ASR trailing anomaly','removed_from_teaching_text':anomaly,'evidence':'Original video captions at 1755, 1758, 1759, 1761 seconds continue the Go/chess example without the unrelated English. Raw ASR and service-audio excerpt retained. No listening verification claimed.'})
        for a,b in replacements.items():
            if a in text:fixes.append({'cue':c,'from':a,'to':b,'basis':'term on inspected course diagram / original visible caption / unmistakable local context'});text=text.replace(a,b)
        # Minimal filler/punctuation polish only. No string-based overlap removal.
        text=text.replace('呃，','').replace('呃，','').replace('，。','。').replace('，：','：')
        paragraphs.append(text)
    body='\n\n'.join(paragraphs)
    if not body:raise ValueError(f'No content for scene {s["id"]}')
    (p/f'work/codex-notes/scene_{s["id"]:03d}.md').write_text(f'## 标题\n{title}\n\n## Light-plus\n{body}\n\n## Visual explainer\n{visual}\n',encoding='utf-8')
    coverage.append({'scene':s['id'],'cue_ids':ids,'source_characters':len(s['transcript_text']),'note_characters':len(body),'image':s['frame_path']})
(p/'work/correction-log.json').write_text(json.dumps({'method':'Complete chronological light polish. All 101 raw chunks retained in manifest; intentional and unverified boundary repetitions preserved. No automatic overlap deletion.','audio_review_limitation':'Runtime cannot accept audio input; source subtitle/diagram comparison performed; review clips are provided for human listening.','corrections':fixes},ensure_ascii=False,indent=2),encoding='utf-8')
(p/'verify/content-coverage.json').write_text(json.dumps({'raw_cues':101,'mapped_cues':c,'complete_ordered_mapping':c==101,'scenes':coverage},ensure_ascii=False,indent=2),encoding='utf-8')
ledger={'schema_version':1,'entries':[{'stage':'transcription','model':'local Qwen3-ASR 0.6B INT8','availability':'unavailable','input_tokens':None,'output_tokens':None,'total_tokens':None,'cost_usd':None,'reason':'Local service does not expose token or cost counts.'},{'stage':'visual_review_notes_and_slides','model':'host assistant','availability':'unavailable','input_tokens':None,'output_tokens':None,'total_tokens':None,'cost_usd':None,'reason':'Host runtime does not expose actual per-stage usage to this task.'}],'totals':{'input_tokens':None,'output_tokens':None,'total_tokens':None,'cost_usd':None,'availability':'unavailable'}}
(p/'work/token-usage.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
print('notes',len(descriptions),'cues',c,'substantive replacements',len(fixes))
