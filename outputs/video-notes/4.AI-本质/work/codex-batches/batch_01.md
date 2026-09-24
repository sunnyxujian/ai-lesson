# Video Notes Codex Batch

Inspect every referenced image and use the transcript as the factual source.
Write one file per scene to the notes directory. This is faithful light polish, not summarization or article rewriting.
Video mode: explainer. Preserve the scripted explanation in full. Prefer meaningful charts, animation states, interfaces, demonstrations, maps, or B-roll over a presenter face when choosing frames.
Visual strategies: screen-state, evidence.

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

Notes directory: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes`

## Scene 1

Time: 00:00:00-00:00:46
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_001_00-00-35.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_001.md`

Transcript:
那我是如何看待这些新概念的？我又是如何去学习它的？我要把这个方法教给同学们。说说这节课，你知道为什么这么重要了吧？你只要掌握好了这个方法，将来无论遇到什么样的概念，随便来，我保证你几分钟时间就搞定。有这么神奇吗？那你听一听就知道了。好，各位同学，这节课的内容啊，非常非常重要。可以这么说，这节课的内容呢，只要AI存在一天，这节课的内容它就。该存在一天，这里头的内容它就会发挥作用一天。我们回顾一下之前，我们讲过了这个裸模型和模型服务，是吧？那么接下来呢，我们要讲这个A I application，就这一层。我们知道每一层实际上是对下一层的封装，比方说这个模型服务，它是封装了什么呢？裸模型的调用，而我们的A I application呢，它是封装了模型服务。啊，它是这么一个关系。然后在讲之前。

---

## Scene 2

Time: 00:00:46-00:02:51
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_002_00-01-48.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_002.md`

Transcript:
啊，它是这么一个关系。然后在讲之前呢，有几点需要给同学们声明一下：第一个呢，就是这两层啊，他们的分界线啊，是没有那么清晰的。它不像那个模型服务跟那个裸模型之间，它的分界非常清晰。裸模型是这个玩意儿，对吧？得到一个投控列表，然后得到一个概率分布。模型服务呢，用一个自回归啊，之前讲过的，去调用那个裸模型的功能，然后对它进行前处理和后处理。它界限比较分明。但是这个AI application呢，和这个模型服务啊，它们之间的界限没有那么分明。有很多概念呢，它可能今天在。很多概念呢，它可能今天在这一层，明天它变到这一层了啊。比方说举个例子，像同学们现在都用的是那个什么Skills，对不对？啊，像这个概念呢，最早的时候是在这里，是这一层玩出来的概念。后来觉得这个概念还挺好，然后呢，模型服务商呢，他就把这个Skills这个概念呢，直接就融到这个模型服务层了。也就是说，你这个开发AI应用的，你就不用去管什么Skills了，我这里已经给你做了。比方说咱们来看一下OpenAI的一个接口啊。好，你看OpenAI的接口。的一个接口啊，好，你看open ai的接口里边，说是有这个skills，也就是你直接调那个api接口，你就可以实现一个skills。也就是说，如果说你要开发ai应用的话，你又调的是open ai的接口的话，那么你就在这里边不用去写这个skills的逻辑了，懂我的意思吧？啊，这只是举了个例子哈。呃，包括像之前的什么m c p什么tools，对吧？那么现在呢，很多模型服务商呢，都直接就支持m c p和tools的，你在开发ai。T和T O是吧？你在开发A I应用的时候呢，就不用去自己处理这一块的功能逻辑了，懂意思吧？就这两层，它的界限没有那么分明。但是呢，很多事儿吧，总得要做，比如Skills这一块跟模型之间的交互逻辑。那么就这一块事儿呢，就看谁做的问题。如果说你使用的模型服务商他没有做的话，那你你就必须要做。反之，如果他做了，你就不需要做了，就这么简单。总归有一个层要做啊。你模型服务商多做一点呢，那我就可以少做一点。你少做的，我就必须。我就可以少做一点，你少做的话，我就必须要多做，总归有个人需要来做。所以说这两层呢是不太稳定的。我们学到目前啊，同学可以发现，像这个裸模型这一层，它是非常稳定的。虽然它的训练方式啊、性能啊、参数啊，里边的一些什么注意力机制啊这些具体的做法呢，可能在不断的更新变化，但它的调用方式是非常稳定的。而到了上一层模型服务和AI应用这一层，是最不稳定的。同学看到那个自媒体上天天上蹿下跳的、大呼小叫的，也就是对这一两层的变动，能懂的意思。

---

## Scene 3

Time: 00:02:51-00:04:50
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_003_00-04-22.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_003.md`

