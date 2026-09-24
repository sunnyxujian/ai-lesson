from pathlib import Path
import sys,json,subprocess,zipfile,shutil,re,hashlib
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
root=Path(__file__).resolve().parents[1];p=root/'outputs/video-notes/4.AI-本质';share=p/'share'
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
from video_notes_common import make_contact_sheet,source_fingerprint
notes=json.loads((p/'work/notes-data.json').read_text(encoding='utf-8'))
manifest=json.loads((p/'work/scene-manifest.json').read_text(encoding='utf-8'))
deck=json.loads((p/'work/deck-manifest.json').read_text(encoding='utf-8'))
light=['# AI 的本质',''];visual=['# AI 的本质','']
for n,s in zip(notes,manifest['scenes']):
 block=f'## {n["id"]:02}. {n["title"]}\n\n![{n["title"]}](keyframes/{Path(s["frame_path"]).name})\n\n{n["body"]}\n'
 light.append(block);visual.append(block+'\n### 画面与校读说明\n\n'+n['visual']+'\n')
(share/'4.AI 本质-light-polished.md').write_text('\n'.join(light),encoding='utf-8')
(share/'4.AI 本质-visual-explainer.md').write_text('\n'.join(visual),encoding='utf-8')
source=next((p/'work/video-use/transcripts').glob('*.json'))
chunks=json.loads(source.read_text(encoding='utf-8'))['words']
pdfpages=p/'verify/pdf-final-v2';pdfpages.mkdir(exist_ok=True)
for old in pdfpages.glob('page-*.png'):old.unlink()
subprocess.run(['pdftoppm','-png','-r','85',str(share/'4.AI 本质-visual-explainer.pdf'),str(pdfpages/'page')],check=True,capture_output=True)
pages=sorted(pdfpages.glob('page-*.png'))
make_contact_sheet(pages,[f'page {i}' for i in range(1,len(pages)+1)],p/'verify/pdf-pages-contact-sheet.jpg',columns=4,thumb_width=260)
slidepng=sorted((p/'verify/deck-pages').glob('slide-*.png'))
make_contact_sheet(slidepng,[f'{i:02}' for i in range(1,len(slidepng)+1)],p/'verify/deck-overview.jpg',columns=3,thumb_width=480)
shutil.copy2(source,share/'source-materials/raw-audio-chunks.json')
shutil.copy2(p/'work/deck-manifest.json',share/'source-materials/slide-source-map.json')
shutil.copy2(p/'work/notes-review.json',share/'source-materials/notes-review.json')
for name in ['audio-join-review.json','token-usage.json','content-coverage.json']:
 if (p/'work'/name).exists():shutil.copy2(p/'work'/name,share/'source-materials'/name)
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
assert browser['tutorial']['broken']==0 and browser['tutorial']['anchors']
audit=json.loads((p/'verify/quality-audit.json').read_text(encoding='utf-8'))
assert audit['transcript']['exact_ordered_coverage']
assert len(notes)==len(manifest['scenes'])==browser['tutorial']['sections']
acq=json.loads((p/'work/acquisition.json').read_text(encoding='utf-8'))
assert source_fingerprint(Path(acq['local_video']))==acq['fingerprint']
report={'audio_chunks':len(chunks),'tutorial_sections':len(notes),'selected_images':len(notes),'supplemental_images':3,'total_images':browser['tutorial']['images'],'slides':len(deck),'pdf_pages':len(pages),'source_immutable':True,'html_references':'pass','ordered_cue_coverage':True,'deck_visual_bounds':'pass','navigation':browser['navigation'],'speaker_notes':browser['notesVisible'],'editing':browser['editing'],'mobile_16_9':all(abs(v['ratio']-16/9)<.001 for v in browser['mobile']),'uncertain_terms':['OpenClaw','OAuth','Skills (one occurrence transcribed as Studio)'],'token_usage':None,'cost_usd':None,'limitations':['ASR chunk timing is approximate, not word alignment.','Not a word-for-word human listening verification.','Lecture-specific product examples, opinions, and simplifications are preserved in context.','Actual host token counts and cost are unavailable.']}
(p/'verify/delivery-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(p/'verify/delivery-audit.json',share/'source-materials/delivery-audit.json')
(share/'阅读说明.md').write_text(f'''# AI 的本质

- 完整教程.html：{len(notes)} 个章节、{len(notes)+3} 张课堂画面，按原课顺序保留完整讲解、例子、代码推导和反复强调。图片可点击放大。
- 重点演示稿.html：{len(deck)} 页，浅色书页风格，固定16:9画布，内嵌字体和插图。每页链接回完整教程，并含详细讲者备注。
- 讲者备注.md：逐页讲授提示与对应完整讲解。
- PDF讲义和Markdown：完整内容的阅读副本。
- source-materials：原始转写、章节映射及校读记录。

演示操作：方向键、空格、Page Up/Down、滚轮或手机横向滑动翻页；N 查看讲者备注；F 全屏；E 编辑，Ctrl+S 下载修改后的HTML。编辑内容也保存在本机浏览器。保留整个 share 文件夹可确保教程插图和相互链接有效。

校读范围：本机 Qwen3-ASR 转写，结合画面修正术语、明显识别错误和分块衔接。{len(chunks)} 个原始音频块按顺序完整映射，已对69个音频块交界和5处疑点做本地音频重识别。未逐字人工听校；OpenClaw、OAuth 及一处 Skills 的术语校读保留存疑标记。时间约为25秒的音频块粒度，不是逐句字幕或精确剪辑依据。课程里的产品示例、讲者观点和简化示意保留原语境；不作为最新产品规格。

原视频保持不变；所有语音识别在本地执行。宿主模型实际Token计数与费用未暴露，记为未知。
''',encoding='utf-8')
zpath=p/'4.AI 本质-video-notes.zip'
with zipfile.ZipFile(zpath,'w',zipfile.ZIP_DEFLATED) as z:
 for f in share.rglob('*'):
  if f.is_file():z.write(f,Path('share')/f.relative_to(share))
with zipfile.ZipFile(zpath) as z:
 assert z.testzip() is None
 expected={str(Path('share')/f.relative_to(share)).replace('\\','/') for f in share.rglob('*') if f.is_file()};assert set(z.namelist())==expected
print(json.dumps({'audit':report,'zip_files':len(expected),'zip_bytes':zpath.stat().st_size},ensure_ascii=False,indent=2))
