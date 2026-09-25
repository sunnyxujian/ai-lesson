"""Build offline, independently portable Transformer teaching laboratories."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'work/transformer_interactive'
OUT = ROOT / 'outputs/Transformer'
MODULES = [
    ('token', 'Token 与向量', 'u06', '从词块查表到位置编码，让文字拥有可计算的表示。'),
    ('qkv', 'Q、K、V', 'u16', '逐项展开三组投影，亲手改变一个权重，看三个角色如何形成。'),
    ('attention', '注意力计算', 'u23', '从点积到加权求和，完整计算一行注意力，再看整张矩阵。'),
    ('multihead', '多头注意力', 'u34', '两个头分别观察，再拼接、投影回同一个表示空间。'),
    ('norm', 'Add & Norm', 'u36', '保留输入，融合更新，再沿每个词的特征维度做归一化。'),
    ('ffn', '前馈网络', 'u38', '升维、激活、降维，观察同一网络如何加工不同位置。'),
    ('encoder', '编码器', 'u40', '把注意力和前馈网络组成层，再追踪信息穿过多层。'),
    ('generation', '逐词生成英文', 'u42', '生成一个词，把它放回输入，直到遇到结束符。'),
    ('mask', '带掩码的多头自注意力', 'u45', '逐行揭开可见范围，观察掩码如何阻止未来信息泄漏。'),
    ('cross', '多头交叉注意力', 'u48', '英文提出查询，中文提供线索，观察两条序列怎样对齐。'),
    ('decoder', '解码器', 'u50', '跟随一个预测位置，经过两种注意力，走到词表概率。'),
    ('architecture', 'Transformer 的经典架构', 'u53', '把局部组件连起来，走完理解、生成和回填的完整路径。'),
]

def filename(index, title):
    return f'{index:02d}-{title}-交互演示.html'

ARTICLE_LINKS = {row[2]: filename(i, row[1]) for i, row in enumerate(MODULES, 1)}

def build():
    OUT.mkdir(parents=True, exist_ok=True)
    css = (SOURCE / 'style.css').read_text(encoding='utf-8')
    js = (SOURCE / 'app.js').read_text(encoding='utf-8')
    for i, (key, title, anchor, subtitle) in enumerate(MODULES, 1):
        config = json.dumps(dict(key=key, title=title, number=i, anchor=anchor), ensure_ascii=False)
        prev = f'<a href="{filename(i-1, MODULES[i-2][1])}">← 上一模块</a>' if i > 1 else '<span></span>'
        nxt = f'<a href="{filename(i+1, MODULES[i][1])}">下一模块 →</a>' if i < len(MODULES) else '<a href="Transformer-交互演示目录.html">完成 · 返回目录 →</a>'
        page = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · Transformer 交互实验室</title><style>{css}</style></head>
<body><header class="masthead"><a href="Transformer-交互演示目录.html">TRANSFORMER / 交互实验室</a><a href="Transformer-图文文章.html#{anchor}">阅读对应章节 ↗</a></header>
<main><div class="intro"><div class="eyebrow">实验 {i:02d} / 12 {' · 详细推导' if key in ('qkv','attention') else ''}</div><h1>{title}</h1><p>{subtitle}</p></div>
<div class="lab"><section class="stage" aria-label="交互动画"><div id="steps" class="steps" aria-label="步骤选择"></div><div id="visual"></div><div id="explanation" class="explanation" aria-live="polite"></div></section>
<aside class="settings"><h2>动手试一试</h2><div id="parameters"></div><div id="hint" class="hint"></div></aside></div>
<div class="transport" aria-label="动画控制"><button id="prev" aria-label="上一步">← 上一步</button><button id="play" class="primary" aria-label="播放">▶ 播放</button><button id="next" aria-label="下一步">下一步 →</button><button id="reset">↺ 重置</button><label class="speed">速度 <select id="speed" aria-label="播放速度"><option value="2400">慢</option><option value="1500" selected>正常</option><option value="800">快</option></select></label><output id="counter"></output></div>
<p class="keyboard">← → 逐步查看 · 空格播放 / 暂停 · 修改参数后即时重算</p>
<details class="principle"><summary>示例约定与公式依据</summary><p>这是用于理解计算过程的教学示例。分词、低维向量、投影权重及示意概率不代表已训练模型的真实参数或输出。数值面板由当前参数实际计算；架构连线用于说明数据流。</p><p>遵循原始 Transformer 的 Post-LN 顺序：LayerNorm(x + Sublayer(x))。注意力为 softmax(QKᵀ / √dₖ)V。推导依据：<a href="https://arxiv.org/html/1706.03762v7">Attention Is All You Need</a>，<a href="https://arxiv.org/abs/1607.06450">Layer Normalization</a>。教学案例承接小白debug的 Transformer 图解。</p></details>
<nav class="module-nav">{prev}{nxt}</nav></main><footer>小矩阵，看清每一步。所有演示可离线运行。</footer>
<script>const CONFIG={config};\n{js}</script></body></html>'''
        # Place playback adjacent to the visualization, before the mobile settings.
        import re
        transport = re.search(r'<div class="transport".*?</output></div>', page).group(0)
        page = page.replace(transport, '').replace('</section>\n<aside class="settings">', transport + '</section>\n<aside class="settings">')
        (OUT / filename(i, title)).write_text(page, encoding='utf-8')
    cards = ''.join(f'<a class="catalog-card" href="{filename(i,title)}"><span class="eyebrow">{i:02d} / {"详细推导" if key in ("qkv","attention") else "交互动画"}</span><h2>{title}</h2><p>{subtitle}</p><span class="enter">开始探索 ↗</span></a>' for i,(key,title,anchor,subtitle) in enumerate(MODULES,1))
    index = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Transformer · 交互演示目录</title><style>{css}</style></head><body><header class="masthead"><span>TRANSFORMER / 交互实验室</span><a href="Transformer-图文文章.html">阅读图文文章 ↗</a></header><main><div class="intro catalog-intro"><div class="eyebrow">12 个实验 · 一条完整学习路径</div><h1>把抽象原理，<br>变成眼前的变化。</h1><p>选择一个模块，逐步播放；改变一个参数，看信息如何流动。<br>从一个词的向量，走到一句话的生成。</p></div><div class="catalog">{cards}</div><p class="keyboard">每个动画都是独立 HTML，可单独复制、离线打开。建议按编号学习，也可以直接进入感兴趣的模块。</p></main><footer>Transformer · 交互实验室</footer></body></html>'''
    (OUT / 'Transformer-交互演示目录.html').write_text(index, encoding='utf-8')
    return ARTICLE_LINKS

if __name__ == '__main__':
    build()
    print('Built 12 standalone laboratories and catalog.')
