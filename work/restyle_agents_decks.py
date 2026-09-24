from pathlib import Path
import sys,re,json,shutil,urllib.request,urllib.parse,base64
sys.path.insert(0,str(Path(__file__).parent/'slide-style-tools'))
from bs4 import BeautifulSoup
ROOT=Path(r'C:\Users\micro\Desktop\ai-lesson');BASE=ROOT/'outputs/model-watchless-service'
files=sorted(BASE.glob('*/slides/index.html'))
ref=BeautifulSoup((ROOT/'outputs/video-notes/2.AI最底层的Raw-Model/share/重点演示稿.html').read_text(encoding='utf-8'),'html.parser')
fontfile=ROOT/'work/agents-cartesian-fonts.css'
if not fontfile.exists():
 chars=set()
 for f in files:
  s=BeautifulSoup(f.read_text(encoding='utf-8'),'html.parser')
  for a in s.select('.speaker-notes'):a.decompose()
  chars.update(re.findall(r'[\u3000-\u9fff]',''.join(x.get_text() for x in s.select('.slide'))))
 chars=sorted(chars);blocks=[ref.select_one('#cartesian-fonts').string]
 for family,label in [('Noto+Serif+SC','Cartesian Serif SC'),('Noto+Sans+SC','Cartesian Sans SC')]:
  for start in range(0,len(chars),150):
   chunk=chars[start:start+150]
   url='https://fonts.googleapis.com/css2?family='+family+':wght@400&text='+urllib.parse.quote(''.join(chunk))
   css=urllib.request.urlopen(url,timeout=30).read().decode()
   for asset in set(re.findall(r'url\((https://[^)]+)\)',css)):
    data=urllib.request.urlopen(asset,timeout=30).read();css=css.replace(asset,'data:font/woff2;base64,'+base64.b64encode(data).decode())
   css=css.replace(f"'{family.replace('+',' ')}'",f"'{label}'")
   css=css.replace('}','unicode-range:'+','.join('U+'+format(ord(c),'X') for c in chunk)+';}')
   blocks.append(css)
 fontfile.write_text('\n'.join(blocks),encoding='utf-8')
