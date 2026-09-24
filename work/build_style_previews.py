from pathlib import Path
import sys, re, json
sys.path.insert(0, str(Path(__file__).parent/'slide-style-tools'))
from bs4 import BeautifulSoup

ROOT=Path(r'C:\Users\micro\Desktop\ai-lesson')
OUT=ROOT/'outputs/model-watchless-service/style-previews'
OUT.mkdir(exist_ok=True)
BASE=(Path(r'C:\Users\micro\.codex\skills\frontend-slides')/'viewport-base.css').read_text(encoding='utf-8')
styles=[('blue-professional','A · 蓝白专业','清晰的标题层级，蓝色强调重点。适合整套课程统一使用。'),('cobalt-grid','B · 钴蓝方格','方格纸与细线结构，更有学术讲义的气质。适合公式和网络结构。'),('cartesian','C · 米灰极简','温暖纸色与克制的几何线条。适合概念讲解与长时间观看。')]
def content(el, html):
    el.clear()
    el.append(BeautifulSoup(html,'html.parser'))
def fixed(css):
    return re.sub(r'(-?\d*\.?\d+)(vw|vh)',lambda m: f'{float(m[1])*(19.2 if m[2]=="vw" else 10.8):g}px',css)
for slug,label,desc in styles:
    s=BeautifulSoup((ROOT/'beautiful-html-templates/templates'/slug/'template.html').read_text(encoding='utf-8'),'html.parser')
    s.html['lang']='zh-CN'
    s.title.string='前向传播 · '+label
    for el in s.select('.slide')[1:]: el.decompose()
    for el in s.select('.nav-dot')[1:]: el.decompose()
    for el in s.select('script[src]'): el.decompose()
    for el in s.select('script'):
        if el.string and '// Bar Chart' in el.string: el.string=el.string.split('// Bar Chart')[0]
    for el in s.select('style'): el.string=fixed(el.string or '')
    for el in s.select('[style]'): el['style']=fixed(el['style'])
    font=s.new_tag('link',rel='stylesheet',href='https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&family=Noto+Serif+SC:wght@400;600&display=swap'); s.head.append(font)
    slide=s.select_one('.slide')
    if slug=='blue-professional':
        content(slide.select_one('h1'),'前向传播')
        content(slide.select_one('.subtitle'),'一层一层，<br>把数字算出来。')
        content(slide.select_one('.meta'),'AGENTS / 底层逻辑 &nbsp; · &nbsp; 第三课')
        extra='''body{font-family:'Inter','Noto Sans SC',sans-serif}.layout-cover h1{font-family:'Space Grotesk','Noto Sans SC',sans-serif;font-size:144px;line-height:1.2;margin-bottom:44px;max-width:1120px}.layout-cover .subtitle{font-size:48px;line-height:1.6;max-width:1000px;margin-bottom:68px}.layout-cover .meta{font-size:26px;color:var(--text-muted)}.layout-cover .accent-line{width:96px;height:6px;margin-bottom:48px}'''
        bg='var(--bg)'
    elif slug=='cobalt-grid':
        content(slide.select_one('h1'),'前向<br>传播')
        content(slide.select_one('.subkicker .l'),'AGENTS / 底层逻辑 · 第三课')
        content(slide.select_one('.subkicker .ed'),'一层一层，把数字算出来。')
        for el,t in zip(slide.select('.v-row'),['输入','隐藏层','输出']): el.string=t
        cols=slide.select('.colf')
        content(cols[0],'<div class="ftag caption">计算路径</div><div>输入 → 隐藏层 → 输出</div>')
        content(cols[1],'<div class="ftag caption">核心概念</div><div>参数 · 激活值 · 矩阵运算</div>')
        slide.select_one('.pagenum').string='03 / AGENTS'
        extra='''body{font-family:'Hanken Grotesk','Noto Sans SC',sans-serif}.s-cover .title{font-family:'Newsreader','Noto Serif SC',serif;font-size:176px;line-height:1.12;margin:0}.s-cover .titlewrap{top:155px}.s-cover .subkicker{margin-top:45px;gap:20px}.s-cover .subkicker .l{font-family:'Hanken Grotesk','Noto Sans SC',sans-serif;font-size:26px}.s-cover .subkicker .ed{font-family:'Newsreader','Noto Serif SC',serif;font-size:40px}.s-cover .cfooter .colf{font-family:'Hanken Grotesk','Noto Sans SC',sans-serif;font-size:24px}.s-cover .cfooter .ftag{font-size:20px;margin-bottom:16px}.s-cover .vstack .v-row{font-family:'DM Mono','Noto Sans SC',sans-serif;font-size:22px}.stage::before{z-index:3;opacity:.55}.pagenum{font-size:22px}'''
        bg='var(--paper)'
    else:
        content(slide.select_one('.label'),'AGENTS / 底层逻辑 · 第三课')
        content(slide.select_one('h1'),'前向传播')
        content(slide.select_one('.subtitle'),'一层一层，<br>把数字算出来。')
        extra='''body{font-family:'Inter','Noto Sans SC',sans-serif}.slide-title .label{font-family:'Inter','Noto Sans SC',sans-serif;font-size:26px;margin-bottom:52px;color:var(--text-secondary)}.slide-title h1{font-family:'Playfair Display','Noto Serif SC',serif;font-size:144px;line-height:1.25;margin-bottom:40px}.slide-title .subtitle{font-family:'Inter','Noto Sans SC',sans-serif;font-size:46px;line-height:1.7}.slide-title{padding-left:154px}'''
        bg='var(--bg-primary)'
    # Preserve each template's navigation and composition in a uniformly scaled stage.
    wrapper=s.new_tag('div',attrs={'class':'deck-viewport'})
    stage=s.new_tag('div',attrs={'class':'deck-stage','id':'previewStage'})
    for child in list(s.body.contents):
        if getattr(child,'name',None)!='script': stage.append(child.extract())
    wrapper.append(stage); s.body.insert(0,wrapper)
    override=s.new_tag('style')
    override.string=BASE+'\n/* === FIXED CANVAS AND CHINESE TYPE SUPPORT === */\n'+f':root{{--slide-bg:{bg};--stage-bg:{bg}}}'+''' .deck,.stage,.presentation{width:1920px;height:1080px}.slide{width:1920px;height:1080px}.slide.active{visibility:visible;opacity:1}.layout-cover,.slide-title{display:flex}.nav-controls,.nav-arrows,.nav-dots,.keyboard-hint,.nav-hint,.slide-counter,.progress-bar{display:none}'''+extra
    s.head.append(override)
    script=s.new_tag('script');script.string="""function fitPreview(){const el=document.getElementById('previewStage'),k=Math.min(innerWidth/1920,innerHeight/1080);el.style.transform=`translate(${(innerWidth-1920*k)/2}px,${(innerHeight-1080*k)/2}px) scale(${k})`;}addEventListener('resize',fitPreview);fitPreview();""";s.body.append(script)
    (OUT/f'{slug}.html').write_text(str(s),encoding='utf-8')

