# Video Notes Codex Batch

Inspect every referenced image and use the transcript as the factual source.
Write one file per scene to the notes directory. This is faithful light polish, not summarization or article rewriting.
Video mode: explainer. Preserve the scripted explanation in full. Prefer meaningful charts, animation states, interfaces, demonstrations, maps, or B-roll over a presenter face when choosing frames.
Visual strategies: evidence, screen-state.

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

Notes directory: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes`

## Scene 1

Time: 00:00:00-00:01:11
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_001_00-01-04.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_001.md`

Transcript:
他知不知道什么叫自然语言？他知不知道你说的话什么意思？他知不知道什么叫中文？什么叫英文？他知不知道？你看他的输入输出就完事了，他输出的是个啥？啊，这是个啥？这是中文吗？这是英文吗？这是图片吗？这是视频吗？这是啥？好，各位同学，咱们今天聊的是裸Model啊，我把它翻译成为裸模型。裸模型呢是整个AI技术体系的最底层，就是你无论你。体系的最底层，就是你无论你用什么样的AI技术，最终你都是用的它裸模型。其实有些资料里边呢，用的是另外一个词，叫做基础模型，或者是把这个裸model呢把它翻译成原始模型啊。其实无所谓的，就是我把它翻译成裸模型呢，就是告诉同学们这一块呢，它是剥离了任何花里胡哨的功能，看到AI最本质的真相，就这个东西。而且这一块的技术啊，它的原理上。啊，它的原理上，或者说它的知识体系上是非常稳定的。从那个二零二三年g p t三点五出来到现在，它就没变过，一直是这么一套技术体系。这个模型到底是啥呢？你简单的理解啊，它就是一个函数，它接收一个输入，产生一个输出。输入和输出，输入是啥呢？输入我们把它叫做头啃列表。什么叫头啃列表呢？你可以把它想象成就是一个数字的数组，比方说。

---

## Scene 2

Time: 00:01:11-00:02:05
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_002_00-01-52.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_002.md`

Transcript:
一个数字的数组，比方说你拿数字是啥呢？数字就是这么一个东西啊，二、三、四、五、一、八啊，就这么一个东西啊。那它数字个有可能很大。那这个头啃到底是什么东西呢？它就是我们的自然语言换算成数字的结果。那么至于说怎么换算的，这个你不用管啊。这个东西叫做分词。一般来说，那我们中文啊，平均一个字它能分出一点五个头啃。啊，平均下来啊，你说哪有半个头啃的？其实没有的啊。就是平均下来，有的中文呢，它可能就是一个头啃，有的中文呢，可能两个头啃，甚至三个头啃。它分出来的话，它。两个头啃，甚至三个头啃，它分出来的话，它可能平均下来的话，中文就是一点五个头啃。那么英文呢？英文的话，一个单词啊，就是一个字，约等于啊一点五个头啃。那么英文的话，就是一个单词，大概分出来呢是一点三个头啃啊，大概就是这样子。但每个单词可能分出来不一样啊，比如说有词根，对吧？还有前缀，就是它都可能会进行划分的啊，大概就是这么一个东西。最终呢，就是说我们给这个罗马行一个消息，这个消息呢，会先进行分词，把它分成一个个的头啃，那么就会形成。

---

## Scene 3

Time: 00:02:05-00:03:23
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_003_00-03-15.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_003.md`

