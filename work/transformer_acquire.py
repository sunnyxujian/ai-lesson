from pathlib import Path
import sys,json
root=Path(__file__).parent/'transformer';root.mkdir(exist_ok=True)
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
from local_qwen import LocalQwenTranscriber
source=Path(__file__).parents[1]/'video/速通AI世一论文Transformer.mp4'
result=LocalQwenTranscriber().recognize_audio(source,lang='zh')
(root/'transcript.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(result['result']['text'],flush=True)
