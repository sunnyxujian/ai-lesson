"""Manually reviewed corrections. No automatic matching or duplicate deletion."""
from pathlib import Path
import json,re,runpy
root=Path(__file__).resolve().parents[1];p=root/'outputs/video-notes/4.AI-本质'
notes=runpy.run_path(str(root/'work/ai-essence-notes.py'))['notes']
raw=json.loads((p/'work/video-use/transcripts/4.AI-本质.json').read_text(encoding='utf-8'))['words']
t=[w['text'] for w in raw]
# At every overlap, the local audio join was re-recognized and read. Keep the
# complete later rendition, remove only the explicit earlier context duplicate.
cuts={1:'这节课的内容它就。',2:'啊，它是这么一个关系。然后在讲之前。',3:'有很多概念呢，它可能今天在。',4:'好，你看OpenAI的接口。',5:'你在开发ai。',6:'你少做的，我就必须。',7:'能懂的意思。',8:'比方说哈。',9:'都要经过很。',10:'都是至少啊，我嫂子说的。',11:'我都不是说说。',12:'说去微调呢。',13:'然后去做一个。',14:'啊，讲到这，我就顺便多。',15:'但是，他给你提供。',16:'然后下。',17:'同学们可以来了解一下咱们。',18:'找咱们的方式啊。',19:'你不认识那些概念。',20:'你要说什么？',21:'好，那么我们这。',22:'这东西太多了，新的概念层出不穷。',23:'你只要掌握好。',24:'一，输入。',25:'由于模型呢。',26:'所以说，处理的是。',27:'AI应用考虑是什么？我这里给模型。',28:'然后后续呢？',29:'玩的是啥？玩的就是。',30:'所以说，我知道了吧为什么。',31:'你就可以把它搞不清。',32:'将来朋友们遇到其他。',33:'那么模。',34:'那我这里简单一点啊，我在这里呢去加。',35:'你给他提要求啊，让他帮你写一些。',36:'咱们把启动先看一下吧，好，这里运行啊。',37:'然后这里呢，就是。',38:'好，那你看这边，我这个代理服务器。',39:'就是让你的A I口井工具调用模型服。',40:'那我这里就以这个。',41:'你经常的问。',42:'好，然后。',43:'你可以看到Cloud。',44:'都要经过这个。',45:'然后呢，给他传递的。',46:'呃，然后呢，有一些参数怎么去传递，它就在描述这个。',47:'但是我明明用的是。',48:'你看这一段。',49:'它这里边说，首先告诉了。',50:'至于说怎么去使用。”',51:'再回过头来想看一下，我们玩的那个。',52:'好，咱们就使用这个语句啊，走。',53:'现在首先问。',54:'好，你看一下这里啊，在这里，这是AI的响应。',55:'之前是不是看过的，见过某一种格式。',56:'刚才那个日志里边，最开始的时候，是不是告诉他我有哪些工具？其。',57:'来看一下这个流程啊，用户。”',58:'好，模型这。',59:'如果说要使用技能，要决定使用。',60:'他会进一步。',61:'然后到。',62:'会把技能。',63:'这里是模型输出。',64:'但我再次重申啊，我讲的是skill嘛，不是我后面讲的。',65:'因为说来说去，整个模型到现在。',66:'如果说你听到现在还需要去解释一个一个的概念的话，那真的是想多了。',67:'不然的话你就容易陷入到知识的海洋里。',68:'因为我全部发出来了。',69:'我去开发一个效能工具，提升你的效率，降低整个团队的成。'}
# Fix the confirmed fabricated tail before handling the 24/25 overlap.
t[23]=t[23].split('<|endoftext|>')[0]
for k,s in cuts.items():
 assert t[k-1].endswith(s),(k,s,t[k-1][-100:])
 t[k-1]=t[k-1][:-len(s)]