Transcript:
分成一个个的投肯，那么就会形成一串数字。把这串数字呢，就喂给或者说传递给这个二层模型。那么他得到的是什么呢？得到的是一个概率分布。什么概率分布呢？它就是下一个投肯的概率分布。他得到的大概就是这么一个数据结构。呃，表示一个对象吧，就是你给了他一个数字，对吧？一串数字。然后呢，他得到的就是下一个数字有哪些可能性。比如说十五，它可能性为零点七啊，就百分之七十。然后呢，下一个投肯是二百八十八。投肯是二百八十八，它的可能性呢为零点二啊，就这么个意思。它把那个各种可能性给你排列起来，这就是罗模型没了。罗模型就是做一套数学计算，罗模型就在做这么一个事儿。它算出下一个投肯的概率分布，就跟我们平时用的模型感觉，或者是平时用的一些A I工具感觉差别特别特别大呀，对吧？因为这是最底层东西啊。那么后边，上层是怎么来利用它玩出那些花样？的我们后边再说。最核心的东西没了，罗模型就这样子。那说说这个玩意儿。我不行，就是这样子。那你说这个玩意儿有啥意义呢？你想啊，这些数字啊，是跟我们的自然语言是有对应关系的。比如说中文，它一个数字可能对应八个或者是一个中文。也就这些数字串起来的话，会串成一个什么？串成一个自然语言，对不对？那么它返回的下一个 token 是不是也是自然语言的一部分？比如说这一块，它得到自然语言可能是啊“你好”。那么下一个数字它可能是表示的是一个逗号，也有可能表示的是“吗”，是不是就这个意思？

---

## Scene 4

Time: 00:03:23-00:05:31
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_004_00-05-01.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_004.md`

Transcript:
妈，是不是就这个意思啊？那就是往后边猜测下一个词到底是啥，或者是下一个字到底是啥。好，这个图，同学们一定要记住哈，这就是我模型最原始的状态。那么后边呢还有很多的术语，这些术语呢我们平时还是蛮常见的，就是说给大家解释一下平时经常遇到的这些术语，在这个图里边它对应到哪个地方。第一个呢就是上下文窗口，它叫做context呃window，这个玩意儿是啥呢？非常简单，你只要知道这个图了，很好解释的，它指的就是这个玩意儿的长度，就这么简单，就什么。的长度就这么简单，就这么简单。这就是双向门窗口。呃，这个输出的长度为一百，那么目前双向门窗口就是一百。那我们提示说，呃，有这个模型，现在新发布的一个模型，它支持最大的双向门窗口多少多少多少。那指的什么意思呢？它指的就是它最大能支持多长的这个输出长度，给它扔进去。超过这个长度，它就受不了了。它也不会给你报错，它就把前面东西给截断了。比方说它只支持一万的双向门窗口，你结果给它传了两万，那么前面的一万它。我给他传了两万，那么前面的以外他就不要了，自动扔掉。这就是注意大的上下文窗口。目前呢，呃，咱们模型啊，一般的上下文窗口有什么幺二八的啊，都是比较常见的啊。幺二八K，这个K呢，不是说占了什么池盘空间啊，跟池盘空间没有什么关系。这个K呢，表示千。那么算出来就是十二点八万，K。就是这个数组它的长度可以是十二点八万，就这么个意思，就最大啊。那么你可以想一想，十二点八万它化换成中文的话，可以容纳多少个字。中文的话，可以容纳多少个字？就是说，平均一个文字，它是占一点五个。头啃的话，我们就估算一下呗。啊，大概就是十二点八，啊，或者是十二八幺零零零除一个什么，除一个一点五啊，大概就是八万多个中文字符。啊，或者一百二十八K的，还有什么二百五十六K的，还有什么万名零的啊一兆。注意啊，这不是磁盘空间啊，一兆的话指的是一百万啊，million，对吧？那么，如果说一兆的话。对吧？那么，如果说一兆的话，支持多少个中文字符呢？呃，那么就是除以一点五，那就支持六十六万个中文字符。也就是说，这个函数啊，它能处理的最大的token数量，那么就是上下文窗口。好理解了吧？啊，不过这一点呢，有一个特性啊，给同学们说一下：上下文窗口指的是它能装得下的token数量，就它最大能够处理多少个token，并不代表它能够把这些东西处理好。因为现在AI呢，也是有泡沫的，同学们都知道。就大模型之间竞争。

---

## Scene 5

Time: 00:05:31-00:06:50
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_005_00-06-31.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_005.md`