cards=''.join(f'<article><a class="visual" href="{slug}.html" target="_blank"><img src="{slug}.png" alt="{label}：前向传播封面"></a><div class="detail"><h2>{label}</h2><p>{desc}</p><a class="open" href="{slug}.html" target="_blank">打开完整预览 ↗</a></div></article>' for slug,label,desc in styles)
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Agents 课程 · 样式对比</title><style>*{box-sizing:border-box}body{margin:0;background:#f5f4f0;color:#172426;font-family:'Microsoft YaHei',sans-serif}main{max-width:1450px;margin:auto;padding:48px 40px 70px}.eyebrow{font-size:12px;letter-spacing:3px;color:#687375}h1{font-size:38px;margin:18px 0 16px}.intro{color:#596568;line-height:1.8;margin-bottom:34px}section{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}article{background:white;border:1px solid #dbdeda;border-radius:12px;overflow:hidden}.visual{display:block;background:#eee}.visual img{width:100%;aspect-ratio:16/9;display:block}.detail{padding:24px}h2{font-size:22px;margin:0 0 12px}.detail p{font-size:15px;line-height:1.85;min-height:84px;color:#596568}.open{display:inline-block;color:#214d87;text-decoration:none;border-bottom:1px solid;padding-bottom:4px}footer{margin-top:30px;color:#596568;font-size:14px;line-height:1.9}@media(max-width:900px){section{grid-template-columns:1fr}main{padding:30px 20px}.detail p{min-height:0}}a:focus-visible{outline:3px solid #214d87}</style></head><body><main><div class="eyebrow">AGENTS / 课程视觉系统</div><h1>让知识更清楚，让课程更统一。</h1><p class="intro">同一课、同一段内容，三种浅色方案。点击封面可查看实际 16:9 效果。<br>建议选择 A：投影时重点明确，也便于容纳原有截图、公式和讲者备注。</p><section>'''+cards+'''</section><footer>适用范围：AI 的分类 / 神经元 / 前向传播 / 梯度下降 / 训练模式。<br>当前为封面风格预览，原有 5 套、79 页演示稿尚未修改。</footer></main></body></html>'''
(OUT/'index.html').write_text(html,encoding='utf-8')
print(OUT)
