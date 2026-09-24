const fs=require('fs');const path=require('path');const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/micro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
const root=__dirname,out=path.resolve(root,'../../output/AI的分类');fs.mkdirSync(path.join(root,'renders'),{recursive:true});
const browser=await chromium.launch({headless:false,args:['--headless=new'],executablePath:'C:/Users/micro/.cache/puppeteer/chrome/win64-1095492/chrome-win/chrome.exe'});
const page=await browser.newPage({viewport:{width:1440,height:900},deviceScaleFactor:1});let errors=[];let external=[];
page.on('pageerror',e=>errors.push(String(e)));page.on('request',r=>{if(r.url().startsWith('http'))external.push(r.url())});
await page.goto(pathToFileURL(path.join(out,'演示稿.html')).href);await page.waitForFunction(()=>window.Reveal&&Reveal.isReady());await page.evaluate(()=>document.fonts.ready);
const count=await page.evaluate(()=>Reveal.getTotalSlides());let issues=[];
for(let i=0;i<count;i++){
 await page.evaluate(i=>{Reveal.slide(i);Reveal.configure({transition:'none'})},i);await page.waitForTimeout(70);
 const result=await page.evaluate(()=>{let s=Reveal.getCurrentSlide(),r=s.getBoundingClientRect();let bad=[...s.querySelectorAll('h2,.prose,figure,.source')].map(e=>({text:e.textContent.slice(0,70),rect:e.getBoundingClientRect()})).filter(o=>o.rect.bottom>r.bottom-15||o.rect.right>r.right+1);let imgs=[...s.querySelectorAll('img')].filter(i=>!i.complete||!i.naturalWidth);return {bad:bad.map(x=>x.text),images:imgs.length,scroll:s.scrollHeight,client:s.clientHeight};});
 if(result.bad.length||result.images)issues.push({slide:i+1,...result});
 await page.screenshot({path:path.join(root,'renders',String(i+1).padStart(3,'0')+'.png')});
}
await page.evaluate(()=>Reveal.slide(0));await page.keyboard.press('ArrowRight');await page.waitForTimeout(100);let right=await page.evaluate(()=>Reveal.getIndices().h);await page.keyboard.press('ArrowLeft');let left=await page.evaluate(()=>Reveal.getIndices().h);
await page.click('#jump');await page.selectOption('#chapterSelect','50');await page.keyboard.press('ArrowDown');let selectH=await page.evaluate(()=>Reveal.getIndices().h);await page.selectOption('#chapterSelect','50');await page.click('#go');await page.waitForTimeout(100);let jumped=await page.evaluate(()=>Reveal.getIndices().h);
await page.click('#fullscreen');await page.waitForTimeout(120);let full=await page.evaluate(()=>({active:!!document.fullscreenElement,tools:getComputedStyle(document.querySelector('#tools')).display}));await page.evaluate(()=>document.fullscreenElement?document.exitFullscreen():null);
await page.goto(pathToFileURL(path.join(out,'图文教程.html')).href);await page.evaluate(async()=>{document.querySelectorAll('img').forEach(i=>i.loading='eager');await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
let doc=await page.evaluate(()=>({units:document.querySelectorAll('.unit').length,images:[...document.images].map(i=>({ok:i.complete&&i.naturalWidth>0,src:i.getAttribute('src')})),overflow:document.documentElement.scrollWidth>innerWidth}));
await page.screenshot({path:path.join(root,'tutorial-desktop.png')});await page.locator('#u075').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(root,'tutorial-mid.png')});
await page.setViewportSize({width:390,height:844});await page.goto(pathToFileURL(path.join(out,'图文教程.html')).href);await page.screenshot({path:path.join(root,'tutorial-mobile.png')});let mobile=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth}));
const report={count,issues,errors,external,keyboard:{right,left,selectH,jumped},fullscreen:full,document:doc,mobile};fs.writeFileSync(path.join(root,'qa.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report));await browser.close();
})();
