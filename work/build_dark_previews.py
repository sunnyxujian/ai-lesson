from pathlib import Path
import sys,re,json
sys.path.insert(0,str(Path(__file__).parent/'slide-style-tools'))
from bs4 import BeautifulSoup
ROOT=Path(r'C:\Users\micro\Desktop\ai-lesson')
OUT=ROOT/'outputs/model-watchless-service/style-previews-dark'
OUT.mkdir(exist_ok=True)
BASE=Path(r'C:\Users\micro\.codex\skills\frontend-slides\viewport-base.css').read_text(encoding='utf-8')
choices=[('8-bit-orbit','A · 霓虹矩阵','深蓝底、青色标题、像素网格。科技感最鲜明，适合 AI 技术课程。'),('studio','B · 黑金极客','近黑底、电光黄大字、网络连线。对比强，适合现场演示和强调重点。'),('signal','C · 深蓝研究室','藏蓝底、暖白标题、细金线。克制沉稳，适合长时间授课与原理讲解。')]
def sethtml(el,html):
    el.clear();el.append(BeautifulSoup(html,'html.parser'))
def fixed(css):
    return re.sub(r'(-?\d*\.?\d+)(vw|vh)',lambda m:f'{float(m[1])*(19.2 if m[2]=="vw" else 10.8):g}px',css)
for slug,label,desc in choices:
    s=BeautifulSoup((ROOT/'beautiful-html-templates/templates'/slug/'template.html').read_text(encoding='utf-8'),'html.parser')
    s.html['lang']='zh-CN';s.title.string='前向传播 · '+label
    for el in s.select('.slide')[1:]:el.decompose()
    slide=s.select_one('.slide');slide['class']=slide.get('class',[])+['active','visible','is-active']
    for el in s.select('style'):el.string=fixed(el.string or '')
    for el in s.select('[style]'):el['style']=fixed(el['style'])
    for el in s.select('script'):
        if el.string:el.string=el.string.replace('const totalSlides = 10;','const totalSlides = 1;')
    s.head.append(s.new_tag('link',rel='stylesheet',href='https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;900&family=Noto+Serif+SC:wght@400;600;700&display=swap'))
    if slug=='8-bit-orbit':
        sethtml(slide.select_one('.hero-subtitle'),'AGENTS / 底层逻辑 · 第三课')
        sethtml(slide.select_one('h1'),'前向传播')
        sethtml(slide.select_one('.hero-tagline'),'一层一层，把数字算出来。')
        for el,t in zip(slide.select('.hero-badge'),['输入','隐藏层','输出']):el.string=t
        css='''body{font-family:'Chakra Petch','Noto Sans SC',sans-serif}.slide{display:flex}.pixel-hero-text{font-family:'Tektur','Noto Sans SC',sans-serif;font-size:172px;line-height:1.35}.hero-subtitle{font-family:'Space Mono','Noto Sans SC',sans-serif;font-size:26px;margin-bottom:55px}.hero-tagline{font-family:'Chakra Petch','Noto Sans SC',sans-serif;font-size:42px;max-width:1200px;margin-top:40px}.hero-badges{gap:28px;margin-top:65px}.hero-badge{font-family:'Space Mono','Noto Sans SC',sans-serif;font-size:28px;padding:14px 40px}.slide-content{max-width:1600px}'''
        bg='var(--dark-void)'
    elif slug=='studio':
        sethtml(slide.select_one('h1'),'前向传播')
        cols=slide.select('.cover-meta-col')
        for el,t in zip(cols,['AGENTS / 底层逻辑<br>第三课','一层一层，把数字算出来。','输入 → 隐藏层 → 输出']):sethtml(el,t)
        lines=[]
        layers=[[(1050,240),(1050,460),(1050,680)],[(1310,150),(1310,355),(1310,560),(1310,765)],[(1570,280),(1570,630)]]
        for left,right in zip(layers,layers[1:]):
            for x1,y1 in left:
                for x2,y2 in right:lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
        nodes=''.join(f'<circle cx="{x}" cy="{y}" r="16"/>' for layer in layers for x,y in layer)
        sethtml(slide.select_one('.cover-img-area'),'<svg viewBox="0 0 1920 1080" width="1920" height="1080" role="img" aria-label="输入、隐藏层、输出之间的连接示意"><g fill="none" stroke="currentColor" stroke-width="2" opacity=".35">'+''.join(lines)+'</g><g fill="currentColor" opacity=".7">'+nodes+'</g></svg>')
        css='''.slide--cover{display:flex}.cover-type{padding-top:180px}.display{font-size:190px;line-height:1.3}.cover-img-area{color:var(--c-fg);overflow:hidden}.cover-meta-col{font-family:'IBM Plex Mono','Noto Sans SC',sans-serif;font-size:25px}.cover-meta{padding-top:32px;padding-bottom:64px}.cover-type h1{max-width:1150px}'''
        bg='var(--c-bg)'
    else:
        sethtml(slide.select_one('.cover-body > .label'),'AGENTS / 底层逻辑 · 第三课')
        sethtml(slide.select_one('h1'),'前向<em>传播</em>')
        sethtml(slide.select_one('.lead'),'一层一层，<br>把数字算出来。')
        for el,t in zip(slide.select('.cover-meta .label'),['神经网络 / 输入 → 隐藏层 → 输出','参数 · 激活值 · 矩阵运算']):el.string=t
        css='''.slide--cover{display:flex}.display{font-size:166px;line-height:1.3}.display em{font-style:normal}.lead{font-size:46px;line-height:1.65}.label{font-family:'IBM Plex Mono','Noto Sans SC',sans-serif;font-size:25px}.cover-body{gap:38px}.cover-meta{margin-top:64px;padding-top:28px}.cover-meta .label{font-size:23px}.slide--cover{padding-bottom:86px}'''
        bg='var(--c-bg)'
    viewport=s.new_tag('div',attrs={'class':'deck-viewport'})
    stage=s.new_tag('div',attrs={'class':'deck-stage','id':'previewStage'})
    for el in list(s.body.contents):
        if getattr(el,'name',None)!='script':stage.append(el.extract())
    viewport.append(stage);s.body.insert(0,viewport)
    style=s.new_tag('style');style.string=BASE+'\n/* === FIXED STAGE AND CHINESE TYPOGRAPHY === */\n'+f':root{{--slide-bg:{bg};--stage-bg:{bg}}}'+'.deck,#deck,.slides-container{width:1920px!important;height:1080px!important}.slide{width:1920px;height:1080px}.nav-dots,#nav-dots,#slide-counter,.slide-counter{display:none}'+css
    s.head.append(style)
    js=s.new_tag('script');js.string="""function fitPreview(){const k=Math.min(innerWidth/1920,innerHeight/1080);document.getElementById('previewStage').style.transform=`translate(${(innerWidth-1920*k)/2}px,${(innerHeight-1080*k)/2}px) scale(${k})`;}addEventListener('resize',fitPreview);fitPreview();""";s.body.append(js)
    text=slide.get_text(' ',strip=True)
    assert '[' not in text and 'PLACEHOLDER' not in text and 'Template' not in text
    assert len(s.select('.slide'))==1
    (OUT/f'{slug}.html').write_text(str(s),encoding='utf-8')
