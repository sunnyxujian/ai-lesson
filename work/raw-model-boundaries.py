from pathlib import Path
import sys,json,subprocess
skill=Path('C:/Users/micro/.codex/skills/watchless')
sys.path.insert(0,str(skill/'scripts'))
import windows_runtime
root=Path(__file__).resolve().parents[1]
project=root/'outputs/video-notes/2.AI最底层的Raw-Model'
data=json.loads((project/'work/video-use/transcripts/2.AI最底层的Raw-Model.json').read_text(encoding='utf-8'))['words']
ends=[3,5,8,13,16,20,22,24,26,31,35,37]
reasons=['开场提问与裸模型、函数及输入引入','分词和中英文 Token 数量例子','概率分布和你好续写例子','上下文窗口含义及容量估算','长上下文表现与独立任务建议，衔接权重','权重、参数单位、部署与训练引入','训练微调与语料作用','权重调用和架构示意','适用范围与数学函数抽象','确定性、拟人化评论与GPU浮点演示','多模态数字表征与输出解释例子','体系回顾与模型服务预告']
out=project/'verify/boundary-timelines';out.mkdir(exist_ok=True,parents=True)
for end in ends[:-1]:
 t=data[end-1]['end']-1
 subprocess.run([sys.executable,str(skill/'vendor/video-use/helpers/timeline_view.py'),str(root/'video/2.AI最底层的Raw Model.mp4'),str(t-4),str(t+4),'--n-frames','3','-o',str(out/f'boundary-{end:02}.png')],check=True,stdout=subprocess.DEVNULL)
(project/'work/timeline/scene-boundaries.json').write_text(json.dumps({'mode':'explainer','timestamp_granularity':'audio_chunk','scenes':[{'end_cue':e,'reason':r} for e,r in zip(ends,reasons)]},ensure_ascii=False,indent=2),encoding='utf-8')
print('12 semantic scenes; 11 boundary evidence strips')
