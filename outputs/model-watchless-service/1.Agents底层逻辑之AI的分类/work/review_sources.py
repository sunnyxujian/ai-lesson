from pathlib import Path
import sys,wave,subprocess
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
from media_service import extract_frames
from video_notes_common import make_contact_sheet
p=Path(__file__).resolve().parents[1];out=p/'verify/source-review';out.mkdir(exist_ok=True)
times=[367,1030,1320,1595,1918,1999,2430,2490,2510,490,500,1755,1758]
paths=[out/f'frame-{t}.png' for t in times]
extract_frames(Path('C:/Users/micro/Desktop/ai-lesson/model/1.Agents底层逻辑之AI的分类.mp4'),times,paths)
for k in range(0,len(paths),4):make_contact_sheet(paths[k:k+4],[str(t) for t in times[k:k+4]],out/f'sheet-{k//4+1}.jpg',columns=2,thumb_width=800)
# Clips are cut only from the WAV already provided by the identity-checked audio service.
source=Path('C:/Users/micro/Desktop/codex-tech/video-mate-pick/output/audio/20260919-234453-8b3329fb/audio.wav')
with wave.open(str(source),'rb') as w:
    for name,a,b in [('english-check',1746,1766),('model-name',470,494),('overlaps',21,33)]:
        w.setpos(int(a*w.getframerate()));data=w.readframes(int((b-a)*w.getframerate()))
        target=out/f'{name}.wav'
        with wave.open(str(target),'wb') as dst:dst.setparams(w.getparams());dst.writeframes(data)
        subprocess.run(['ffmpeg','-y','-v','error','-i',str(target),'-ar','16000','-b:a','24k',str(out/f'{name}.mp3')],check=True)
print(out)
