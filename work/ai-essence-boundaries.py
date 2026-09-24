from pathlib import Path
import sys,json,subprocess
skill=Path('C:/Users/micro/.codex/skills/watchless');sys.path.insert(0,str(skill/'scripts'))
from video_notes_common import make_contact_sheet
root=Path(__file__).resolve().parents[1];p=root/'outputs/video-notes/4.AI-本质'
d=json.loads((p/'work/video-use/transcripts/4.AI-本质.json').read_text(encoding='utf-8'))['words']
ends=[2,7,12,16,19,21,25,28,32,36,39,43,46,51,54,57,60,64,67,70]
reasons=['开场与三层封装','应用服务边界及底层稳定性','微调成本案例','应用开发及框架','课程体系介绍及工具使用引入','工具范围与概念寿命','理解概念的方法和输入输出论点','前后处理及应用增加消息','HTTP类比及技能例子','代理原理与项目准备','环境配置和代理测试','Claude Code接入代理','初始化请求及技能工具约定','身份回答与提示词注入','触发技能并定位响应','SSE与工具调用JSON','输入封装及调用判断','读取技能全文及调用闭环','方法推广与学习核心','课程收尾及后续安排']
out=p/'verify/boundary-timelines';out.mkdir(exist_ok=True,parents=True)
paths=[]
for i,end in enumerate(ends[:-1],1):
 t=d[end-1]['end']-1;f=out/f'boundary-{i:02}.png'
 subprocess.run([sys.executable,str(skill/'vendor/video-use/helpers/timeline_view.py'),str(root/'video/4.AI 本质.mp4'),str(t-4),str(t+4),'--n-frames','3','-o',str(f)],check=True,stdout=subprocess.DEVNULL)
 paths.append(f)
make_contact_sheet(paths,[f'{i:02}: cue {e}' for i,e in enumerate(ends[:-1],1)],p/'verify/boundary-overview.jpg',columns=2,thumb_width=650)
(p/'work/timeline/scene-boundaries.json').write_text(json.dumps({'mode':'explainer','timestamp_granularity':'audio_chunk','scenes':[{'end_cue':e,'reason':r} for e,r in zip(ends,reasons)]},ensure_ascii=False,indent=2),encoding='utf-8')
print('20 semantic scenes, 19 boundary strips; timing approximate')
