import sys, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILL=Path('C:/Users/micro/.codex/skills/watchless')
sys.path.insert(0,str(SKILL/'scripts'))
from video_notes_common import parse_transcript_file,make_contact_sheet
state=json.loads((ROOT/'work/run-state.json').read_text(encoding='utf-8'))
cues=parse_transcript_file(Path(state['transcript']))
ends=[6,10,14,18,22,25,31,36,39,41,44,48,50,54,56]
reasons=['学习目标与数学思维类比完成','树突接收、轴突输出的工作方式完成','向量输入与标量输出的解释完成','神经元公式及各项命名完成','年份职业薪资的输入输出含义示例完成','图像像素与分类ID例子及含义总结完成','调节权重改变输出的完整示例完成','激活和不激活的类比完成','正负偏置改变激活阈值的说明完成','ReLU函数及计算顺序回顾完成','演示启动和三个输入的含义说明完成','可调参数和审批输出的设定完成','调旋钮与亮度演示以及输出含义变更完成','不同输入共同满足预期、参数与训练的解释完成','最终总结完整覆盖最后语音块']
out={'mode':'demo','timestamp_granularity':'audio_chunk','scenes':[{'end_cue':n,'reason':r} for n,r in zip(ends,reasons)]}
(ROOT/'work/timeline/scene-boundaries.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
paths=[]
for i,n in enumerate(ends[:-1],1):
    t=(cues[n-1]['end_sec']+cues[n]['start_sec'])/2
    dest=ROOT/f'verify/boundary-timelines/boundary_{i:02}.png'
    subprocess.run([sys.executable,'-X','utf8',str(SKILL/'vendor/video-use/helpers/timeline_view.py'),state['source'],str(t-4),str(t+4),'-o',str(dest),'--n-frames','5','--transcript',state['transcript_json']],check=True)
    paths.append(dest)
make_contact_sheet(paths,[f'Boundary {i}' for i in range(1,len(paths)+1)],ROOT/'verify/boundary-overview.jpg',columns=2,thumb_width=700)
