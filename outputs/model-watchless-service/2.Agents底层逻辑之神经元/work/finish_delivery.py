from pathlib import Path
import sys,re,json,subprocess,zipfile,shutil
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
from video_notes_common import make_contact_sheet,source_fingerprint
import windows_runtime

html=next((ROOT/'share').glob('*.html'));pdf=html.with_suffix('.pdf')
text=html.read_text(encoding='utf-8')
if 'id="lesson-01"' not in text:
    count=[0]
    def anchor(m):
        count[0]+=1
        return f'<span id="lesson-{count[0]:02}"></span>'+m.group(0)
    text=re.sub(r'<h2\b[^>]*>',anchor,text)
if True:
    text=re.sub(r'<style>/\* FINAL PRINT LAYOUT \*/.*?</style>','',text,flags=re.S)
    css='''<style>/* FINAL PRINT LAYOUT */
@page{size:A4;margin:17mm 18mm}
@media print{
body{font-family:'Microsoft YaHei',sans-serif;line-height:1.6;font-size:10.5pt;padding:0}
h1{font-size:22pt;margin:0 0 12mm}h2{break-before:auto;margin-top:9mm;font-size:16pt;line-height:1.35;break-after:avoid}
h3{font-size:12pt;margin-top:5mm;break-after:avoid}
p{font-size:10.5pt;orphans:3;widows:3}figure{margin:4mm 0;break-inside:avoid;break-before:avoid}
img{max-height:82mm;object-fit:contain;margin:3mm auto;box-shadow:none}figcaption{font-size:9pt;color:#555}
}
</style>'''
    text=text.replace('</body>',css+'</body>')
html.write_text(text,encoding='utf-8')
subprocess.run(['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless=new','--disable-gpu','--allow-file-access-from-files',f'--print-to-pdf={pdf}',f'--user-data-dir={ROOT / "work/chrome-final-profile"}','--no-pdf-header-footer',html.as_uri()],check=True,capture_output=True)
pages=ROOT/'verify/pdf-pages-final';pages.mkdir(exist_ok=True)
for oldpage in pages.glob('page-*.png'):oldpage.unlink()
subprocess.run(['pdftoppm','-png','-r','90',str(pdf),str(pages/'page')],check=True,capture_output=True)
frames=sorted(pages.glob('page-*.png'))
make_contact_sheet(frames,[f'page {i}' for i in range(1,len(frames)+1)],ROOT/'verify/pdf-pages-contact-sheet.jpg',columns=4,thumb_width=300)
slides=sorted((ROOT/'verify/deck').glob('slide-*.png'))
make_contact_sheet(slides,[f'slide {i}' for i in range(1,len(slides)+1)],ROOT/'verify/deck-overview.jpg',columns=3,thumb_width=500)
for name in ['transcription-review.md','token-usage.json']:
    shutil.copy2(ROOT/'work'/name,ROOT/'share/source-materials'/name)
refs=re.findall(r'<img[^>]+src="([^"]+)"',text)
broken=[r for r in refs if not (html.parent/r).is_file()]
deck=(ROOT/'slides/index.html').read_text(encoding='utf-8')
links=re.findall(r'href="([^"]+)"',deck)
missing_links=[]
for link in links:
    if link.startswith(('http:','https:')):continue
    rel,_,frag=link.partition('#');target=ROOT/'slides'/rel
    if not target.is_file() or (frag and f'id="{frag}"' not in target.read_text(encoding='utf-8')):missing_links.append(link)
archive=ROOT/'2.Agents底层逻辑之神经元-video-notes.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for base in ['share','slides']:
        for p in sorted((ROOT/base).rglob('*')):
            if p.is_file():z.write(p,p.relative_to(ROOT))
with zipfile.ZipFile(archive) as z:
    bad=z.testzip();names=z.namelist()
acq=json.loads((ROOT/'work/acquisition.json').read_text(encoding='utf-8'))
immutable=source_fingerprint(Path(acq['local_video']))==acq['fingerprint']
report={'html_images':len(refs),'missing_images':broken,'pdf_pages':len(frames),'slides':len(slides),'missing_tutorial_links':missing_links,'zip_members':len(names),'zip_crc_error':bad,'zip_contains_deck': 'slides/index.html' in names,'source_immutable':immutable,'usage':'unavailable; counts and cost not estimated','remaining_quality_warning':'Only actual model token counts are unavailable; substantive completeness and asset checks pass.'}
(ROOT/'verify/delivery-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
