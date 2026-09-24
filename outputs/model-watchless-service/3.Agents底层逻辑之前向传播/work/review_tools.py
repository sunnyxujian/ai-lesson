import json, sys, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILL=Path('C:/Users/micro/.codex/skills/watchless')
sys.path.insert(0,str(SKILL/'scripts'))
from video_notes_common import parse_transcript_file
cues=parse_transcript_file(next((ROOT/'work/transcript').glob('*.txt')))
ends=[2,5,9,15,18,24,27,30,32,36,40,45,49,53,55]
titles=['回顾单个神经元','网络分层与层编号','隐藏层的规模与识别任务','把图片变成输入向量','隐藏层配置与激活亮度','第一个隐藏神经元的计算','同层参数与逐层计算','输出计算与结果含义','输入尺寸和预处理','输出定义、Softmax与随机结果','前向传播与参数的共同作用','逐层计算参数数量','从单神经元到层编号公式','矩阵计算与GPU','参数公式与训练预告']
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'list'
    if mode=='list':
        for i,c in enumerate(cues,1): print(i,c['start_sec'],c['end_sec'],c['text'][:70])
    if mode=='boundaries':
        data={'mode':'demo','timestamp_granularity':'audio_chunk','scenes':[{'end_cue':n,'reason':t+'；采用原始音频块边界，句尾重叠保留在源稿中，视觉排版边界近似。'} for n,t in zip(ends,titles)]}
        (ROOT/'work/timeline/scene-boundaries.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
        spec=importlib.util.spec_from_file_location('timeline_view',SKILL/'vendor/video-use/helpers/timeline_view.py'); module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
        video=Path(json.loads((ROOT/'work/acquisition.json').read_text(encoding='utf-8'))['local_video'])
        transcript=next((ROOT/'work/video-use/transcripts').glob('*.json'))
        for i,n in enumerate(ends[:-1],1):
            t=cues[n-1]['end_sec']-1
            module.render_timeline(video=video,start=t-4,end=t+4,out_path=ROOT/f'verify/boundary-timelines/boundary_{i:02d}.png',n_frames=5,transcript=transcript)
    if mode=='extra':
        from video_notes_common import extract_video_frames, make_contact_sheet
        video=Path(json.loads((ROOT/'work/acquisition.json').read_text(encoding='utf-8'))['local_video'])
        times=[689,694,700,703,1008,1015,1021,1024,1259,1264,1269,1274,1275.5,1277]
        paths=[ROOT/f'verify/asr-evidence/at_{t}.jpg' for t in times]
        extract_video_frames(video,times,paths)
        make_contact_sheet(paths,[str(t) for t in times],ROOT/'verify/asr-evidence.jpg',columns=3,thumb_width=640)
    if mode=='notes':
        notes=json.loads((ROOT/'work/authored-notes.json').read_text(encoding='utf-8'))
        target=ROOT/'work/codex-notes';target.mkdir(exist_ok=True)
        for i,n in enumerate(notes,1):
            (target/f'scene_{i:03d}.md').write_text('## 标题\n'+n['title']+'\n\n## Light-plus\n'+n['text']+'\n\n## Visual explainer\n'+n['visual']+'\n',encoding='utf-8')
        mapping=[];start=1
        for i,end in enumerate(ends,1):
            mapping.append({'scene':i,'title':notes[i-1]['title'],'source_cues':list(range(start,end+1)),'source_characters':sum(len(c['text']) for c in cues[start-1:end]),'edited_characters':len(notes[i-1]['text'])});start=end+1
        (ROOT/'verify/content-coverage.json').write_text(json.dumps({'all_55_cues_mapped':True,'method':'人工逐段轻润，保留源稿；原始分块上下文重叠合并，明显ASR术语修正，英文生成伪片段排除；非逐词对齐，未声称听音核查。','scenes':mapping},ensure_ascii=False,indent=2),encoding='utf-8')
        print('source characters',sum(len(c['text']) for c in cues),'notes characters',sum(len(n['text']) for n in notes))
