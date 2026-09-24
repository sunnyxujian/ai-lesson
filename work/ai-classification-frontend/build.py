from pathlib import Path
import json,html,base64,re
W=Path(__file__).parent; ROOT=W.parents[1]; OLD=ROOT/'output/AI的分类'; OUT=ROOT/'output/AI的分类_课堂结构图.html'
SKILL=Path('C:/Users/micro/.codex/skills/frontend-slides')
units=json.loads((W.parent/'ai-classification/content.json').read_text(encoding='utf-8'))
manifest=json.loads((W.parent/'ai-classification/slide_manifest.json').read_text(encoding='utf-8'))
by_id={u['id']:u for u in units}; chapters=list(dict.fromkeys(u['chapter'] for u in units)); output=[]; records=[]; editid=0
def esc(s): return html.escape(str(s),quote=True)
def edit(text,tag='span',cls=''):
 global editid
 editid+=1
 return f'<{tag} data-edit="t{editid}" class="{cls}">{esc(text)}</{tag}>'
def notes(u=None,extra=''):
 if not u:return '<aside class="notes">'+extra+'</aside>'
 text=''.join('<p>'+esc(p)+'</p>' for p in u['paragraphs'])
 if u.get('note'):text+='<p>'+esc(u['note'])+'</p>'
 if u.get('source'):text+='<p class="notes-source"><a href="'+esc(u['source']['url'])+'" target="_blank" rel="noopener">'+esc(u['source']['label'])+'</a></p>'
 return '<aside class="notes">'+text+extra+'</aside>'
def add(title,content,chapter='',kind='text',unit='',n=''):
 page=len(output)+1; ci=chapters.index(chapter)+1 if chapter in chapters else 0
 foot=f'<footer class="slide-footer"><span>渡一前端公开大师课 · AI 的分类</span><span class="chapter-progress">'+''.join(f'<i class="{"done" if j<ci else ""}"></i>' for j in range(6))+f'</span><span>{page:03d}</span></footer>'
 output.append(f'<section class="slide {kind}" data-title="{esc(title)}" data-unit="{unit}" data-kind="{kind}">'+content+foot+n+'</section>')
 records.append(dict(title=title,kind=kind,chapter=chapter,unit=unit))
def head(title,chapter,label=''):
 ci=chapters.index(chapter)+1 if chapter in chapters else 0
 return '<div class="kicker">'+esc(f'{ci:02d} / {chapter}' if ci else label)+'</div>'+edit(title,'h2','slide-title animate')
