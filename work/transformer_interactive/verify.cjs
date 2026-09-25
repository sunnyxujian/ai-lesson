const {chromium}=require('C:/Users/micro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path'),assert=require('assert'),crypto=require('crypto');
const root=path.resolve(__dirname,'../..'),out=path.join(root,'outputs/Transformer'),report=path.join(root,'work/transformer/verify/interactive');
fs.mkdirSync(report,{recursive:true});
const url=p=>'file:///'+p.replace(/\\/g,'/');
const near=(a,b,eps=1e-8)=>assert(Math.abs(a-b)<eps,`${a} != ${b}`);
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1100},reducedMotion:'reduce'}),results=[];
 const files=fs.readdirSync(out).filter(n=>/^\d\d-.*交互演示\.html$/.test(n)).sort();assert.equal(files.length,12);
 for(const file of files){
  const errors=[],requests=[];const error=e=>errors.push(e.message),request=r=>{if(/^https?:/.test(r.url()))requests.push(r.url())};page.on('pageerror',error);page.on('request',request);
  await page.goto(url(path.join(out,file)));await page.waitForFunction(()=>window.lab);
  assert.equal(await page.evaluate(()=>lab.playing),false);
  const count=await page.evaluate(()=>lab.count);
  for(let i=0;i<count;i++){await page.evaluate(n=>lab.go(n),i);assert(await page.locator('#visual').innerText());assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,file+' desktop overflow');}
  await page.getByRole('button',{name:'↺ 重置',exact:true}).click();assert.equal(await page.evaluate(()=>lab.step),0);
  await page.getByRole('button',{name:'下一步',exact:true}).click();assert.equal(await page.evaluate(()=>lab.step),1);
  await page.getByRole('button',{name:'上一步',exact:true}).click();assert.equal(await page.evaluate(()=>lab.step),0);
  // Every parameter must accept an interaction and leave a valid render.
  const ids=await page.locator('[data-param]').evaluateAll(els=>els.map(x=>x.id));
  for(const id of ids){const el=page.locator('#'+id);const tag=await el.evaluate(x=>x.tagName),type=await el.getAttribute('type');
   if(tag==='SELECT'){const vals=await el.locator('option').evaluateAll(xs=>xs.map(x=>x.value));await el.selectOption(vals.at(-1));}
   else if(type==='checkbox')await el.click();
   else await el.evaluate(x=>{x.value=x.max;x.dispatchEvent(new Event('input',{bubbles:true}))});
   assert(await page.locator('#explanation').innerText());
  }
  await page.evaluate(()=>lab.reset());
  const audit=await page.evaluate(()=>lab.audit);
  if(file.startsWith('02')){const a=await page.evaluate(()=>{lab.go(6);return lab.audit});near(a.terms.reduce((x,y)=>x+y,0),a.out[0]);}
  if(file.startsWith('03')){assert.deepEqual(audit.raw[1],[8,11,4]);for(const r of audit.weights)near(r.reduce((a,b)=>a+b,0),1);near(audit.weights[1][1],.83717517,1e-7);for(let c=0;c<3;c++)near(audit.out[1][c],audit.parts.reduce((s,r)=>s+r[c],0));}
  if(file.startsWith('04')||file.startsWith('10')){for(const h of audit.heads)for(const r of h.weights)near(r.reduce((s,x)=>s+x,0),1);assert.equal(audit.concat[0].length,4);assert.equal(audit.out[0].length,3);}
  if(file.startsWith('05')){near(audit.z.reduce((a,b)=>a+b,0),0);assert(audit.z.some(v=>v<0));}
  if(file.startsWith('09')){for(let i=0;i<audit.weights.length;i++){near(audit.weights[i].reduce((a,b)=>a+b,0),1);for(let j=i+1;j<audit.weights.length;j++)near(audit.weights[i][j],0);}}
  if(file.startsWith('11'))for(const r of audit.prob)near(r.reduce((a,b)=>a+b,0),1);
  await page.locator('#speed').selectOption('800');await page.getByRole('button',{name:'播放',exact:true}).click();await page.waitForTimeout(900);assert.equal(await page.evaluate(()=>lab.step),1);await page.getByRole('button',{name:'暂停',exact:true}).click();assert.equal(await page.evaluate(()=>lab.playing),false);
  await page.evaluate(()=>lab.go(Math.min(3,lab.count-1)));await page.screenshot({path:path.join(report,file.slice(0,2)+'-desktop.png'),fullPage:true});
  await page.setViewportSize({width:390,height:844});
  for(let i=0;i<count;i++){await page.evaluate(n=>lab.go(n),i);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,file+' mobile overflow at '+i);}
  await page.screenshot({path:path.join(report,file.slice(0,2)+'-mobile.png'),fullPage:true});
  await page.setViewportSize({width:1440,height:1100});
  assert.deepEqual(errors,[],file);assert.deepEqual(requests,[],file+' network requests');
  page.off('pageerror',error);page.off('request',request);results.push({file,steps:count,controls:ids.length,errors,network:requests.length});
 }
 await page.goto(url(path.join(out,'Transformer-交互演示目录.html')));assert.equal(await page.locator('.catalog-card').count(),12);await page.screenshot({path:path.join(report,'catalog.png'),fullPage:true});
 const broken=await page.locator('a').evaluateAll(as=>as.map(a=>a.getAttribute('href')).filter(h=>h&&!h.startsWith('http')));for(const h of broken)assert(fs.existsSync(path.join(out,decodeURIComponent(h.split('#')[0]))));
 await page.goto(url(path.join(out,'Transformer-图文文章.html')));assert.equal(await page.locator('section#u02').count(),0);assert.equal(await page.locator('article section').count(),55);assert.equal(await page.locator('.interactive-entry').count(),12);
 const links=await page.locator('.interactive-entry a').evaluateAll(as=>as.map(a=>a.getAttribute('href')));for(const h of links)assert(fs.existsSync(path.join(out,h)));
 assert(await page.locator('#u03 .chapter-label').innerText().then(x=>x.includes('02')));
 assert(await page.locator('nav a').evaluateAll(as=>as.every(a=>document.querySelector(a.hash))));
 const deckHash=crypto.createHash('sha256').update(fs.readFileSync(path.join(out,'Transformer-演示文稿.html'))).digest('hex');assert(!fs.readFileSync(path.join(out,'Transformer-演示文稿.html'),'utf8').includes('data-unit="u57"'));
 // Copy outside output folder: embedded scripts/styles must still work without sibling resources.
 const portable=path.join(report,'portable-attention.html');fs.copyFileSync(path.join(out,files[2]),portable);await page.goto(url(portable));await page.evaluate(()=>lab.go(7));assert.equal(await page.evaluate(()=>lab.audit.out.length),3);
 fs.writeFileSync(path.join(report,'audit.json'),JSON.stringify({results,articleEntries:12,articleSections:55,deckHash,standaloneCopy:true},null,2));
 console.log(JSON.stringify({pages:results.length,steps:results.reduce((s,x)=>s+x.steps,0),allPassed:true,report}));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
