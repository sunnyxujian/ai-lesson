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

## Scene 7

Time: 00:08:28-00:09:16
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_007_00-09-11.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_007.md`

Transcript:
跟咱们没关系，你只需要知道这个概念就行了。而且有的时候说，我们就要对模型进行微调，也是指的是去处理这个矩阵。训练是什么？从无到有，一开始没有这个矩阵，然后通过训练得到这么个矩阵的过程。微调是什么？已经有这个矩阵了，我把这个矩阵里面有些数字呢，通过一些二次训练，对它的里面的东西呢做一些改动。能理解吧？啊，我们站在外面看啊，不深入到里边，里面是个黑盒子，你不用去管它怎么去得到的。然后我们无论是训练还是微调，它的原材料都是语料，因为模型的本质。材料都是语料，因为模型的本质作用是给我一个投坑列表，我来预测下一个投坑的概率分布，对吧？那它一定要见过足够多的投坑，它预测的结果呢才更加精准，或者说才更加合理。那么它要去进行语料的训练。为什么现在编程的模型那么强大呢？主要是因为我们有大量的庞大的开源库，开源库里边有大量的编程的各种语言的代码，可以通过这些语料进行训练。它见过足够多的投坑之后，那么它能够进行。

---

## Scene 8

Time: 00:09:16-00:10:07
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_008_00-10-02.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_008.md`

Transcript:
逐个的头啃之后，那么还能够进行下一个头啃的预测了。训练的结果就是这个全动矩阵。严格来说，逻辑模型是啥？逻辑模型是一个图形，它不是一个函数。但是呢，这个模型要用啊，你不能光把它给数字打怪，我咋用呢？因此呢，我们一般来说会通过哈金费斯的一个库啊去调用这个模型。那么调用的方式呢，那就看你用什么样的模型架构了。比方说我们目前最常见的啊是什么架构？来大声告诉我，就是Transformer模型架构。那么你就可以用Transformer这个架构，它里边可以提供一个函数来去调用这个矩阵。那如果说你。这个矩阵。那如果说你用的是另外的一些架构呢，比如说Tensor，那么你用Tensor里面提供的函数去调用这个矩阵，懂那个意思吧？就不同的架构呢，它使用矩阵的方式不一样。但一般来说呢，就是你训练的时候，你是基于什么架构来训练的，一般就要用什么架构去调用。比方说，你现在用的达摩系都是基于Transformer架构来训练的，对吧？训练出来的矩阵，这个全动矩阵，那肯定要用Transformer的架构来调用。你用别的架构能不能调用呢？如果说你要调用的话，你要对这个矩阵做一些转换才行啊，比如这套模式。啊，不过这套模式呢，再。

---

## Scene 9

Time: 00:10:07-00:11:00
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_009_00-10-40.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_009.md`

Transcript:
啊，就这套模式啊，不过这套模式呢，再顺便多说一句啊，呃，这套模式呢，他们都是属于神经网络和深度学习啊，它是有使用这种方式。那如果说你用的是什么机器学习之类的其他的AI技术的话，那可能就不是这套模式了啊。我们现在讲的模式都是基于神经网络和深度学习的。那么这个东西就是啥？不扯远了啊，因为我们目前基本上玩的都是玩的Transformer。好吧，说这一块呢，我们再总结一下，就是你传入一个头看列表，那么这是一个函数，传给这个函数，这个函数是基于Transformer架构的一个函数，它拿到这个头看列表。面结构的一个函数，它拿到这个投控列表过后，它要进行一段运算。它运算的过程就是去使用这个矩阵里面的参数啊，就是这里边各种各样的数字，然后再结合这个东西，就它加它，然后再加上算法，就得到这个概率分布的结果。所以说，大模型的本质是啥？大模型的本质，从技术上来讲，是一个数学函数，甚至你都可以认为它是个纯函数，不是可以认为它就是个纯函数，就是你个投控列表是一定的，它得到的结果一定是不变化的，你输入一、二、三。

---

## Scene 10

Time: 00:11:00-00:12:59
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_010_00-12-31.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_010.md`

