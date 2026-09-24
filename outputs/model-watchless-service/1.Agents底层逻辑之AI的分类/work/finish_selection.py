from pathlib import Path
import sys,json
from PIL import Image,ImageOps,ImageDraw
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
from media_service import extract_frames
from video_notes_common import make_contact_sheet
p=Path(__file__).resolve().parents[1];f=p/'work/scene-manifest.json';m=json.loads(f.read_text(encoding='utf-8'))
source=Path('C:/Users/micro/Desktop/ai-lesson/model/1.Agents底层逻辑之AI的分类.mp4')
out=p/'verify/source-review';times=[478,480,482,1759,1761,2496,2010,2449]
extract_frames(source,times,[out/f'frame-{t}.png' for t in times])
for sid,t in [(3,367),(11,1320),(14,1595),(20,1999),(21,2010),(26,2449),(27,2496)]:
    src=out/f'frame-{t}.png';dst=p/f'work/keyframes/reviewed_{sid:03d}.png'
    # Only crop the service-returned screenshot to remove app sidebar; no new raw extraction.
    with Image.open(src) as im:im.crop((0,60,1584,945)).save(dst)
    s=m['scenes'][sid-1];s['frame_path']=str(dst);s['frame_timestamp_sec']=t
    s['candidate_paths'].append(str(dst));s['candidate_timestamps_sec'].append(t);s['preferred_candidate']=len(s['candidate_paths'])
# Preserve both text and audio labeling examples in one explicitly paired evidence figure.
sid=19;s=m['scenes'][sid-1];pieces=[]
for src in [out/'frame-1918.png',Path(s['frame_path'])]:
    with Image.open(src) as im:
        im=im.convert('RGB');im.thumbnail((1200,700));pieces.append(im.copy())
canvas=Image.new('RGB',(1200,sum(im.height for im in pieces)+38),'white');y=0
for k,im in enumerate(pieces):canvas.paste(im,((1200-im.width)//2,y));y+=im.height+38
dst=p/'work/keyframes/reviewed_019.png';canvas.save(dst);s['frame_path']=str(dst);s['candidate_paths'].append(str(dst));s['candidate_timestamps_sec'].append(1918);s['preferred_candidate']=len(s['candidate_paths'])
f.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
for offset in range(0,len(m['scenes']),6):
    ss=m['scenes'][offset:offset+6];make_contact_sheet([Path(s['frame_path']) for s in ss],[f"Scene {s['id']}" for s in ss],p/f'verify/final-review-{offset//6+1}.jpg',columns=2,thumb_width=760)
make_contact_sheet([out/f'frame-{t}.png' for t in times],[str(t) for t in times],out/'extra-check.jpg',columns=2,thumb_width=800)
selections={str(s['id']):s['preferred_candidate'] for s in m['scenes']}
(p/'work/keyframe-selections.json').write_text(json.dumps(selections),encoding='utf-8')
