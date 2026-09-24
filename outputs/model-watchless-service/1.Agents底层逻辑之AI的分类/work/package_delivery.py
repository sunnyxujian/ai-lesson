from pathlib import Path
import json,sys,shutil,zipfile,re,subprocess
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
from video_notes_common import source_fingerprint
p=Path(__file__).resolve().parents[1];share=p/'share';src=share/'source-materials';title='1.Agents底层逻辑之AI的分类'
logp=p/'work/correction-log.json';log=json.loads(logp.read_text(encoding='utf-8'))
log['corrections'].append({'scene':15,'from':'人越少','to':'人越傻','basis':'Original video subtitle at 1792 seconds explicitly reads 学的越多人越傻; verified visually, not by listening.'})
log['corrections'].append({'scene':26,'from':'内设计 / 内图','to':'类设计 / 类图','basis':'Original visible note at 2466 seconds explicitly lists 类设计 类图.'})
logp.write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
service=Path('C:/Users/micro/Desktop/codex-tech/video-mate-pick/output/audio/20260919-234453-8b3329fb')
for a,b in [(service/'transcript.json',src/'raw-service-transcript.json'),(p/'work/video-use/transcripts'/f'{title}.json',src/'timestamped-chunks.json'),(logp,src/'correction-log.json'),(p/'verify/content-coverage.json',src/'content-coverage.json'),(p/'work/token-usage.json',src/'token-usage.json'),(p/'verify/source-review/english-check.mp3',src/'asr-anomaly-review-audio.mp3')]:shutil.copy2(a,b)
pages=json.loads((p/'verify/refined-pdf.json').read_text(encoding='utf-8'))['pdf_pages']
readme=f'''# AI 的分类 · 完整教程与重点讲稿

- 完整图文教程：share/{title}-visual-explainer.html
- PDF：share/{title}-visual-explainer.pdf（{pages} 页）
- 图文 Markdown 与轻润 Markdown：share 目录中同名文件
- 重点 HTML 演示稿：slides/index.html（18 页，含详细讲者备注与完整教程链接）

演示稿：方向键、空格、PageUp/PageDown、滚轮或滑动翻页；N 打开讲者备注；E 编辑文字；Ctrl+S 导出修改后的 HTML。编辑默认保存在本机浏览器。演示稿图片已内嵌；字体链接来自 Google Fonts，离线时浏览器使用可用字体回退。保持 share 与 slides 的相对位置，教程链接才能继续工作。

本次处理通过本地 video-mate-pick 队列取得 Qwen 转写及全部原始截图。未使用其他 ASR，也未修改原视频。27 个场景保留原讲解的顺序、例子、追问、限定与重复强调；完整教程与重点演示稿分别交付。初始 SSIM 扫描产生 154 个状态，人工检查后合并平移、缩放和临时编辑状态；图片中保留有信息的展开、板书及标注示例。

识别时间是约 25 秒音频块的近似边界，不是逐词或逐句对齐。101 个原始块全部保存在 source-materials，并在 content-coverage.json 中逐块映射；原始块前后上下文可能重叠。正文逐段人工轻润，修复确定的术语、断句与重复的分块尾部，不用摘要替代教程。

核对采用原视频画面字幕和导图。运行环境不能接受音频作为模型输入，因此不声称完成听音核验或百分之百准确。无关的英文 ASR 尾部已按原字幕上下文从教学正文移除，原异常仍保存在原始转写，附有可供人工听取的服务音频片段。GPT Live 按原画面字幕保留；一个模型名称仍标记为识别不清。课程本身的直观例子、历史判断与概念简化按原意保留，没有把它们另行扩写为当前事实结论。

Token 与费用：服务和宿主未提供实际计数，均记录为 unavailable/null，不估算、不当成零。

核验资料：verification 目录中包含覆盖审计、浏览器图片检查、幻灯片布局及交互检查。PDF 页图已实际生成并逐页概览复核，HTML 27 张图片均成功加载。仅供本地使用。
'''
(p/'README.md').write_text(readme,encoding='utf-8')
acq=json.loads((p/'work/acquisition.json').read_text(encoding='utf-8'));unchanged=source_fingerprint(Path(acq['local_video']))==acq['fingerprint']
info=subprocess.run(['pdfinfo',str(share/f'{title}-visual-explainer.pdf')],capture_output=True,check=True).stdout.decode('utf-8',errors='replace')
actual=int(re.search(r'Pages:\s+(\d+)',info).group(1));assert actual==pages
assert unchanged
for path in (p/'work/codex-notes').glob('scene_*.md'):assert 'Human Rights Watch' not in path.read_text(encoding='utf-8')
result={'status':'pass','scenes':27,'selected_images':27,'pdf_pages':actual,'deck_slides':18,'raw_cues':101,'raw_exact_ordered_coverage':True,'manual_polish_complete':True,'html_images_loaded':27,'source_fingerprint_unchanged':unchanged,'token_usage':'unavailable','cost':'unknown','known_limitations':['Audio chunk timestamps are approximate, not word aligned.','No listening verification: host does not support audio input; corrections checked against original visible subtitles/diagrams.','One model name remains uncertain in tutorial.','Source conceptual simplifications preserved; no independent fact revision.']}
(p/'verify/final-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
zip_path=p/f'{title}-video-notes.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
 for folder in [share,p/'slides']:
  for f in folder.rglob('*'):
   if f.is_file():z.write(f,f.relative_to(p))
 z.write(p/'README.md','README.md')
 for name in ['quality-audit.json','content-coverage.json','deck-check.json','tutorial-check.json','final-verification.json']:
  z.write(p/'verify'/name,'verification/'+name)
with zipfile.ZipFile(zip_path) as z:
 assert z.testzip() is None
 names=z.namelist();assert 'slides/index.html' in names and f'share/{title}-visual-explainer.pdf' in names
 assert len([n for n in names if n.startswith('share/keyframes/')])==27
result['zip_verified']=True;result['zip_entries']=len(names);result['zip_bytes']=zip_path.stat().st_size
(p/'verify/final-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
