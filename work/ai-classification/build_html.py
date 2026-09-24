import pathlib,json,html,re,shutil,math,unicodedata
R=pathlib.Path(__file__).parent;O=R.parent.parent/'output'/'AI的分类';A=O/'assets';A.mkdir(exist_ok=True,parents=True)
U=json.loads((R/'content.json').read_text(encoding='utf8'))
E=html.escape
slides=[];mapping={}
slides.append({'type':'cover','title':'AI 的分类','body':'Agents 底层逻辑','chapter':'人工智能基础'})
def split_para(p,n=260):
 if len(p)<=n:return [p]
 clauses=re.findall(r'.+?[。？！；，]|.+$',p)
 out=[];s=''
 for c in clauses:
  if len(s)+len(c)>n and s:out.append(s);s=''
  s+=c
 if s:out.append(s)
 return out
for u in U:
 paras=[a for p in u['paragraphs'] for a in split_para(p)]
 batches=[];b=[]
 for p in paras:
  def lines(t):return math.ceil(sum(1 if unicodedata.east_asian_width(c) in 'WF' else .57 for c in t)/36)
  if (sum(map(len,b))+len(p)>315 or sum(lines(x) for x in b+[p])>.5+8 or sum(lines(x) for x in b+[p])+len(b)*.4>8.6) and b:batches.append(b);b=[]
  b.append(p)
 if b:batches.append(b)
 mapping[u['id']]=len(slides)
 u['document_target']='图文教程.html#'+u['id'];u['slides_target']=[]
 for i,b in enumerate(batches):
  slides.append({'type':'text','title':u['title']+(f'（{i+1}/{len(batches)}）' if len(batches)>1 else ''),'paragraphs':b,'chapter':u['chapter'],'unit':u['id']})
  u['slides_target'].append(len(slides))
 for f in u.get('figures',[]):
  name='figure-'+f['frame']+'.jpg';shutil.copyfile(R/'frames'/(f['frame']+'.jpg'),A/name);f['src']='assets/'+name
  slides.append({'type':'figure','title':f['title'],'figure':f,'chapter':u['chapter'],'unit':u['id']});u['slides_target'].append(len(slides))
 if u.get('note'):
  slides.append({'type':'note','title':u['title']+'：概念说明','paragraphs':[u['note']],'source':u.get('source'),'chapter':u['chapter'],'unit':u['id']});u['slides_target'].append(len(slides))
chapters=list(dict.fromkeys(u['chapter'] for u in U))
font='"Microsoft YaHei","PingFang SC","Noto Sans CJK SC",sans-serif'
common=f'''*{{box-sizing:border-box}}:root{{--ink:#172b36;--muted:#596c74;--accent:#126c70;--paper:#f9f8f3;--line:#d8e0dc}}body{{margin:0;font-family:{font};color:var(--ink);background:var(--paper)}}a{{color:var(--accent)}}button,input,select{{font:inherit}}button,a{{touch-action:manipulation}}button:focus-visible,a:focus-visible{{outline:3px solid #cc892c;outline-offset:4px}}button{{cursor:pointer}}img{{max-width:100%}}'''
toc=''.join(f'<details open><summary>{E(ch)}</summary>'+''.join(f'<a href="#{u["id"]}">{E(u["title"])}</a>' for u in U if u['chapter']==ch)+'</details>' for ch in chapters)
article=[]
for j,ch in enumerate(chapters):
 article.append(f'<header class="chapter" id="chapter-{j+1}"><span>第 {j+1} 章</span><h2>{E(ch)}</h2></header>')
 for u in U:
  if u['chapter']!=ch:continue
  article.append(f'<section class="unit" id="{u["id"]}"><h3>{E(u["title"])}</h3>')
  article.extend('<p>'+E(p)+'</p>' for p in u['paragraphs'])
  for f in u.get('figures',[]):article.append(f'<figure><a class="enlarge" href="{f["src"]}" target="_blank" title="打开大图"><img loading="lazy" src="{f["src"]}" alt="{E(f["title"])}"></a><figcaption><strong>{E(f["title"])}</strong><br>{E(f["caption"])}</figcaption></figure>')
  if u.get('note'):
   src=u.get('source');article.append('<aside class="note">'+E(u['note'])+(f' <a href="{E(src["url"])}" target="_blank" rel="noopener">{E(src["label"])}</a>' if src else '')+'</aside>')
  article.append(f'<a class="present-link" href="演示稿.html#/{mapping[u["id"]]}">在演示稿中打开本节 ↗</a></section>')
