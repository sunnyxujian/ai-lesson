from pathlib import Path
import json, re, shutil
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'work/scene-manifest.json').read_text(encoding='utf-8'))
points=[
['Transformer 是神经网络的一种实现形式。','先认识术语与概念，再建立知识体系。','本课先理解单个神经元。'],
['多个树突：接收不同的输入信号。','一个轴突：输出一个信号。','分叉把同一个输出传给其他神经元。'],
['输入是向量，可先理解为一维数组。','二维、三维到更高维：都是多个数字。','输出是标量，即单个数字。'],
['每个输入 xᵢ 乘上对应的权重 wᵢ。','把乘积相加，再加偏置 b。','经过激活函数 σ，得到输出 y。'],
['示例输入：[25, 11, 33]。','人为解释：年份、职业编号、年薪。','人为设定希望输出下一年的薪资涨幅。'],
['图像可以用像素的 R、G、B、A 数值表示。','输出数字可对应一个分类 ID。','输入与输出的业务含义都由人规定。'],
['w₁、w₂、…、wₙ 控制各输入的影响。','改变权重，就会改变计算结果。','示例数值仅为演示，需要调整才可能符合预期。'],
['课程用“休眠”比喻未激活。','用输出 y 表示激活程度。','此处以非负输出的演示模型理解。'],
['偏置 b 平移加权和。','减 10：加权和要超过 10 才能激活。','加 10：降低达到激活状态的门槛。'],
['ReLU 把负数截为 0。','非负值保持原值。','本课借这个简单函数理解激活步骤。'],
['输入：收入 30 万/年。','输入：信用分 750，负债率 30%。','界面用三个输入连接到单个神经元。'],
['输入由外界给定。','当前演示的激活函数在设计时选定。','可调对象是权重和偏置。'],
['依次调节 w₁、w₂、w₃、b。','观察 y 值与节点明暗的变化。','通过率、可贷金额都是讲解中临时设定的意义。'],
['把收入改为 35 万/年，信用分改为 350。','新输入也要得到符合预期的输出。','权重和偏置统称参数；训练围绕参数调整展开。'],
['向量输入 → 标量输出。','权重和偏置决定当前模型的可调行为。','目标：让不同输入都得到符合预期的结果。']]
assets=ROOT/'slides/assets';assets.mkdir(parents=True,exist_ok=True)
slides=[]
for i,(scene,ps) in enumerate(zip(m['scenes'],points),1):
    t=(ROOT/f'work/codex-notes/scene_{i:03}.md').read_text(encoding='utf-8')
    title=t.split('## 标题\n')[1].split('\n\n')[0]
    lecture=t.split('## Light-plus\n')[1].split('\n\n## Visual explainer')[0]
    visual=t.split('## Visual explainer\n')[1]
    name=f'frame-{i:02}.jpg';shutil.copy2(scene['frame_path'],assets/name)
    slides.append({'title':title,'points':ps,'image':'assets/'+name,'alt':visual,'notes':lecture.split('\n\n')+['画面依据：'+visual], 'anchor':f'#lesson-{i:02}'})
data={'tutorial':'../share/2.Agents底层逻辑之神经元-visual-explainer.html','slides':slides}
(ROOT/'work/deck-content.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
