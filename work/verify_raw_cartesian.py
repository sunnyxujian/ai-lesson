from pathlib import Path
import sys,json,re
sys.path.insert(0,str(Path(__file__).parent/'slide-style-tools'))
from playwright.sync_api import sync_playwright
from PIL import Image,ImageOps,ImageDraw
root=Path(r'C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model')
file=root/'share/重点演示稿.html'
out=root/'verify/cartesian';out.mkdir(exist_ok=True)
issues=[];checks={};errors=[]
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True)
 page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 page.on('pageerror',lambda e:errors.append(str(e)))
 # Verify fully offline: all required fonts and figures should already be embedded.
 page.route('https://**/*',lambda route:route.abort())
 page.goto(file.as_uri(),wait_until='load')
 page.evaluate('document.fonts.ready');page.wait_for_timeout(800)
 bar=page.locator('#deckControls');progress=page.locator('#progress')
 checks['default_hidden']=not bar.is_visible() and not progress.is_visible()
 page.keyboard.press('o');checks['O_shows']=bar.is_visible() and progress.is_visible()
 page.keyboard.press('h');checks['H_hides']=not bar.is_visible() and not progress.is_visible()
 page.keyboard.press('Shift+O');checks['uppercase_O']=bar.is_visible()
 page.keyboard.press('Shift+H');checks['uppercase_H']=not bar.is_visible()
 page.evaluate("document.querySelector('h2').contentEditable='true';document.querySelector('h2').focus()")
 page.keyboard.press('o');checks['editing_ignores_O']=not bar.is_visible()
 page.evaluate("document.querySelector('h2').contentEditable='false';document.querySelector('h2').blur()")
 # Reload in a new browser context after the editing test to avoid persisted edits.
 page.close()
 page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
 page.route('https://**/*',lambda route:route.abort())
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(file.as_uri(),wait_until='load');page.evaluate('document.fonts.ready')
 page.keyboard.press('ArrowRight');checks['next_slide']=page.locator('.slide.active').get_attribute('aria-label')=='第2页'
 page.keyboard.press('n');checks['notes_open']=page.locator('#notes').is_visible()
 page.keyboard.press('Escape');checks['notes_close']=not page.locator('#notes').is_visible()
 for i in range(18):
  page.evaluate(f'presentation.showSlide({i})');page.wait_for_timeout(800)
  metrics=page.evaluate('''() => {const s=document.querySelector('.slide.active'),r=s.getBoundingClientRect(),f=s.querySelector('.footer').getBoundingClientRect(),c=s.querySelector('.content').getBoundingClientRect();const bad=[];for(const e of s.querySelectorAll('h2,.content *')){if(e.closest('.speaker-notes')||e.classList.contains('title-line'))continue;const b=e.getBoundingClientRect();if(!b.width||!b.height)continue;if(b.right>r.right+1||b.left<r.left-1||b.bottom>f.top+1)bad.push({class:e.className,text:e.innerText?.slice(0,25),bounds:[b.left,b.top,b.right,b.bottom],footer:f.top});}return {bad,brokenImages:[...s.querySelectorAll('img')].filter(e=>!e.complete||!e.naturalWidth).length,ratio:r.width/r.height};}''')
  if metrics['bad'] or metrics['brokenImages']:issues.append({'slide':i+1,**metrics})
  page.screenshot(path=str(out/f'slide-{i+1:02d}.png'))
 page.keyboard.press('o')
 with page.expect_download() as download:
  page.locator('#save').click()
 downloaded=out/'saved-verification.html';download.value.save_as(downloaded)
 from bs4 import BeautifulSoup
 saved=BeautifulSoup(downloaded.read_text(encoding='utf-8'),'html.parser')
 checks['export_default_hidden']=saved.select_one('#deckControls').has_attr('hidden') and saved.select_one('#progress').has_attr('hidden')
 page.set_viewport_size({'width':390,'height':844});page.evaluate('presentation.showSlide(0)');page.keyboard.press('h');page.wait_for_timeout(800)
 page.screenshot(path=str(out/'phone-cover.png'))
 checks['phone_ratio']=page.evaluate("(()=>{const r=document.querySelector('.deck-stage').getBoundingClientRect();return Math.abs(r.width/r.height-16/9)<.001})()")
 page.keyboard.press('o');checks['phone_O_shows']=page.locator('#deckControls').is_visible()
 page.screenshot(path=str(out/'phone-controls.png'))
 page.reload();checks['reload_hides']=not page.locator('#deckControls').is_visible()
 browser.close()
sheet=Image.new('RGB',(1280,6*204),(226,219,209));draw=ImageDraw.Draw(sheet)
for i in range(18):
 im=Image.open(out/f'slide-{i+1:02d}.png').resize((416,234))
 # 3 columns, 6 rows; keep the exact 16:9 thumbnail ratio.
 if i==0:sheet=Image.new('RGB',(1280,6*264),(226,219,209));draw=ImageDraw.Draw(sheet)
 x=(i%3)*426;y=(i//3)*264
 sheet.paste(im,(x+5,y+22));draw.text((x+8,y+4),str(i+1),fill=(26,26,26))
sheet.save(out/'contact-sheet.jpg',quality=90)
report={'checks':checks,'issues':issues,'errors':errors}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
