from pathlib import Path
import json,re,html,shutil
root=Path(__file__).resolve().parent.parent
base=Path('C:/Users/micro/.codex/skills/frontend-slides/viewport-base.css').read_text(encoding='utf-8')
manifest=json.loads((root/'work/scene-manifest.json').read_text(encoding='utf-8'))
title='4.Agents底层逻辑之梯度下降'
tutorial=root/'share'/f'{title}-visual-explainer.html'
text=tutorial.read_text(encoding='utf-8')
count=0
def anchor(m):
 global count
 count+=1
 return re.sub(r' id="[^"]*"','',m.group())[:-1]+f' id="scene-{count}">'
text=re.sub(r'<h2\b[^>]*>',anchor,text)
print_css='''<style id="local-print-refinement">
@page {size:A4;margin:17mm 16mm 17mm}
@media print {body{font-family:'Microsoft YaHei',sans-serif;font-size:10.5pt;line-height:1.6;padding:0;margin:0;} p{font-size:10.5pt;orphans:3;widows:3}h1{font-size:22pt;margin:0 0 12pt}h2{break-before:auto!important;break-after:avoid;font-size:15pt;line-height:1.35;margin-top:21pt;margin-bottom:10pt}h3{font-size:11pt;margin:10pt 0 4pt;break-after:avoid}img{max-height:82mm;width:100%;object-fit:contain;box-shadow:none;margin:9pt auto;break-inside:avoid}blockquote{font-size:9pt} }
</style>'''
text=text.replace('</head>',print_css+'</head>')
tutorial.write_text(text,encoding='utf-8')
cards=[
('先问：什么影响预测？','参数 = 全部权重 + 全部偏置','输入固定时，要改变结果，就要调整参数。','两万多个参数，交给计算机自动调整。'),
('用标签告诉它正确答案','图片是“1”，目标位置只亮一格','预测值来自网络计算；标签来自数据标注。','注意原口述最大值更正与画面数值不一致。'),
('把差距变成一个数字','损失函数 → 损失值','演示：逐项相减、平方、求和。','课件均方公式另含 1/m；两种约定要区分。'),
('输入和标签固定','参数 → 输出 → 损失','把复杂计算记为 y = C(参数)。','训练要寻找让损失减少的参数变化。'),
('不必先看清整条曲线','先求当前点的切线','局部斜率决定朝左还是朝右。','方向有了，步幅还需要另外控制。'),
('黑夜下山的比喻','沿当前最陡的下坡方向走','两个参数形成曲面上的两个坐标方向。','高维参数空间遵循同样的直观思路。'),
('谷底不一定是最低点','局部最优 ≠ 全局最优','不同初始位置可能落入不同凹谷。','课程提到：噪声可帮助摆脱某些较差位置。'),
('为什么每次只走一点？','学习率控制步幅','步子过大，可能跨过谷底跑到上坡。','继续计算新位置的方向，再走下一步。'),
('参数不会整齐划一地动','有的多变，有的少变','下降方向在 x、y 上的分量可以不同。','高维计算也要得到每个参数的变化信息。'),
('从输出层开始','0 − 0.64；1 − 0.18','一个希望减少 0.64，一个希望增加 0.82。','箭头方向与长短表示不同的调整期望。'),
('一个神经元的三个依赖','权重 · 偏置 · 上层激活','w₁…w₁₆ 和 b 是可调整的参数。','隐藏层输出 a₁…a₁₆ 也会影响当前输出。'),
('如何知道各项该怎么变？','偏导与链式法则','从笼统方向，变成每一项具体的数量。','先算出各项信息，再统一更新。'),
('上一层输出没有旋钮','把“期望”向前传','当前层能改自己的权重和偏置。','对上层输出的需求，交给上一层继续计算。'),
('多个箭头合成一个','对同一节点的期望相加','汇总后再计算本层参数与更前一层的需求。','传播到第一个隐藏层，原始输入保持固定。'),
('一次更新只是一步','前向 → 反向 → 更新 → 重复','参数调整可组织成矩阵，结合学习率更新。','界面是教学示意，不是数值收敛实验。'),
('学习与训练的含义','反复计算，逐步调整参数','目标是使损失变小，得到较好的状态。','不保证最完美；下一课继续讨论实施问题。')]
def esc(s):return html.escape(s)
sections=['''<section class="slide active visible cover"><div class="eyebrow">AGENTS / 神经网络 · 第四课</div><h1 contenteditable="false">梯度下降</h1><p class="cover-sub">从“哪里错了”，到“参数怎样调整”。</p><div class="path"><span>预测</span><b>→</b><span>损失</span><b>→</b><span>梯度</span><b>→</b><span>更新</span></div><p class="cover-foot">用曲线、山谷和神经元箭头，理解反向传播。</p><aside class="speaker-notes">本课沿原讲解顺序：先以手写数字说明预测、标签和损失；再用单参数曲线与双参数曲面解释下降方向、局部最优及学习率；最后用输出层和隐藏层的箭头解释反向传播、偏导、链式法则以及训练循环。全部细节和源画面核对说明在完整教程。按 N 查看每页详细讲稿，方向键翻页，E 编辑，Ctrl+S 保存。</aside></section>''']
for i,(card,scene) in enumerate(zip(cards,manifest['scenes']),1):
 note=(root/f'work/codex-notes/scene_{i:03d}.md').read_text(encoding='utf-8')
 body=note.split('## Light-plus\n')[1].split('\n## Visual explainer')[0].strip()
 caption=note.split('## Visual explainer\n')[1].strip()
 sections.append(f'''<!-- === TEACHING POINT {i} === -->
<section class="slide"><div class="eyebrow">第四课 / {i:02d}</div><div class="copy reveal"><h2>{esc(card[0])}</h2><p class="thesis">{esc(card[1])}</p><ul><li>{esc(card[2])}</li><li>{esc(card[3])}</li></ul><a class="tutorial" href="../share/{title}-visual-explainer.html#scene-{i}" target="_blank">阅读本节完整教程 ↗</a></div><figure class="reveal"><img src="../share/keyframes/{Path(scene['frame_path']).name}" alt="{esc(card[0])} 的源画面"><figcaption>{esc(card[1])}</figcaption></figure><span class="big-number">{i:02d}</span><aside class="speaker-notes">{esc(body)}\n\n【画面与复核】\n{esc(caption)}</aside></section>''')
css='''
/* === PAPER AND GRAPH THEME === */
:root{--slide-bg:#f6f3e9;--stage-bg:#171d1b;--ink:#162b2d;--accent:#bc492d}*{box-sizing:border-box}body{font-family:'Noto Sans SC',sans-serif;color:var(--ink)}.slide{background-image:linear-gradient(rgba(32,70,67,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(32,70,67,.035) 1px,transparent 1px);background-size:48px 48px;padding:80px 96px}.eyebrow{font-size:26px;letter-spacing:4px;font-weight:700;border-top:3px solid var(--ink);padding-top:22px}.copy{position:absolute;left:96px;top:212px;width:640px}h2{font-family:'Noto Serif SC',serif;font-weight:700;font-size:60px;line-height:1.3;margin:0 0 40px}p.thesis{font-size:36px;font-weight:700;color:var(--accent);line-height:1.5;margin:0 0 35px}ul{padding-left:28px;margin:0;font-size:28px;line-height:1.8}li+li{margin-top:22px}.tutorial{display:inline-block;margin-top:38px;color:var(--ink);font-size:24px;text-underline-offset:8px}figure{position:absolute;left:800px;top:246px;width:1010px;margin:0}figure img{width:1010px;height:569px;object-fit:contain;background:#fff;border:2px solid #d5dace;box-shadow:12px 12px 0 #dddccf}figcaption{margin-top:24px;font-size:25px;color:#506366}.big-number{position:absolute;bottom:30px;left:92px;font-family:Georgia,serif;font-size:150px;opacity:.07;line-height:1}.cover h1{font-family:'Noto Serif SC',serif;font-size:158px;margin:108px 0 30px}.cover-sub{font-size:42px}.path{display:flex;gap:32px;align-items:center;margin-top:92px;font-size:48px}.path span{border-bottom:5px solid var(--accent);padding-bottom:22px}.path b{font-weight:400;color:#78928c}.cover-foot{font-size:27px;margin-top:85px}.reveal{transform:translateY(20px);opacity:0;transition:transform .45s,opacity .45s}.visible .reveal{transform:none;opacity:1}.speaker-notes{display:none}.deck-controls{color:#fff;background:#172522ed;border:1px solid #68726d;border-radius:8px;padding:8px 14px;font-size:14px;display:flex;gap:15px;align-items:center}button{cursor:pointer;border:0;background:#edf0e8;color:#18312e;border-radius:4px;padding:8px 13px}.notes-panel{position:fixed;z-index:2000;inset:8% 8%;background:#f6f3e9;color:#173235;padding:28px 40px;overflow:auto;white-space:pre-wrap;font-size:20px;line-height:1.8;display:none;box-shadow:0 10px 80px #0009}.notes-panel.open{display:block}.edit-hotzone{position:fixed;left:0;top:0;width:80px;height:80px;z-index:2500}.edit-toggle{position:fixed;left:12px;top:12px;z-index:2600;opacity:0;pointer-events:none}.edit-toggle.show,.edit-toggle.active{opacity:1;pointer-events:auto}[contenteditable=true]{outline:2px dashed #bf5238;outline-offset:5px}@media print{.notes-panel,.edit-hotzone,.edit-toggle{display:none!important}} 
'''
js=r'''
/* === FIXED STAGE AND NAVIGATION === */
class SlidePresentation{constructor(){this.slides=[...document.querySelectorAll('.slide')];this.index=0;this.stage=document.getElementById('deckStage');this.editing=false;this.notes=document.getElementById('notes');this.scale=()=>{let s=Math.min(innerWidth/1920,innerHeight/1080);this.stage.style.transform=`translate(${(innerWidth-1920*s)/2}px,${(innerHeight-1080*s)/2}px) scale(${s})`};addEventListener('resize',this.scale);this.scale();this.show(0);document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key==='s'){e.preventDefault();this.save();return}if(e.target.isContentEditable)return;if(e.key.toLowerCase()==='e'){this.edit();return}if(e.key.toLowerCase()==='n'){this.toggleNotes();return}if(e.key==='Escape'){this.notes.classList.remove('open');return}if(['ArrowRight','ArrowDown',' ','PageDown'].includes(e.key)){e.preventDefault();this.show(this.index+1)}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();this.show(this.index-1)}});let start=0;document.addEventListener('touchstart',e=>start=e.touches[0].clientX,{passive:true});document.addEventListener('touchend',e=>{let d=e.changedTouches[0].clientX-start;if(Math.abs(d)>45&&!this.editing)this.show(this.index+(d<0?1:-1))},{passive:true});let last=0;document.addEventListener('wheel',e=>{if(this.notes.classList.contains('open')||this.editing)return;let now=Date.now();if(now-last>500&&Math.abs(e.deltaY)>20){this.show(this.index+(e.deltaY>0?1:-1));last=now}},{passive:true});document.getElementById('prev').onclick=()=>this.show(this.index-1);document.getElementById('next').onclick=()=>this.show(this.index+1);document.getElementById('noteButton').onclick=()=>this.toggleNotes();document.getElementById('editToggle').onclick=()=>this.edit();const hot=document.querySelector('.edit-hotzone'),btn=document.getElementById('editToggle');let timer;[hot,btn].forEach(el=>{el.onmouseenter=()=>{clearTimeout(timer);btn.classList.add('show')};el.onmouseleave=()=>timer=setTimeout(()=>{if(!this.editing)btn.classList.remove('show')},400)});hot.onclick=()=>this.edit();this.slides.forEach((s,i)=>s.querySelectorAll('h1,h2,p,li').forEach((n,j)=>{n.dataset.editId=i+'-'+j;let value=localStorage.getItem('gradient-lesson-'+n.dataset.editId);if(value!==null)n.textContent=value;n.addEventListener('input',()=>localStorage.setItem('gradient-lesson-'+n.dataset.editId,n.textContent))}))}show(i){this.index=Math.max(0,Math.min(i,this.slides.length-1));this.slides.forEach((s,j)=>{s.classList.toggle('active',j===this.index);s.classList.toggle('visible',j===this.index)});document.getElementById('counter').textContent=(this.index+1)+' / '+this.slides.length;this.notes.textContent=this.slides[this.index].querySelector('.speaker-notes').textContent}toggleNotes(){this.notes.classList.toggle('open')}edit(){this.editing=!this.editing;document.getElementById('editToggle').classList.toggle('active',this.editing);this.slides.forEach(s=>s.querySelectorAll('h1,h2,p,li').forEach(n=>n.contentEditable=this.editing))}save(){let blob=new Blob(['<!doctype html>\n'+document.documentElement.outerHTML],{type:'text/html;charset=utf-8'});let a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='gradient-descent-slides.html';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),2000)}}window.deck=new SlidePresentation();
'''
out=root/'slides';out.mkdir(exist_ok=True)
page='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>梯度下降 · 第四课</title><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&family=Noto+Serif+SC:wght@700&display=swap" rel="stylesheet"><style>'+base+css+'</style></head><body><div class="deck-viewport"><main class="deck-stage" id="deckStage">'+''.join(sections)+'</main></div><nav class="deck-controls"><button id="prev">←</button><span id="counter"></span><button id="next">→</button><button id="noteButton">讲稿 N</button><span>E 编辑 · Ctrl+S 保存</span></nav><div class="notes-panel" id="notes" aria-label="详细讲稿"></div><div class="edit-hotzone"></div><button class="edit-toggle" id="editToggle">编辑 E</button><script>'+js+'</script></body></html>'
(out/'index.html').write_text(page,encoding='utf-8')
shutil.copy2(root/'work/transcription-corrections.md',root/'share/source-materials/transcription-corrections.md')
shutil.copy2(root/'work/token-usage.json',root/'share/source-materials/token-usage.json')
(out/'README.md').write_text('17页重点讲解幻灯片。方向键/空格/滚轮/滑动翻页，N显示完整讲稿，E启用文字编辑，Ctrl+S保存。每页有完整教程对应章节链接。字体通过Google Fonts加载；断网时使用浏览器替代字体。图片来自同包share/keyframes。\n',encoding='utf-8')
print('Deck 17 slides; PDF print CSS refined')
