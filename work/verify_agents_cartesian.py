from pathlib import Path
import sys,json,math
sys.path.insert(0,str(Path(__file__).parent/'slide-style-tools'))
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw
ROOT=Path(r'C:\Users\micro\Desktop\ai-lesson');items=json.loads((ROOT/'work/agents-cartesian-manifest.json').read_text(encoding='utf-8'));reports=[]
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True)
 for idx,item in enumerate(items):
  file=Path(item['file']);out=file.parent.parent/'verify/cartesian';out.mkdir(parents=True,exist_ok=True)
  page=browser.new_page(viewport={'width':1280,'height':720},reduced_motion='reduce')
  page.route('https://**/*',lambda r:r.abort());errors=[];issues=[];checks={};page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(file.as_uri(),wait_until='load');page.evaluate('document.fonts.ready')
  bar=page.locator('#deckControls');checks['default_hidden']=not bar.is_visible()
  page.keyboard.press('o');checks['O_shows']=bar.is_visible()
  page.keyboard.press('h');checks['H_hides']=not bar.is_visible()
  page.keyboard.press('Shift+O');checks['uppercase_O']=bar.is_visible()
  page.keyboard.press('Shift+H');checks['uppercase_H']=not bar.is_visible()
  page.keyboard.press('ArrowRight');checks['next_slide']=page.locator('.slide').nth(1).evaluate("e=>e.classList.contains('active')")
  panel='#notesPanel' if idx in [1,2] else '#notes'
  page.keyboard.press('n');checks['notes_open']=page.locator(panel).is_visible()
  page.keyboard.press('n');checks['notes_close']=not page.locator(panel).is_visible()
  method='show' if idx==3 else 'showSlide'
  for i in range(item['slides']):
   page.evaluate(f'deck.{method}({i})');page.wait_for_timeout(240)
   metrics=page.evaluate('''() => {const s=document.querySelector('.slide.active'),r=s.getBoundingClientRect(),foot=s.querySelector('.foot,.footer,.slide-foot,footer'),f=foot?.getBoundingClientRect(),limit=f?.top??r.bottom-20,bad=[];
   for(const e of s.querySelectorAll('h1,h2,li,p,.hero,.copy,.content,figure,.figure,.signal,.path,.flow,figcaption')){if(e.closest('.speaker-notes')||e.matches('.cover-note,.cover-foot'))continue;const b=e.getBoundingClientRect();if(!b.width||!b.height)continue;if(b.right>r.right+2||b.left<r.left-2||b.bottom>limit+2)bad.push({class:e.className,text:e.innerText?.slice(0,25),bounds:[b.left,b.top,b.right,b.bottom],limit});}
   const overlaps=[];for(const grid of s.querySelectorAll('.layout,.content.with-image,.content:has(>.figure)')){const a=[...grid.children];for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++){const x=a[i].getBoundingClientRect(),y=a[j].getBoundingClientRect();if(Math.min(x.right,y.right)-Math.max(x.left,y.left)>2&&Math.min(x.bottom,y.bottom)-Math.max(x.top,y.top)>2)overlaps.push(grid.className);}}
   const left=s.querySelector(':scope>.copy'),right=s.querySelector(':scope>figure');if(left&&right){const a=left.getBoundingClientRect(),b=right.getBoundingClientRect();if(a.right>b.left+2&&a.bottom>b.top)overlaps.push('copy / image');}
   return {bad,overlaps,brokenImages:[...s.querySelectorAll('img')].filter(e=>!e.complete||!e.naturalWidth).length,ratio:r.width/r.height};}''')
   if metrics['bad'] or metrics['overlaps'] or metrics['brokenImages']:issues.append({'slide':i+1,**metrics})
   page.screenshot(path=str(out/f'slide-{i+1:02d}.png'))
  page.keyboard.press('o')
  with page.expect_download() as d:page.keyboard.press('Control+s')
  saved=out/'saved-verification.html';d.value.save_as(saved);doc=BeautifulSoup(saved.read_text(encoding='utf-8'),'html.parser');checks['export_hidden']=doc.select_one('#deckControls').has_attr('hidden')
  page.reload();checks['reload_hidden']=not bar.is_visible();page.close()
  sheet=Image.new('RGB',(1280,math.ceil(item['slides']/3)*264),(226,219,209));draw=ImageDraw.Draw(sheet)
  for i in range(item['slides']):
   im=Image.open(out/f'slide-{i+1:02d}.png').resize((416,234));x=(i%3)*426;y=(i//3)*264;sheet.paste(im,(x+5,y+22));draw.text((x+8,y+4),str(i+1),fill=(26,26,26))
  sheet.save(out/'contact-sheet.jpg',quality=90)
  report={'course':item['course'],'slides':item['slides'],'checks':checks,'issues':issues,'errors':errors};reports.append(report)
  (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=True),flush=True)
 browser.close()
(ROOT/'work/agents-cartesian-verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