Transcript:
有的同学你们都知道，就是大模型之间竞争呢，也比较激烈。所以说各大厂商呢，为了让自己的模型有卖一下，所以说不停的给你堆参数。可能就结果你用下来呢，不是那么回事儿。什么意思呢？比如说它支持一兆的双向文本，指的是什么？指的是这个文本的列表长度能够容纳一百万。但是你把这个玩意儿沾沾惹惹扔进去了过后，你会发现它好多东西是根本就处理不过来的。同学们平时用那个AI的时候，有没有发现一个现象？就是你刚开始打开一个新的窗口的时候去用这个AI，就他聊天。去用这个A I，跟他聊天儿。哎，他觉得挺聪明的，你说啥他都记得住。当你聊天聊了很多了过后，你会发现他变傻了。之前的一些规则他就忘了。明明说好的每次显关代码要提交，他就把这个规则忘了。明明说好的一个代码文件一个模块不能超过两百行代码，他写的时候就忘了。为什么呢？这就是上下文窗口的问题。就他虽然能够容纳这么多头啃，但是呢，他记不住。你干整多过后，他的模型能力会下降。所以说，这点在提示我们啊，就是。所以说，对大家提示我们啊，就是模型原生就有这么一个特性。所以提示我们平时用这些模型的时候啊，那些相对独立的事情，尽量的去新开上一条文窗口去做。啊，后面我们还会讲到一些工具的使用。你会发现他会用了很多的子代理，对吧？为什么要用子代理，就是来处理这个问题。啊，这是第一个，跟我们要讲的概念啊，叫做上一条文窗口。好，第二个呢，就是我们到这一部分来。这部分我们目前把它看成是一个函数。实际上它是不是函数呢？实际上它不是函数，它是个什么东西呢？它是一个矩阵。应该说这个函数呢。

---

## Scene 6

Time: 00:06:50-00:08:28
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_006_00-07-52.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_006.md`

Transcript:
它是一个矩阵，应该说这个函数呢，是我们自己写的。呃，实际上它这个函数里边呢，再雕一个什么东西呢，再雕一个矩阵，呃，我这里用一个双端箭头吧。好，我们把它叫做权重矩阵。我跟你们说一下，这个到底是怎么回事啊。实际上我们的模型是这个东西。啊，有些同学可能在本地部署过模型，对吧？本地部署模型的时候，是不是要下载？把模型下载到本地。下载的实际上是啥呢？就是这个矩阵。啊，当然还有一些其他的配置文件啊，一些什么呃，config之类的配置文件。不过核心就是这个矩阵。这个矩阵是个啥呢？核心就是个矩阵，这个矩阵是个啥呢？就是一串数字，超级多的数字。我说，我们下模型的时候会发现，有些模型几个G，对吧？或者几十个G，或者几百个G，甚至一个T。那么就是主要占空间的，就是个矩阵，数字超级多。我们平时经常说：“哎，这个模型有多少个参数？那个模型有多少个参数？”指的是什么呢？指的就是这个矩阵里面的数字的数量。比方说，我们说一个模型，这个模型参数，它有七b，b什么b零。七b，b是什么？b零是吧？b零是十亿，那就是七十亿，指的是什么？七十亿个参数。那么换句话说，就是这个矩阵里边有七十亿个数字，简单吧？啊，一般本地模型的话就是七b啊，啊什么十六b啊，不会太大。但是一些商用级的，就是放到一些专用的推理服务器上的，那么那些模型的参数呢就比较大了。啊，现在目前有超过一个t的，不是一个t有十个t。那我记得什么g p t。一个T是十个T，我记得什么GPT五还是什么模型是超过十个T的，十万亿以上的参数。啊，T就是万亿嘛。那么指的就是那个矩阵里边有十万亿个数字。我们平时说模型训练，模型训练指的是什么呢？指的就是得到这么一个矩阵的过程。训练的目的是什么？就生成这么一个权重矩阵。那么至于说他怎么训练的，又是如何得到这个矩阵的？这个矩阵里边是啥意思？那是大模型工程师，也就是算法工程师要考虑的事情啊，跟咱们没关系。你只需要做这个。

---