Transcript:
不变化的，你输入一、二、三，它就得到四。啊，我就随便加几个例子啊。你输入不变，得到结果就不变。输入再吓人一点，它跟这个玩意儿没有什么区别，纯函数嘛。输入一加二等于三。啊，只不过呢，它公式没有那么简单，哈，公式是比较复杂的，这是一个比加法更加复杂的公式，得到一个结果。因此你看网上有些人开始都崇拜AI了，是吧？快要形成宗教了。什么AI要统治全人类了？AI开始出现自我意识了。你看一下这个玩意就行了。什么AI开始对人类发脾气了？你看一下这个玩意就行了。他天天膜拜的是个啥？你看一下这个玩意就行了。它天然膜拜的是个啥？膜拜的是一个函数，就是我们高中课本里边一个公式。它对膜拜的玩意，它说：“那个玩意儿开始出现感情了，我也不知道这个玩意能有啥感情。”它就是个数学运算啊，传着啥得到啥。而且是个纯函数，它不会变化的啊。当然理论上是个纯函数啊，但实际上呢，它可能没有那么纯，没有那么纯的原因不是说这个函数不是纯函数，它函数还是纯函数，只是呢，它在运行的时候呢是经过G P U去运行的，因为它的参数量太大了，它要计算的数学运算太多了，因此它需要通过G P U去并行运算。它把那些数学公式。都去并行运算，他把那些数学公式里面进行拆解，拆解过后再进行运算，最后来合并啊，大概是这么个意思。那么由于GPU是个并行运算，就会导致一个问题呢，就是哎，你们知道那个在计算机的世界里面，就使用的是浮点数，这个没问题吧？而浮点数是不满足结合律的。什么意思呢？我给你们举个例子啊，比方说放大一点啊，零点一加零点二加零点三，它有误差，对不对？然后你看。它有误差，对不对？然后你看一下另外一个，很神奇，零点一加上，啊，就这个，看一下，它就没误差了。你看它是不满足结合率的，也就是意味着是啥呢？在计算机的浮点数的世界里边，这个东西它等于这个吗？你会发现它不等于。啊，至于说为什么，以前我一个抖音短视频专门讲过这个问题啊，就是这种误差到底是怎么来的。万万没想到在这个地方用上了，是吧？所以说知识永远都是有用的，你不知道它将来在什么地方会用上。啊，总之它不满足。在什么地方会用不上？啊，总之它不满足结合率。它不满足结合率有什么问题呢？因为它现在有很长的一个公式要去进行运算。那么结果呢？它一拆解过后，是不是它拆解的位置不同，得到的结果就可能不一样？是不是？所以说理论上它是个纯函数，但实际上呢，它可能没有那么的纯。好，老有同学说袁老师，那现在的模型不都是什么多模态模型吗？那你怎么有解释多模态的？那我告诉你没啥好解释的，一样的。对这个东西呢。

---

## Scene 11

Time: 00:12:59-00:14:44
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_011_00-14-34.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_011.md`

Transcript:
一样的。对这个东西来说，我问你啊，听到现在，我问你一个问题啊：他知不知道什么叫自然语言？他知不知道什么叫中文？什么叫英文？你好好想一想。我再问一次：他知不知道什么叫自然语言？他知不知道你说的话什么意思？他知不知道什么叫中文？什么叫英文？他知不知道？你看他的输入输出，就完事了。他输入的是个啥？啊，这是个啥？这是中文吗？这是英文吗？这是图片吗？这是视频吗？这是啥？这是个。这啥？这是个数字的数组，他哪知道个数字是啥东西？他不知道。总尾因为对它来说都是数字，他不知道那是啥玩意儿。反正就是他看到这个数字，经常后面会跟另外一个数字，他不知道那是啥意思。这是很多人崇拜的模型，要产生自我意识的模型，这就是这么个玩意儿。因此呢，什么多模态、什么图片、视频、音频、声音，对他来说没有区别，都是数字。我经常训练的，他看这个数字后面跟的是另外一个数字，那我就可以算出概率分布。就这个意思。啊，当然这里边。就这个意思。啊，当然，这里边没有那么简单。哈，它里边还有一些特别看起，那就是模型内部的东西。我们不扯远了。总之，基本上就是个逻辑。所以说，多模态的模型，对它来说是没有区别的。因为音频也好，视频也好，图像也好，对它来说都是数字。你给它训练的是啥，它就能做啥。只不过呢，人拿到这个东西过后呢，人要分辨一下，对吧？哎，比方说我这句话告诉你是，请帮我生成一张啥啥啥图片，那么它吐出来一个头啃啊，不是一个头啃，是一个下一个头啃的概率分布。那么我要判断。头啃的概率分布。那么我要判断一下，哎，这个头啃是文字呢，还是图像？其实也很好判断，因为头啃呢，它是个字典，有一个列表，有字典列表的。比方说，他给我的是一个五零零零零八，随便吧啊。哎，我发现这个头啃它坐落在一个叫做一米几范围的区间。哦，原来我知道这个头啃呢是一个跟一个图像相关的一个东西。那么我就把它当成一个图像里边的信息，我再进行转码啊。进行转换过后呢，就得到一个图像的可能就是某一个像素点的信息，懂这意思吧？好，就没啥了呀。我模型认识到这儿就够了。而这。

---

## Scene 12

Time: 00:14:44-00:15:36
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\keyframes\scene_012_00-15-30.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\codex-notes\scene_012.md`

Transcript:
我请认识到这儿，就够了。而这套东西哈，从Transformer出现那一天起到现在，应该有八年多了吧，七八年了，就没变过。我们现在玩的是啥呢？无非就是玩了这么几个地方，就是怎么去训练这么一套矩阵出来，然后给的语料可能有中文的、有英文的、有代码的、有图像的，让它能够适配多种，多款的预测。但是这个函数没变，都是这个样子。无非就是调矩阵得到下一个概率分布，无非就是不同的模型，就是不同的矩阵，它能支持的最大上下文。对，它能支持的最大的上下文是不一样的，仅此而已。还记得以前我一个视频里面说的吗？我说全系统Model发展到现在没有本质的变化。为什么我这样说，就是指的这个，它的基础能力没有什么本质的变化。现在我从技术角度跟你讲清楚这个原因的哈。好，理解到这一层过后，就可以很好的理解我们接下来要讲的上一层，就是模型服务那一层，它又是怎么去基于这个东西玩出花样出来的。好，咱们下节课再说啊。

---