cover='<div class="kicker">AGENTS / 底层逻辑</div>'+edit('AI 的分类','h1','animate')+'<p class="intro animate">从哲学流派到工程实现<br>理解概念之间的关系</p><div class="cover-map animate"><div class="root-node">人工智能</div><div class="branches"><div class="branch-node">哲学流派<small>符号主义 · 连接主义 · 行为主义</small></div><div class="branch-node">要解决的问题</div><div class="branch-node">实现方法<small>机器学习 → 神经网络 → 深度学习</small></div></div></div>'
add('AI 的分类',cover,kind='cover',n=notes(extra='<p>Agents 底层逻辑：认识人工智能的分类，以及各个概念之间的关系。</p>'))
agenda=head('从抽象概念，走向工程实现','','课程导览')+'<div class="agenda-grid">'+''.join('<div class="agenda-entry animate"><b>'+str(i+1).zfill(2)+'</b>'+edit(c)+'</div>' for i,c in enumerate(chapters))+'</div>'
add('课程导览',agenda,kind='agenda')
subtitles=['先想清楚问题，再讨论代码','认识三种思想，理解它们可以交融','业务领域与模型架构，是不同的分类角度','用任务、经验和性能理解学习','答案从哪里来，反馈如何给出','把机器学习、神经网络与深度学习放回各自的位置']
routes=[['具体需求','前置问题','抽象层级'],['推理规则','大脑结构','环境互动'],['语言','语音','视觉'],['任务 T','经验 E','性能 P'],['人工答案','数据自身','结构与奖惩'],['机器学习','神经网络','深度学习','Transformer']]
diagrams={
'u017':('一个需求，向上追问前置问题',[('具体需求','输入一句话\n自动生成视频'),('生成画面','视频由一帧帧图像组成'),('理解语言','理解用户的话\n理解语言本身'),('智能问题','如何让机器有智能\n什么是智能')],'path','每上一层，都在回答下一步实现所依赖的问题。'),
'u030':('三种流派，三种思考方向',[('符号主义','推理规则\n苏格拉底三段论\n规则式 NPC 与迷宫'),('连接主义','大脑结构\n神经元之间的连接\n研究连接与学习'),('行为主义','环境互动\n探索、协作与反馈\n在互动中调整行为')],'compare','这些思想可以交融，不必把现代产品硬分到某一个流派。'),
'u043':('先区分业务领域，再讨论实现架构',[('自然语言处理','文本分类、翻译\n文本生成、问答'),('语音技术','ASR、TTS\n语音唤醒、声纹识别'),('计算机视觉','图像分类、目标检测\n分割、识别与文字提取')],'compare','Transformer 是架构；NLP、语音技术、计算机视觉描述要解决的问题。'),
'u057':('什么样的变化，才叫学习？',[('T / 任务','要 AI 做什么？'),('E / 经验','给 AI 什么经验？'),('P / 性能','怎样衡量好坏？')],'compare','程序在任务 T 上的性能 P，随着经验 E 的增加而提升。'),
'u073':('给数据，不等于已经发生学习',[('输入','棋谱、文章\n只是经验材料'),('训练方法','让机器从经验中学习\n形成可用的能力'),('表现','在任务上做得更好\n用明确标准衡量')],'path','把棋谱打印一百遍，不能代替设计让机器学习的训练方法。'),
'u080':('监督与自监督：答案从哪里来？',[('监督学习','人给出标准答案\n例如标注猫、狗和实体'),('自监督学习','从数据本身构造目标\n例如遮住 1＋1＝2 的后半部分')],'compare','自监督仍需要人的任务设计和数据准备；答案不是凭空产生的。'),
'u088':('学习范式，关注训练如何进行',[('监督学习','人类提供答案'),('自监督学习','从数据构造目标'),('无监督学习','发现结构或异常'),('强化学习','用奖惩反馈调整策略')],'compare','不同范式可以组合；模型架构名并不能替代完整的训练设计。'),
'u093':('强化学习与深度学习，不是同一分类角度',[('强化学习','一种学习范式\n关注反馈与策略调整'),('深度学习','神经网络这一方向\n关注多层网络的表示与学习')],'compare','一个系统可以使用深度神经网络，也可以用强化学习进行训练。'),
'u099':('从方法到实现，一层一层具体化',[('机器学习','通过经验提升表现'),('神经网络','一种实现方法'),('深度学习','神经网络这一方向'),('Transformer','具体架构设计')],'path','还需要结合行业特点继续设计，最后进入工程实现。')}
seen=set()
for m in manifest[1:]:
 uid=m.get('unit','');u=by_id.get(uid); ch=m.get('chapter',''); typ=m['type'];title=m['title']
 if ch not in seen and ch in chapters:
  seen.add(ch);idx=chapters.index(ch)
  h=f'<div class="kicker">AGENTS / AI 的分类</div><div class="chapter-number">{idx+1:02d}</div>'+edit(ch,'h2','animate')+edit(subtitles[idx],'p','chapter-subtitle animate')+'<div class="chapter-route">'+''.join('<span>'+esc(s)+'</span>' for s in routes[idx])+'</div>'
  add(ch,h,ch,'chapter-slide')
 if typ=='text':
  ps=m['paragraphs'];count=sum(map(len,ps));mark='课堂讲解'
  content=head(title,ch)+f'<div class="content-grid"><div class="side-mark animate">{mark}<span class="unit-no">{int(uid[1:]):02d}</span><span class="tag-label">'+esc(ch)+'</span></div><div class="body-copy '+('dense' if count>230 else '')+' animate">'+''.join(edit(p,'p') for p in ps)+'</div></div>'
  add(title,content,ch,'reading',uid,notes(u))
 elif typ=='figure':
  f=m['figure'];data=base64.b64encode((OLD/f['src']).read_bytes()).decode()
  content=head(title,ch)+'<div class="figure-layout animate"><img alt="'+esc(title)+'" src="data:image/jpeg;base64,'+data+'"><div class="figure-caption"><b>图解 · '+esc(ch)+'</b>'+edit(f['caption'],'p')+'</div></div>'
  add(title,content,ch,'figure-slide',uid,notes(u))
 elif typ=='note':
  note=m.get('body') or m.get('text') or (u or {}).get('note','');source=(u or {}).get('source')
  content=head(title,ch)+'<div class="content-grid"><div class="side-mark">概念边界<span class="tag-label">结合例子理解，也保留适用条件。</span></div><div class="body-copy animate">'+edit(note,'p')
  if source:content+='<p class="source-link"><a href="'+esc(source['url'])+'" target="_blank" rel="noopener">'+esc(source['label'])+' ↗</a></p>'
  content+='</div></div>';add(title,content,ch,'clarification',uid,notes(u))
 else: raise ValueError(m)
 # Insert diagrams once, after the final existing page for this teaching unit.
 next_idx=manifest.index(m)+1
 if uid in diagrams and (next_idx==len(manifest) or manifest[next_idx].get('unit')!=uid):
  dt,nodes,layout,caption=diagrams[uid]
  h=head(dt,ch)+'<div class="diagram '+layout+'">'
  for j,(label,text) in enumerate(nodes):
   if j and layout=='path':h+='<span class="diagram-arrow">→</span>'
   h+='<div class="diagram-node animate">'+edit(label,'b')+'<p>'+esc(text).replace('\n','<br>')+'</p></div>'
  h+='</div>'+edit(caption,'p','comparison-caption');add(dt,h,ch,'diagram-slide',uid,notes(u))
