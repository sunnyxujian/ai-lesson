from pathlib import Path
import sys,json,re,shutil,subprocess,zipfile,html
P=Path(__file__).resolve().parent.parent
sys.path.insert(0,r'C:\Users\micro\.codex\skills\watchless\scripts')
from video_notes_common import make_contact_sheet
import windows_runtime
S=P/'share'
ht=next(S.glob('*visual-explainer.html'))
txt=ht.read_text(encoding='utf8')
txt=re.sub(r'<style id="reading-refinements">.*?</style>','',txt,flags=re.S)
txt=re.sub(r'<div class="intro">.*?</div>','',txt,flags=re.S)
style='''<style id="reading-refinements">
body{font-family:'Microsoft YaHei',sans-serif;background:#faf9f4;color:#173338;max-width:1040px;padding:48px 54px;font-size:16px}h1,h2,h3{font-family:'Microsoft YaHei',sans-serif}h2{border-color:#087e82}figure{margin:18px 0}figcaption{font-size:12px;color:#647777;text-align:center}h3{font-size:16px}p{line-height:1.8}a{color:#087e82}.intro{padding:28px;background:#e9f1ed;border-left:5px solid #087e82}.intro ol{line-height:2}.intro h2{border:0;margin:0;padding:0}
@page{size:A4;margin:15mm 16mm}
@media print{body{background:white;font-size:10pt;padding:0;max-width:none}p{font-size:10pt;line-height:1.57;margin:0 0 2.5mm}h1{font-size:22pt;line-height:1.3}h2{font-size:15pt;margin:0 0 4mm;break-before:page;break-after:avoid}h3{font-size:10.5pt;line-height:1.4;margin:3mm 0 2mm;break-after:avoid}figure{margin:0 0 3mm;break-inside:avoid}img{width:135mm;max-height:76mm;object-fit:contain;box-shadow:none;margin:0 auto}figcaption{font-size:8pt;line-height:1.3}header#title-block-header{display:none}.intro{font-size:11pt;margin-top:14mm;padding:8mm}.intro ol{line-height:2.2}.intro h2{break-before:auto}.intro p{font-size:11pt;line-height:1.8}}
</style>'''
txt=txt.replace('</body>',style+'</body>')
heads=re.findall(r'<h2 id="([^"]+)">(.*?)</h2>',txt,re.S)
intro='<div class="intro"><p>从一次参数调整，到一个可运行的模型。</p><p>本教程保留三种训练模式、手写数字案例、张量与并行、灾难性遗忘、泛化与拟合、架构与框架、模型文件和部署的完整讲解。</p><ol>'+''.join(f'<li><a href="#{a}">{re.sub("<.*?>", "",b)}</a></li>' for a,b in heads)+'</ol><p><a href="../slides/index.html">打开重点讲解幻灯片</a></p></div>'
pos=txt.find('</h1>',txt.find('<body'))+5
txt=txt[:pos]+intro+txt[pos:]
ht.write_text(txt,encoding='utf8')
pdf=ht.with_suffix('.pdf')
subprocess.run([r'C:\Program Files\Google\Chrome\Application\chrome.exe','--headless=new','--disable-gpu','--allow-file-access-from-files',f'--print-to-pdf={pdf}',f'--user-data-dir={P / "work/chrome-pdf-profile-final"}','--no-pdf-header-footer',ht.as_uri()],check=True,capture_output=True)
out=P/'verify/pdf-final-pages';out.mkdir(exist_ok=True)
assert out.resolve().is_relative_to(P.resolve())
for stale in out.glob('page-*.png'): stale.unlink()
subprocess.run(['pdftoppm','-png','-r','80',str(pdf),str(out/'page')],check=True,capture_output=True)
pages=sorted(out.glob('page-*.png'))
make_contact_sheet(pages,[f'page {i}' for i in range(1,len(pages)+1)],P/'verify/pdf-pages-contact-sheet.jpg',columns=4,thumb_width=260)
print('pdf_pages',len(pages))
