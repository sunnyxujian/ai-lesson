"""Build the complete tutorial and a separate speaking deck from reviewed notes."""
from pathlib import Path
import ast,base64,html,io,json,re,subprocess,sys,shutil
from fontTools import subset
root=Path(__file__).resolve().parents[1]
p=root/'outputs/video-notes/4.AI-本质';share=p/'share';share.mkdir(exist_ok=True)
skill=Path('C:/Users/micro/.codex/skills/watchless');sys.path.insert(0,str(skill/'scripts'))
import windows_runtime
notes=json.loads((p/'work/notes-data.json').read_text(encoding='utf-8'))
manifest=json.loads((p/'work/scene-manifest.json').read_text(encoding='utf-8'))
slides=json.loads((p/'work/deck-data.json').read_text(encoding='utf-8'))
extras={11:[('scene_011/candidate_04_00-15-39.jpg','环境变量：测试目标、端口与日志级别')],14:[('scene_014/candidate_04_00-20-13.jpg','CLAUDE.md 内容进入请求上下文')],18:[('scene_018/candidate_03_00-25-28.jpg','下一轮请求包含技能文档正文')]}
extra_html={}
for chapter,items in extras.items():
 extra_html[chapter]=''
 for rel,caption in items:
  source=p/'work/candidates'/rel;name=f'extra-{chapter:02}-'+source.name
  shutil.copy2(source,share/'keyframes'/name)
  extra_html[chapter]+=f'<figure class="supplement"><img src="keyframes/{name}" alt="{caption}"><figcaption>{caption}</figcaption></figure>'
esc=lambda s:html.escape(str(s))
def md(s):
 return subprocess.run(['pandoc','-f','markdown','-t','html'],input=s,capture_output=True,text=True,encoding='utf-8',check=True).stdout
def image(n):
 f=Path(manifest['scenes'][n-1]['frame_path']);return 'data:image/jpeg;base64,'+base64.b64encode(f.read_bytes()).decode()
# Reuse the previous lesson's visual system, without executing its content builder.
tree=ast.parse((root/'work/raw-model-build.py').read_text(encoding='utf-8'))
constants={}
for node in tree.body:
 if isinstance(node,ast.Assign) and isinstance(node.value,ast.Constant):
  for t in node.targets:
   if isinstance(t,ast.Name) and t.id in ('css','article_css'):constants[t.id]=node.value.value
css=constants['css']
css+='''
/* === AI ESSENCE DIAGRAMS === */
.content{margin-top:48px}.flow{margin-top:60px;gap:25px}.flow .node{min-width:300px;padding:30px}.steps{display:flex;align-items:stretch;gap:24px;margin-top:55px}.steps>div{flex:1;border-top:3px solid var(--accent);padding:32px 24px;background:#f0eae1;font-size:37px;line-height:1.7}.steps small{display:block;font-size:26px;color:var(--muted);margin-top:22px}.steps>b{align-self:center;font-size:55px;color:var(--accent)}.bigword{font-size:118px;color:var(--accent);font-family:'Noto Serif SC',serif;margin-top:80px}.code{font-size:31px;line-height:1.65;white-space:pre-wrap;padding:32px 40px;background:#ede8e0;border-left:5px solid var(--accent);margin:0;font-family:'Noto Sans SC',monospace}.code em{font-style:normal;color:var(--accent);font-weight:700}.split{grid-template-columns:740px 1fr;gap:60px}.split p{font-size:33px}.split figure img{max-height:450px;object-fit:contain;background:#fff}.pointlist{list-style:none;padding:0;margin:40px 0}.pointlist li{font-size:43px;line-height:1.6;padding:22px 0;border-bottom:1px solid var(--line)}.pointlist b{color:var(--accent)}.band{font-size:43px;padding:35px 40px;border-left:5px solid var(--accent);background:#f0eae1;margin-top:38px;line-height:1.6}.large-number{font-size:105px;font-family:'Noto Serif SC',serif;color:var(--accent)}.minor{font-size:28px;color:var(--muted)}.takeaway{margin-top:45px;font-size:40px}.comparison p{font-size:47px}.comparison strong{font-size:33px}.comparison em{font-size:31px}.title h2{margin-top:130px;font-size:103px}.deck-controls{width:max-content;max-width:calc(100vw - 16px);white-space:nowrap}@media(max-width:500px){.deck-controls{font-size:11px;gap:3px;padding:5px 6px}.deck-controls button,.deck-controls a{padding:5px}}
'''
base=(Path('C:/Users/micro/.codex/skills/frontend-slides/viewport-base.css')).read_text(encoding='utf-8')
sections=[]
for i,s in enumerate(slides,1):
 n=notes[s['scene']-1];body=re.sub(r'\{\{image:(\d+)\}\}',lambda m:image(int(m[1])),s['body'])
 speaker='<h3>'+esc(s['title'].replace('<br>',' '))+'</h3><p class="note-hint">'+esc(s['hint'])+'</p><h4>完整讲解</h4>'+md(n['body'])+'<h4>画面与校读</h4>'+md(n['visual'])
 sections.append(f'<section class="slide {s.get("kind","")}'+(' active visible' if i==1 else '')+f'" aria-label="第{i}页"><div class="eyebrow">AI 基础 / 第四课</div><h2 class="reveal" data-edit>{s["title"]}</h2><div class="content reveal">{body}</div><div class="footer"><a class="source-link" href="完整教程.html#section-{s["scene"]:02}" target="_blank">阅读完整讲解 ↗</a><span>AI ESSENCE / {i:02}</span></div><aside class="speaker-notes">{speaker}</aside></section>')
