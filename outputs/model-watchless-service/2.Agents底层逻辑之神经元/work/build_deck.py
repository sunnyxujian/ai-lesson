from pathlib import Path
import json, html, re

ROOT = Path(__file__).resolve().parents[1]
BASE = Path('C:/Users/micro/.codex/skills/frontend-slides/viewport-base.css').read_text(encoding='utf-8')
DATA = ROOT / 'work/deck-content.json'
CSS = r'''
/* === THEME: NEURON LAB === */
:root{--stage-bg:#071718;--slide-bg:#eef3e9;--ink:#113337;--muted:#52716e;--accent:#007b6b;--line:#b6cfbd}
*{box-sizing:border-box}body{font-family:'Noto Sans SC',sans-serif;color:var(--ink)}
.slide{padding:90px 110px;background:radial-gradient(circle at 90% 10%,#dcebdc 0,transparent 40%),var(--slide-bg)}
.eyebrow{font-size:25px;letter-spacing:5px;text-transform:uppercase;color:var(--accent);margin:0 0 30px}
h1,h2{font-family:'Noto Serif SC',serif;font-weight:700;margin:0;line-height:1.45}h1{font-size:110px;max-width:1500px}h2{font-size:74px;max-width:1600px;padding-bottom:8px}
.intro{font-size:38px;line-height:1.6;max-width:1350px;color:var(--muted);margin:36px 0}
.content{display:grid;grid-template-columns:620px 1fr;gap:70px;margin-top:36px;align-items:start}
.content.no-image{grid-template-columns:1fr}.points{font-size:34px;line-height:1.6;padding:0;list-style:none;margin:0}
.points li{padding:20px 0 24px;border-top:2px solid var(--line)}
.figure{width:100%;height:590px;object-fit:contain;object-position:top center;border:1px solid var(--line);background:#fff}
.formula{font-family:'Noto Serif SC',serif;font-size:55px;line-height:1.5;padding:36px 42px;background:#113337;color:#e5f8d4;margin:45px 0 0;max-width:1500px}
.footer{position:absolute;bottom:60px;left:110px;right:110px;display:flex;justify-content:space-between;font-size:23px;color:var(--muted)}
.footer a{color:inherit;position:absolute;right:160px;bottom:0}.reveal{opacity:0;transform:translateY(22px);transition:opacity .5s,transform .5s}.visible .reveal{opacity:1;transform:none}.reveal:nth-child(2){transition-delay:.1s}.reveal:nth-child(3){transition-delay:.2s}
/* === CONTROLS AND NOTES === */
.deck-controls{display:flex;gap:10px;align-items:center;border-radius:8px;padding:7px 12px;background:#113337e8;color:white;font:14px sans-serif;width:max-content;max-width:calc(100vw - 20px);white-space:nowrap}
button{border:0;border-radius:5px;padding:8px 12px;background:#e5f8d4;color:#113337;cursor:pointer}
#notesPanel{position:fixed;right:16px;top:16px;bottom:80px;width:min(620px,90vw);padding:26px;background:#fffdf5;z-index:2000;overflow:auto;box-shadow:0 10px 50px #0007;font-size:17px;line-height:1.8;display:none}
#notesPanel.open{display:block}.speaker-notes{display:none}.edit-hotzone{position:fixed;top:0;left:0;width:80px;height:80px;z-index:10000}
.edit-toggle{position:fixed;top:16px;left:16px;opacity:0;pointer-events:none;z-index:10001}.edit-toggle.show,.edit-toggle.active{opacity:1;pointer-events:auto}
[contenteditable=true]{outline:2px dashed #007b6b;outline-offset:4px}
@media print{#notesPanel,.edit-hotzone,.edit-toggle{display:none!important}.reveal{opacity:1;transform:none}}
'''
JS = r'''
/* === SLIDE PRESENTATION CONTROLLER === */
class SlidePresentation{
 constructor(){this.slides=[...document.querySelectorAll('.slide')];this.currentSlide=0;this.stage=document.getElementById('deckStage');this.editing=false;this.scale();addEventListener('resize',()=>this.scale());this.setup();this.showSlide(0)}
 scale(){const f=Math.min(innerWidth/1920,innerHeight/1080);this.stage.style.transform=`translate(${(innerWidth-1920*f)/2}px,${(innerHeight-1080*f)/2}px) scale(${f})`}
 showSlide(n){this.currentSlide=Math.max(0,Math.min(n,this.slides.length-1));this.slides.forEach((s,i)=>{s.classList.toggle('active',i===this.currentSlide);s.classList.toggle('visible',i===this.currentSlide)});document.getElementById('count').textContent=`${this.currentSlide+1} / ${this.slides.length}`;document.getElementById('notesBody').innerHTML=this.slides[this.currentSlide].querySelector('.speaker-notes').innerHTML}
 toggleNotes(){document.getElementById('notesPanel').classList.toggle('open')}
 toggleEdit(){this.editing=!this.editing;document.querySelectorAll('[data-editable]').forEach(e=>e.contentEditable=this.editing);document.getElementById('editToggle').classList.toggle('active',this.editing)}
 save(){document.querySelectorAll('[contenteditable]').forEach(e=>e.removeAttribute('contenteditable'));this.editing=false;const u=URL.createObjectURL(new Blob(['<!doctype html>\n'+document.documentElement.outerHTML],{type:'text/html'}));const a=document.createElement('a');a.href=u;a.download='神经元-重点讲义.html';a.click();URL.revokeObjectURL(u)}
 setup(){addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key==='s'){e.preventDefault();this.save();return}if(e.target.isContentEditable)return;if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();this.showSlide(this.currentSlide+1)}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();this.showSlide(this.currentSlide-1)}if(e.key.toLowerCase()==='n')this.toggleNotes();if(e.key.toLowerCase()==='e')this.toggleEdit();if(e.key==='Home')this.showSlide(0);if(e.key==='End')this.showSlide(this.slides.length-1)});let t=0;addEventListener('wheel',e=>{if(this.editing||document.getElementById('notesPanel').contains(e.target))return;if(Date.now()-t>600&&Math.abs(e.deltaY)>15){this.showSlide(this.currentSlide+Math.sign(e.deltaY));t=Date.now()}},{passive:true});let x=0;addEventListener('touchstart',e=>x=e.changedTouches[0].clientX,{passive:true});addEventListener('touchend',e=>{let d=e.changedTouches[0].clientX-x;if(Math.abs(d)>50)this.showSlide(this.currentSlide+(d<0?1:-1))},{passive:true});document.querySelectorAll('[data-editable]').forEach((e,i)=>{let v=localStorage.getItem('neuron-slide-'+i);if(v)e.innerHTML=v;e.addEventListener('input',()=>localStorage.setItem('neuron-slide-'+i,e.innerHTML))});const h=document.querySelector('.edit-hotzone'),b=document.getElementById('editToggle');let hide;[h,b].forEach(e=>{e.addEventListener('mouseenter',()=>{clearTimeout(hide);b.classList.add('show')});e.addEventListener('mouseleave',()=>hide=setTimeout(()=>{if(!this.editing)b.classList.remove('show')},400))});h.onclick=b.onclick=()=>this.toggleEdit()}
}
window.deck=new SlidePresentation();
'''

