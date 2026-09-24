const fs=require('fs');
const path=require('path');
const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/micro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..');
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
 const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(pathToFileURL(path.join(root,'slides/index.html')).href);await page.evaluate(()=>document.fonts.ready);await page.waitForTimeout(600);
 const count=await page.locator('.slide').count(),checks=[];
 const dir=path.join(root,'verify/deck');fs.mkdirSync(dir,{recursive:true});
 for(let i=0;i<count;i++){
  await page.evaluate(i=>deck.showSlide(i),i);await page.waitForTimeout(600);
  checks.push(await page.evaluate(()=>{const s=document.querySelector('.slide.active');return {slide:deck.currentSlide+1,stage:{w:s.offsetWidth,h:s.offsetHeight},broken:[...s.querySelectorAll('img')].filter(x=>!x.complete||!x.naturalWidth).length,overflow:[...s.querySelectorAll('h2,.points,.figure')].filter(e=>e.scrollHeight>e.clientHeight+2||e.scrollWidth>e.clientWidth+2).map(e=>e.className||e.tagName),contentEnd:s.querySelector('.content').getBoundingClientRect().bottom,footerTop:s.querySelector('.footer').getBoundingClientRect().top}}));
  await page.screenshot({path:path.join(dir,`slide-${String(i+1).padStart(2,'0')}.png`)});
 }
 await page.keyboard.press('Home');await page.keyboard.press('ArrowRight');const nav=await page.evaluate(()=>deck.currentSlide===1);await page.keyboard.press('n');const notes=await page.locator('#notesPanel').evaluate(e=>e.classList.contains('open'));await page.keyboard.press('n');await page.keyboard.press('e');const edit=await page.locator('[data-editable]').first().getAttribute('contenteditable');await page.keyboard.press('e');
 await page.setViewportSize({width:390,height:844});await page.evaluate(()=>deck.showSlide(0));await page.waitForTimeout(600);await page.screenshot({path:path.join(dir,'phone.png')});
 const mobile=await page.evaluate(()=>{const r=document.querySelector('.deck-stage').getBoundingClientRect();return{width:r.width,height:r.height,ratio:r.width/r.height,left:r.left,top:r.top}});
 fs.writeFileSync(path.join(root,'verify/deck-checks.json'),JSON.stringify({count,errors,checks,nav,notes,edit,mobile},null,2));await browser.close();
})();
