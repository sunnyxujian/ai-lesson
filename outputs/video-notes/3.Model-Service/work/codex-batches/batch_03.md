# Video Notes Codex Batch

Inspect every referenced image and use the transcript as the factual source.
Write one file per scene to the notes directory. This is faithful light polish, not summarization or article rewriting.
Video mode: explainer. Preserve the scripted explanation in full. Prefer meaningful charts, animation states, interfaces, demonstrations, maps, or B-roll over a presenter face when choosing frames.
Visual strategies: document-evidence, screen-state.

Light-plus rules:
- Preserve the original speaking order, question-and-answer structure, reasoning path, examples, figures, caveats, disagreements, and repeated emphasis.
- Only fix ASR errors, punctuation, broken sentences, obvious stutters, and meaningless filler. Do not merge distant points or reorganize the argument.
- Keep first-person speech and dialogue. Do not convert it into third-person narration such as 'the host said' or 'the guest believes' unless those words are in the source.
- Apply the completed speaker map and timestamped turn overrides; otherwise keep '说话人N' for unresolved identities. Never guess gender or identity beyond the recorded evidence/confidence.
- Do not shorten for elegance. If the polished text loses substantive clauses from the transcript, it is wrong even when the summary is accurate.
- Do not add web facts or conclusions that the speakers did not state.

Visual explainer rules:
- State only useful visible facts: the named speaker when established, on-screen text, charts, interfaces, demonstrations, objects, and actions.
- For a plain talking-head frame, use one short factual caption. Do not invent emotion, intent, symbolism, or explain how the shot 'reinforces' the argument.
- The complete spoken content belongs in Light-plus; do not replace it with visual commentary.

Each file must use this exact shape:

## 标题
Short descriptive scene title; do not turn it into a synthesized thesis

## Light-plus
Near-verbatim corrected scene text following all rules above.

## Visual explainer
A concise factual description of useful visible information.

Notes directory: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes`

## Scene 13

Time: 00:17:00-00:19:05
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_013_00-18-46.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_013.md`

Transcript:
一个概率分布。好，那么接下来呢，我们要从这个概率分布里边，是不是要去选一个头啃？是不是要选头啃？那么选的话，我们可以理解为这里它封装了一个方法啊，叫做pick头啃，传入这么一个概率分布，然后传入一些配置，它就可以在这些东西中挑选出一个头啃，然后呢，把这个头啃呢就追加到输出里边。啊，这个输出，输出里边就会加入一个头啃，push头啃啊，当然前面还有。头啃，啊，当然在前面还要判断一下啊，呃，is over啊，这个头啃是不是一个结束的头啃？往往模型那边输出完了过后呢，它会有一个结束。当然，这个不同的模型可能结束的符号不一样啊，结束的头啃不一样。总之，它这里肯定会有一个判断。如果说是一个结束头啃的话，我们就break了；如果说没有结束的话，那么这个头啃就加入到输出里边。同时呢，在input里边也要加进去。我给他写完啊，写完你捋一下这个逻辑。这是模型的输出，加入到这个输出里边。然后呢，同时把模型的下一个头啃又加入到输入里边。然后呢，输入里边。加到输入里边，然后那个输入里边是不是多了一个？接下来进行下一次循环，哎，下一次循环再把那个输入传进去，又拿到下一个token，拿到下一个token过后又追加到输入里边，再下一次循环又追加进去。那么看上去有点像啥呢？比方说用户的问题是你是谁？好，传入是什么？传入是这个的token对吧？传进去的。那么他预测的下一个token呢？可能取出来是什么呢？取出来是我。好，就把这个我呢追加进去，又把这个玩意传进去，传到这里边，然后又拿到下一个token啊，是。又拿到下一个头坑，啊，是好，又把这个东西传进去，又去拿下一个头坑，懂那意思吧？他是这么玩的，直到模型那边输出结束，拿到一个结束头坑，那就over了。那么这一次交互就结束了。那么结束过后，那么这里面存的，就是不是，就是模型的输出，对不对？因为奥托子里面它只存了啥，只存了这一部分，能看懂吧？好好捋一下啊。如果说你这个大一把都看不懂的话，我觉得你现在还不适合去玩什么AI，先把这些东西先搞定吧。那你就是语言。这东西先搞定吧。那你就是语言基础这一块，都还有问题啊。复利课程看一看啊。好，这个整体结构就是自回归。什么叫自回归？你看呗。就是我们输入，然后追加，追加过后又来进行输入，输入过后得到下一个，又来追加，就是自回归。这个整体结构你理解过后呢，接下来我可以解释一个问题了哈。解释什么现象呢？就是解释为什么输入的头肯比较便宜一点，而输出的头肯比较贵一点。你就通过这个。

