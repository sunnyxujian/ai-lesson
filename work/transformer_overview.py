from PIL import Image,ImageDraw,ImageFont
from pathlib import Path
p=Path(__file__).parent/'transformer'
files=list((p/'frames').glob('*.jpg'))
sel=[min(files,key=lambda f:abs(float(f.stem)-t)) for t in range(0,676,5)]
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
for k in range(0,len(sel),24):
 s=Image.new('RGB',(1600,1488),'#ddd');d=ImageDraw.Draw(s)
 for i,f in enumerate(sel[k:k+24]):
  x=i%4*400;y=i//4*248;s.paste(Image.open(f).resize((400,225)),(x,y));d.text((x+4,y+226),f.stem,font=font,fill='black')
 s.save(p/f'overview_{k//24:02}.jpg')
