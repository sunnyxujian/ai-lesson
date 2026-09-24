from pathlib import Path
import sys,base64
root=Path(__file__).resolve().parents[1]
out=root/'.frontend-slides/slide-previews';out.mkdir(parents=True,exist_ok=True)
base=Path('C:/Users/micro/.codex/skills/frontend-slides/viewport-base.css').read_text(encoding='utf-8')
common='*{box-sizing:border-box}.slide{padding:88px 108px}h1{font-size:110px;line-height:1.4;margin:120px 0 40px;font-family:"Noto Serif SC",serif}p{font-size:36px;line-height:1.8}body{font-family:"Noto Sans SC",sans-serif}.label{font-size:25px;letter-spacing:3px}.foot{position:absolute;bottom:80px;font-size:25px} .line{width:160px;height:7px;margin-top:50px;background:currentColor}'
styles=[('a',':root{--slide-bg:#faf9f7;--stage-bg:#242424}.slide{color:#24221f}.label,.line{color:#b22d3f}','认识模型服务接口','从自然语言，到模型计算，再回到自然语言。'),('b',':root{--slide-bg:#2e4a2a;--stage-bg:#243a21}.slide{color:#efe7d4}.label{border-bottom:2px solid #efe7d4;padding-bottom:30px}h1{color:#e89cb1;font-weight:500;font-size:128px;margin-top:135px}.line{display:none}','认识模型<br>服务接口','MODEL SERVICE / API'),('c',':root{--slide-bg:#082d32;--stage-bg:#061e22}.slide{color:#f3eddc;background-image:linear-gradient(#b8d1c51a 1px,transparent 1px),linear-gradient(90deg,#b8d1c51a 1px,transparent 1px);background-size:72px 72px}.label,.line{color:#b9e27b}h1{font-family:"Noto Sans SC",sans-serif}.foot{border:2px solid #b9e27b;padding:25px 40px}','认识模型服务接口','预处理 → 自回归生成 → 后处理')]
for k,css,title,sub in styles:
 s='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>认识模型服务接口</title><style>'+base+common+css+'</style><div class="deck-viewport"><main class="deck-stage" id="stage"><section class="slide active visible"><div class="label">AI 基础 · 第三课</div><div class="line"></div><h1>'+title+'</h1><p>'+sub+'</p><div class="foot">从 Raw Model 到 Model Service</div></section></main></div><script>function fit(){let s=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform=`translate(${(innerWidth-1920*s)/2}px,${(innerHeight-1080*s)/2}px) scale(${s})`}onresize=fit;fit()</script></html>'
 (out/f'style-{k}.html').write_text(s,encoding='utf-8')
print(out)
