from pathlib import Path
import sys,shutil,re,base64,urllib.request,urllib.parse,json
sys.path.insert(0,str(Path(__file__).parent/'slide-style-tools'))
from bs4 import BeautifulSoup
ROOT=Path(r'C:\Users\micro\Desktop\ai-lesson')
BASE=ROOT/'outputs/video-notes'
reference=BeautifulSoup((BASE/'2.AI最底层的Raw-Model/share/重点演示稿.html').read_text(encoding='utf-8'),'html.parser')
common=reference.select_one('#cartesian-theme').string
fonts=reference.select_one('#cartesian-fonts').string
items=[('1. 认识AI','认识AI'),('3.认识模型服务接口','share'),('4.AI-本质','share')]
extra=r'''
/* === COURSE-SPECIFIC CODE, STEPS AND COMPARISON LAYOUTS === */
.steps>div{border-top:1px solid var(--line);background:rgba(255,255,255,.3);color:var(--text-primary)}
.steps>b,.pointlist b,.code em,.bigword,.large-number{color:var(--text-primary)}
.bigword,.large-number{font-family:'Playfair Display','Noto Serif SC',serif;font-weight:400}
.code{background:var(--bg-secondary);border-left:1px solid var(--line);color:var(--text-primary)}
.band{border-left:1px solid var(--text-primary);background:rgba(255,255,255,.3)}
.comparison p{font-size:47px}.comparison strong{font-size:33px}.comparison em{font-size:28px}
.split figure img{max-height:450px}
.slide.title .content{max-width:1350px}
'''
intro=r'''
/* === INTRODUCTORY COURSE: KEEP ITS IMAGE AND PROCESS LAYOUTS === */
body{font-family:'Inter','Lesson','Noto Sans SC',sans-serif}
.slide,.slide.light{--slide-bg:var(--bg-primary);--ink:var(--text-primary);--muted:var(--text-secondary);--line:#b8b0a4;color:var(--text-primary)}
h1,h2,.quote,.tile b{font-family:'Playfair Display','Cartesian CJK','Noto Serif SC',serif;font-weight:400}
.topbar{border:0;padding-top:0;color:var(--accent);font-size:24px}
.slide h2{font-weight:400;line-height:1.4;letter-spacing:0;font-size:76px;margin:45px 0 25px}
.lede{color:var(--text-secondary);font-size:31px;margin-bottom:28px}
.content{height:590px;margin-top:0;gap:65px}
.point{font-size:35px}.point span{color:var(--accent);font-family:'Inter',sans-serif}
.visual img{border-radius:0;border:1px solid var(--line);background:var(--bg-secondary);max-height:490px}
.caption{color:var(--text-secondary)}
.slide-footer{left:108px;right:108px;bottom:48px;color:var(--accent);font-size:21px}
.slide-footer a{color:var(--text-secondary)}
.title .topbar{margin-top:180px}
.title h1{font-size:118px;line-height:1.25;letter-spacing:0;margin:45px 0 35px;max-width:1290px;position:relative;z-index:1}
.title .lede{font-size:36px;line-height:1.7;max-width:1000px;position:relative;z-index:1}
.title .emblem{display:none}.title .ghost{color:var(--line);opacity:.24;font-weight:400;font-family:'Playfair Display',serif;font-size:125px;right:135px;bottom:95px}
.title .slide-footer{left:154px}
.quote{font-size:74px;font-weight:400}.quote em{color:var(--text-primary)}
.tile{border-top:1px solid var(--line)}.tile b{font-size:44px;font-weight:400}.tile p{color:var(--text-secondary)}
.node{border:1px solid var(--line);background:rgba(255,255,255,.3)}.arrow{color:var(--text-primary)}
#notes{border-radius:0}.edit-toggle{background:var(--text-primary);color:var(--bg-primary);border-radius:0}
.deck-controls button,.deck-controls a{border-radius:0}
'''
controller=r'''
/* === TOOLBAR VISIBILITY: H HIDE, O OPEN, HIDDEN ON EVERY LOAD === */
function setDeckControls(visible){
 const bar=document.querySelector('#deckControls');
 if(!visible&&bar.contains(document.activeElement))document.activeElement.blur();
 bar.hidden=!visible;
 const progress=document.querySelector('#progress');if(progress)progress.hidden=!visible;
}
setDeckControls(false);
document.querySelector('#hideControls').onclick=()=>setDeckControls(false);
document.addEventListener('keydown',event=>{
 if(event.ctrlKey||event.metaKey||event.altKey||event.target.isContentEditable||event.target.closest('input,textarea,select'))return;
 const key=event.key.toLowerCase();
 if(key==='h'||key==='o'){event.preventDefault();event.stopImmediatePropagation();setDeckControls(key==='o');}
},true);
'''
reports=[]
for course,sub in items:
 directory=BASE/course;work=directory/'work';work.mkdir(exist_ok=True)
 file=directory/sub/'重点演示稿.html';backup=work/'重点演示稿.before-cartesian.html'
 if not backup.exists():shutil.copy2(file,backup)
 raw=backup.read_text(encoding='utf-8');s=BeautifulSoup(raw,'html.parser')
 original=[x.get_text() for x in s.select('.slide')]
 images=[x['src'] for x in s.select('.slide img')]
 st=s.new_tag('style',id='cartesian-fonts');st.string=fonts;s.head.append(st)
 if course.startswith('1.'):
  fontfile=work/'cartesian-cjk.css'
  if not fontfile.exists():
   visible=BeautifulSoup(raw,'html.parser')
   for el in visible.select('.notes-text'):el.decompose()
   chars=sorted(set(re.findall(r'[\u3000-\u9fff]', ''.join(x.get_text() for x in visible.select('.slide')))))
   blocks=[]
   for start in range(0,len(chars),120):
    chunk=chars[start:start+120]
    url='https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400&text='+urllib.parse.quote(''.join(chunk))
    body=urllib.request.urlopen(url,timeout=30).read().decode()
    for asset in set(re.findall(r'url\((https://[^)]+)\)',body)):
     data=urllib.request.urlopen(asset,timeout=30).read();body=body.replace(asset,'data:font/woff2;base64,'+base64.b64encode(data).decode())
    body=body.replace("'Noto Serif SC'","'Cartesian CJK'")
    body=body.replace('}', 'unicode-range:'+','.join('U+'+format(ord(c),'X') for c in chunk)+';}')
    blocks.append(body)
   fontfile.write_text('\n'.join(blocks),encoding='utf-8')
  font=s.new_tag('style');font.string=fontfile.read_text(encoding='utf-8');s.head.append(font)
 st=s.new_tag('style',id='cartesian-theme');st.string=common+extra+(intro if course.startswith('1.') else '');s.head.append(st)
 for sl in s.select('.slide.title'):
  sl.insert(0,s.new_tag('div',attrs={'class':'geo-decoration','aria-hidden':'true'}))
 nav=s.select_one('.deck-controls');nav['hidden']='';nav['id']='deckControls';nav['aria-label']='演示操作栏：O 显示，H 隐藏'
 if s.select_one('#progress'):s.select_one('#progress')['hidden']=''
 hide=s.new_tag('button',id='hideControls',type='button',title='隐藏操作栏（H）；按 O 重新显示');hide.string='隐藏 H';nav.append(hide)
 for script in s.select('script'):
  js=script.string or ''
  for clone in ['copy','clone']:
   old=f"{clone}.querySelector('#notes').hidden=true;"
   if old in js:js=js.replace(old,old+f"{clone}.querySelector('#deckControls').hidden=true;const exportedProgress={clone}.querySelector('#progress');if(exportedProgress)exportedProgress.hidden=true;")
  script.string=js
 js=s.new_tag('script',id='toolbar-shortcuts');js.string=controller;s.body.append(js)
 assert original==[x.get_text() for x in s.select('.slide')]
 assert images==[x['src'] for x in s.select('.slide img')]
 file.write_text(str(s),encoding='utf-8')
 reports.append({'course':course,'file':str(file),'slides':len(original),'images':len(images),'content_preserved':True})
(ROOT/'work/cartesian-batch-manifest.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(reports,ensure_ascii=True))
