from pathlib import Path
import json,re,html,base64,urllib.request,urllib.parse
P=Path(__file__).resolve().parent.parent
m=json.loads((P/'work/scene-manifest.json').read_text(encoding='utf8'))
slides=[
('训练模式\n架构与模型','从“怎样更新参数”走到“怎样使用模型”',['三种训练模式','张量、遗忘与泛化','架构 → 框架 → 模型'],0),
('为什么单样本更新会震荡？','SGD · 一次 1 个样本',['每个样本给出不同的调整方向','换输入，就像换了一座“山”','马上更新，参数可能东跑西跑'],1),
('先有数据，才谈训练','DATA · 手写数字案例',['多种笔迹，已经标注','同一个数字，也有不同写法','拿到好的训练数据很麻烦'],2),
('全部计算，再求平均','FULL BATCH · 暂不逐样本更新',['每个样本先得到调整结果','同一参数的梯度汇总求平均','更新后重来，直到结果可接受'],3),
('把大数据集切成小批次','MINI-BATCH · 一批更新一次',['批内计算 → 求平均 → 更新','下一批使用更新后的参数','示意逐个讲，实际可以并行'],4),
('张量组织批量数据','TENSOR · 从标量到多维数组',['0 维：标量，例如 3','1 维：向量；2 维：矩阵','更高维组织数据，供 GPU 并行计算'],5),
('寻找一个可接受的结果','OPTIMIZATION · 反复训练与协调',['跑一批、更新，再跑下一批','各样本对参数的要求共同参与','目标是可接受，而非绝对完美'],6),
('学会 1，却忘了 0','FORGETTING · 为什么要打乱',['先只训练 0，参数向 0 倾斜','接着只训练 1，旧能力可能受损','混合训练样本，兼顾不同类别'],7),
('认识训练之外的样本','GENERALIZATION · 三个术语',['泛化：没见过的输入，也能识别','过拟合：训练集好，集外表现差','欠拟合：连训练集也没学好'],8),
('网络架构是一张图纸','ARCHITECTURE · 设计层与连接',['多少层、多少神经元、怎样连接','CNN：课件中的图像经典架构','Transformer：从语言走向多模态'],9),
('框架把图纸落成代码','FRAMEWORK · 训练与运行',['TensorFlow 与 PyTorch','本课用手机小任务解释边缘计算','框架把网络设计变成可执行程序'],10),
('固定参数，前向出结果','INFERENCE · 与训练的区别',['训练：预测、反向传播、更新参数','推理：载入参数，执行前向传播','训练框架也能用于推理'],11),
('模型保存了训练的结果','MODEL · 权重与配置',['权重文件：主要参数和体积','配置文件：架构、维度、精度','本地调试之外，生产还要考虑性能'],12)]
notes=[]
for s in m['scenes']:
 raw=(P/f'work/codex-notes/scene_{s["id"]:03}.md').read_text(encoding='utf8')
 notes.append(raw.split('## Light-plus\n')[1].split('\n## Visual explainer')[0].strip())
base=Path(r'C:\Users\micro\.codex\skills\frontend-slides\viewport-base.css').read_text(encoding='utf8')
deck=P/'slides';deck.mkdir(exist_ok=True)
allchars=''.join(x[0]+x[1]+''.join(x[2]) for x in slides)+''.join(notes)+'完整教程备注编辑上一页下一页保存'
fontcss=''
try:
 url='https://fonts.googleapis.com/css2?'+urllib.parse.urlencode({'family':'Noto Sans SC:wght@400;700','text':''.join(sorted(set(allchars)))})
 css=urllib.request.urlopen(url,timeout=40).read().decode()
 for u in set(re.findall(r'url\((https[^)]+)\)',css)):
  data=urllib.request.urlopen(u,timeout=40).read();css=css.replace(u,'data:font/woff2;base64,'+base64.b64encode(data).decode())
 fontcss=css
except Exception as e:
 print('font warning',str(e));fontcss="@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');"
