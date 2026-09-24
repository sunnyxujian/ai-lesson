from pathlib import Path
import sys,json,re,html,shutil,zipfile
from urllib.parse import unquote
P=Path(__file__).resolve().parent.parent
sys.path.insert(0,r'C:\Users\micro\.codex\skills\watchless\scripts')
from video_notes_common import make_contact_sheet
files=sorted((P/'verify/deck-pages').glob('*.png'))
make_contact_sheet(files,[f'slide {i}' for i in range(1,len(files)+1)],P/'verify/deck-overview.jpg',columns=3,thumb_width=480)
sources=P/'share/source-materials'
for f in [P/'work/transcript-corrections.md',P/'work/token-usage.json',next((P/'work/video-use/transcripts').glob('*.json'))]:shutil.copy2(f,sources/f.name)
(P/'README.md').write_text('''# 第5课：训练模式与框架

- 完整图文教程：share/5.Agents底层逻辑之训练模式-visual-explainer.html
- PDF：share/5.Agents底层逻辑之训练模式-visual-explainer.pdf（13页，含目录）
- Markdown：share 下 light-polished.md 与 visual-explainer.md
- 重点幻灯片：slides/index.html（13页，字体和12张图片内嵌）
- 讲者备注：幻灯片按 N；另有 slides/speaker-notes.md。
- 导航：方向键、空格、Page Up/Down、滚轮、触屏滑动。E 进入编辑，Ctrl+S 或保存按钮导出修改后的HTML，修改也自动存本机 localStorage。
- 12个场景、108张候选图、12张正式配图，36个原始转写块顺序覆盖通过。

原始识别及校订日志在 share/source-materials。使用新版本地 video-mate-pick 音频与画面队列；没有启动旧ASR或旁路抽帧。Qwen时间为约25秒块，不能用作精确逐句定位。正文按连续语义轻润，不是原始分块拼接。本模型未听音复核；少数口语笑话仍有识别不确定性，参见校订日志。行业流行程度等表述保留课程语境，未做额外事实验证。真实token/费用不可得，均记null。
''',encoding='utf8')
errors=[];images=0
for f in [*list((P/'share').glob('*.html')),P/'slides/index.html']:
 t=f.read_text(encoding='utf8')
 for src in re.findall(r'<img[^>]+src="([^"]+)"',t):
  images+=1
  if not src.startswith('data:') and not (f.parent/unquote(html.unescape(src))).exists():errors.append(src)
 for href in re.findall(r'href="([^"]+)"',t):
  if href.startswith(('http','data:','#')):continue
  if not (f.parent/unquote(html.unescape(href.split('#')[0]))).exists():errors.append(href)
assert not errors,errors
zip_path=P/'5.Agents底层逻辑之训练模式-video-notes.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
 for root in [P/'share',P/'slides']:
  for f in root.rglob('*'):
   if f.is_file():z.write(f,f.relative_to(P))
 z.write(P/'README.md','README.md')
with zipfile.ZipFile(zip_path) as z:
 assert z.testzip() is None
 entries=z.namelist()
 assert 'slides/index.html' in entries
 assert any(x.endswith('.pdf') for x in entries)
audit={'status':'pass','scenes':12,'candidate_frames':108,'selected_frames':12,'pdf_pages':13,'deck_slides':13,'image_references_checked':images,'broken_references':errors,'zip_entries':len(entries),'zip_crc':'pass','pdf_visual_review':'13 page overview plus full page 2 verified; no clipped text or orphan caption pages','deck_visual_review':'13 screenshots plus 390x844 phone screenshot verified; no overlaps; controls outside stage','token_usage':None,'cost_usd':None,'limitations':['audio_chunk timestamps approximate','No auditory input verification','Some colloquial ASR uncertainty retained in correction log','Course simplifications not independently fact checked']}
(P/'verify/final-delivery-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(audit,ensure_ascii=False))