Transcript:
这两层的变动，能懂这意思吧？呃，其实这也符合咱们技术里边的一个规律：任何一个技术站，越底层越稳定，越上层越不稳定。就说到这一点，我顺便给大家说一下啊，这也是为什么现在几乎是没有人去玩这个微调了。我们之前说过，微调、微调和训练其实都是在生成什么，生成这个裸模型要调用的权重矩阵，都是改动这里边的参数。呃，为什么现在没有人去玩微调这个事儿呢？因为从成本上就划不来，比方说哈。面上就划不来。比方说哈，呃，举个例子，呃，你这里的这个权重矩阵呢，是比较基于GPT三点五的。哎，你觉得三点五的功能还不够啊？至少对你们目前公司里边的很多知识呢，是没有经过训练的。你们是公司里面有大量的内部知识。那么过去的做法会怎么样呢？过去的做法会对它进行微调，是吧？微调的作用是什么？就是把它原本生成的权重矩阵呢，某一些参数给它改了啊，都要经过很。参数给它改了啊，都要经过很多的二次训练的哈。微调过后呢，是不是生成一个新的啊？就基于GPT三点五的权重矩阵啊，就更改后的权重矩阵，这个没问题吧？好，这件事儿要做多久呢？少说你要两三个月。微调其实本身呢，它训练花不了多少时间，主要是要要验证它训练的结果是不是符合预期的。这个验证过程是非常麻烦的，你整了两三个月啊，都是至少啊，我嫂子说的。是至少啊，我少的说的，你搞不好的话，半年都是有可能的。你好不容易整了半年，把它微调出来了，那训练效果还不错。好，结果G P T四出来了，你会发现G P T四，你不用微调，你就给它微一些提示词，它的上下文窗口更大，识别更准确，幻觉更少。你会发现，即便不用微调，都比你这个微调的结果好。你就给它微一些提示词，都可以搞定的。所以说，你之前那半年在干嘛？这瞎折腾，你花了那么多成本。我都不是说说。花了那么多成本，我都不是说算力的成本了啊。算力其实花不了多少成本，主要是人力的成本。你要大量的去验证这些成本花了过后，你会发现大模型更新呢，比你之前要更强了。你直接用它，比你之前微调的结果更好。说反复这样折腾下去啊，有些公司就发现这个微调这个活是真不能干了。因为现在AI发展呢，还没有那么成熟，还在不断的发展过程当中。虽然这个调用方式是稳定的，但是这一块训练的结果不稳定啊。说去微调呢。

---

## Scene 4

Time: 00:04:50-00:06:34
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_004_00-06-24.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_004.md`

Transcript:
结果不稳定啊，所以说去微调呢，划不来。因此现在基本上啊，除了一些少部分极端的场景之外，没有人去玩微调了。因此现在这玩啥呢？主要就是玩这两层，就是这两层。那这一层你玩不了，就是别人模型服务商给你提供的接口，对吧？你玩不了，那么玩啥呢？就玩这一层。那么这一层无非就两个层面可以玩，一个是啥呢？一个是应用开发。就是我们说的AI应用开发，指的是什么呢？指的就是去调用模型服务商给你提供的接口，然后去做一个。刚给你提供的接口，然后去做一个具体有价值的AI工具，比如说像我们这个AI构建，对吧？我们后边要讲的AI效能工具，主要是讲AI编程啊。那么AI编程的工具，哎，请问大家属于哪一层？属于哪一层？是这一层吗？不是吧？这一层吗？也不是吧？是啊，是AI应用这一层。好，这一层除了涉及到应用开发之外呢，呃，另外呢还涉及到另一个，就是工具使用啊。这两个很好理解吧？应用开发什么意思？就是你开发一个AI应用，去调用这些接口，去完成一个AI应用开发。啊，讲到这，我就顺便多。A I应用开发啊，讲完之后，我就顺便多讲一点吧。一个是应用开发层面啊，它主要是调用这个接口去完成应用开发。那么这里呢，需要知道的是，一个是概念，这里有很多概念啊，什么tools啊、M C P啊、R A G啊、skills啊等等等等一系列的概念。像我们之前说的，很多很多的A I概念啊，都是跟应用层相关的啊。当然，我刚才也说了啊，这个概念呢，它在这两层之间呢是分界线，没有那么明确。有些概念呢，现在已经被模型服务商所吸收了啊，他自己就给你提供这样的一个东西了。但是，他给你提供。提供这样的一个东西呢？但是它一提供你还需要知道，不然的话你使用不知道怎么去使用。啊，一个是你需要知道概念，第二个呢，就是一些开发框架啊，像什么呃，lunch，啊，lunch，graph，还有什么D P agents啊等等等等啊，一些常见的一些开发框架。这是你需要了解的，就是你如果说要做这个应用开发的话，你需要知道这些东西。好，这些东西呢，就在咱们的架构课里边啊，给大家看一下啊。好，你看，咱们架构课里边除了很多的架构项目之外，那么还包含了A I的应用开发相关的东西啊，这是A I的相关概念。然后下。

---

## Scene 5

Time: 00:06:34-00:07:52
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_005_00-07-13.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_005.md`

