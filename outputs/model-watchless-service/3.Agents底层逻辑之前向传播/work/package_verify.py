import json,sys,subprocess,zipfile,hashlib,re,shutil
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
import windows_runtime
from video_notes_common import make_contact_sheet,source_fingerprint
pdf=next((R/'share').glob('*visual-explainer.pdf'))
pages=R/'verify/pdf-pages-final';pages.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-png','-r','90',str(pdf),str(pages/'page')],check=True,capture_output=True)
imgs=sorted(pages.glob('page-*.png'))
make_contact_sheet(imgs,[f'page {i}' for i in range(1,len(imgs)+1)],R/'verify/pdf-pages-contact-sheet.jpg',columns=4,thumb_width=280)
for w in [1280,390]:
    frames=sorted((R/'verify').glob(f'deck-{w}-*.png'))
    make_contact_sheet(frames,[f'slide {i}' for i in range(1,len(frames)+1)],R/f'verify/deck-{w}-overview.jpg',columns=4,thumb_width=400 if w==1280 else 150)
acq=json.loads((R/'work/acquisition.json').read_text(encoding='utf-8'))
browser=json.loads((R/'verify/browser-verification.json').read_text(encoding='utf-8'))
bad=[x for x in browser['deck'] if x['outside'] or x['overflow'] or x['brokenImages'] or abs(x['stageRatio']-16/9)>0.001 or x['visibleSlides']!=1]
report={'status':'pass_with_documented_limitation','scenes':15,'source_audio_chunks':55,'candidate_frames':90,'images':15,'pdf_pages':len(imgs),'slides':16,'html_images_valid':not browser['tutorial']['broken'],'deck_overflow_records':bad,'source_unchanged':source_fingerprint(Path(acq['local_video']))==acq['fingerprint'],'boundary_timeline_images_reviewed':14,'desktop_and_phone_screenshots':32,'token_usage_available':False,'cost_available':False}
(R/'verify/final-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
readme='''# 前向传播 · 完整教程与演示稿

- 完整教程：share/3.Agents底层逻辑之前向传播-visual-explainer.html
- PDF、图文 Markdown、轻润讲解 Markdown：同在 share/。
- 重点演示稿：slides/index.html（16页，固定16:9舞台）。字体和15张截图均已嵌入，可以离线打开。
- 演示操作：方向键、空格、翻页键、滚轮或左右滑动；N 打开详细讲者备注；E 开关文字编辑；Ctrl+S 或“保存”导出修改版。每页“完整讲解”链接回教程对应段落。

完整教程保留输入数字化、网络规模、激活值、全连接计算、输出定义、图像尺寸处理、Softmax、随机结果、参数传递、逐层参数统计、公式记号、矩阵与GPU以及训练预告。原始55个音频块原样保存在 source-materials，正文为人工轻润稿；源稿覆盖映射与正文内容审阅分别记录。

使用本机 video-mate-pick 服务音频/画面队列，本地 Qwen 识别；未使用云端ASR。分块时间为近似时间，没有逐词对齐、说话人识别，也未声称逐句听音验证。画面字幕、公式及语义用于核对明显识别错误；原始英文生成伪片段仍保留在源稿，未带入正文。

课程中模型规格、Sigmoid与“除最大值”的混称、8次口头示意和10个输出的差异、矩阵“点乘”等原述，已在相应画面说明中标明。CPU比较语句有不清晰ASR词语，仅保留明确的GPU加速含义。模型token和费用未由宿主运行环境提供，记为未知，没有估算或伪造。
'''
(R/'README.md').write_text(readme,encoding='utf-8')
review='''# 审阅与限制

## 边界与字幕
直接审阅14个约±4秒的边界时间线，结合画面变化、烧录字幕和波形；未把波形或25秒分块当作词级时间。边界与语义推进一致，跨块断句在正文中接成完整句子，原始scene transcript不改。

另外检查689/694/700/703秒、1008/1015/1021/1024秒及1259—1277秒附近原画面：前两处始终是中文神经网络推导，ASR出现的 <|endoftext|> 后英文无上下文支撑，作为生成伪片段从正文排除，原始转写不删。700秒字幕确有“8个神经元”，图中输出可见10个，保留冲突并注释。CPU不清晰词语未强行恢复。

## 内容
逐场景对照55个音频块的全部原文，修复重叠断句，保留图像RGB/十六进制示意、1600输入而非8输入、1920×1080例子与处理方式、每层自己的随机参数、相同输入不同参数、输出意义人为规定、Softmax百分比、随机结果不代表识别成功、参数影响逐层传递、三层参数计算、层编号非指数、矩阵与GPU、训练预告。经主agent抽查补回第7场景两处随机初值强调，并重新检查各场景有意重复与限制。

## 自动审计警告处置
quality-audit.json 唯一警告是宿主未提供实际模型token。work/token-usage.json明确写为unavailable，所有计数和成本为null；不写虚假0或假条目使审计表面通过。其余转写映射、15篇笔记、15张选帧、无字节重复、HTML图片等均通过。最终发布验证记录采用pass_with_documented_limitation。
'''
(R/'verify/review-resolution.md').write_text(review,encoding='utf-8')
zip_path=R/'3.Agents底层逻辑之前向传播-video-notes.zip'
sources=list((R/'share').rglob('*'))+list((R/'slides').rglob('*'))+[R/'README.md',R/'verify/final-verification.json',R/'verify/review-resolution.md',R/'verify/content-coverage.json']
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sources:
        if p.is_file():z.write(p,p.relative_to(R))
with zipfile.ZipFile(zip_path) as z:
    assert z.testzip() is None
    for p in sources:
        if p.is_file():assert hashlib.sha256(z.read(str(p.relative_to(R)).replace('\\','/'))).digest()==hashlib.sha256(p.read_bytes()).digest()
    report['zip_members']=len(z.namelist());report['zip_crc_and_contents_valid']=True
(R/'verify/final-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
# Refresh the ZIP to include the finalized verification record without duplicate names.
with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sources:
        if p.is_file():z.write(p,p.relative_to(R))
with zipfile.ZipFile(zip_path) as z:assert z.testzip() is None
print(json.dumps(report,ensure_ascii=False,indent=2))
