import pathlib,json,time
from faster_whisper import WhisperModel,BatchedInferencePipeline
from faster_whisper.audio import decode_audio
r=pathlib.Path(__file__).parent;p=next(r.parent.parent.joinpath('model').glob('1.*'))
audio=decode_audio(str(p),sampling_rate=16000)
model=WhisperModel('medium',device='cpu',compute_type='int8',cpu_threads=8,local_files_only=True)
pipe=BatchedInferencePipeline(model)
ranges=[(1318,1342),(1514,1548),(1638,1682),(1867,1942),(2324,2359),(2398,2439)]
with (r/'audio_verification.jsonl').open('w',encoding='utf8') as f:
 for a,b in ranges:
  segments,info=pipe.transcribe(audio[a*16000:b*16000],language='zh',beam_size=3,batch_size=4,initial_prompt='人工智能，机器学习，神经网络，深度学习，Transformer，Java，图灵完备，数据标注，连接主义。')
  for s in segments:
   row={'start':a+s.start,'end':a+s.end,'text':s.text}
   f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
  print('verified',a,b,flush=True)
