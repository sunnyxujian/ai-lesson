const {chromium}=require('C:/Users/micro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),url=require('url');
(async()=>{
const project=path.resolve(__dirname,'..');
const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
const page=await browser.newPage({viewport:{width:1280,height:720}});
const errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.goto(url.pathToFileURL(path.join(project,'slides/index.html')).href);
await page.waitForTimeout(1800);
const count=await page.locator('.slide').count(),checks=[];
fs.mkdirSync(path.join(project,'verify/deck'),{recursive:true});
for(let i=0;i<count;i++){
await page.evaluate(n=>deck.showSlide(n),i);await page.waitForTimeout(600);
checks.push(await page.evaluate(()=>{const s=document.querySelector('.slide.active'),r=s.getBoundingClientRect();return{slide:deck.currentSlide+1,stageRatio:r.width/r.height,brokenImages:[...s.querySelectorAll('img')].filter(x=>!x.complete||x.naturalWidth===0).length,overflow:[...s.querySelectorAll('h1,li,figure,.content')].filter(x=>{const a=x.getBoundingClientRect();return a.right>r.right+1||a.bottom>r.bottom-25}).map(x=>x.tagName),footOverlap:s.querySelector('.content').getBoundingClientRect().bottom>s.querySelector('.foot').getBoundingClientRect().top}}));
await page.screenshot({path:path.join(project,`verify/deck/slide-${String(i+1).padStart(2,'0')}.png`)});
}
await page.setViewportSize({width:390,height:844});await page.evaluate(()=>deck.showSlide(0));await page.waitForTimeout(700);await page.screenshot({path:path.join(project,'verify/deck/phone.png')});
await page.locator('#showNotes').click();const noteText=await page.locator('#notesBody').innerText();
await page.locator('#notesClose').click();await page.keyboard.press('ArrowRight');const nav=await page.evaluate(()=>deck.currentSlide===1);
await page.keyboard.press('e');const edit=await page.locator('[data-edit]').first().getAttribute('contenteditable');
fs.writeFileSync(path.join(project,'verify/deck-check.json'),JSON.stringify({checks,errors,speakerNotesAvailable:noteText.length>50,keyboardNavigation:nav,editing:edit==='true',phoneViewport:{width:390,height:844}},null,2));
await browser.close();
console.log(JSON.stringify({slides:count,checks,errors}));
})();
