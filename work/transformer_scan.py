from pathlib import Path
import cv2,json,numpy as np
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).parent/'transformer';root.mkdir(exist_ok=True)
(root/'frames').mkdir(exist_ok=True)
cap=cv2.VideoCapture(str(Path(__file__).parents[1]/'video/速通AI世一论文Transformer.mp4'))
fps=cap.get(5);n=0;prev=None;anchor=None;changes=[];candidates=[]
while True:
 ok,f=cap.read()
 if not ok:break
 a=cv2.resize(cv2.cvtColor(f,cv2.COLOR_BGR2GRAY),(320,180))
 if prev is not None:
  d=float((np.abs(a.astype('int16')-prev.astype('int16'))>30).mean())
  if d>.035:changes.append([round(n/fps,3),round(d,4)])
 if n%30==0:
  delta=1 if anchor is None else float((np.abs(a.astype('int16')-anchor.astype('int16'))>25).mean())
  if delta>.06 or n%300==0:
   candidates.append(n/fps);anchor=a.copy()
   cv2.imencode('.jpg',f,[cv2.IMWRITE_JPEG_QUALITY,92])[1].tofile(str(root/'frames'/f'{n/fps:06.1f}.jpg'))
 prev=a;n+=1
cap.release()
(root/'visual_scan.json').write_text(json.dumps({'frames_scanned':n,'fps':fps,'changes':changes,'candidates':candidates}),encoding='utf-8')
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
for offset in range(0,len(candidates),24):
 sheet=Image.new('RGB',(1600,6*246),'#ddd');draw=ImageDraw.Draw(sheet)
 for j,t in enumerate(candidates[offset:offset+24]):
  im=Image.open(root/'frames'/f'{t:06.1f}.jpg');im.thumbnail((400,225));x=j%4*400;y=j//4*246
  sheet.paste(im,(x,y));draw.text((x+5,y+225),str(t),font=font,fill='black')
 sheet.save(root/f'contact_{offset//24:02d}.jpg')
print({'frames':n,'candidates':len(candidates),'sheets':(len(candidates)+23)//24})