common=r'''
/* === CARTESIAN: STONE, INK, REGULAR SERIFS AND HAIRLINE RULES === */
:root{--bg-primary:#ede8e0;--bg-secondary:#e2dbd1;--text-primary:#1a1a1a;--text-secondary:#5a5a5a;--accent:#8a8178;--line:#b8b0a4;--slide-bg:var(--bg-primary);--stage-bg:var(--bg-primary);--ink:var(--text-primary);--muted:var(--text-secondary)}
body{font-family:'Inter','Cartesian Sans SC','Noto Sans SC',sans-serif;color:var(--text-primary)}
.slide{background:var(--bg-primary);background-image:none}
.slide:before,.slide:after,.stripe{display:none}
.slide h1,.slide h2{font-family:'Playfair Display','Cartesian Serif SC','Noto Serif SC',serif;font-weight:400;letter-spacing:0}
.eyebrow,.kicker,.folio{color:var(--accent);font-weight:400}
li,p{color:var(--text-secondary)}
figure img,.figure,.evidence img{border:1px solid var(--line);box-shadow:none;border-radius:0;background:rgba(255,255,255,.3)}
figure,figcaption,.evidence figcaption{color:var(--text-secondary)}
.foot,.footer,.slide-foot,footer{color:var(--accent);border:0;font-weight:400}
.foot a,.footer a,footer a,.source-link,.tutorial{color:var(--text-secondary)}
footer strong{color:var(--accent);font-weight:400}
.geo-decoration{position:absolute;right:96px;bottom:108px;width:576px;height:576px;border:1px solid var(--line);border-radius:50%;opacity:.4;pointer-events:none;z-index:0}
.geo-decoration:before{content:'';position:absolute;inset:15%;border:1px dashed var(--line);border-radius:50%}
.cover h1,.cover p,.cover .kicker,.cover .eyebrow{position:relative;z-index:1}
/* === CONSISTENT CONTROLS: DEFAULT HIDDEN, H HIDE, O OPEN === */
.deck-controls{background:var(--bg-primary);color:var(--text-primary);border:1px solid var(--line);border-radius:0;box-shadow:none;padding:9px 12px;gap:10px;font:13px 'Inter','Cartesian Sans SC',sans-serif;bottom:12px;align-items:center;width:max-content;max-width:calc(100vw - 20px)}
.deck-controls[hidden]{display:none!important}
button{background:transparent;color:var(--text-primary);border:1px solid var(--line);border-radius:0;font:inherit}
.deck-controls button{padding:7px 10px}.deck-controls button:hover{background:var(--text-primary);color:var(--bg-primary)}
.edit-toggle{background:var(--text-primary);color:var(--bg-primary);border-radius:0}
#notes,#notesPanel,.notes-panel{background:var(--bg-primary);color:var(--text-primary);border:1px solid var(--line);box-shadow:none;border-radius:0}
.notes-panel a{color:var(--text-secondary)}
[contenteditable=true]{outline:1px dashed var(--accent)}
'''
variants=[r'''
.folio{border:0;padding-bottom:0;font-size:24px}.eyebrow{margin-top:50px;font-size:25px}.slide h1{font-size:78px;line-height:1.35;margin:22px 0 44px}
li{border-left:1px solid var(--line);font-size:43px}.with-image li{font-size:36px}
figure{background:rgba(255,255,255,.3);border:1px solid var(--line);padding:12px}figure img{border:0}
.foot{border:0;padding-top:0;font-size:22px;bottom:48px}
''',r'''
.slide h2{font-size:70px;line-height:1.4}.points li{border-top:1px solid var(--line)}
.figure{height:550px;object-position:center}.formula{font-family:'Playfair Display','Cartesian Serif SC',serif;background:var(--bg-secondary);color:var(--text-primary);border:1px solid var(--line);font-weight:400}
.footer{font-size:22px;bottom:48px}
''',r'''
.slide h2{font-size:70px;line-height:1.4;margin:35px 0 40px}.copy{padding-top:18px}
.hero{font-family:'Playfair Display','Cartesian Serif SC',serif;font-weight:400;color:var(--text-primary);font-size:58px}.hero.formula{font-size:46px}
.copy li{border-left:1px solid var(--line)}figure{border-top:1px solid var(--line)}figure img{background:rgba(255,255,255,.3)}
.slide-foot{color:var(--accent);font-size:21px;bottom:48px}
.cover{padding:0 154px}.cover .kicker{margin-top:218px;letter-spacing:3px}.cover h1{font-size:118px;line-height:1.25;letter-spacing:0;margin:45px 0 35px}.cover .lead{font-size:46px;line-height:1.6;font-weight:400}
.signal{right:175px;top:490px;gap:18px}.signal span{border:1px solid var(--line);font-size:28px;padding:16px 30px;color:var(--text-secondary)}.signal i{color:var(--accent);font-size:40px}
.cover-note{font-size:24px;bottom:92px}
''',r'''
.eyebrow{border:0;padding-top:0;font-size:24px}.slide h2{font-size:62px;font-weight:400;line-height:1.4}
p.thesis{font-size:34px;color:var(--text-primary);font-weight:400}figure img{border:1px solid var(--line);box-shadow:none}
figcaption{color:var(--text-secondary);font-size:23px}.big-number{color:var(--accent);font-family:'Playfair Display',serif;font-weight:400}
.cover{padding:0 154px}.cover .eyebrow{margin-top:218px}.cover h1{font-size:118px;line-height:1.25;margin:45px 0 35px}.cover-sub{font-size:36px}.path{font-size:40px;margin-top:60px;position:relative;z-index:1}.path span{border-bottom:1px solid var(--line)}.path b{color:var(--accent)}.cover-foot{font-size:24px;margin-top:54px}
''',r'''
.kicker{color:var(--accent);font-size:24px}.slide h1{font-size:70px;line-height:1.35;font-weight:400;letter-spacing:0;margin-bottom:48px}
.copy{top:215px}.evidence img{box-shadow:none;border:1px solid var(--line)}.evidence figcaption{color:var(--text-secondary)}
.flow b{font-family:'Playfair Display','Cartesian Serif SC',serif;font-weight:400;border:1px solid var(--line);background:rgba(255,255,255,.3)}.flow span{color:var(--accent)}
footer{border:0;padding-top:0;bottom:48px;font-size:22px}
''']
controller=r'''
/* === TOOLBAR VISIBILITY: H HIDE, O OPEN === */
function setDeckControls(visible){const bar=document.getElementById('deckControls');if(!visible&&bar.contains(document.activeElement))document.activeElement.blur();bar.hidden=!visible;}
setDeckControls(false);
document.getElementById('hideControls').onclick=()=>setDeckControls(false);
document.addEventListener('keydown',e=>{if(e.ctrlKey||e.metaKey||e.altKey||e.target.isContentEditable||e.target.closest('input,textarea,select'))return;const k=e.key.toLowerCase();if(k==='h'||k==='o'){e.preventDefault();e.stopImmediatePropagation();setDeckControls(k==='o');}},true);
'''
manifest=[]
for idx,f in enumerate(files):
 directory=f.parent.parent;work=directory/'work';work.mkdir(exist_ok=True);backup=work/'slides-index.before-cartesian.html'
 if not backup.exists():shutil.copy2(f,backup)
 raw=backup.read_text(encoding='utf-8');s=BeautifulSoup(raw,'html.parser');original=[x.get_text() for x in s.select('.slide')];images=[x['src'] for x in s.select('.slide img')]
 for id,css in [('cartesian-fonts',fontfile.read_text(encoding='utf-8')),('cartesian-theme',common+variants[idx])]:
  tag=s.new_tag('style',id=id);tag.string=css;s.head.append(tag)
 for sl in s.select('.slide.cover'):sl.insert(0,s.new_tag('div',attrs={'class':'geo-decoration','aria-hidden':'true'}))
 bar=s.select_one('.deck-controls');bar['id']='deckControls';bar['hidden']='';bar['aria-label']='演示操作栏：O 显示，H 隐藏'
 hide=s.new_tag('button',id='hideControls',type='button');hide.string='隐藏 H';bar.append(hide)
 for tag in s.select('script'):
  js=tag.string or ''
  # All exports reset toolbar visibility on disk without changing the live presentation.
  for name in ['copy','doc']:
   old=f'{name}=document.documentElement.cloneNode(true);'
   if old in js:js=js.replace(old,old+f"{name}.querySelector('#deckControls').hidden=true;{name}.querySelectorAll('#notes,#notesPanel').forEach(p=>{{p.classList.remove('open');if(p.hasAttribute('hidden'))p.hidden=true;}});")
  if idx==1:
   js=js.replace("const u=URL.createObjectURL(new Blob(['<!doctype html>\\n'+document.documentElement.outerHTML]", "const copy=document.documentElement.cloneNode(true);copy.querySelector('#deckControls').hidden=true;copy.querySelector('#notesPanel').classList.remove('open');const u=URL.createObjectURL(new Blob(['<!doctype html>\\n'+copy.outerHTML]")
  if idx==4:js=js.replace('(innerHeight-48)','innerHeight').replace('(innerHeight-48-1080*f)','(innerHeight-1080*f)')
  tag.string=js
 tag=s.new_tag('script',id='toolbar-shortcuts');tag.string=controller;s.body.append(tag)
 assert original==[x.get_text() for x in s.select('.slide')]
 assert images==[x['src'] for x in s.select('.slide img')]
 f.write_text(str(s),encoding='utf-8')
 manifest.append({'course':directory.name,'file':str(f),'slides':len(original),'images':len(images),'content_preserved':True})
(ROOT/'work/agents-cartesian-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(manifest,ensure_ascii=True))
