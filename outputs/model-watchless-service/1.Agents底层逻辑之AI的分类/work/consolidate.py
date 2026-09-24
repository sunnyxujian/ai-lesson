from pathlib import Path
import json,sys,shutil
sys.path.insert(0,'C:/Users/micro/.codex/skills/watchless/scripts')
from video_notes_common import parse_transcript_file,make_contact_sheet
p=Path(__file__).resolve().parents[1];mp=p/'work/scene-manifest.json'
orig=p/'work/scene-manifest-ssim-original.json'
if not orig.exists():shutil.copy2(mp,orig)
m=json.loads(orig.read_text(encoding='utf-8'));raw=m['scenes'];cues=parse_transcript_file(Path(m['transcript']['path']))
# Direct review: consolidate cursor, panning, resize, and temporary editing states.
groups=[(1,3,3),(4,8,8),(9,14,13),(15,19,15),(20,20,19),(21,24,24),(25,30,30),(31,36,36),(37,37,37),(38,41,40),(42,52,52),(53,59,59),(60,68,68),(69,89,80),(90,96,96),(97,98,98),(99,100,100),(101,110,110),(111,113,113),(114,116,116),(117,117,117),(118,118,118),(119,122,122),(123,126,126),(127,145,145),(146,148,148),(149,154,154)]
new=[]
for sid,(a,b,choice) in enumerate(groups,1):
    r=dict(raw[choice-1]);r.update(id=sid,start_sec=raw[a-1]['start_sec'],end_sec=raw[b-1]['end_sec'])
    relevant=[c for c in cues if r['start_sec']<=c['start_sec']<r['end_sec']]
    r['transcript_text']=''.join(c['text'] for c in relevant)
    r['source_cues']=relevant
    r['candidate_paths']=[x['frame_path'] for x in raw[a-1:b]]
    r['candidate_timestamps_sec']=[x['frame_timestamp_sec'] for x in raw[a-1:b]]
    if choice<a or choice>b:
        r['candidate_paths'].append(raw[choice-1]['frame_path']);r['candidate_timestamps_sec'].append(raw[choice-1]['frame_timestamp_sec'])
    r['preferred_candidate']=r['candidate_paths'].index(r['frame_path'])+1
    r['selection_method']='codex_visual_consolidation_of_ssim_states'
    r['visual_review']='Merged transient pan/zoom/editor states; retained legible teaching state and all ordered source cues.'
    new.append(r)
m['scenes']=new;m['keyframe_review']={'status':'pending'}
m['manual_visual_consolidation']={'original_scene_count':154,'retained_scene_count':len(new),'groups':groups,'basis':'Direct inspection of original contact sheet; original scan and all candidates preserved.'}
mp.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
for offset in range(0,len(new),6):
    subset=new[offset:offset+6]
    make_contact_sheet([Path(x['frame_path']) for x in subset],[f"scene {x['id']}" for x in subset],p/f'verify/review-{offset//6+1}.jpg',columns=2,thumb_width=760)
make_contact_sheet([Path(x['frame_path']) for x in new],[f"scene {x['id']}" for x in new],p/'verify/selected-keyframes.jpg',columns=4)
print('scenes',len(new),'source cues',sum(len(x['source_cues']) for x in new))
