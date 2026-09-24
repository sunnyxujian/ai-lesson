from pathlib import Path
import sys,base64
root=Path(__file__).resolve().parents[1]
out=root/'outputs/video-notes/4.AI-本质/verify/style-previews';out.mkdir(parents=True,exist_ok=True)
base=Path('C:/Users/micro/.codex/skills/frontend-slides/viewport-base.css').read_text(encoding='utf-8')
common='*{box-sizing:border-box}.slide{padding:88px 108px}h1{font-size:110px;line-height:1.4;margin:120px 0 40px;font-family:"Noto Serif SC",serif}p{font-size:36px;line-height:1.8}body{font-family:"Noto Sans SC",sans-serif}.label{font-size:25px;letter-spacing:3px}.foot{position:absolute;bottom:80px;font-size:25px} .line{width:160px;height:7px;margin-top:50px;background:currentColor}'
styles=[('a',':root{--slide-bg:#faf9f7;--stage-bg:#242424}.slide{color:#24221f}.label,.line{color:#b22d3f}','AI 的本质','从模型到应用，透过输入与输出理解 AI。'),('b',':root{--slide-bg:#1c1c1c;--stage-bg:#1c1c1c}.slide{color:#f5d200}.label{border-bottom:2px solid #f5d200;padding-bottom:30px}h1{color:#f5d200;font-weight:900;font-size:156px;margin-top:135px}.line{display:none}','AI 的<br>本质','AI / UNDER THE HOOD'),('c',':root{--slide-bg:#082d32;--stage-bg:#061e22}.slide{color:#f3eddc;background-image:linear-gradient(#b8d1c51a 1px,transparent 1px),linear-gradient(90deg,#b8d1c51a 1px,transparent 1px);background-size:72px 72px}.label,.line{color:#b9e27b}h1{font-family:"Noto Sans SC",sans-serif}.foot{border:2px solid #b9e27b;padding:25px 40px}','AI 的本质','模型 → 服务 → 应用')]
for k,css,title,sub in styles:
 s='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI 的本质</title><style>'+base+common+css+'</style><div class="deck-viewport"><main class="deck-stage" id="stage"><section class="slide active visible"><div class="label">AI 基础 · 第四课</div><div class="line"></div><h1>'+title+'</h1><p>'+sub+'</p><div class="foot">模型 · 服务 · 工具 · 应用</div></section></main></div><script>function fit(){let s=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform=`translate(${(innerWidth-1920*s)/2}px,${(innerHeight-1080*s)/2}px) scale(${s})`}onresize=fit;fit()</script></html>'
 (out/f'style-{k}.html').write_text(s,encoding='utf-8')
print(out)
