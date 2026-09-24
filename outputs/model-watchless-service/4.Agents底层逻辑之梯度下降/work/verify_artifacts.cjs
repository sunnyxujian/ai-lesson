const {chromium}=require('C:/Users/micro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const root=path.dirname(__dirname),title='4.Agents底层逻辑之梯度下降';
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true,args:['--allow-file-access-from-files']});
 const page=await browser.newPage({viewport:{width:1280,height:720}});
 await page.goto(pathToFileURL(path.join(root,'share',title+'-visual-explainer.html')).href,{waitUntil:'load'});
 const images=await page.locator('img').evaluateAll(a=>a.map(x=>({src:x.getAttribute('src'),ok:x.complete&&x.naturalWidth>0})));
 await page.pdf({path:path.join(root,'share',title+'-visual-explainer.pdf'),preferCSSPageSize:true,printBackground:true});
 if(process.argv.includes('--pdf-only')){await browser.close();console.log('PDF re-rendered');return;}
 await page.goto(pathToFileURL(path.join(root,'slides/index.html')).href,{waitUntil:'load'});
 await page.evaluate(()=>document.fonts.ready);
 const slides=await page.locator('.slide').count(),checks=[];
 const folder=path.join(root,'verify/deck-pages');fs.mkdirSync(folder,{recursive:true});
 for(let i=0;i<slides;i++){
  await page.evaluate(i=>window.deck.show(i),i);await page.waitForTimeout(500);
  checks.push(await page.evaluate(()=>{const s=document.querySelector('.slide.active'),stage=s.getBoundingClientRect();const copy=s.querySelector('.copy'),fig=s.querySelector('figure');const a=copy?.getBoundingClientRect(),b=fig?.getBoundingClientRect();return {number:window.deck.index+1,stageRatio:stage.width/stage.height,imageOK:[...s.querySelectorAll('img')].every(x=>x.complete&&x.naturalWidth),textOverflow:[...s.querySelectorAll('h1,h2,p,li,.copy')].filter(x=>x.scrollHeight>x.clientHeight+2).map(x=>x.tagName),panelOverlap:!!(a&&b&&a.right>b.left&&a.left<b.right&&a.bottom>b.top&&a.top<b.bottom),bottomOK:!a||a.bottom<stage.bottom};}));
  await page.screenshot({path:path.join(folder,`slide-${String(i+1).padStart(2,'0')}.png`)});
 }
 await page.keyboard.press('n');const notesWorks=await page.locator('#notes').evaluate(x=>x.classList.contains('open')&&x.textContent.length>100);await page.keyboard.press('Escape');
 await page.setViewportSize({width:390,height:844});await page.evaluate(()=>deck.show(9));await page.waitForTimeout(500);await page.screenshot({path:path.join(root,'verify/deck-phone.png')});
 const mobile=await page.locator('.deck-stage').evaluate(s=>{let r=s.getBoundingClientRect();return {width:r.width,height:r.height,ratio:r.width/r.height}});
 fs.writeFileSync(path.join(root,'verify/artifact-browser-checks.json'),JSON.stringify({htmlImages:images,slideCount:slides,slideChecks:checks,notesWorks,mobile},null,2));
 await browser.close();console.log(JSON.stringify({slides,images:images.length,notesWorks,mobile,issues:checks.filter(x=>x.panelOverlap||!x.bottomOK||!x.imageOK||x.textOverflow.length)}));
})();
