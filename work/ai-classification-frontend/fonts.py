from pathlib import Path
import json,urllib.request,urllib.parse,re,base64
W=Path(__file__).parent
c=json.loads((W.parent/'ai-classification/content.json').read_text(encoding='utf-8'))
text=json.dumps(c,ensure_ascii=False)+''.join(chr(x) for x in range(32,127))+'目录全屏退出编辑保存备注上一页下一页关闭搜索跳转课程导览核心要点回顾完整版正文讲解帮助浏览器自动离线比例页面缩放按键演讲者笔记含全部详细讲解无远程请求开始学习训练反馈环境行动策略比较路径嵌套概念边界条件'
text+=''.join((W/name).read_text(encoding='utf-8') for name in ['build.py','deck.js','deck.css'])
chars=''.join(sorted(set(text)-set('\n\r\t')))
parts=[]
for family,weights in [('Noto Sans SC','400;700')]:
 for start in range(0,len(chars),150):
  chunk=chars[start:start+150]
  url='https://fonts.googleapis.com/css2?family='+urllib.parse.quote(family)+':wght@'+weights+'&text='+urllib.parse.quote(chunk)
  css=urllib.request.urlopen(url,timeout=60).read().decode()
  def inline(m):
   data=urllib.request.urlopen(m.group(1),timeout=60).read()
   return 'url(data:font/ttf;base64,'+base64.b64encode(data).decode()+')'
  css=re.sub(r'url\((https[^)]+)\)',inline,css)
  css=css.replace('}', 'unicode-range:'+','.join('U+%X'%ord(x) for x in chunk)+';}')
  parts.append(css)
 (W/(family.replace(' ','-')+'.css')).write_text(''.join(parts),encoding='utf-8')
 parts=[]
print('Embedded font CSS ready;',len(chars),'unique characters')