cards=''.join(f'<article><iframe title="{label}" src="{slug}.html" loading="eager"></iframe><div><h2>{label}</h2><p>{desc}</p><a href="{slug}.html" target="_blank">全屏查看 ↗</a></div></article>' for slug,label,desc in choices)
(OUT/'index.html').write_text('''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Agents 课程 · 深色科技风格</title><style>*{box-sizing:border-box}body{margin:0;background:#0b101b;color:#e8edf6;font-family:'Microsoft YaHei',sans-serif}main{max-width:1500px;margin:auto;padding:48px 36px 70px}header{margin-bottom:32px}header small{color:#71dbef;letter-spacing:3px}h1{font-size:38px;margin:18px 0}p{color:#a4b0c2;line-height:1.9}section{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}article{border:1px solid #2a3447;background:#121a29;border-radius:12px;overflow:hidden}iframe{display:block;width:100%;aspect-ratio:16/9;border:0}article>div{padding:24px}h2{font-size:24px;margin:0}article p{min-height:92px}a{color:#76dcef;text-decoration:none;border-bottom:1px solid;padding-bottom:5px}footer{margin-top:32px;color:#8998ad;font-size:14px;line-height:1.8}@media(max-width:1000px){section{grid-template-columns:1fr}main{padding:30px 20px}article p{min-height:0}}</style></head><body><main><header><small>AGENTS / 深色科技系列</small><h1>让技术原理，在深色画布上展开。</h1><p>三种候选均使用第三课「前向传播」的真实内容。点击下方链接查看完整画面。<br>科技感优先选 A，演示冲击力优先选 B，长时间授课选 C。</p></header><section>'''+cards+'''</section><footer>当前为风格封面预览，原有 5 套、79 页演示稿未改动。<br>选定后将统一处理标题、图表、配图与页码，并保留讲者备注。</footer></main></body></html>''',encoding='utf-8')
print(json.dumps({'directory':str(OUT),'previews':[x[0] for x in choices],'slides_per_preview':1,'placeholder_check':'passed'},ensure_ascii=True))
