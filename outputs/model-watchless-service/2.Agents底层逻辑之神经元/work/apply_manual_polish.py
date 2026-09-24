from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]
manual=(ROOT/'work/manual-polish.md').read_text(encoding='utf-8')
blocks=re.split(r'^@@(\d+)\s*$',manual,flags=re.M)
for i in range(1,len(blocks),2):
    n=int(blocks[i]);body=blocks[i+1].strip()
    path=ROOT/f'work/codex-notes/scene_{n:03}.md'
    old=path.read_text(encoding='utf-8')
    title=old.split('## 标题\n')[1].split('\n\n## Light-plus')[0]
    visual=old.split('## Visual explainer\n')[1]
    path.write_text(f'## 标题\n{title}\n\n## Light-plus\n{body}\n\n## Visual explainer\n{visual}',encoding='utf-8')
review='''# 人工轻润复核

完整阅读 56 个原始音频块后，人工逐场景整理了 15 段连贯讲稿。原始分块未改动，保存在 source-materials。

## 连接处处理

- 合并“因为 Transformer 它 / 不开神经网络的，因为 Transformer …”等重复上下文，恢复完整句。
- 合并“而不是说 / 以知识体系为主，而不是说 …”等跨块截断。
- 合并“这个偏置呢，就可以 / 它有一个阈值啊，这个偏置呢，就可以 …”等重复起句。
- 其他场景逐段合并同一句被音频块分开的前后半句；没有用字符串匹配自动批量删除。
- 开场预告和中段再次出现的“大开眼界”完整保留；“只能调这个”“人怎么调”等有意强调保留。

## 核对依据和限制

依据是完整原始转写、音频块的重叠范围、已查看的原画面字幕、14 处局部音画时间线，以及 90 张候选图。未声称逐字听过全片。树突、轴突、向量、标量、权重、偏置、ReLU 用课件可见文字确认。安装和运行命令用代码候选帧确认。框架名及可视化库名仍标注需核对配套源码。

讲稿保留全部论述路径：课程目标及循环/数组类比；树突与轴突；二维三维高维向量；MP 模型；薪资预测；RGBA 与分类 ID；权重示例；听课/饥饿等激活类比；正负偏置例子；ReLU；安装运行；贷款三个输入；可调对象；明暗与输出；通过率改为贷款额；更换输入兼顾前例；参数与训练；最后总结。

界面顶部还显示 tanh，正文画面说明保留这一差异。口述和便笺权重示例不同，均注明是假设数字。对“激活函数不影响输出”的简化口述明确解释为本次调参不改变它，没有把它误写成普遍数学事实。

音频块时间只作近似导航，不代表逐词对齐。实际模型 tokens 和费用未提供，保持未知。
'''
(ROOT/'work/transcription-review.md').write_text(review,encoding='utf-8')
