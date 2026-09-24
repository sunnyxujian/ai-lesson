from pathlib import Path
import urllib.request, urllib.parse, re, base64

ROOT=Path(__file__).resolve().parents[2]
WORK=Path(__file__).parent
SKILL=Path('C:/Users/micro/.codex/skills/frontend-slides')
OUT=ROOT/'.frontend-slides/slide-previews'
OUT.mkdir(parents=True,exist_ok=True)
TEXT='AI的分类Agents底层逻辑从哲学流派到工程实现人工智能要解决的问题实现方法符号主义连接主义行为主义机器学习神经网络深度学习渡一前端公开大师课理解概念之间的关系学习准备与抽象层级01/02/03abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 →·'
def font(family,weights):
    url='https://fonts.googleapis.com/css2?family='+urllib.parse.quote(family)+':wght@'+weights+'&text='+urllib.parse.quote(TEXT)
    css=urllib.request.urlopen(url).read().decode()
    def inline(m):
        data=urllib.request.urlopen(m.group(1)).read()
        return 'url(data:font/ttf;base64,'+base64.b64encode(data).decode()+')'
    return re.sub(r'url\((https[^)]+)\)',inline,css)
fonts=font('Noto Sans SC','400;700;900')+font('Noto Serif SC','600;700')+font('Barlow','900')
(WORK/'preview-fonts.css').write_text(fonts,encoding='utf-8')
base=(SKILL/'viewport-base.css').read_text(encoding='utf-8')
common='''*{box-sizing:border-box}body{font-family:'Noto Sans SC';color:var(--fg)}.slide{padding:88px 100px}.eyebrow{font-size:26px;letter-spacing:3px}.foot{position:absolute;bottom:62px;left:100px;right:100px;display:flex;justify-content:space-between;font-size:22px}.line{height:2px;background:currentColor;opacity:.3;margin:30px 0}h1,p{margin:0}h1{line-height:1.18}.intro{font-size:34px;line-height:1.75}.enter{animation:enter .8s both}@keyframes enter{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}'''
variants={
'a':(''' :root{--stage-bg:#e8e5df;--slide-bg:#faf9f7;--fg:#24231f;--accent:#b52f27}.slide:after{content:'';position:absolute;left:70px;top:80px;bottom:78px;width:5px;background:var(--accent)}h1{font:700 154px/1.25 'Noto Serif SC';letter-spacing:-3px;margin:130px 0 38px}.columns{position:absolute;top:290px;right:110px;width:545px}.row{border-top:1px solid #bab7af;padding:34px 0;font-size:38px}.row span{font-family:'Noto Serif SC';color:var(--accent);font-size:28px;margin-right:30px}.label{color:var(--accent)}''',
'''<div class="eyebrow label">AGENTS / 底层逻辑</div><div class="enter"><h1>AI 的分类</h1><p class="intro">从哲学流派到工程实现<br>理解概念之间的关系</p></div><div class="columns enter" style="animation-delay:.15s"><div class="row"><span>01</span>哲学流派</div><div class="row"><span>02</span>要解决的问题</div><div class="row"><span>03</span>实现方法</div></div>'''),
'b':(''' :root{--stage-bg:#111;--slide-bg:#111;--fg:#f0ece5;--accent:#e85d26}.eyebrow{border-bottom:1px solid #505048;padding-bottom:26px}h1{font-size:174px;font-weight:900;letter-spacing:0;margin-top:45px}.latin{font:900 290px/.95 'Barlow';color:var(--accent);margin-left:-8px}.right{position:absolute;left:1050px;right:100px;top:228px;border-left:1px solid #505048;padding-left:76px}.right p{font-size:60px;line-height:1.6}.tag{margin-top:90px;font-size:28px;color:#e85d26}.foot{border-top:1px solid #505048;padding-top:22px}''',
'''<div class="eyebrow">AGENTS / 底层逻辑</div><div class="enter"><div class="latin">ai</div><h1>的分类</h1></div><div class="right enter" style="animation-delay:.15s"><p>哲学流派<br>要解决的问题<br>实现方法</p><div class="tag">理解概念之间的关系</div></div>'''),
'c':(''' :root{--stage-bg:#0b2926;--slide-bg:#103d35;--fg:#eceddb;--accent:#c4ed83}.slide{background-image:linear-gradient(#ffffff08 1px,transparent 1px),linear-gradient(90deg,#ffffff08 1px,transparent 1px);background-size:48px 48px}.eyebrow{color:var(--accent)}h1{font-size:152px;font-weight:700;margin-top:120px}.intro{margin-top:50px;color:#c6d6c8}.map{position:absolute;top:230px;left:1110px;width:700px}.root{font-size:42px;color:#c4ed83;border:2px solid #c4ed83;padding:26px 34px;width:320px}.branch{border-left:2px solid #a9c2b9;margin-left:65px;padding:35px 0 5px 65px}.node{font-size:36px;position:relative;margin:0 0 48px}.node:before{position:absolute;content:'';height:2px;width:48px;background:#a9c2b9;left:-65px;top:29px}.node small{display:block;font-size:23px;margin-top:10px;color:#a9c2b9}.foot{color:#a9c2b9}''',
'''<div class="eyebrow">AGENTS / 底层逻辑</div><div class="enter"><h1>AI 的分类</h1><p class="intro">从哲学流派到工程实现<br>理解概念之间的关系</p></div><div class="map enter" style="animation-delay:.15s"><div class="root">人工智能</div><div class="branch"><div class="node">哲学流派<small>符号主义 · 连接主义 · 行为主义</small></div><div class="node">要解决的问题</div><div class="node">实现方法<small>机器学习 → 神经网络 → 深度学习</small></div></div></div>''')}
for key,(css,body) in variants.items():
    html='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 的分类</title><style>'+fonts+base+common+css+'</style><body><div class="deck-viewport"><main class="deck-stage" id="deckStage"><section class="slide active">'+body+'<footer class="foot"><span>渡一前端公开大师课</span><span>AI 的分类 / 01</span></footer></section></main></div><script>function fit(){const s=Math.min(innerWidth/1920,innerHeight/1080);deckStage.style.transform=`translate(${(innerWidth-1920*s)/2}px,${(innerHeight-1080*s)/2}px) scale(${s})`}addEventListener("resize",fit);fit()</script></body></html>'
    (OUT/f'style-{key}.html').write_text(html,encoding='utf-8')
print(OUT)