starts={2:('该存在一天，这里头的内容它就会','这节课的内容就会'),4:('很多概念呢','有很多概念呢'),5:('的一个接口啊，好，','好，'),6:('T和T O是吧？',''),7:('我就可以少做一点，',''),8:('这两层的变动，',''),9:('面上就划不来。',''),10:('参数给它改了啊，',''),11:('是至少啊，我少的说的，','这是至少，我往少了说，'),12:('花了那么多成本，',''),13:('结果不稳定啊，',''),14:('刚给你提供的接口，',''),15:('A I应用开发啊，讲完之后，','讲到这，'),16:('提供这样的一个东西呢？但是它一提供','但是他提供了，'),17:('AI的相关概念，',''),18:('一个薪资的空间。',''),19:('去了解了解，',''),20:('没有什么区别，',''),21:('的程序，儿吧，对吧？',''),22:('来介绍一下，所以没事儿。',''),23:('东西太多了，','这东西太多了，'),24:('为什么这么重要了吧？',''),26:('过一串数学运算。',''),27:('一个东西啊，',''),29:('起传给模型，',''),30:('存对不对？',''),31:('也是一样的，',''),32:('需要做一件事儿，',''),33:('以为例哈，',''),34:('然后去拿到结果，是这意思吧？',''),35:('简单一点啊，','那我这里简单一点，'),36:('他提要求啊，','你给它提要求，'),38:('启动那个服务器的端口。',''),40:('构建工具调用模型服务的时候，','让你的 AI 编程工具调用模型服务的时候，'),41:('我后边会说。',''),42:('后边会说啊，',''),43:('啊，对，暴露吧。',''),44:('那一条日志了。',''),45:('填没填消息，',''),46:('一下这个模型通不通？',''),47:('怎么去传递？他就在描述这个。','还有参数怎么传递，它就在描述这个。'),48:('是模型回复的呀，',''),49:('它前面还有消息，',''),50:('他这里边说：“','它这里边说，'),51:('之后要去使用这个技能。',''),52:('看一下，','再回过头来看一下，'),53:('走，来看一下。','使用这个语句，来看一下。'),54:('是rev u u叉。',''),55:('这里啊，在这里，','看这里，'),56:('之前是不是看过的，','之前是不是看过，'),57:('就是告诉他：“我有哪些工具？','刚才日志最开始告诉模型有哪些工具。'),58:('流程啊，','来看一下流程。'),59:('就传给模型了。',''),60:('要使用技能，要决定使用技能。过后，','如果要使用技能，决定使用之后，'),61:('库什么消息？他会进一步','它会进一步'),62:('复制一下，然后到','然后到'),64:('再处理输出，','哪些在处理输出？'),65:('讲的是Skill吗？','但我再次重申，我讲的是 Skill 吗？'),66:('去整个模型，到现在几年了，','因为说来说去，整个模型到现在几年了，'),67:('一个一个的概念的话，那真的是想多了啊。','如果听到现在还需要逐个解释概念，那真的是想多了。'),68:('一陷入到知识的海洋里边，','不然容易陷入知识的海洋，'),69:('呃，付费课里边啦，',''),70:('提升你的效率，','我去开发一个效能工具，提升你的效率，')}
for k,(a,b) in starts.items():
 assert t[k-1].startswith(a),(k,a,t[k-1][:90])
 t[k-1]=b+t[k-1][len(a):]