tutorial=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 的分类 · 图文教程</title><style>{common}
html{{scroll-behavior:smooth;scroll-padding-top:35px}}.sidebar{{position:fixed;width:274px;inset:0 auto 0 0;padding:34px 22px;overflow:auto;border-right:1px solid var(--line);background:#eef2ee}}.brand{{font-size:21px;font-weight:700;text-decoration:none}}.side-top{{font-size:13px;margin:10px 0 24px;color:var(--muted)}}summary{{font-size:15px;font-weight:700;margin:18px 0 10px;cursor:pointer}}details a{{display:block;padding:5px 0;font-size:13px;text-decoration:none;line-height:1.6;color:#52666d}}details a:hover{{color:var(--accent)}}main{{max-width:1120px;margin-left:274px;padding:70px 72px 90px}}.hero{{padding-bottom:52px;border-bottom:1px solid var(--line)}}.eyebrow{{font-size:14px;letter-spacing:.16em;color:var(--accent)}}h1{{font-size:56px;line-height:1.15;letter-spacing:-.03em;margin:19px 0 22px}}.lead{{font-size:21px;line-height:1.8;color:var(--muted);max-width:660px}}.hero-links{{display:flex;gap:26px;margin-top:30px;font-size:15px}}.chapter{{margin:76px 0 36px;border-top:3px solid var(--accent);padding-top:25px}}.chapter span{{font-size:14px;color:var(--accent)}}h2{{font-size:31px;margin:10px 0 0}}.unit{{margin:45px 0 56px}}h3{{font-size:24px;line-height:1.5;margin:0 0 18px}}p{{font-size:18px;line-height:2;text-align:justify;margin:0 0 17px}}figure{{margin:32px 0;background:#fff;border:1px solid var(--line)}}figure img{{display:block;width:100%;height:auto}}figcaption{{padding:16px 20px;font-size:14px;line-height:1.8;color:var(--muted)}}figcaption strong{{color:var(--ink);font-size:16px}}.note{{border-left:3px solid #b08546;background:#f2eee4;padding:16px 20px;font-size:15px;line-height:1.9;margin:24px 0}}.present-link{{font-size:13px;color:var(--muted);text-decoration:none}}footer{{border-top:1px solid var(--line);padding-top:28px;color:var(--muted);font-size:13px;line-height:1.8}}.mobile-nav{{display:none}}@media(min-width:1500px){{main{{margin-left:max(274px,calc((100vw - 1100px)/2))}}}}@media(max-width:1000px){{.sidebar{{width:225px;padding:28px 16px}}main{{margin-left:225px;padding:50px 35px}}h1{{font-size:46px}}}}@media(max-width:720px){{.sidebar{{position:relative;width:100%;max-height:320px;border-right:0;border-bottom:1px solid var(--line);padding:22px}}.sidebar details{{display:none}}.sidebar.expanded details{{display:block}}.mobile-nav{{display:inline-block;float:right;border:0;background:transparent;color:var(--accent);padding:5px}}main{{margin:0;padding:42px 22px}}h1{{font-size:42px}}h2{{font-size:27px}}p{{font-size:17px;line-height:1.95}}.hero-links{{flex-wrap:wrap}}}}@media print{{.sidebar,.hero-links,.present-link{{display:none}}main{{margin:0;padding:0;max-width:none}}.chapter{{break-before:page}}figure{{break-inside:avoid}}a{{color:inherit;text-decoration:none}}}}
</style></head><body><nav class="sidebar" aria-label="教程目录"><a class="brand" href="#">AI 的分类</a><button class="mobile-nav" aria-expanded="false" onclick="const n=this.parentElement;n.classList.toggle('expanded');this.setAttribute('aria-expanded',n.classList.contains('expanded'))">☰</button><div class="side-top">Agents 底层逻辑 · 图文教程</div>{toc}</nav><main><header class="hero"><div class="eyebrow">AGENTS · 人工智能基础</div><h1>AI 的分类</h1><p class="lead">从抽象层级与哲学流派，到应用问题、机器学习与实现方法。</p><div class="hero-links"><a href="演示稿.html">打开教学演示稿 ↗</a><a href="#chapter-1">开始阅读 ↓</a></div></header>{''.join(article)}<footer>课程内容与图示署名：渡一前端公开大师课。<br>演示稿采用 Reveal.js。图文教程和演示稿可离线打开，补充资料链接需要联网。</footer></main></body></html>'''
(O/'图文教程.html').write_text(tutorial,encoding='utf8')
ss=[]
for i,s in enumerate(slides):
 content=f'<div class="kicker">{E(s["chapter"])}</div><h2>{E(s["title"])}</h2>'
 if s['type']=='cover':content=f'<div class="cover-kicker">AGENTS · 底层逻辑</div><h1>AI 的分类</h1><p class="cover-sub">哲学流派、应用问题与实现方法</p><p class="cover-topics">机器学习 · 神经网络 · 深度学习 · Transformer</p><div class="cover-footer">渡一前端公开大师课</div>'
 elif s['type']=='figure':
  f=s['figure'];content+=f'<figure><img src="{f["src"]}" alt="{E(f["title"])}" data-zoom><figcaption>{E(f["caption"])}</figcaption></figure>'
 else:
  content+='<div class="prose">'+''.join('<p>'+E(p)+'</p>' for p in s['paragraphs'])+'</div>'
  if s.get('source'):content+=f'<a class="source" href="{s["source"]["url"]}" target="_blank" rel="noopener">{E(s["source"]["label"])}</a>'
 ss.append(f'<section class="{s["type"]}" data-unit="{s.get("unit", "cover")}">{content}</section>')
menu=''.join(f'<optgroup label="{E(ch)}">'+''.join(f'<option value="{mapping[u["id"]]}">{E(u["title"])}</option>' for u in U if u['chapter']==ch)+'</optgroup>' for ch in chapters)
deck=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 的分类 · 教学演示稿</title><link rel="stylesheet" href="assets/reveal/reveal.css"><style>{common}
.reveal{{font-family:{font};font-size:31px;color:var(--ink)}}.reveal .slides{{text-align:left}}.reveal .slides>section{{padding:35px 50px;height:720px}}.reveal h1,.reveal h2,.reveal p{{margin:0;font-weight:400}}.reveal h2{{font-size:43px;font-weight:700;line-height:1.35;letter-spacing:-.02em;margin:13px 0 29px}}.kicker{{font-size:18px;color:var(--accent);letter-spacing:.07em}}.prose p{{font-size:31px;line-height:1.85;margin:0 0 23px;text-align:justify;word-break:normal;overflow-wrap:anywhere}}.prose{{max-width:1135px}}.reveal section.note .prose{{border-left:4px solid #b08546;padding:22px 30px;background:#f1ede4;margin-top:55px}}.source{{display:inline-block;margin-top:24px;font-size:18px;color:var(--accent)}}.reveal figure{{margin:0}}.reveal figure img{{display:block;max-width:1180px;width:100%;height:476px;object-fit:contain;background:#fff;cursor:zoom-in}}.reveal figcaption{{font-size:21px;line-height:1.5;margin-top:14px;color:#415963}}.figure h2{{margin-bottom:19px}}.cover{{background:#112f3b;color:#faf9ef;padding:105px 85px!important}}.cover-kicker{{font-size:23px;letter-spacing:.13em;color:#c0dbcf}}.reveal .cover h1{{font-size:105px;line-height:1.25;font-weight:700;margin:55px 0 22px}}.reveal .cover-sub{{font-size:33px;color:#e3ece4}}.reveal .cover-topics{{font-size:23px;color:#bdcdc7;margin-top:46px}}.cover-footer{{position:absolute;bottom:54px;font-size:16px;color:#abc1b8}}.reveal .progress{{color:#248c87;height:4px}}.reveal .slide-number{{font:15px {font};right:22px;bottom:17px;background:transparent;color:#48646b}}#tools{{position:fixed;z-index:50;bottom:18px;left:22px;display:flex;align-items:center;gap:4px;border:1px solid #d7e0da;background:rgba(249,248,243,.95);padding:5px 8px;border-radius:9px}}#tools button,#tools a{{border:0;background:transparent;color:#274e58;text-decoration:none;font-size:21px;width:38px;height:34px;display:grid;place-items:center;border-radius:5px}}#tools button:hover,#tools a:hover{{background:#e3ebe5}}:fullscreen #tools,:fullscreen .reveal .slide-number{{display:none}}dialog{{border:1px solid #cedbd2;border-radius:12px;max-width:min(680px,90vw);padding:26px;color:var(--ink);background:var(--paper)}}dialog::backdrop{{background:#102c36aa}}dialog label{{display:block;margin-bottom:16px;font-size:22px;font-weight:700}}dialog select{{width:100%;padding:12px;font-size:17px}}dialog .actions{{margin-top:20px;display:flex;gap:12px;justify-content:flex-end}}dialog button{{border:1px solid #bacbc2;background:#eef2ec;color:#193e47;padding:9px 19px}}#zoom{{max-width:98vw;max-height:98vh;padding:5px;background:white}}#zoom img{{display:block;max-height:90vh;max-width:95vw;object-fit:contain}}#zoom button{{float:right;padding:3px 10px}}@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important}}}}
</style></head><body><div class="reveal"><div class="slides">{''.join(ss)}</div></div><nav id="tools" aria-label="演示工具栏"><button id="prev" title="上一页（左方向键）" aria-label="上一页">‹</button><button id="next" title="下一页（右方向键）" aria-label="下一页">›</button><button id="overview" title="总览（Esc）" aria-label="总览">▦</button><button id="jump" title="选择章节" aria-label="选择章节">☷</button><button id="fullscreen" title="全屏（F，Esc 退出）" aria-label="全屏">⛶</button><a id="read" href="图文教程.html" title="打开对应图文教程" aria-label="打开图文教程">↗</a></nav><dialog id="jumpDialog"><form method="dialog"><label for="chapterSelect">选择讲解主题</label><select id="chapterSelect"><option value="0">封面</option>{menu}</select><div class="actions"><button value="cancel">取消</button><button id="go" value="go">前往</button></div></form></dialog><dialog id="zoom"><button id="closeZoom" aria-label="关闭大图">×</button><img id="zoomImage" alt="教学图解"></dialog><script src="assets/reveal/reveal.js"></script><script>
const reveal=Reveal;const jumpDialog=document.getElementById('jumpDialog');const zoom=document.getElementById('zoom');
reveal.initialize({{width:1280,height:720,margin:.05,center:false,controls:false,progress:true,slideNumber:'c/t',hash:true,transition:'fade',transitionSpeed:'fast',view:'slide',scrollActivationWidth:null,keyboardCondition:e=>!document.querySelector('dialog[open]')&&!e.target.closest('input,textarea,select,[contenteditable="true"]')}});
document.getElementById('prev').onclick=()=>reveal.prev();document.getElementById('next').onclick=()=>reveal.next();document.getElementById('overview').onclick=()=>reveal.toggleOverview();
document.getElementById('fullscreen').onclick=()=>{{if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen();}};
document.getElementById('jump').onclick=()=>{{document.getElementById('chapterSelect').value=String(reveal.getIndices().h);jumpDialog.showModal();}};
jumpDialog.addEventListener('close',()=>{{if(jumpDialog.returnValue==='go')reveal.slide(Number(document.getElementById('chapterSelect').value));}});
document.querySelectorAll('[data-zoom]').forEach(img=>img.onclick=()=>{{document.getElementById('zoomImage').src=img.src;document.getElementById('zoomImage').alt=img.alt;zoom.showModal();}});document.getElementById('closeZoom').onclick=()=>zoom.close();
reveal.on('slidechanged',e=>{{document.getElementById('read').href='图文教程.html#'+(e.currentSlide.dataset.unit||'');}});
</script></body></html>'''
(O/'演示稿.html').write_text(deck,encoding='utf8')
(O/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=图文教程.html"><title>AI 的分类</title><a href="图文教程.html">图文教程</a>　<a href="演示稿.html">教学演示稿</a></html>',encoding='utf8')
coverage=[]
for u in U:
 coverage.append({k:u.get(k,'') for k in ['id','start','end','kind','title','document_target','slides_target','uncertainty','review_status']})
 coverage[-1]['transcript']='\n'.join(u['paragraphs']);coverage[-1]['visual_evidence']=u.get('figures',[])
(R/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf8')
(R/'slide_manifest.json').write_text(json.dumps(slides,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'units':len(U),'slides':len(slides),'figures':sum(len(u.get('figures',[])) for u in U),'chars':sum(sum(map(len,u['paragraphs'])) for u in U)},ensure_ascii=False))
