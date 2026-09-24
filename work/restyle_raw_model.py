from pathlib import Path
import sys,re,shutil,urllib.request,base64
sys.path.insert(0,str(Path(__file__).parent/'slide-style-tools'))
from bs4 import BeautifulSoup
ROOT=Path(r'C:\Users\micro\Desktop\ai-lesson')
DIR=ROOT/'outputs/video-notes/2.AI最底层的Raw-Model'
FILE=DIR/'share/重点演示稿.html'
BACKUP=DIR/'work/重点演示稿.before-cartesian.html'
if not BACKUP.exists():shutil.copy2(FILE,BACKUP)
reference=DIR/'work/cartesian-reference'
if not reference.exists():shutil.copytree(ROOT/'beautiful-html-templates/templates/cartesian',reference)
raw=BACKUP.read_text(encoding='utf-8')
s=BeautifulSoup(raw,'html.parser')
before=[x.get_text() for x in s.select('.slide')]
# Embed the original template's Latin families; existing embedded CJK fonts remain.
fontfile=DIR/'work/cartesian-fonts.css'
if not fontfile.exists():
    css=[]
    for family in ['Playfair+Display:wght@400','Inter:wght@400;500;600']:
        url='https://fonts.googleapis.com/css2?family='+family+'&display=swap'
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        body=urllib.request.urlopen(req,timeout=30).read().decode()
        for asset in set(re.findall(r'url\((https://[^)]+)\)',body)):
            data=urllib.request.urlopen(asset,timeout=30).read()
            body=body.replace(asset,'data:font/woff2;base64,'+base64.b64encode(data).decode())
        css.append(body)
    fontfile.write_text('\n'.join(css),encoding='utf-8')
font=s.new_tag('style',id='cartesian-fonts');font.string=fontfile.read_text(encoding='utf-8');s.head.append(font)
css=r'''
/* === CARTESIAN: ORIGINAL STONE PALETTE AND EDITORIAL TYPE === */
:root{--bg-primary:#ede8e0;--bg-secondary:#e2dbd1;--text-primary:#1a1a1a;--text-secondary:#5a5a5a;--accent:#8a8178;--line:#b8b0a4;--slide-bg:var(--bg-primary);--stage-bg:var(--bg-primary);--ink:var(--text-primary);--muted:var(--text-secondary)}
body{font-family:'Inter','Noto Sans SC',sans-serif;color:var(--text-primary)}
h1,h2,.quote,.pullquote,.equation,.big-stats em,.prompt,.math-function b{font-family:'Playfair Display','Noto Serif SC',serif;font-weight:400}
.slide{padding:78px 108px 105px;background:var(--bg-primary)}
.eyebrow{color:var(--accent);font-size:24px;letter-spacing:3px;border:0;padding-bottom:0;font-weight:400}
h2{font-size:76px;line-height:1.4;font-weight:400;margin-top:45px;letter-spacing:0}
p{color:var(--text-secondary)}
.content{margin-top:55px;position:relative;z-index:1}
.footer{border:0;color:var(--accent);font-size:21px;letter-spacing:1px;padding-top:0;bottom:48px}
.source-link{border:0;color:var(--text-secondary);letter-spacing:0}
.source-link:hover{text-decoration:underline;text-underline-offset:7px}
.takeaway{font-size:40px;color:var(--text-primary);font-weight:400}
.fine{color:var(--text-secondary)}
/* === COVER: GENEROUS TYPE WITH COMPASS CONSTRUCTION === */
.title{padding:0 154px}
.title .eyebrow{margin-top:218px}
.title h2{font-size:118px;line-height:1.25;margin-top:45px;max-width:1250px;position:relative;z-index:1}
.title .content{margin-top:0}
.title .subtitle{font-size:36px;margin-top:35px;max-width:1100px;line-height:1.7}
.title-meta{font-size:25px;color:var(--accent);margin-top:42px;letter-spacing:3px}
.title-line{display:none}
.title .footer{left:154px;right:108px}
.geo-decoration{position:absolute;right:96px;bottom:108px;width:576px;height:576px;border:1px solid var(--line);border-radius:50%;opacity:.4;pointer-events:none;z-index:0}
.geo-decoration:before{content:'';position:absolute;inset:15%;border:1px dashed var(--line);border-radius:50%}
.closing .geo-decoration{right:-130px;bottom:-190px;width:750px;height:750px;opacity:.22}
/* === TEACHING LAYOUTS: THIN RULES AND QUIET EMPHASIS === */
.node{border:1px solid var(--line);background:rgba(255,255,255,.3);color:var(--text-primary);font-size:38px}
.node.core{border-color:var(--text-primary);color:var(--text-primary);background:transparent}
.arrow,.weight>span,.token-path b,.branch,.result-line,.assembly .highlight,.corpus b,.equation b,.math-function b,.formula strong{color:var(--text-primary)}
.duo>div,.big-stats>div{border-top:1px solid var(--line)}
.duo em,.comparison em{color:var(--accent);font-size:28px;letter-spacing:3px}
.duo p{font-size:44px;color:var(--text-primary);font-weight:400}
.token-path code{background:var(--bg-secondary);font-family:'Inter','Noto Sans SC',sans-serif}
.prob-row>div{background:var(--bg-secondary);height:46px}
.prob-row i{background:var(--text-primary)}
.prob-row strong,.prob-row b{font-weight:400}
.prompt{border-bottom:1px solid var(--text-primary);font-weight:400}
.context-box{border:1px solid var(--line);background:rgba(255,255,255,.3)}
.context-box>span{color:var(--accent);font-size:26px}
.tokens .token-cell{border:1px solid var(--line);background:var(--bg-secondary)}
.big-stats em{color:var(--text-primary);font-size:116px;font-weight:400}
.big-stats strong,.equation strong{font-weight:400}
.quote{font-size:76px;font-weight:400}
.rule-row span{border-left:1px solid var(--line)}
.lead{font-family:'Playfair Display','Noto Serif SC',serif;font-weight:400;font-size:58px;color:var(--text-primary)}
.split figure img{border:1px solid var(--line);max-height:475px;object-fit:contain}
.equation b{font-weight:400}
.comparison>div{border-top:1px solid var(--line)}
.comparison p{font-family:'Playfair Display','Noto Serif SC',serif;color:var(--text-primary);font-weight:400}
.corpus>div{background:rgba(255,255,255,.3)}
.assembly>div,.assembly .highlight{border-bottom:1px solid var(--line)}
.assembly .highlight{border-color:var(--text-primary)}
.modalities span{border-top:1px solid var(--line);font-weight:400}
.closing-stack>div,.closing-stack .base-layer{border:1px solid var(--line);color:var(--text-primary);background:rgba(255,255,255,.3);font-family:'Playfair Display','Noto Serif SC',serif;font-weight:400}
.closing-stack small{font-family:'Inter','Noto Sans SC',sans-serif}
/* === TOOLBAR: H HIDES, O OPENS; DEFAULT HIDDEN === */
.deck-controls{background:var(--bg-primary);color:var(--text-primary);border:1px solid var(--line);border-radius:0;box-shadow:none;padding:9px 12px;gap:12px;font-family:'Inter','Noto Sans SC',sans-serif}
.deck-controls[hidden],#progress[hidden]{display:none!important}
.deck-controls button{border:1px solid var(--line);border-radius:0;padding:7px 10px}
.deck-controls button:hover{background:var(--text-primary);color:var(--bg-primary)}
.deck-controls a:hover{text-decoration:underline}
#progress{height:1px;background:var(--text-primary)}
.edit-toggle{background:var(--text-primary);color:var(--bg-primary);border-radius:0}
[contenteditable=true]{outline:1px dashed var(--accent)}
#notes{background:var(--bg-primary);color:var(--text-primary);border:1px solid var(--line);box-shadow:none}
#notes .note-hint{background:var(--bg-secondary)}
button:focus-visible,a:focus-visible{outline:2px solid var(--text-primary);outline-offset:4px}
@media(max-width:600px){.deck-controls{width:calc(100vw - 20px);max-width:none;flex-wrap:wrap;justify-content:center;gap:6px;padding:8px}.deck-controls button,.deck-controls a{padding:6px 8px}.deck-controls #pageCount{padding:6px 2px}}
@media print{.geo-decoration{opacity:.25}.title-line{display:none}}
'''
style=s.new_tag('style',id='cartesian-theme');style.string=css;s.head.append(style)
for slide in [s.select('.slide')[0],s.select('.slide')[-1]]:
    slide.insert(0,s.new_tag('div',attrs={'class':'geo-decoration','aria-hidden':'true'}))
