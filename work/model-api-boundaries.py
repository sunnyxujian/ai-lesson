from pathlib import Path
import sys,json,subprocess
skill=Path('C:/Users/micro/.codex/skills/watchless');sys.path.insert(0,str(skill/'scripts'))
from video_notes_common import make_contact_sheet
root=Path(__file__).resolve().parents[1];p=root/'outputs/video-notes/3.认识模型服务接口'
d=json.loads((p/'work/video-use/transcripts/3.认识模型服务接口.json').read_text(encoding='utf-8'))['words']
ends=[2,7,9,15,17,21,25,27,30,35,36,40,45,49,53,56,59,61,64,66]
reasons=['裸模型回顾和Model Service引入','三类接口规格及HTTP请求响应','网络基础要求与课程领取说明','SDK调用与Kimi兼容OpenAI实操','Anthropic兼容与SDK选择','取各服务交集作为学习核心','输入输出Token计费与包月限制','前处理三步概览和身份权限认证','系统提示词注入示例与换牌猜想','用户系统提示词及角色训练','Tokenization分词','伪代码输入和概率分布','采样结束判断追加输入与自回归例子','输出成本推导与行业观点','temperature含义和随机性','temperature场景选择及默认值','截断采样和top_k','top_p数值累加完整例子','后处理Detokenization及合规检查','流程复盘与课程收尾']
out=p/'verify/boundary-timelines';out.mkdir(exist_ok=True,parents=True)
paths=[]
for i,end in enumerate(ends[:-1],1):
 t=d[end-1]['end']-1;f=out/f'boundary-{i:02}.png'
 subprocess.run([sys.executable,str(skill/'vendor/video-use/helpers/timeline_view.py'),str(root/'video/3.认识模型服务接口.mp4'),str(t-4),str(t+4),'--n-frames','3','-o',str(f)],check=True,stdout=subprocess.DEVNULL)
 paths.append(f)
make_contact_sheet(paths,[f'{i:02}: cue {e}' for i,e in enumerate(ends[:-1],1)],p/'verify/boundary-overview.jpg',columns=2,thumb_width=650)
(p/'work/timeline/scene-boundaries.json').write_text(json.dumps({'mode':'explainer','timestamp_granularity':'audio_chunk','scenes':[{'end_cue':e,'reason':r} for e,r in zip(ends,reasons)]},ensure_ascii=False,indent=2),encoding='utf-8')
print('20 semantic scenes, 19 boundary strips; timing approximate')
