from pathlib import Path
import json, html, re, base64

project = Path(__file__).resolve().parents[1]
manifest = json.loads((project/'work/scene-manifest.json').read_text(encoding='utf-8'))
slides = json.loads((project/'work/deck-content.json').read_text(encoding='utf-8'))
base = Path('C:/Users/micro/.codex/skills/frontend-slides/viewport-base.css').read_text(encoding='utf-8')
title = manifest['source']['title']
tutorial = '../share/'+title+'-visual-explainer.html'
sections=[]
for i,s in enumerate(slides):
    notes=[]
    for sid in s['scenes']:
        text=(project/f'work/codex-notes/scene_{sid:03d}.md').read_text(encoding='utf-8')
        body=text.split('## Light-plus',1)[1].split('## Visual explainer',1)[0].strip()
        notes.append('<p>'+html.escape(body).replace('\n\n','</p><p>')+'</p>')
    figure=''
    if s.get('image'):
        frame=Path(manifest['scenes'][s['image']-1]['frame_path'])
        data=base64.b64encode(frame.read_bytes()).decode()
        figure=f'<figure><img src="data:image/png;base64,{data}" alt="原课程中的思维导图画面"></figure>'
    points=''.join('<li data-edit>'+html.escape(v)+'</li>' for v in s['points'])
    sections.append(f'''<!-- === SLIDE {i+1}: {s['title']} === -->
    <section class="slide {'active visible' if i==0 else ''}" aria-label="{html.escape(s['title'])}">
      <div class="folio">AGENTS / 底层逻辑 <span>{i+1:02d} / {len(slides):02d}</span></div>
      <div class="eyebrow" data-edit>{html.escape(s['kicker'])}</div>
      <h1 data-edit>{html.escape(s['title'])}</h1>
      <div class="content {'with-image' if figure else ''}"><ul class="reveal">{points}</ul>{figure}</div>
      <div class="foot">AI 的分类 <a href="{tutorial}" target="_blank">阅读完整教程 ↗</a></div>
      <aside class="speaker-notes"><h2>{html.escape(s['title'])} · 讲者备注</h2>{''.join(notes)}<p><a href="{tutorial}" target="_blank">完整教程与全部例子 ↗</a></p></aside>
    </section>''')
