"""Local Qwen re-recognition around chunk joins; no cloud ASR."""
from pathlib import Path
import json,sys,os
root=Path(__file__).resolve().parents[1];p=root/'outputs/video-notes/3.认识模型服务接口'
config=json.loads(Path('C:/Users/micro/.codex/skills/watchless/local-qwen.json').read_text())
sys.path.insert(0,config['project']);import qwen_engine,sherpa_onnx
folder=Path(config['model'])
r=sherpa_onnx.OfflineRecognizer.from_qwen3_asr(conv_frontend=str(folder/'conv_frontend.onnx'),encoder=str(folder/'encoder.int8.onnx'),decoder=str(folder/'decoder.int8.onnx'),tokenizer=str(folder/'tokenizer'),num_threads=min(8,os.cpu_count() or 4),provider='cpu',max_total_len=1024,max_new_tokens=300)
samples=qwen_engine.decode_audio(root/'video/3.认识模型服务接口.mp4')
words=json.loads((p/'work/video-use/transcripts/3.认识模型服务接口.json').read_text(encoding='utf-8'))['words']
ranges=[(f'join-{i+1:02}-{i+2:02}',max(0,w['end']-5),min(len(samples)/16000,w['end']+3)) for i,w in enumerate(words[:-1])]
ranges += [('term-gemini',25,51),('term-qwen',704,724),('asr-tail-artifact',1252,1283)]
rows=[]
for k in range(0,len(ranges),4):
 streams=[]
 for name,a,b in ranges[k:k+4]:
  s=r.create_stream();s.set_option('language','Chinese');s.accept_waveform(16000,samples[int(a*16000):int(b*16000)]);streams.append(s)
 r.decode_streams(streams)
 for (name,a,b),s in zip(ranges[k:k+4],streams):rows.append(dict(name=name,start=a,end=b,text=s.result.text))
 (p/'work/audio-join-review.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
 print(f'Local join review: {len(rows)}/{len(ranges)}',flush=True)
