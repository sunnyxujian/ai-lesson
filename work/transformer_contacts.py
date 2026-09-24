from PIL import Image,ImageDraw
from pathlib import Path
p=Path(__file__).parent/'transformer/verify'
files=sorted(p.glob('slide-*.png'))
for k in range(0,len(files),12):
 s=Image.new('RGB',(1920,1480),'#ccc');d=ImageDraw.Draw(s)
 for i,f in enumerate(files[k:k+12]):
  x=i%3*640;y=i//3*370
  s.paste(Image.open(f).resize((640,360)),(x,y));d.text((x+5,y+356),f.stem,fill='black')
 s.save(p/f'deck-contact-{k//12}.jpg')