---

## Scene 14

Time: 00:19:05-00:20:51
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_014_00-19-48.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_014.md`

Transcript:
比较故意一点，你就通过这个代码，然后去推迪一下，你就知道为啥了。你想想为啥呢？想想，它输出越多，就是它结束的越晚，它输出的输出越多，就是O T P O里边，它东西越多，就意味着什么？假设O T P O里边有十个头肯，假设十个肯定是不止的啊，可不？可能几百个、上千个都有可能。那比方说吧，他得到了是一千个头肯，那个O T P O里边，就意味着他输出了一千次，对吧？输出一。千次，对吧？输出一千次的时候，它意味着啥呢？你看一下，它每一次输出是不是要把全量传进去啊？它每一次传的是一个token进去吗？不是，传的是一串儿，把之前的输入再追加上之前的输出，全部要传进去啊。所以它计算量比较大呀，也就意味着它耗费的算力是不是更多呀？你这里有一千次输出，就意味着这边要调用这个一千次，是吧？耗费的算力就越多，因此的输出它耗费的算力多，因此它的成本更高，它的token就越贵。它的头啃就越贵，而输入呢，其实没事儿，输入的话就一次嘛，就第一次，对吧？就是你输入传进消息，远分部都是传给模型，只有第一次，后续的都是要最佳输出的。简单来说，这套逻辑就意味着输出的头啃数量决定了它调用这个裸模型的次数，也就决定了它耗费的算力多少。所以说输出的头啃呢，往往比较贵。实际上呢，现在的模型提供商啊，它的收费都已经很温柔了，知道吧？我这么跟你说啊，我不敢说百分之百。我这么跟你说啊，我不敢说百分之百啊，其实我认为就是百分之百，都是亏着钱给你做的，一点儿不夸张。他们赚不到钱的。所以说这种模型啊，玩到后边一定是大鱼吃小鱼，小的模型股商耗不起的，那就被淘汰掉了。那么剩下的市场上里边就被那个一些大的公司、大的模型提供商给你占据了。就跟以前玩这个共享单车是一样的，先亏着钱做，先占据到市场再说，以后呢再慢慢把价格提高。其实最近好多新闻，你再看，是不是这个服务的价格都已经在往上涨了，大公司也不一定能撑得到多久啊，这太烧钱了。

---

## Scene 15

Time: 00:20:51-00:22:25
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_015_00-21-30.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_015.md`

Transcript:
得到多久啊？这太烧钱了。好，理解这个结构之后呢，我们再说一下这个地方，它是怎么来选择token的？因为它拿到了是一个概率分布，是吧？那么如何从这个token的概率分布里边去选一个token出来？啊，这里呢涉及到这个配置，这个配置是谁传递的呢？是用户传递的，用户传消息的时候呢，他会传一些配置进来，因为他调的是API嘛，对不对？呃，一般有哪些配置会影响到这一块呢？呃，主要是三个啊，了解一下啊，呃，一个是temperature，表示温度，一个是top k。Human Rights Watch is a non-profit organization dedicated to exposing and preventing human rights abuses in the Middle East and North Africa.一个是top K，一个是top T。好，其实你看一下个接口文档。呃，这个我们收一下啊。temperature。好，你看在这里啊，它有选项，它是个数字。呃，在OpenAI的接口里边，它是一个零到二的数字，表示温度。这个数字决定了啥呢？决定了它在一个token的概率分布当中，它的选择的随机性。这个值越小呢，它的随机性就越小；这个值越大呢，它的随机性就越大。比方说你加。性就越大。比方说，你刚传的是零，那它就没有随机性，就是完全确定的结果。你这个概率分布中，哪个概率最大？那我就选哪一个，它完全没有随机性。那如果说这一块传的是二，最大的，那就是完全随机了，可能不管概率了。哪怕一个投粉，它的概率只有百分之一，它也有可能会被选中。当然，它取中间值呢，你就是进行一下调节，是吧？能懂这个意思吧？都要乘以一。件，所以A I的随机。都要参数一起。说A I的随机性哪来的？是来自于这儿。实际上，某模型有没有随机性？某模型它没有随机性，至少理论上是没有的。这个是我们上节课讲清楚的啊。它一定要说有随机性的话，只来自于G P U的运算，它不满足结合律，就那一块有点随机性。从理论上来讲，这个函数本身是没有随机性的，它的下一个token的概率分布是确定的。它随机性来自于这个参数一起。哎，我把参数设置为零，是不是？呃，就可以拿到一个完全确定的结果呢？就是这样的。

