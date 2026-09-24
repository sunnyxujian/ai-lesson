const {chromium}=require('C:/Users/micro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const root=path.resolve('outputs/video-notes/4.AI-本质'),share=path.join(root,'share'),out=path.join(root,'verify/deck-pages');fs.mkdirSync(out,{recursive:true});
(async()=>{
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage({viewport:{width:1280,height:720}});let errors=[];page.on('pageerror',e=>errors.push(String(e)));
await page.goto(pathToFileURL(path.join(share,'重点演示稿.html')).href);await page.evaluate(()=>document.fonts.ready);
const count=await page.locator('.slide').count();let checks=[];
for(let i=0;i<count;i++){
 await page.evaluate(n=>presentation.showSlide(n),i);await page.waitForTimeout(800);
 checks.push(await page.evaluate(()=>{const s=document.querySelector('.slide.active'),box=s.getBoundingClientRect(),footer=s.querySelector('.footer').getBoundingClientRect();return{title:s.querySelector('h2').innerText,overflow:[...s.querySelectorAll('h2,p,pre,li,.steps,.band,.flow,.comparison,figure,.large-number,.bigword')].filter(e=>!e.closest('.speaker-notes')).filter(e=>{let b=e.getBoundingClientRect();return b.left<box.left-1||b.right>box.right+1||b.bottom>footer.top-8||e.scrollWidth>e.clientWidth+2}).map(e=>e.tagName+': '+e.innerText?.slice(0,65)),brokenImages:[...s.querySelectorAll('img')].filter(i=>!i.complete||!i.naturalWidth).length}}));
 await page.screenshot({path:path.join(out,`slide-${String(i+1).padStart(2,'0')}.png`)});
}
await page.keyboard.press('Home');await page.keyboard.press('ArrowRight');const nav=await page.locator('#pageCount').innerText();await page.keyboard.press('n');const notes=await page.locator('#notes').isVisible();await page.keyboard.press('Escape');await page.keyboard.press('e');const edit=await page.locator('[data-edit]').first().getAttribute('contenteditable');await page.evaluate(()=>editor.active&&editor.toggle());
let mobile=[];for(const v of [{width:390,height:844},{width:844,height:390}]){await page.setViewportSize(v);await page.evaluate(()=>presentation.showSlide(1));await page.waitForTimeout(300);mobile.push(await page.locator('.deck-stage').evaluate(e=>{let b=e.getBoundingClientRect();return{width:b.width,height:b.height,ratio:b.width/b.height,left:b.left,top:b.top}}));await page.screenshot({path:path.join(out,`mobile-${v.width}.png`)});}
await page.setViewportSize({width:1440,height:1000});await page.goto(pathToFileURL(path.join(share,'完整教程.html')).href);await page.evaluate(()=>document.fonts.ready);
const tutorial=await page.evaluate(()=>({sections:document.querySelectorAll('article section').length,images:document.querySelectorAll('figure img').length,broken:[...document.querySelectorAll('figure img')].filter(i=>!i.complete||!i.naturalWidth).length,anchors:[...document.querySelectorAll('nav a')].every(a=>document.querySelector(a.hash))}));await page.screenshot({path:path.join(root,'verify/tutorial-top.png')});
await page.pdf({path:path.join(share,'4.AI 本质-visual-explainer.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});
fs.writeFileSync(path.join(root,'verify/browser-audit.json'),JSON.stringify({errors,slides:count,slideChecks:checks,navigation:nav,notesVisible:notes,editing:edit,mobile,tutorial},null,2));await browser.close();console.log(JSON.stringify({slides:count,overflow:checks.filter(x=>x.overflow.length),errors,tutorial}));
})().catch(e=>{console.error(e);process.exit(1)});
