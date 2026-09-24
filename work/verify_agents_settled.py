from pathlib import Path
import sys,json,math
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'work/slide-style-tools'))
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw
items=json.loads((ROOT/'work/agents-cartesian-manifest.json').read_text(encoding='utf-8'))
reports=json.loads((ROOT/'work/agents-cartesian-verification.json').read_text(encoding='utf-8'))
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome',headless=True)
 page=browser.new_page(viewport={'width':1280,'height':720},reduced_motion='reduce')
 page.route('https://**/*',lambda r:r.abort())
 file=Path(items[2]['file'])
 page.goto(file.as_uri(),wait_until='load')
 page.keyboard.press('n');page.wait_for_timeout(550)
 opened=page.locator('#notesPanel').is_visible()
 page.keyboard.press('n');page.wait_for_timeout(550)
 closed=not page.locator('#notesPanel').is_visible()
 assert opened and closed, 'Notes panel failed'
 reports[2]['checks'].update(notes_open=opened,notes_close=closed)
 (file.parent.parent/'verify/cartesian/report.json').write_text(json.dumps(reports[2],ensure_ascii=False,indent=2),encoding='utf-8')
 file=Path(items[1]['file']);out=file.parent.parent/'verify/cartesian'
 page.goto(file.as_uri(),wait_until='load');page.evaluate('document.fonts.ready')
 for i in range(items[1]['slides']):
  page.evaluate(f'deck.showSlide({i})');page.wait_for_timeout(650)
  page.screenshot(path=str(out/f'slide-{i+1:02d}.png'))
 sheet=Image.new('RGB',(1280,math.ceil(items[1]['slides']/3)*264),(226,219,209));draw=ImageDraw.Draw(sheet)
 for i in range(items[1]['slides']):
  im=Image.open(out/f'slide-{i+1:02d}.png').resize((416,234));x=(i%3)*426;y=(i//3)*264
  sheet.paste(im,(x+5,y+22));draw.text((x+8,y+4),str(i+1),fill=(26,26,26))
 sheet.save(out/'contact-sheet.jpg',quality=90)
 browser.close()
(ROOT/'work/agents-cartesian-verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(all(r['checks'].values()) and not r['issues'] and not r['errors'] for r in reports)
print('PASS: 5 decks / 79 slides; notes settled; screenshots refreshed.')
