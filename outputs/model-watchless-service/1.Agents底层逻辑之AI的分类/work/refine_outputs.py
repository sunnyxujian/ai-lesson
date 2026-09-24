from pathlib import Path
import sys,json,subprocess,shutil,re
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
from video_notes_common import make_contact_sheet
p=Path(__file__).resolve().parents[1];share=p/'share';name='1.Agents底层逻辑之AI的分类-visual-explainer'
style='''<style id="local-print-refinement">
@page { size:A4; margin:17mm 17mm 18mm; }
@media print {
body { font-size:10.5pt;line-height:1.58;padding:0; }
p { font-size:10.5pt;line-height:1.58;orphans:3;widows:3;margin:.62em 0;break-inside:avoid; }
figure {break-inside:avoid;}
h1 { font-size:20pt;margin:.2em 0 .8em; }
h2 {font-size:15pt;margin:1.4em 0 .75em;break-before:auto;break-after:avoid;}
h2:first-of-type {break-before:auto;}
h3 {font-size:11pt;line-height:1.35;margin:.8em 0 .3em;break-after:avoid;}
img {max-height:80mm;object-fit:contain;box-shadow:none;margin:.6em auto;}
blockquote {font-size:9pt;margin:.4em 0 1em;color:#666;}
}
</style>'''
html=share/(name+'.html');text=html.read_text(encoding='utf-8');text=re.sub(r'<style id="local-print-refinement">.*?</style>','',text,flags=re.S);text=text.replace('</body>',style+'\n</body>');html.write_text(text,encoding='utf-8')
md=share/(name+'.md');mdtext=re.sub(r'<style id="local-print-refinement">.*?</style>','',md.read_text(encoding='utf-8'),flags=re.S);md.write_text(mdtext+'\n'+style,encoding='utf-8')
chrome='C:/Program Files/Google/Chrome/Application/chrome.exe';pdf=share/(name+'.pdf')
subprocess.run([chrome,'--headless=new','--disable-gpu','--allow-file-access-from-files',f'--print-to-pdf={pdf}',f'--user-data-dir={p/"work/chrome-refined-profile"}','--no-pdf-header-footer',html.as_uri()],check=True,capture_output=True)
out=p/'verify/pdf-pages-refined';out.mkdir(exist_ok=True)
assert out.resolve().is_relative_to(p.resolve())
for stale in out.glob('page-*.png'):stale.unlink()
subprocess.run(['pdftoppm','-png','-r','90',str(pdf),str(out/'page')],check=True,capture_output=True)
pages=sorted(out.glob('page-*.png'))
make_contact_sheet(pages,[f'page {i+1}' for i in range(len(pages))],p/'verify/pdf-pages-contact-sheet.jpg',columns=4,thumb_width=240)
for k in range(0,len(pages),6):make_contact_sheet(pages[k:k+6],[f'page {k+i+1}' for i in range(len(pages[k:k+6]))],p/f'verify/pdf-review-{k//6+1}.jpg',columns=2,thumb_width=500)
deck=sorted((p/'verify/deck').glob('slide-*.png'))
for k in range(0,len(deck),6):make_contact_sheet(deck[k:k+6],[f'slide {k+i+1}' for i in range(len(deck[k:k+6]))],p/f'verify/deck-review-{k//6+1}.jpg',columns=2,thumb_width=640)
(p/'verify/refined-pdf.json').write_text(json.dumps({'pdf_pages':len(pages),'rendered_pages':str(out),'reason':'Reduce orphaned continuation captions and excessive page breaks; all source text and images retained.'},ensure_ascii=False,indent=2),encoding='utf-8')
print('refined pdf pages',len(pages))