Transcript:
AI的相关概念，然后下边呢是一个浪线啊，还有浪杠，后边还有AI的项目啊，这个就相当于是你们用的什么AI编程，我给你实践了一遍，怎么去做一个AI编程出来，后边还会加入很多的其他的AI应用开发的项目啊。整个架构课呢，其实目的非常明确，就是如果说你工作了两三年了，然后薪资呢涨不动了，那么这个时候呢，你就需要咱们的整个架构课去提升你的薪资。整个这个架构课啊，就是说白了，目的很明确，就是打开你一个薪资的空间。同学们可以来了解一下咱们。一个薪资的空间。同学们可以来了解一下咱们的课程啊。高薪课呢，是从零基础到高级业务开发的；然后架构课呢，是从高级业务开发到架构师的AI应用开发的内容。在架构课里边，啊，除了这个体系化课程之外呢，我们还有很多的福利课程。这些福利课程讲的就是一些核心知识点，来自于咱们的付费课，送给大家。他可以在极短的时间里边解决你的一些核心问题。就有些同学呢，特别是白嫖的，就仅仅通过咱们的福利课程也可以完成薪资大幅度的提升。像这些课程啊，都可以来找咱们去了解了解，找咱们的方式啊。去了解了解，找到咱们的方式啊！在咱们账号主页点击头像进入账号主页，根据提示来找找我们就可以了啊。好，话说回来啊，呃，AI应用这个层面呢，除了应用开发之外，还有一个什么呢？就是我们这门课要讲的就是AI效能工具，最后要讲的啊，工具使用。那这一块就不涉及到开发了啊，就是如何来使用工具来提升我们的工作效率。那这里边也会涉及到概念，而且这个概念的认识啊，和前面概念的认识是一样的，没有什么区别。你不认识那些概念。

---

## Scene 6

Time: 00:07:52-00:08:45
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_006_00-07-58.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_006.md`

Transcript:
没有什么区别，你不认识那些概念，你工具也使用不好。然后才是具体工具介绍，什么Cloud Code呀、Code X啊、Open Code呀这些乱七八糟东西啊。其实呢，到时候你只要理解了概念过后，我稍微一点拨，你就明白了。很会用这个工具，用着老火，不知道该怎么用，就是因为概念不明。好，这个体系我就讲清楚了啊。我们这门课讲的是什么？前面技术认讲完过后，我们后面就会讲这个编程工具啊，就是A I编程工具，主要就是A I编程工具。因为我们这个课呢，面向的是程序员吧，对吧？你要说什么？的程序，儿吧，对吧？你要说什么？AI短句也不在我们这个课的范畴之内啊。那也倒是也属于工具，呃，使用层面，但是不在我们这个课的范畴之内啊。主要就是AI编程工具。那后边如果说还有一些新奇的工具呢，我们可以介绍介绍，像什么OpenCL啊之类的，对吧？最近比较火。但是很多新奇的工具吧，它的生命周期很短，大部分工具都是玩概念的，生命周期有的可能连一周都撑不过，有些呢能够撑几个月，但是很快就销声匿迹了啊。不过同学们如果说感兴趣的话，跟大家介绍介绍也没事儿。好，那么我们这。

---