sections=[]
for i,(title,kicker,bullets,scene) in enumerate(slides):
 img=''
 if scene:
  imagefile=Path(m['scenes'][scene-1]['frame_path']);data=base64.b64encode(imagefile.read_bytes()).decode()
  img=f'<figure class="evidence"><img src="data:image/jpeg;base64,{data}" alt="{html.escape(title)}对应课程画面"><figcaption>课程画面 · {scene:02d}</figcaption></figure>'
  note=notes[scene-1]
 else:
  img='<div class="flow"><b>梯度</b><span>↓</span><b>参数</b><span>↓</span><b>模型</b></div>'
  note='本课重点是连接术语和全过程：训练模式决定何时更新参数；架构描述网络设计；框架执行训练和推理；模型文件保存训练结果。完整教程保持所有原课程案例与展开，幻灯片只放讲解重点。'+notes[0].split('\n')[0]
 sections.append(f'''<!-- === SLIDE {i+1}: {html.escape(title)} === -->
 <section class="slide {'active visible' if i==0 else ''}" data-scene="{scene}">
 <div class="stripe"></div><header class="kicker editable">05 / AGENTS · {html.escape(kicker)}</header>
 <div class="copy"><h1 class="editable reveal">{html.escape(title).replace(chr(10),'<br>')}</h1><ul>{''.join(f'<li class="editable reveal">{html.escape(b)}</li>' for b in bullets)}</ul></div>
 {img}<footer><span>训练模式与框架</span><a href="../share/5.Agents底层逻辑之训练模式-visual-explainer.html" target="_blank">完整教程 ↗</a><strong>{i+1:02d} / {len(slides):02d}</strong></footer>
 <aside class="speaker-notes" hidden>{html.escape(note)}</aside></section>''')
