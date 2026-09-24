import subprocess,pathlib,json,cv2,numpy as np
from PIL import Image,ImageDraw,ImageFont
import imageio_ffmpeg
r=pathlib.Path(__file__).parent
p=next(r.parent.parent.joinpath('model').glob('1.*'))
cmd=[imageio_ffmpeg.get_ffmpeg_exe(),'-v','error','-i',str(p),'-an','-vf','scale=384:216','-f','rawvideo','-pix_fmt','gray','-']
proc=subprocess.Popen(cmd,stdout=subprocess.PIPE)
prev=None; anchor=None; changes=[]; per_second=[]; n=0; peak=0
while True:
 b=proc.stdout.read(384*216)
 if len(b)!=384*216:break
 a=np.frombuffer(b,np.uint8).reshape(216,384)[16:206,:310]
 if prev is not None:
  d=np.abs(a.astype(np.int16)-prev.astype(np.int16))
  metric=float((d>24).mean());peak=max(peak,metric)
  if metric>.035:changes.append([round(n/30,3),round(metric,4)])
 if n%30==0:
  delta=1. if anchor is None else float((np.abs(a.astype(np.int16)-anchor.astype(np.int16))>30).mean())
  per_second.append([n//30,round(peak,4),round(delta,4)])
  if delta>.07:anchor=a.copy()
  peak=0
 prev=a.copy();n+=1
proc.wait()
(r/'visual_scan.json').write_text(json.dumps({'frames_scanned':n,'changes':changes,'seconds':per_second}),encoding='utf-8')
times=set(range(0,int(n/30),45))
for sec,peak,delta in per_second:
 if delta>.07:times.add(min(sec+2,int(n/30)-1))
times=sorted(times)
# keep one frame within a 6 second window of related changes
selected=[]
for t in times:
 if not selected or t-selected[-1]>=6:selected.append(t)
cap=cv2.VideoCapture(str(p));out=r/'frames';out.mkdir(exist_ok=True)
for t in selected:
 cap.set(cv2.CAP_PROP_POS_MSEC,t*1000);ok,f=cap.read()
 if ok:cv2.imwrite(str(out/f'{t:04d}.jpg'),f,[cv2.IMWRITE_JPEG_QUALITY,90])
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
for batch in range(0,len(selected),20):
 sheet=Image.new('RGB',(1600,1000),'#ddd');dr=ImageDraw.Draw(sheet)
 for j,t in enumerate(selected[batch:batch+20]):
  im=Image.open(out/f'{t:04d}.jpg');im.thumbnail((400,225));x=(j%4)*400;y=(j//4)*200
  im=im.resize((356,200));sheet.paste(im,(x,y));dr.rectangle((x,y,x+70,y+23),fill='white');dr.text((x+3,y+1),str(t),font=font,fill='black')
 sheet.save(r/f'contact_{batch//20:02d}.jpg')
(r/'frames_index.json').write_text(json.dumps(selected),encoding='utf-8')
print(json.dumps({'frames_scanned':n,'selected':len(selected),'sheets':(len(selected)+19)//20}))