controller=(root/'work/raw-model-deck-controller.js').read_text(encoding='utf-8').replace('raw-model-paper-ink-v1','ai-essence-paper-ink-v1').replace('Raw-Model-重点演示稿.html','AI本质-重点演示稿.html')
deck='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 的本质 · 重点演示稿</title><style>FONT_CSS\n'+base+css+'</style></head><body><div class="deck-viewport"><main class="deck-stage">'+''.join(sections)+'''</main></div><nav class="deck-controls" aria-label="演示控制"><button id="prev" aria-label="上一页">←</button><span id="pageCount"></span><button id="next" aria-label="下一页">→</button><button id="notesToggle">讲者备注 N</button><button id="save">保存</button><a href="完整教程.html" target="_blank">完整教程 ↗</a></nav><aside id="notes" hidden><button id="closeNotes" aria-label="关闭备注">×</button><div id="notesContent"></div></aside><div class="edit-hotzone"></div><button class="edit-toggle" id="editToggle">编辑 E</button><div id="progress"></div><script>'''+controller+'</script></body></html>'
article_css=constants['article_css']+'''
/* === CODE, TABLES AND PRINT LAYOUT === */
pre{padding:22px;background:#f0eae1;border-left:3px solid #b22d3f;overflow-x:auto;line-height:1.6}code{font-family:'Noto Sans SC',monospace;font-size:.9em}table{border-collapse:collapse;width:100%;font-size:15px}th,td{border-bottom:1px solid #d8d1c7;padding:10px;text-align:left}li{font-size:17px}h3{font-size:20px}strong{font-weight:700}@media print{header{padding-top:10mm;min-height:230mm}header::after{content:"学习路径\\A \\A TOC_CONTENT";white-space:pre-line;display:block;font-size:11px;line-height:1.85;margin-top:10mm}p,li{font-size:11.7px;line-height:1.9}pre{font-size:10px;padding:12px;white-space:pre-wrap;break-inside:avoid}table{font-size:10px}h3{font-size:14px;break-after:avoid}.source-note{break-before:auto;margin-top:18px}figure img{max-height:73mm}h2{break-after:avoid}thead{display:table-header-group}}
'''
article_css=article_css.replace('TOC_CONTENT',r'\A '.join(f'{n["id"]:02}  {n["title"]}' for n in notes))
article_css+='@media print{figure img{max-height:65mm}p,li{font-size:11.5px;line-height:1.8}.supplement{break-before:auto}.visual pre{font-size:10px}}'
article_css+='@media print{#section-11 figure img,#section-14 figure img,#section-18 figure img{max-height:48mm}#section-11 figure,#section-14 figure,#section-18 figure{margin:9px 0}#section-11>p,#section-14>p,#section-18>p{font-size:11px;line-height:1.72;margin:9px 0}#section-11 .visual{padding:5px 12px}#section-11 .visual pre{margin:5px 0;padding:6px;font-size:9px;line-height:1.4}}'
article_css+='@media print{#section-14 figure img{max-height:36mm}#section-14 .visual{margin-top:12px;padding:6px 12px}}'
article='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 的本质 · 完整教程</title><style>FONT_CSS\n'+article_css+'</style></head><body><header><div class="kicker">AI 基础 · 第四课</div><h1>AI 的本质</h1><p>从 Raw Model、Model Service 到 AI Application，沿着真实请求追踪提示词、技能与工具调用。保留课堂推理、案例及操作细节。</p><div class="actions"><a href="重点演示稿.html">重点演示稿 ↗</a><a href="4.AI 本质-visual-explainer.pdf">PDF 讲义 ↗</a></div></header><div class="layout"><nav aria-label="章节目录">'+''.join(f'<a href="#section-{n["id"]:02}">{n["id"]:02} · {esc(n["title"])}</a>' for n in notes)+'</nav><article>'
for n,s in zip(notes,manifest['scenes']):
 article+=f'<section id="section-{n["id"]:02}"><h2>{n["id"]:02} · {esc(n["title"])}</h2><figure><img src="keyframes/{Path(s["frame_path"]).name}" alt="{esc(n["title"])}课堂画面"><figcaption>课堂画面 · 点击放大</figcaption></figure>'+md(n['body'])+extra_html.get(n['id'],'')+'<aside class="visual"><h3>画面与校读说明</h3>'+md(n['visual'])+'</aside></section>'
