const {chromium}=require('C:/Users/micro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('url');
const path=require('path');
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});const page=await browser.newPage({viewport:{width:1280,height:720}});for(const key of ['a','b','c']){const file=path.resolve('.frontend-slides/slide-previews/style-'+key+'.html');await page.goto(pathToFileURL(file).href,{waitUntil:'domcontentloaded'});await page.waitForTimeout(1300);await page.screenshot({path:file.replace('.html','.png'),timeout:10000});}await browser.close()})().catch(e=>{console.error(e);process.exit(1)});
