from pathlib import Path
import sys,json,math
sys.path.insert(0,str(Path(__file__).parent/'slide-style-tools'))
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw
ROOT=Path(r'C:\Users\micro\Desktop\ai-lesson')
manifest=json.loads((ROOT/'work/cartesian-batch-manifest.json').read_text(encoding='utf-8'))
all_reports=[]
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True)
 for item in manifest:
  file=Path(item['file']);course=file.parent.parent;out=course/'verify/cartesian';out.mkdir(parents=True,exist_ok=True)
  errors=[];issues=[];checks={}
  page=browser.new_page(viewport={'width':1280,'height':720},reduced_motion='reduce')
  page.route('https://**/*',lambda route:route.abort())
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(file.as_uri(),wait_until='load');page.evaluate('document.fonts.ready')
  bar=page.locator('#deckControls');checks['default_hidden']=not bar.is_visible()
  page.keyboard.press('o');checks['O_show']=bar.is_visible()
  page.keyboard.press('h');checks['H_hide']=not bar.is_visible()
  page.keyboard.press('Shift+O');checks['uppercase_O']=bar.is_visible()
  page.keyboard.press('Shift+H');checks['uppercase_H']=not bar.is_visible()
  page.keyboard.press('ArrowRight');checks['next_slide']=page.locator('.slide').nth(1).evaluate("e=>e.classList.contains('active')")
  page.keyboard.press('n');checks['notes_open']=page.locator('#notes').is_visible()
  page.keyboard.press('n');checks['notes_close']=not page.locator('#notes').is_visible()
  ctrl='deck' if item['course'].startswith('1.') else 'presentation'
  for i in range(item['slides']):
   page.evaluate(f'{ctrl}.showSlide({i})');page.wait_for_timeout(240)
   metrics=page.evaluate('''() => {const s=document.querySelector('.slide.active'),r=s.getBoundingClientRect(),f=s.querySelector('.footer,.slide-footer').getBoundingClientRect(),bad=[];for(const e of s.querySelectorAll('h1,h2,.content *,.lede')){if(e.closest('.speaker-notes,.notes-text')||e.classList.contains('title-line')||e.classList.contains('geo-decoration'))continue;const b=e.getBoundingClientRect();if(!b.width||!b.height)continue;if(b.right>r.right+2||b.left<r.left-2||b.bottom>f.top+2)bad.push({class:e.className,text:e.innerText?.slice(0,30),bottom:b.bottom,footer:f.top});}const overlaps=[];for(const grid of s.querySelectorAll('.split,.steps,.grid,.comparison,.chain')){const a=[...grid.children];for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++){const x=a[i].getBoundingClientRect(),y=a[j].getBoundingClientRect();if(Math.min(x.right,y.right)-Math.max(x.left,y.left)>2&&Math.min(x.bottom,y.bottom)-Math.max(x.top,y.top)>2)overlaps.push(grid.className);}}return {bad,overlaps,brokenImages:[...s.querySelectorAll('img')].filter(e=>!e.complete||!e.naturalWidth).length,ratio:r.width/r.height};}''')
   if metrics['bad'] or metrics['overlaps'] or metrics['brokenImages']:issues.append({'slide':i+1,**metrics})
   page.screenshot(path=str(out/f'slide-{i+1:02d}.png'))
  page.keyboard.press('o')
  with page.expect_download() as dl:
   page.locator('#deckControls button',has_text='保存').click()
  saved=out/'saved-verification.html';dl.value.save_as(saved)
  doc=BeautifulSoup(saved.read_text(encoding='utf-8'),'html.parser')
  checks['export_hidden']=doc.select_one('#deckControls').has_attr('hidden')
  page.set_viewport_size({'width':390,'height':844});page.evaluate(f'{ctrl}.showSlide(0)');page.wait_for_timeout(250)
  checks['phone_toolbar_fits']=page.evaluate("[...document.querySelectorAll('#deckControls > *')].every(e=>{let r=e.getBoundingClientRect();return r.left>=0&&r.right<=innerWidth})")
  page.screenshot(path=str(out/'phone-controls.png'))
  page.keyboard.press('h');page.screenshot(path=str(out/'phone-cover.png'))
  checks['phone_ratio']=page.evaluate("(()=>{let r=document.querySelector('.deck-stage').getBoundingClientRect();return Math.abs(r.width/r.height-16/9)<.001})()")
  page.reload();checks['reload_hidden']=not bar.is_visible()
  page.close()
  sheet=Image.new('RGB',(1280,math.ceil(item['slides']/3)*264),(226,219,209));draw=ImageDraw.Draw(sheet)
  for i in range(item['slides']):
   im=Image.open(out/f'slide-{i+1:02d}.png').resize((416,234));x=(i%3)*426;y=(i//3)*264
   sheet.paste(im,(x+5,y+22));draw.text((x+8,y+4),str(i+1),fill=(26,26,26))
  sheet.save(out/'contact-sheet.jpg',quality=90)
  report={'course':item['course'],'slides':item['slides'],'checks':checks,'issues':issues,'errors':errors}
  (out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
  all_reports.append(report);print(json.dumps(report,ensure_ascii=True),flush=True)
 browser.close()
(ROOT/'work/cartesian-batch-verification.json').write_text(json.dumps(all_reports,ensure_ascii=False,indent=2),encoding='utf-8')