article+='</article></div><footer class="source-note"><p>来源：用户提供的《4.AI 本质.mp4》。正文依照课堂顺序轻度整理；课程中的产品、价格、工具能力和讲者判断保留录制时语境，不作为当前产品规格。</p><p>本地 Qwen3-ASR 0.6B INT8 转写，结合画面核对术语；原始音频块保存在 source-materials。时间仅为音频块粒度，不是逐词对齐；未进行逐字人工听校，可能仍有识别误差。已对全部 69 个音频块交界和 5 处疑点做本地音频重识别；这不等于逐字人工听校。实际模型 Token 用量与费用未由运行环境提供。</p></footer><dialog id="zoom"><button class="close" onclick="this.parentElement.close()">关闭 ×</button><img alt="放大画面"></dialog><script>document.querySelectorAll("figure img").forEach(im=>im.onclick=()=>{let d=document.querySelector("#zoom");d.querySelector("img").src=im.src;d.showModal()});document.querySelector("#zoom").addEventListener("click",e=>{if(e.target.tagName==="DIALOG")e.target.close()})</script></body></html>'
alltext=html.unescape(re.sub('<[^>]*>','',article+deck))+''.join(chr(i) for i in range(32,127))+'结束编辑保存上一页下一页讲者备注完整教程'
fontcss=''
for family,file in [('Noto Sans SC','NotoSansSC-VF.ttf'),('Noto Serif SC','NotoSerifSC-VF.ttf')]:
 options=subset.Options();options.flavor='woff2';font=subset.load_font('C:/Windows/Fonts/'+file,options);sub=subset.Subsetter(options=options);sub.populate(text=alltext);sub.subset(font);font.flavor='woff2';buf=io.BytesIO();font.save(buf)
 fontcss+=f'@font-face{{font-family:"{family}";font-weight:100 900;src:url(data:font/woff2;base64,{base64.b64encode(buf.getvalue()).decode()}) format("woff2");font-display:swap}}\n'
for name,content in [('完整教程.html',article),('重点演示稿.html',deck),('4.AI 本质-visual-explainer.html',article)]:
 (share/name).write_text(content.replace('FONT_CSS',fontcss),encoding='utf-8')
(share/'讲者备注.md').write_text('# AI 的本质 · 讲者备注\n\n'+''.join(f'## {i:02} {s["title"].replace("<br>"," ")}\n\n{s["hint"]}\n\n### 对应完整讲解\n\n{notes[s["scene"]-1]["body"]}\n\n### 画面与校读\n\n{notes[s["scene"]-1]["visual"]}\n\n' for i,s in enumerate(slides,1)),encoding='utf-8')
(p/'work/deck-manifest.json').write_text(json.dumps([{'slide':i,'title':s['title'],'source_scene':s['scene']} for i,s in enumerate(slides,1)],ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Tutorial: {len(notes)} chapters. Deck: {len(slides)} slides. Fonts embedded.')
