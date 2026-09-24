import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=next((R/'share').glob('*visual-explainer.html'))
text=p.read_text(encoding='utf-8')
idx=0
def heading(m):
    global idx
    idx+=1
    return '<h2 id="scene-%02d">'%idx+m.group(1)+'</h2>'
text=re.sub(r'<h2[^>]*>(.*?)</h2>',heading,text,flags=re.S)
style='''<style id="publication-style">
html{scroll-behavior:smooth}body{background:#fffefa;color:#213d37;font-family:'Microsoft YaHei','Noto Sans SC',sans-serif;font-size:16px;line-height:1.95;max-width:1080px;padding:50px 60px}h1{font-size:35px;color:#123f36}h2{border-color:#c59143;color:#174f43;scroll-margin-top:20px}h3{color:#46695d;font-size:18px}img{border-radius:5px}figure{margin:1.2em 0}figcaption{font-size:12px;text-align:center;color:#789185}.reader-nav{border-top:1px solid #bccfc6;border-bottom:1px solid #bccfc6;padding:12px 0;margin-bottom:30px;display:flex;gap:22px;font-size:14px}.reader-nav a{color:#286b54}.reading-note{font-size:13px;color:#5c7368}.toc{columns:2;font-size:14px;margin:24px 0 36px}.toc a{display:block;color:#357461;margin-bottom:8px;text-decoration:none}.screen-only{display:block}
@media print{@page{size:A4;margin:15mm 16mm}body{max-width:none;padding:0;background:white;font-size:10.5pt;line-height:1.6;color:#172d27}p{font-size:10.5pt;line-height:1.6;margin:.65em 0;widows:3;orphans:3}h1{font-size:19pt;margin:0 0 6mm}h2{font-size:14pt;margin:0 0 4mm;break-before:page;break-after:avoid}h2:first-of-type{break-before:auto}h3{font-size:10pt;margin:3mm 0 1mm;break-after:avoid}figure{margin:2mm 0 3mm;break-inside:avoid}img{width:auto!important;max-width:100%!important;max-height:74mm!important;box-shadow:none;margin:0 auto}figcaption{font-size:7pt;margin:1mm 0}.reader-nav,.toc,.screen-only,blockquote{display:none}.reading-note{font-size:8.5pt}.visual-note{break-inside:avoid}}
</style>'''
text=text.replace('</body>',style+'</body>')
notes=json.loads((R/'work/authored-notes.json').read_text(encoding='utf-8'))
nav='<nav class="reader-nav"><a href="../slides/index.html">打开重点演示稿 ↗</a><a href="'+p.stem+'.pdf">PDF 下载</a><a href="'+p.stem+'.md">Markdown</a></nav>'
toc='<nav class="toc screen-only">'+''.join('<a href="#scene-%02d">%02d · %s</a>'%(i,i,n['title']) for i,n in enumerate(notes,1))+'</nav>'
text=text.replace('</h1>','</h1>'+nav+toc,1)
p.write_text(text,encoding='utf-8')
print(p)
