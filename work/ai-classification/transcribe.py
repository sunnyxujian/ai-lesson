import os,json,time,pathlib
os.environ['HF_HUB_OFFLINE']='1'
from faster_whisper import WhisperModel, BatchedInferencePipeline
root=pathlib.Path(__file__).parent
source=next(root.parent.parent.joinpath('model').glob('1.*'))
t=time.time()
model=WhisperModel('base',device='cpu',compute_type='int8',cpu_threads=8,local_files_only=True)
pipeline=BatchedInferencePipeline(model=model)
segments,info=pipeline.transcribe(str(source),language='zh',beam_size=3,batch_size=8,vad_filter=True,initial_prompt='人工智能，AI，Agents，符号主义，连接主义，行为主义，机器学习，深度学习，神经网络，监督学习，无监督学习，强化学习。')
with (root/'transcript.jsonl').open('w',encoding='utf-8') as f:
 for i,s in enumerate(segments):
  row={'id':i+1,'start':s.start,'end':s.end,'text':s.text,'avg_logprob':s.avg_logprob,'no_speech_prob':s.no_speech_prob}
  f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
  if i%30==0: print(f'{i+1} segments; audio {s.end:.0f}s; elapsed {time.time()-t:.0f}s',flush=True)
(root/'asr_done.json').write_text(json.dumps({'duration':info.duration,'elapsed':time.time()-t}),encoding='utf-8')
print('DONE',flush=True)
