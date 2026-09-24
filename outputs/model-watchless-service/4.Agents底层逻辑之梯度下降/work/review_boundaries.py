import json, subprocess, sys
from pathlib import Path
root=Path(__file__).resolve().parent.parent
skill=Path('C:/Users/micro/.codex/skills/watchless')
sys.path.insert(0,str(skill/'scripts'))
from video_notes_common import parse_transcript_file
state=json.loads((root/'work/run-state.json').read_text(encoding='utf-8'))
cues=parse_transcript_file(Path(state['transcript']))
ends=[4,8,13,18,25,30,35,40,44,48,51,56,59,63,67,70]
reasons=['从随机预测引入自动调参，进入标签示例','标签向量说明完成，进入损失量化','平方差损失与教学范围交代完成','损失作为参数函数，进入单参数图像','切线确定单参数方向，进入双参数曲面','下山比喻及高维推广，进入局部最优','局部最优与噪声说明，进入学习率','学习率与大步越谷示例，进入分量','分量差异说明完毕，进入反向传播','输出层调整期望说明，进入单神经元依赖','权重偏置和上一层输出列举完成','偏导链式法则及整层参数，进入上层期望','期望反传引入完成，进入多对多汇总','逐层汇总与输入固定，进入整体更新','矩阵更新和训练循环完成，进入术语定义','课程结束与下节预告']
data={'mode':'demo','timestamp_granularity':'audio_chunk','scenes':[{'end_cue':i,'reason':r} for i,r in zip(ends,reasons)]}
(root/'work/timeline/scene-boundaries.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
for i in ends[:-1]:
    t=cues[i-1]['end_sec']-1
    out=root/f'verify/boundary-timelines/cue_{i:03d}.png'
    if not out.exists():
        subprocess.run([sys.executable,'-X','utf8',str(skill/'vendor/video-use/helpers/timeline_view.py'),state['source'],str(max(0,t-4)),str(t+4),'--n-frames','5','--transcript',state['transcript_json'],'-o',str(out)],check=True)
print('Boundary images complete',flush=True)
