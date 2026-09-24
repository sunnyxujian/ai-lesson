import pathlib,subprocess,json,cv2,numpy as np,time
import imageio_ffmpeg
from rapidocr_onnxruntime import RapidOCR
r=pathlib.Path(__file__).parent;p=next(r.parent.parent.joinpath('model').glob('1.*'))
ocr=RapidOCR(intra_op_num_threads=1,inter_op_num_threads=1)
proc=subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(),'-v','error','-threads','2','-i',str(p),'-an','-vf','crop=1560:76:0:948,fps=4','-f','rawvideo','-pix_fmt','bgr24','-'],stdout=subprocess.PIPE)
prev=None;n=0;rows=[];lasttext='';pending=None
with (r/'subtitles.jsonl').open('w',encoding='utf-8') as out:
 while True:
  b=proc.stdout.read(1560*76*3)
  if len(b)!=1560*76*3:break
  im=np.frombuffer(b,np.uint8).reshape(76,1560,3)
  gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
  delta=1 if prev is None else (np.abs(gray.astype(np.int16)-prev.astype(np.int16))>25).mean()
  if delta>.012:
   # The burned-in caption has a centered grey background at this fixed band.
   row=gray[6];mask=(row>55)&(row<190)
   indices=np.flatnonzero(mask)
   runs=np.split(indices,np.where(np.diff(indices)>1)[0]+1)
   runs=[a for a in runs if len(a)>60 and a[0]<1020 and a[-1]>860]
   txt='';conf=0
   if runs:
    run=max(runs,key=len);left=max(0,int(run[0])+5);right=min(1560,int(run[-1])-4)
    res,_=ocr(im[7:73,left:right],use_det=False,use_cls=False)
    if res:txt,conf=res[0]
   if txt and txt!=lasttext:
    row={'time':n/4,'text':txt,'confidence':round(float(conf),3)}
    out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush();rows.append(row);lasttext=txt
   prev=gray.copy()
  n+=1
  if n%1200==0:print(f'audio {n/4:.0f}s; subtitles {len(rows)}',flush=True)
proc.wait();print('DONE',len(rows),flush=True)
