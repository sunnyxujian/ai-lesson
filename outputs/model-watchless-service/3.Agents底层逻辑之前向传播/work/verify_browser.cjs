const fs=require('fs'),path=require('path');
const {chromium}=require('C:/Users/micro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..');
const {pathToFileURL}=require('url');
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',args:['--allow-file-access-from-files']});
 const page=await browser.newPage({viewport:{width:1280,height:900}});
 const report={};
 const file=fs.readdirSync(path.join(root,'share')).find(n=>n.endsWith('visual-explainer.html'));
 await page.goto(pathToFileURL(path.join(root,'share',file)).href);await page.waitForLoadState('networkidle');
 report.tutorial=await page.evaluate(()=>({images:[...document.images].length,broken:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),headings:document.querySelectorAll('h2').length,anchors:[...document.querySelectorAll('h2')].map(h=>h.id),text:document.body.innerText.length}));
 await page.pdf({path:path.join(root,'share',file.replace('.html','.pdf')),format:'A4',printBackground:true,preferCSSPageSize:true});
 if(fs.existsSync(path.join(root,'slides','index.html'))){
  report.deck=[];
  for(const size of [{width:1280,height:720},{width:390,height:844}]){
   await page.setViewportSize(size);await page.goto(pathToFileURL(path.join(root,'slides','index.html')).href);await page.waitForTimeout(900);
   const count=await page.locator('.slide').count();
   for(let i=0;i<count;i++){
    await page.evaluate(i=>deck.showSlide(i),i);await page.waitForTimeout(550);
    const errors=await page.evaluate(()=>{let s=document.querySelector('.slide.active'),r=s.getBoundingClientRect();let elems=[...s.querySelectorAll('h1,h2,.hero,li,figure,.source-link,.lead,.cover-note')];return {stageRatio:r.width/r.height,visibleSlides:document.querySelectorAll('.slide.active').length,brokenImages:[...s.querySelectorAll('img')].filter(x=>!x.complete||!x.naturalWidth).length,outside:elems.filter(e=>{let t=e.getBoundingClientRect();return t.right>r.right+2||t.bottom>r.bottom+2||t.left<r.left-2||t.top<r.top-2}).map(e=>e.className||e.tagName),overflow:elems.filter(e=>e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+3).map(e=>e.className||e.tagName)}});
    report.deck.push({viewport:size,slide:i+1,...errors});
    await page.screenshot({path:path.join(root,'verify',`deck-${size.width}-${String(i+1).padStart(2,'0')}.png`)});
   }
  }
  await page.keyboard.press('n');report.notesVisible=await page.locator('#notesPanel').evaluate(e=>e.classList.contains('open'));
  await page.keyboard.press('n');await page.keyboard.press('e');report.editable=await page.locator('[contenteditable="true"]').count();await page.keyboard.press('e');
 }
 fs.writeFileSync(path.join(root,'verify','browser-verification.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify(report.tutorial));console.log('Deck screenshots',report.deck?.length,'notes',report.notesVisible,'editable',report.editable);await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