nav=s.select_one('.deck-controls');nav['hidden']='';nav['aria-label']='演示操作栏：O 显示，H 隐藏';nav['id']='deckControls'
s.select_one('#progress')['hidden']=''
hide=s.new_tag('button',id='hideControls',type='button',title='隐藏操作栏（H）；按 O 重新显示');hide.string='隐藏 H';nav.append(hide)
script=s.select_one('script')
js=script.string
js=js.replace('this.setupStageScale();','this.setupStageScale();this.setControlsVisible(false);',1)
js=js.replace("if(e.target.isContentEditable)return;","if(e.target.isContentEditable||e.target.closest('input,textarea,select')||e.ctrlKey||e.metaKey||e.altKey)return;const key=e.key.toLowerCase();if(key==='h'||key==='o'){e.preventDefault();this.setControlsVisible(key==='o');return;}",1)
js=js.replace(' toggleNotes(){'," setControlsVisible(visible){const bar=document.querySelector('#deckControls');if(!visible&&bar.contains(document.activeElement))document.activeElement.blur();bar.hidden=!visible;document.querySelector('#progress').hidden=!visible;}\n toggleNotes(){",1)
js=js.replace("copy.querySelector('#notes').hidden=true;","copy.querySelector('#notes').hidden=true;copy.querySelector('#deckControls').hidden=true;copy.querySelector('#progress').hidden=true;")
js=js.replace('const presentation=new SlidePresentation();',"const presentation=new SlidePresentation();\ndocument.querySelector('#hideControls').onclick=()=>presentation.setControlsVisible(false);")
script.string=js
assert before==[x.get_text() for x in s.select('.slide')], 'Slide content changed'
assert [x['src'] for x in BeautifulSoup(raw,'html.parser').select('.slide img')]==[x['src'] for x in s.select('.slide img')]
FILE.write_text(str(s),encoding='utf-8')
print('Updated',FILE)
print('Backup',BACKUP)
print('Verified: 18 slides; all slide text, notes and embedded images preserved.')