css='''
/* === THEME: PAPER & INK, COPPER ANNOTATIONS === */
:root{--stage-bg:#242521;--slide-bg:#f3f0e8;--ink:#252f2b;--accent:#a34b2c}
*{box-sizing:border-box}body{font-family:'Noto Sans SC',sans-serif;color:var(--ink)}
.slide{padding:70px 110px;background:linear-gradient(110deg,#f7f5ef,#eae7dd)}
.slide:after{content:'';position:absolute;right:72px;top:148px;width:8px;height:740px;background:var(--accent)}
.folio{font-size:25px;letter-spacing:5px;border-bottom:2px solid #b9bcb0;padding-bottom:25px}.folio span{float:right;letter-spacing:2px}
.eyebrow{font-size:28px;letter-spacing:4px;color:var(--accent);margin-top:60px}
h1{font-family:'Noto Serif SC',serif;font-weight:700;font-size:84px;line-height:1.3;margin:22px 0 48px;max-width:1650px}
.content{display:grid;grid-template-columns:1fr;gap:55px;align-items:start}.content.with-image{grid-template-columns:650px 1fr}
ul{list-style:none;margin:0;padding:0;max-width:1480px}li{font-size:46px;line-height:1.65;margin-bottom:29px;padding-left:33px;border-left:5px solid #bdc8b6}
.with-image li{font-size:38px}figure{margin:0;background:white;border:1px solid #c4c7bc;padding:12px}figure img{display:block;object-fit:contain;width:100%;height:490px}
.foot{position:absolute;bottom:65px;left:110px;right:110px;border-top:2px solid #b9bcb0;padding-top:22px;font-size:24px;color:#59655a}.foot a{float:right;color:var(--accent)}
/* === REVEALS === */
.reveal{opacity:0;transform:translateY(25px);transition:opacity .5s,transform .5s}.visible .reveal{opacity:1;transform:none}
/* === CONTROLS AND SPEAKER NOTES === */
.deck-controls{display:flex;gap:8px;background:#202820d9;padding:8px;border-radius:9px;color:white;font:14px sans-serif;width:max-content;max-width:calc(100vw - 16px)}
button{cursor:pointer;background:#f2efe6;border:0;padding:9px 14px;border-radius:4px;color:#263026;white-space:nowrap;flex-shrink:0}#counter{padding:9px;white-space:nowrap}
.speaker-notes{display:none}#notes{position:fixed;right:0;top:0;bottom:0;width:min(640px,95vw);background:#faf8f0;padding:35px;overflow:auto;z-index:2000;box-shadow:0 0 40px #0005;font-size:17px;line-height:1.9}#notes[hidden]{display:none}#notesClose{float:right}
.edit-hotzone{position:fixed;top:0;left:0;width:80px;height:80px;z-index:10000}.edit-toggle{position:fixed;top:15px;left:15px;opacity:0;pointer-events:none;z-index:10001}.edit-toggle.show,.edit-toggle.active{opacity:1;pointer-events:auto}
[contenteditable=true]{outline:2px dashed #a34b2c}
'''
js='''
/* === FIXED STAGE AND NAVIGATION === */
class SlidePresentation{
 constructor(){this.slides=[...document.querySelectorAll('.slide')];this.currentSlide=0;this.stage=document.querySelector('.deck-stage');this.scale();window.addEventListener('resize',()=>this.scale());this.showSlide(0);this.events();}
 scale(){const s=Math.min(innerWidth/1920,innerHeight/1080);this.stage.style.transform=`translate(${(innerWidth-1920*s)/2}px, ${(innerHeight-1080*s)/2}px) scale(${s})`;}
 showSlide(n){this.currentSlide=Math.max(0,Math.min(n,this.slides.length-1));this.slides.forEach((s,i)=>{s.classList.toggle('active',i===this.currentSlide);s.classList.toggle('visible',i===this.currentSlide)});document.querySelector('#counter').textContent=`${this.currentSlide+1} / ${this.slides.length}`;if(!notes.hidden)this.showNotes();}
 showNotes(){notesBody.innerHTML=this.slides[this.currentSlide].querySelector('.speaker-notes').innerHTML;notes.hidden=false;}
 events(){document.querySelector('#prev').onclick=()=>this.showSlide(this.currentSlide-1);document.querySelector('#next').onclick=()=>this.showSlide(this.currentSlide+1);document.querySelector('#showNotes').onclick=()=>{notes.hidden?this.showNotes():notes.hidden=true};document.querySelector('#notesClose').onclick=()=>notes.hidden=true;document.addEventListener('keydown',e=>{if(e.target.isContentEditable)return;if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();this.showSlide(this.currentSlide+1)}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();this.showSlide(this.currentSlide-1)}if(e.key==='n'||e.key==='N')notes.hidden?this.showNotes():notes.hidden=true;if(e.key==='Escape')notes.hidden=true;});let x=0;document.addEventListener('touchstart',e=>x=e.touches[0].clientX,{passive:true});document.addEventListener('touchend',e=>{if(!notes.hidden)return;let d=e.changedTouches[0].clientX-x;if(Math.abs(d)>50)this.showSlide(this.currentSlide+(d<0?1:-1));});let last=0;document.addEventListener('wheel',e=>{if(!notes.hidden||Date.now()-last<600)return;last=Date.now();this.showSlide(this.currentSlide+(e.deltaY>0?1:-1))},{passive:true});}
}
const deck=new SlidePresentation();
/* === INLINE EDITING, LOCAL SAVE, FILE EXPORT === */
let editing=false;const editButton=document.querySelector('#editToggle'),editable=[...document.querySelectorAll('[data-edit]')],storageKey='watchless-ai-classification-deck';
try{const saved=JSON.parse(localStorage.getItem(storageKey)||'null');if(saved)saved.forEach((v,i)=>{if(editable[i])editable[i].innerHTML=v})}catch{}
function toggleEdit(){editing=!editing;editable.forEach(x=>x.contentEditable=editing?'true':'false');editButton.classList.toggle('active',editing);editButton.textContent=editing?'结束编辑 (E)':'编辑 (E)'}
editButton.onclick=toggleEdit;let timer;const zone=document.querySelector('.edit-hotzone');for(const el of [zone,editButton]){el.onmouseenter=()=>{clearTimeout(timer);editButton.classList.add('show')};el.onmouseleave=()=>timer=setTimeout(()=>{if(!editing)editButton.classList.remove('show')},400)}zone.onclick=toggleEdit;
document.addEventListener('input',()=>{try{localStorage.setItem(storageKey,JSON.stringify(editable.map(x=>x.innerHTML)))}catch{}});
document.addEventListener('keydown',e=>{if((e.key==='e'||e.key==='E')&&!e.target.isContentEditable)toggleEdit();if((e.ctrlKey||e.metaKey)&&e.key==='s'){e.preventDefault();const copy=document.documentElement.cloneNode(true);copy.querySelectorAll('[contenteditable]').forEach(x=>x.removeAttribute('contenteditable'));const a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['<!doctype html>'+copy.outerHTML],{type:'text/html'}));a.download='AI的分类-重点讲稿.html';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),5000);}});
'''
out=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>AI 的分类 · 重点讲稿</title><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;600&family=Noto+Serif+SC:wght@600;700&display=swap" rel="stylesheet"><style>{base}\n{css}</style></head><body><div class="deck-viewport"><main class="deck-stage">{''.join(sections)}</main></div><nav class="deck-controls"><button id="prev" aria-label="上一页">←</button><span id="counter"></span><button id="next" aria-label="下一页">→</button><button id="showNotes">讲者备注 (N)</button></nav><div id="notes" hidden><button id="notesClose">关闭 ×</button><div id="notesBody"></div></div><div class="edit-hotzone"></div><button class="edit-toggle" id="editToggle">编辑 (E)</button><script>{js}</script></body></html>'''
(project/'slides').mkdir(exist_ok=True)
(project/'slides/index.html').write_text(out,encoding='utf-8')
print(f'deck: {len(slides)} slides')