end=head('听到一个名词，先问它属于哪一层','','课程回顾')+'<div class="diagram compare">'+''.join('<div class="diagram-node animate">'+edit(a,'b')+edit(b,'p')+'</div>' for a,b in [('思想方向','它在解释如何获得智能？'),('业务问题','它在说明要解决什么任务？'),('实现与训练','它在描述方法、架构或学习范式？')])+'</div>'+edit('理解关系，就不必被不断出现的概念牵着走。','p','comparison-caption')
add('课程回顾',end,kind='diagram-slide')
fonts=(W/'Noto-Sans-SC.css').read_text(encoding='utf-8'); css=(OLD/'assets/reveal/reveal.css').read_text(encoding='utf-8')+(SKILL/'viewport-base.css').read_text(encoding='utf-8')+(W/'deck.css').read_text(encoding='utf-8')
reveal=(OLD/'assets/reveal/reveal.js').read_text(encoding='utf-8');reveal=re.sub(r'//# sourceMappingURL=.*','',reveal);js=(W/'deck.js').read_text(encoding='utf-8')
ui='''<div class="edit-hotzone" id="editHotzone"><button class="edit-toggle" id="editToggle">编辑 · E</button></div><div class="edit-status" id="editStatus">已自动保存到此浏览器 · Ctrl+S 导出 HTML</div><nav class="deck-controls" aria-label="演示控制"><button id="prev" title="上一页（←）" aria-label="上一页">←</button><span class="page-display" id="pageDisplay"></span><button id="next" title="下一页（→）" aria-label="下一页">→</button><button id="tocButton" title="目录（G）">目录</button><button id="notesButton" title="讲解（N）">讲解</button><button id="fullButton" title="全屏（F）">全屏</button></nav><div id="progress" class="progress-rail"></div><div class="backdrop" id="backdrop" hidden></div><section class="modal" id="tocModal" role="dialog" aria-modal="true" aria-label="课程目录" hidden><header><h2>课程目录</h2><button data-close>关闭 ×</button></header><input id="search" type="search" placeholder="搜索标题" aria-label="搜索标题"><div class="toc-list" id="tocList"></div></section><section class="modal" id="notesModal" role="dialog" aria-modal="true" aria-labelledby="notesTitle" hidden><header><h2 id="notesTitle"></h2><button data-close>关闭 ×</button></header><div id="notesBody"></div></section>'''
license=(OLD/'assets/reveal/LICENSE').read_text(encoding='utf-8')+'\n\nEmbedded Noto Sans SC font license:\n'+(W/'Noto-OFL.txt').read_text(encoding='utf-8')
doc='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 的分类 · 课堂结构图</title><!-- Reveal.js license\n'+license+'--><style>/* === EMBEDDED GOOGLE FONTS === */'+fonts+'\n'+css+'</style></head><body><div class="deck-viewport"><main id="deckStage" class="deck-stage reveal"><div class="slides">'+''.join(output)+'</div></main></div>'+ui+'<script>/* === EMBEDDED REVEAL.JS === */\n'+reveal+'</script><script>'+js+'</script></body></html>'
OUT.write_text(doc,encoding='utf-8');(W/'manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'file':str(OUT),'slides':len(output),'bytes':OUT.stat().st_size,'editable_blocks':editid},ensure_ascii=False))
