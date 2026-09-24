from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).parent/'slide-style-tools'))
from playwright.sync_api import sync_playwright
out=Path(r'C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\style-previews')
results=[]
with sync_playwright() as p:
    browser=p.chromium.launch(channel='chrome',headless=True)
    page=browser.new_page(viewport={'width':1280,'height':720},device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda e: errors.append(str(e)))
    for slug in ['blue-professional','cobalt-grid','cartesian']:
        page.goto((out/f'{slug}.html').as_uri(),wait_until='networkidle',timeout=60000)
        page.screenshot(path=str(out/f'{slug}.png'))
        for width,height in [(1280,720),(390,844)]:
            page.set_viewport_size({'width':width,'height':height})
            page.wait_for_timeout(200)
            result=page.evaluate('''() => {const stage=document.querySelector('.deck-stage').getBoundingClientRect(); const title=document.querySelector('.slide h1').getBoundingClientRect(); const overflow=[...document.querySelectorAll('.slide h1,.subtitle,.subkicker,.meta,.label,.colf')].filter(e=>e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2).map(e=>e.className);return {ratio:stage.width/stage.height,titleInside:title.left>=stage.left&&title.right<=stage.right&&title.bottom<=stage.bottom,overflow,text:document.querySelector('.slide').innerText}}''')
            results.append({'style':slug,'viewport':[width,height],**result})
        page.screenshot(path=str(out/f'{slug}-phone.png'))
        page.set_viewport_size({'width':1280,'height':720})
    page.goto((out/'index.html').as_uri(),wait_until='load')
    page.screenshot(path=str(out/'comparison.png'),full_page=True)
    browser.close()
(out/'verification.json').write_text(json.dumps({'results':results,'errors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'results':results,'errors':errors},ensure_ascii=True))
