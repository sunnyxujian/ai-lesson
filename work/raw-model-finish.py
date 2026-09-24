from pathlib import Path
import sys,json,subprocess,importlib.util,zipfile,re,shutil
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
root=Path(__file__).resolve().parents[1]
p=root/'outputs/video-notes/2.AI最底层的Raw-Model';share=p/'share';skill=Path('C:/Users/micro/.codex/skills/watchless/scripts')
sys.path.insert(0,str(skill))
from video_notes_common import make_contact_sheet
spec=importlib.util.spec_from_file_location('builder',skill/'05_build_outputs.py');builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
m=json.loads((p/'work/scene-manifest.json').read_text(encoding='utf-8'));notes=builder.load_notes(p/'work/codex-notes')
light,visual=builder.build_markdown_documents(m,notes,'keyframes')
(share/'2.AI最底层的Raw Model-light-polished.md').write_text(light,encoding='utf-8')
(share/'2.AI最底层的Raw Model-visual-explainer.md').write_text(visual,encoding='utf-8')
pdfpages=p/'verify/pdf-final-v2';pdfpages.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-png','-r','85',str(share/'2.AI最底层的Raw Model-visual-explainer.pdf'),str(pdfpages/'page')],check=True)
pages=sorted(pdfpages.glob('page-*.png'))
make_contact_sheet(pages,[f'page {i}' for i in range(1,len(pages)+1)],p/'verify/pdf-pages-contact-sheet.jpg',columns=4,thumb_width=280)
slidepng=sorted((p/'verify/deck-pages').glob('slide-*.png'))
make_contact_sheet(slidepng,[f'{i:02}' for i in range(1,len(slidepng)+1)],p/'verify/deck-overview.jpg',columns=3,thumb_width=480)
source=p/'work/video-use/transcripts/2.AI最底层的Raw-Model.json'
shutil.copy2(source,share/'source-materials/raw-audio-chunks.json')
shutil.copy2(p/'work/deck-manifest.json',share/'source-materials/slide-source-map.json')
(share/'阅读说明.md').write_text('''# AI 最底层的 Raw Model

- 完整教程.html：12 个段落、12 张原课画面，保留讲解顺序、问答、例子、推导及原讲者观点；图片可点击放大。
- 重点演示稿.html：18 页，A「浅色书页」风格，固定16:9画布。文字与字体均内嵌，可离线打开；每页链接到完整教程。
- 讲者备注.md：逐页讲授提示与对应完整讲解；演示稿中也可按 N 打开。
- PDF讲义与两份Markdown：完整内容的阅读副本。
- source-materials：原始分块转写及演示页到教程章节的对应表。

演示操作：方向键、空格、Page Up/Down 翻页；鼠标滚轮和手机滑动也可翻页。F 全屏，N 讲者备注，Esc 关闭备注。左上角悬停或 E 开关编辑，Ctrl+S 下载修改后的HTML；编辑也保存在本机浏览器。修改配色可调整HTML内的 :root 变量。

将整个 share 文件夹保留在一起，教程图片与互相跳转的链接才能正常使用。演示稿本身的字体和插图已内嵌。

校读范围：本地Qwen转写，结合原始板书与字幕修正明显术语和识别错误，整理标点与音频块衔接；保留了开场和多模态段落中的重复提问。音频时间为约25秒的分块粒度，不能用作逐句字幕或精确剪辑。本次未逐字人工听校；可能仍有细小识别误差。课程估算、讲者观点、记忆不确定的参数规模及简化示意均保留，并在“画面与校读说明”和讲者备注中区分。

完整性审计：37个原始音频块按顺序映射到12个段落，没有漏块；此项不等同于对语音识别准确率的保证。原视频保持不变。实际宿主模型Token用量和费用未暴露，因此记为未知。
''',encoding='utf-8')
class Links(HTMLParser):
 def __init__(self):super().__init__();self.refs=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ('src','href') and v:self.refs.append(v)
bad=[]
for f in share.glob('*.html'):
 parser=Links();parser.feed(f.read_text(encoding='utf-8'))
 for ref in parser.refs:
  if ref.startswith(('data:','https:','http:','#')):continue
  rel=unquote(urlsplit(ref).path)
  if rel and not (f.parent/rel).exists():bad.append({'file':f.name,'ref':ref})
assert not bad,bad
browser=json.loads((p/'verify/browser-audit.json').read_text(encoding='utf-8'))
assert not browser['errors']
assert all(not x['overflow'] and x['brokenImages']==0 for x in browser['slideChecks'])
assert browser['tutorial']['broken']==0
audit={'content':'37 source audio chunks mapped in exact order to 12 scenes; polished notes retain examples and sequence','tutorial_sections':12,'selected_images':12,'slides':18,'pdf_pages':len(pages),'html_references':'pass','deck_visual_bounds':'pass','navigation':browser['navigation'],'speaker_notes':browser['notesVisible'],'editing':browser['editing'],'mobile_16_9':all(abs(v['ratio']-16/9)<.001 for v in browser['mobile']),'token_usage':None,'cost_usd':None,'limitations':['ASR chunk-level timing, not word alignment; no claim of verbatim listening verification','Original lecture estimates and uncertain statements preserved with notes','Actual host token usage and cost unavailable']}
(p/'verify/delivery-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(p/'verify/delivery-audit.json',share/'source-materials/delivery-audit.json')
zipfile_path=p/'2.AI最底层的Raw Model-video-notes.zip'
with zipfile.ZipFile(zipfile_path,'w',zipfile.ZIP_DEFLATED) as z:
 for f in share.rglob('*'):
  if f.is_file():z.write(f,Path('share')/f.relative_to(share))
with zipfile.ZipFile(zipfile_path) as z:
 assert z.testzip() is None
 expected={str(Path('share')/f.relative_to(share)).replace('\\','/') for f in share.rglob('*') if f.is_file()}
 assert set(z.namelist())==expected
print(json.dumps({'audit':audit,'zip_files':len(expected),'zip_bytes':zipfile_path.stat().st_size},ensure_ascii=False,indent=2))