def main():
    data=json.loads(DATA.read_text(encoding='utf-8'));sections=[]
    for i,s in enumerate(data['slides'],1):
        points=''.join('<li data-editable>'+html.escape(p)+'</li>' for p in s.get('points',[]))
        picture=('<img class="figure" src="'+html.escape(s['image'])+'" alt="'+html.escape(s.get('alt',s['title']))+'">') if s.get('image') else ''
        formula='<div class="formula reveal" data-editable>'+html.escape(s['formula'])+'</div>' if s.get('formula') else ''
        notes=''.join('<p>'+html.escape(p)+'</p>' for p in s['notes'])
        link=data['tutorial']+s.get('anchor','')
        sections.append(f'''<!-- === SLIDE {i}: {html.escape(s['title'])} === -->
<section class="slide"><p class="eyebrow reveal">NEURON LAB / {i:02}</p><h2 class="reveal" data-editable>{html.escape(s['title'])}</h2><div class="content {'no-image' if not picture else ''} reveal"><ul class="points">{points}</ul>{picture}</div>{formula}<div class="footer"><span>Agents 底层逻辑 · 神经元</span><a href="{html.escape(link)}" target="_blank">完整教程 ↗</a><span>{i:02} / {len(data['slides']):02}</span></div><aside class="speaker-notes"><h3>{html.escape(s['title'])}</h3>{notes}<p><a href="{html.escape(link)}" target="_blank">阅读完整教程</a></p></aside></section>''')
    result='''<!doctype html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>神经元 · Agents底层逻辑</title><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;600&family=Noto+Serif+SC:wght@600;700&display=swap" rel="stylesheet"><style>'''+BASE+CSS+'''</style></head><body><div class="deck-viewport"><main class="deck-stage" id="deckStage">'''+''.join(sections)+'''</main></div><nav class="deck-controls" aria-label="幻灯片导航"><button onclick="deck.showSlide(deck.currentSlide-1)">←</button><span id="count"></span><button onclick="deck.showSlide(deck.currentSlide+1)">→</button><button onclick="deck.toggleNotes()">讲者备注 N</button></nav><aside id="notesPanel"><button onclick="deck.toggleNotes()">关闭</button><div id="notesBody"></div></aside><div class="edit-hotzone"></div><button class="edit-toggle" id="editToggle" title="编辑 E">编辑</button><script>'''+JS+'''</script></body></html>'''
    dest=ROOT/'slides';dest.mkdir(exist_ok=True);(dest/'index.html').write_text(result,encoding='utf-8')

if __name__=='__main__':main()