fix={
'说说这节课':'所以这节课','A I':'AI','AI application':'AI Application','技术站':'技术栈','投控':'Token','G P T四':'GPT-4','GPT三点五':'GPT-3.5','三点五':'3.5','G P T':'GPT','微一些提示词':'喂一些提示词','主要是要要验证':'主要是要验证','AI构建':'AI Coding','R A G':'RAG','M C P':'MCP','m c p':'MCP','open ai':'OpenAI','api接口':'API 接口','ai应用':'AI 应用','lunch，啊，lunch，graph':'LangChain、LangGraph','D P agents':'DeepAgent','浪线':'LangChain','浪杠':'LangGraph','Cloud Code':'Claude Code','Cloud扣等':'Claude Code','clou code':'Claude Code','克隆code':'Claude Code','克劳克的':'Claude Code','cloud的':'Claude Code','克隆的':'Claude Code','Cloud M D五':'CLAUDE.md','Code X':'Codex','Open Code':'OpenCode','AI短句':'AI 短剧','OpenCL':'OpenClaw〔名称校读存疑〕','Open Cloud':'OpenClaw〔名称校读存疑〕','原来水不慌':'袁老师不慌','偷看的话':'Token 化','跟他问一些':'给它喂一些','反Token化':'反 Token 化','说说玩儿来玩儿的去':'所以玩来玩去','写意缓存':'协议缓存','答我你也上传':'大文件上传','那么OS':'那么 OAuth〔术语校读存疑〕','点点登录':'单点登录','我的是啥':'玩的是啥','我的就是':'玩的就是','表示클라우드的吧':'比如说 Claude Code 吧','A T P S':'HTTPS','Python Script':'proxy-server','N P M run demo':'npm run dev','先停了三千端口':'监听了 3000 端口','N五点example':'.env.example','N五文件':'.env 文件','N五这里边':'.env 这里边','N五':'.env','那个号只要三千':'localhost:3000','C C Switch':'CC Switch','Kimi Proxy':'Kimi-Proxy','我的技术都暴露了':'我的 Key 都暴露了','进入这个Cloud':'进入 Claude Code','这个Cloud':'这个 Claude Code','Cloud这个官方':'Claude 官方','请出的是':'请求的是','接生':'JSON','节省格式':'JSON 格式','节省':'JSON','T M模型':'Kimi 模型','doctor compose':'docker-compose','skill create':'skill-create','web design guidelines':'web-design-guidelines','可交互的可利用工具':'可交互的 CLI 工具','review邮箱':'review UX','收这个点赞':'搜这个 design','“web点赞”':'web-design','收一下这个点赞':'搜一下 design','ATTP':'HTTP','S S E':'SSE','Web Design Guide':'web-design-guidelines','web design guide':'web-design-guidelines','通过use':'tool_use','牛式':'流式','某些一起':'这些一起','we be t in guidelines':'web-design-guidelines','为提示词':'喂提示词','技术认讲完':'技术认知讲完','很会用这个工具，用着老火':'很多同学用这个工具用着恼火','每天到颠覆':'每天都要颠覆','将来朋友们':'将来同学们'}
for i,s in enumerate(t):
 for a,b in fix.items():s=s.replace(a,b)
 s=re.sub(r'([：，])，',r'\1',s).replace('啊。','。').replace('呃，','').replace('啊，','，')
 t[i]=s.strip(' ，')
# Exactly retained lecture order; short bridges attach to the neighboring scene.
ends=[2,7,12,16,19,21,25,28,32,36,39,43,46,51,54,57,60,64,67,70]
prev=0
for n,end in zip(notes,ends):
 n['body']='\n\n'.join(x for x in t[prev:end] if x)
 n['body']=n['body'].replace('你这里的这个权重矩阵呢，是比较基于','你这里的这个权重矩阵，是基于')
 prev=end
(p/'work/notes-data.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2),encoding='utf-8')
(p/'work/notes-review.json').write_text(json.dumps({'method':'Full transcript lightly corrected with explicit manually reviewed overlap edits; intentional repetition and promotional portions retained.','joins_reviewed':69,'extra_local_audio_checks':5,'removed_asr_artifact':{'cue':24,'evidence':['asr-artifact','join-24-25','two-questions'],'raw_preserved':True},'manual_overlap_edits':cuts,'manual_head_repairs':starts,'term_corrections':fix,'uncertain_terms':['OpenClaw: Qwen varies between OpenCL and Open Cloud; no legible name at this passage.','OAuth: re-recognition says OS; likely OAuth in context, explicitly marked.'],'word_level_human_listening':False},ensure_ascii=False,indent=2),encoding='utf-8')
print('Faithful text chars',sum(len(n['body']) for n in notes))