---

## Scene 16

Time: 00:22:25-00:23:46
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_016_00-23-41.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_016.md`

Transcript:
全确定的结果呢，就是这样的。那有同学说：“那不挺好吗？我把参数设为零，就可以拿到一个确定性的结果。”现在AI的主要问题不就是它有不确定性嘛，对吧？我就直接把设为零，那不就可以确定了吗？呃，也不能这样想，它确定倒是确定了，它有可能是确定的，是错误结果，它就一错到底了，可能会陷入死循环，它输出的结果就一定是错的。你怎么办呢？所以说还是要稍微给点随机性啊。一般来说呢，就是你写代码呀、写程序之类的，或者是做一些科研这么一个场景里边的，就参数一下呢，尽量写小一点啊，什么零点一啊。尽量写小一点啊，什么零点一啊、零点二啊之类的，或者是写零也行啊。如果他说错了，不妨呢用提示词提示他嘛，对不对？你只要这个音谱扯一遍，是不是他就那个下一个投坑的概率分布就不一样了，对吧？呃，如果说你是做一些创意类的呢，比方说像那个写文章啊、写小说啊，可能要有一些天马行空的一些想法的，那就把这个temperature调一些高一点，比方说一以上也是可以的。如果说一些普通的问题的话，就把设置为零点七左右啊，这是一类的一个共识。当然这个东西呢还要看模型，像这个玩意儿的话。还要看模型，像这个玩意儿的话，不同的模型提供，是很可能你要去慢慢去测，测到哪个统计学合适就OK。如果说你不做了那种非常精细化的处理的话，也没有必要去测它，就普通的一些应用的话，没必要去测它，就摸针就完事儿了啊。模型服务商那边还会有一个摸针值。好，这是第一个啊，统计学，就是它的作用啊，它是在一、二的概率分布当中，如何来进行选择，它的随机性如何。好，下一个，下一个呢是top K啊，top K和top P呢，这两个呢，作用都差不多。

---

## Scene 17

Time: 00:23:46-00:24:56
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_017_00-24-46.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_017.md`

Transcript:
呃，这两个呢，作用都差不多啊，但是呢，它有些细节上的差别。这两个的含义是什么呢？就是在这个概率分布中截断。比如说，这个概率分布中有一百个token，每个token对应一个概率嘛，对吧？那么top K和这个top P，就是我在这一百个里边先进行挑选，我不要那么多，我可能只挑选五个或者是十个。挑选完了过后，再用那个T M P R I小进行来随机选择，懂的意思吧？随机选择，懂的意思吧？就这两个作用，很好理解吧？只是它挑选的规则不一样。然后这个TOP K，咱们看一下啊，搜一下TOP K。哎，呃，现在这个Open AI里边好像就没有这个TOP K了啊，它现在只有TOP P了啊。来，让我都讲一讲吧。我先讲一下这个TOP K，这个TOP K呢，是指的是取数量，比方说这里有一百个头肯啊，就下个头肯有一百种情况，每种头肯呢，它有。有100种情况，每种头坑呢，它有不同的概率。TOP K的意思呢，我就是说我按照概率从高到低排序，我取多少个。比如我这里传一个十，那就表示说我只取概率前十的头坑，在这些头坑里边，再使用TOP K一下啊，来进行随机选择。那么排名十以后的头坑就是绝对不可能出现在结果里边，啊，是TOP K的做法。而TOP P呢，指的是按概率来选择啊，它叫做和采样。比方说这个。

---

## Scene 18

Time: 00:24:56-00:25:49
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_018_00-25-41.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_018.md`

Transcript:
做核采样，比方说这个概率呢是百分之八十啊，那就写的是零点八。那“十”呢是什么意思呢？指的是我还是把那些概率啊，这些概率分布里面的token，按照概率从高到低进行排序，排序完了过后呢，我来进行累加。我加到百分之八十，我就不加了，懂意思吧？比方说它有这么一些token，呃，第一个token呢是一，它的概率呢是零点三，第二个token呢是二，它的概率呢是零点二五，第三个token呢是三。点二五，第三个投坑呢是三，那么概率呢是零点二，然后分别是零点一五、零点一啊，后面不写了啊。那么用这个和采样的方式呢，就是我一定要累加到百分之八十。那么就是说，零点三加零点二五、零点五五、零点七五，然后加到这儿是不是超过百分之八十了？好，那么就取这四个，懂我的意思吧？它是按照总体的概率来进行采样的。那么采样过了过后呢，再用这个统计学来进行随机选择，明白了吧？啊，也就是说这些。

---