css='''/* === THEME: teal technical notebook === */
:root{--stage-bg:#092b31;--slide-bg:#f6f3e9;--ink:#082f35;--accent:#b7462f;--line:#bccfc6}*{box-sizing:border-box}body{font-family:'Noto Sans SC',sans-serif;color:var(--ink)}
/* === FIXED LAYOUT === */
.slide{padding:75px 88px;background:linear-gradient(90deg,transparent 59%,#dfebe3 59%),var(--slide-bg)}.stripe{position:absolute;top:0;left:0;width:18px;height:100%;background:var(--accent)}.kicker{font-size:25px;letter-spacing:2px;color:#3f6868}.copy{position:absolute;left:88px;top:215px;width:875px}h1{font-size:76px;line-height:1.2;margin:0 0 65px;letter-spacing:-2px}ul{padding-left:34px;margin:0}li{font-size:35px;line-height:1.65;margin:18px 0}li::marker{color:var(--accent)}.evidence{position:absolute;left:1050px;top:274px;width:800px;margin:0}.evidence img{width:800px;height:450px;object-fit:contain;box-shadow:0 20px 45px #082f3528;background:white;border:1px solid #bdccc5}.evidence figcaption{font-size:20px;color:#50726c;margin-top:22px}.flow{position:absolute;left:1230px;top:220px;display:flex;flex-direction:column;align-items:center;gap:16px;font-size:52px}.flow b{border:2px solid #678e81;padding:25px 90px}.flow span{color:var(--accent)}footer{position:absolute;left:88px;right:80px;bottom:55px;border-top:2px solid var(--line);padding-top:25px;display:flex;align-items:center;justify-content:space-between;font-size:23px}footer a{color:var(--ink);text-decoration:none}footer strong{color:var(--accent)}
/* === MOTION === */
.reveal{opacity:0;transform:translateY(16px);transition:opacity .45s ease,transform .45s ease}.visible .reveal{opacity:1;transform:translateY(0)}li:nth-child(2){transition-delay:.08s}li:nth-child(3){transition-delay:.16s}
/* === CONTROLS AND NOTES === */
.deck-controls{display:flex;gap:6px;bottom:10px}button{font:inherit;background:#163e43;color:#f6f3e9;border:1px solid #76948c;padding:7px 12px;cursor:pointer;border-radius:4px}.notes-panel{position:fixed;inset:8% 8%;z-index:2000;background:#fffdf5;color:#173338;box-shadow:0 0 0 100vmax #0008;padding:32px;overflow:auto;white-space:pre-wrap;font-size:19px;line-height:1.85}.notes-panel[hidden]{display:none}.notes-panel button{float:right}.edit-hotzone{position:fixed;top:0;left:0;width:80px;height:80px;z-index:3000}.edit-toggle{position:fixed;top:12px;left:12px;z-index:3001;opacity:0;pointer-events:none}.edit-toggle.show,.edit-toggle.active{opacity:1;pointer-events:auto}[contenteditable=true]{outline:2px dashed #b7462f}.speaker-notes{display:none}@media print{.notes-panel,.edit-hotzone,.edit-toggle{display:none}.reveal{opacity:1;transform:none}}
'''
js='''/* === SLIDE PRESENTATION CONTROLLER === */
class SlidePresentation{constructor(){this.slides=[...document.querySelectorAll('.slide')];this.currentSlide=0;this.stage=document.querySelector('.deck-stage');this.editing=false;this.setupStageScale();this.setupKeyboardNav();this.setupTouchNav();this.showSlide(0);let last=0;addEventListener('wheel',e=>{if(this.editing||!document.querySelector('#notes').hidden)return;if(Date.now()-last>400){this.showSlide(this.currentSlide+(e.deltaY>0?1:-1));last=Date.now()}},{passive:true})}
setupStageScale(){const s=()=>{let f=Math.min(innerWidth/1920,innerHeight/1080);this.stage.style.transform=`translate(${(innerWidth-1920*f)/2}px,${(innerHeight-1080*f)/2}px) scale(${f})`};s();addEventListener('resize',s)}
showSlide(n){this.currentSlide=Math.max(0,Math.min(n,this.slides.length-1));this.slides.forEach((s,i)=>{s.classList.toggle('active',i===this.currentSlide);s.classList.toggle('visible',i===this.currentSlide)});document.querySelector('#counter').textContent=`${this.currentSlide+1} / ${this.slides.length}`}
setupKeyboardNav(){addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key==='s'){e.preventDefault();save();return}if(e.target.isContentEditable)return;if(e.key==='Escape'){document.querySelector('#notes').hidden=true;return}if(e.key.toLowerCase()==='n')showNotes();if(e.key.toLowerCase()==='e')toggleEdit();if(!document.querySelector('#notes').hidden)return;if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();this.showSlide(this.currentSlide+1)}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();this.showSlide(this.currentSlide-1)}})}
setupTouchNav(){let x=0;addEventListener('touchstart',e=>x=e.changedTouches[0].clientX,{passive:true});addEventListener('touchend',e=>{if(this.editing||!document.querySelector('#notes').hidden)return;let d=e.changedTouches[0].clientX-x;if(Math.abs(d)>40)this.showSlide(this.currentSlide+(d<0?1:-1))},{passive:true})}}
const deck=new SlidePresentation();window.deck=deck;function showNotes(){let p=document.querySelector('#notes');document.querySelector('#notesText').textContent=deck.slides[deck.currentSlide].querySelector('.speaker-notes').textContent;p.hidden=!p.hidden}
/* === INLINE EDITING AND SAVE === */
const key='watchless-training-mode-deck-v1';const els=[...document.querySelectorAll('.editable')];try{let saved=JSON.parse(localStorage.getItem(key));if(saved)els.forEach((e,i)=>{if(saved[i])e.innerHTML=saved[i]})}catch{}els.forEach(e=>e.addEventListener('input',()=>{try{localStorage.setItem(key,JSON.stringify(els.map(e=>e.innerHTML)))}catch{}}));function toggleEdit(){deck.editing=!deck.editing;els.forEach(e=>e.contentEditable=deck.editing);document.querySelector('#edit').classList.toggle('active',deck.editing)}function save(){let doc=document.documentElement.cloneNode(true);doc.querySelectorAll('[contenteditable]').forEach(e=>e.removeAttribute('contenteditable'));let blob=new Blob(['<!DOCTYPE html>'+doc.outerHTML],{type:'text/html'});let a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='训练模式与框架.html';a.click();URL.revokeObjectURL(a.href)}let hide;const hot=document.querySelector('.edit-hotzone'),btn=document.querySelector('#edit');[hot,btn].forEach(e=>{e.addEventListener('mouseenter',()=>{clearTimeout(hide);btn.classList.add('show')});e.addEventListener('mouseleave',()=>{hide=setTimeout(()=>{if(!deck.editing)btn.classList.remove('show')},400)})});hot.onclick=toggleEdit;btn.onclick=toggleEdit;
'''
out=f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>训练模式与框架</title><style>{fontcss}\n{base}\n{css}</style></head><body><div class="deck-viewport"><main class="deck-stage">{''.join(sections)}</main></div><nav class="deck-controls" aria-label="幻灯片控制"><button onclick="deck.showSlide(deck.currentSlide-1)">←</button><button id="counter"></button><button onclick="deck.showSlide(deck.currentSlide+1)">→</button><button onclick="showNotes()">备注 N</button><button onclick="save()">保存</button></nav><div class="edit-hotzone"></div><button class="edit-toggle" id="edit">编辑 E</button><aside class="notes-panel" id="notes" hidden><button onclick="this.parentElement.hidden=true">关闭</button><div id="notesText"></div></aside><script>{js}</script></body></html>'''
(deck/'index.html').write_text(out,encoding='utf8')
(deck/'speaker-notes.md').write_text('# 训练模式与框架 · 讲者备注\n\n'+'\n\n'.join(f'## {i+1}. {x[0]}\n\n'+(notes[x[3]-1] if x[3] else '先介绍课程路线，再依次讨论训练模式、泛化、架构、框架和模型。') for i,x in enumerate(slides)),encoding='utf8')
print('deck_slides',len(slides),'bytes',len(out.encode()))
