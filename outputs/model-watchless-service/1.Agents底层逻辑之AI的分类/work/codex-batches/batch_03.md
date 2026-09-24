# Video Notes Codex Batch

Inspect every referenced image and use the transcript as the factual source.
Write one file per scene to the notes directory. This is faithful light polish, not summarization or article rewriting.
Video mode: slides. Treat the slide as primary evidence. Preserve all lecture content aligned to this slide, and describe legible titles, labels, figures, table values, and diagram relationships.
Visual strategies: slide-state.

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

Notes directory: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\codex-notes`

## Scene 13

Time: 00:24:22-00:24:52
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\keyframes\scene_013_00-24-52.png`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\codex-notes\scene_013.md`

Transcript:
刚才的那个例子嘛，你要逼逼很多东西，你要想清楚很多东西，过后你才能最终去写代码。外面的这个高层次的事情，你都没想清楚，你写不了代码的。啊，机器学习它要起来想，我怎么才能让机器智能？他就提出来这么一个定义啊，就是说，对于一个计算机程序，如果说它在任务T上的性能P，随着经验E的增加而提升，那么我就称之为这个程序为机器学习。那说的是啥呀？我们看一下它三个维度：任务是什么呢？

---

## Scene 14

Time: 00:24:52-00:27:24
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\keyframes\scene_014_00-26-35.png`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\codex-notes\scene_014.md`

Transcript:
看一下它三个维度，任务是什么呢？任务可以是任何任务，随便你是什么任务。它不是说，哎，我这个机器学习只解决NLP，它不管这个事儿的啊。它的角度都不一样，NLP有NLP的问题，Speech有Speech的问题，CV有CV的问题，它们各自有各自的问题。但是呢，要解决这些问题，都要靠什么智能才能解决？你不靠智能解决不了。要解决它的智能的话，肯定要搭配这些具体的领域里边的东西才行。比方说，Java。这里边的东西才行，比方说Java语言，Java语言只能写Web应用吗？也不是啊，它控制台应用也可以写啊，什么桌面应用也可以写啊，是不是都是可以的？Java是一个通用型的语言，我们把它叫“图灵完备”，什么叫“图灵完备”？就是啥事儿都能干，你在计算机里面能找到什么事儿，它都能干，干得下去，都能做。只是呢，我们通常用它来写什么Web应用，是吧？懂这意思吧？所以说，机器学习呢，不是为了解决某一个领域的问题，它是要解决所有领域这个智能那个点，比方说，是编写语音技术。这个点，比方说，识别语音技术，它有它自身的特点，就怎么把语音转换成一个数字化的东西，这是语音技术要解决的问题，对吧？音频怎么数字化，怎么进行压缩，怎么进行分割，哎，这是个语音技术要解决的问题。但是你怎么解决，最后都要遇到同样一个问题吗？那智能这个点怎么办？是不是？那么实现方法这一块，他探讨的是怎么去做第一智能这个事儿，他要探讨这个问题。那智能这个问题探讨清楚了，那么各行各业是不是都可以利用这个智能，结合这个行业的特点去实现自己的？和这个行业的特点去实现自己的业务需求，能理解这意思吗？啊，我讲的已经很细了啊，你在网上去找任何教程，这些抽象的概念都不回去讲这么细的，你听完了过后一头雾水。我都尽量让你们认识清楚这个概念是啥意思了啊。好，那么机器学习它的定义是啊，我们看一下，它主要是三个关键词，一个是任务，任务表达的是你要做什么，你首先你要做什么，比如说你要识别一个就是呃一篇文章啊，要写一篇文章出来，就是任务。写一篇文章出来，就是任务。好，经验意义是什么？经验意义代表了你要给AI，为什么？你要写文章，你事实上要见过很多很多的文章。说机器学习呢，它有个特点啊，它要进行大数据量的训练啊，这是机器学习的特点。它不管你具体怎么训练的，它完全不管的。它就说“逼逼”，啊，一个人现在就在逼逼。但是呢，它是不是又把事情往前推进了一步了，对吧？又具象化了一步了，就是具体落地，它是一步一步，一步一步从抽象慢慢具象，慢慢具象，到最后一步，好可以落地了。那落地是知。好，可以落地了。那落地是自然而然的事情。那么整个过程就是从AI诞生到现在的Transformer模型，整个过程持续了接近一百年的探讨。啊，当然AI的过程中也走了很多很多的一些其他的一些路线路径。那些其他的路线路径是你要说在历史上完全没用吗？历史总是轮回的，说不定哪天又会被翻出来用。像这个连接主义，对吧？连接主义这一块，过去是被打入死牢的，没有人去探讨这个东西。因为当时只是提出来了，没有人去探讨，就是天方夜。

---

## Scene 15

Time: 00:27:24-00:30:08
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\keyframes\scene_015_00-30-08.png`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\codex-notes\scene_015.md`

Transcript:
出来了，没有人去探讨，就是天方夜谭。而且呢，有些人甚至从数学的角度证明这个根本就不可行。而且我告诉你，数学证明至今仍然正确。不过呢，这个情况呢，跟它那个前提呢，出了一点差异啊。你想了解这段历史的话，你可以去了解啊，自行去了解。以前是符号主义的天下，知道吧？连接主义呢，在大学里边，你要修研究这个方向的话，根本就拿不到经费的。这些玩意儿就纯烧钱，纯B B的，天天一群人在那B B啊，你可以这么去理解。他不管你落地的，反正就是说你要把位给他，怎么位他不管。反正呢，就像人。给他怎么喂，他不管，反正呢，就像人一样，对吧？要见过很多很多篇文章过后，哎，你才能写出一个好的文章。那么，新媒体要关注什么事情呢？你怎么来衡量好坏，你怎么来评判这个文章写的好还是不好啊？比如说靠人类来打分，对不对？就可以再进行衡量。他就把这个事情说清楚就行了。其他你具体怎么做，后续怎么写代码，怎么来训练，他才不管。他就把这个事情说清楚。啊，你后边只要再做这些事儿，你那么也都在我的机器学习的那个范畴里边。所以说机器学习呢，很多的一些。啊，所以说机器学习呢，很多的一些那个大学里边的一些AI课程，那都是讲什么讲机器学习，因为现在最流行嘛啊，我就为什么给你加黑，因为现在最流行的实现手段就是机器学习，在这个大的前提下进行学习。那具体怎么学习，那也有很多的实现路线的啊。但是呢，大的范畴都是机器学习，机器学习做的事情就是我不停的干，我也写数据，他就懂了，然后呢，他就可以做这个事儿了。然后呢，我再通过一种方法来衡量他的做的事儿好还是不好，不好的话，再回去重来，再加大训练量。不好的话，打回去重来，再加把训练量，再调整调整，然后呢，再学习。具体怎么做，他不管的，懂那意思吧？你只要在做这个事儿，就算是机器学习啊。那比方说下棋，就像阿尔法狗是吧？有典型的机器学习的成果呀。你要做什么？你要下棋呀？你要做什么？给你为什么数据？给你为无数的棋盘数据，对吧？呃，你那些著名的棋局，不光是著名的，大大小小的棋局全部为你，人类历史上的所有的棋谱全部为你，你学呗。好，那怎么样？Human Rights Watch is a human rights organization that works to protect human rights around the world.会给你，你学呗。好，那怎么样衡量好坏呢？那就看结果呗，你赢了还是输了，赢多少输多少，对吧？围棋嘛，赢多少输多少，那就通过这个来衡量好坏。机器学习就来说，哎，如果说你这个随着经验益啊，你给他问的东西越来越多，哎，他看这个事儿呢，就可以干得越来越好，有一套标准来衡量好坏。干问的越多，他就能干得越来越好。哎，那么我们就称为这个程序呢，为机器学习，你就达到个机器学习的定义了，就这意思。继续学习的定义了，就这个意思。有时候他说：“这是很自然的事情啊，他看的越多，肯定越好啊。”那可不一定哦，他可不是人呢，程序可不是人呢，有可能看的越多，越少啊。就像书呆子一样，对吧？学的越多，人越少，他不能融会贯通，知识没有内涵。对每一个知识，对他来说，全是一个冷冰冰的文字，就好像背地理啊、背政治、背历史一样啊，就像一个个人名一样，没有任何关联。那么，这学的越多，人越少啊。他不落地的啊，不用想落地。它不落地的啊，不用想落地的啊，它不落地的，它就是你。只要在这个范畴内，都是属于机器学习。所以说，机器学习如果说要讲课的话，呃，把机器学摊开讲的话，是一门非常庞大的课程，因为它的做法太多了，各种样的做法。好，这是它的定义。那么整个机器学习的关键点在什么呢？在如何来设计一套训练方法。这个训练方法可以让机器自主的进行学习，因为机器学的核心概念就是你要学呀。我给你为的目的是啥？你要学呀，你都没有学习能力。你我给你为的个。

---

## Scene 16

Time: 00:30:08-00:30:56
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\keyframes\scene_016_00-30-56.png`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\codex-notes\scene_016.md`

Transcript:
学习能力，你我跟你为了个有啥意义呢？对吧？你在公知台里边打一一百遍棋谱，有啥意义呢？没有任何意义，机器得学，就是你如何来设计这个训练方法，让他学。好，那么这一块呢，又开始比比了啊，还是不落地的啊。但是呢，又往前推了一步，哎，做了一些方法论啊。我们把叫做学习范式，或者叫训练的范式，有落地吗？没有，没有一毫的代码，全在比比。还记得吗？就是。

---

## Scene 17

Time: 00:30:56-00:31:27
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\keyframes\scene_017_00-31-27.png`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\codex-notes\scene_017.md`

Transcript:
全在B B，还记得吗？就是这个，要一直到B B到最后一步啊，可以落地了。好多问题没解决啊。好，那么就单纯的几种学习类型，非常好理解。一种叫监督学习，哎，就是什么人类给答案，比方说识别一张图片是猫还是狗，给他一张图，好，那么他识别出来，他可能不对，对吧？那正确答案应该是什么呢？他也不知道啊，他不知道正确答案是啥。那么这个时候呢，人要去标一下，去框一下，哎，这是只猫，这是只狗，对不对？哎。这是狗，对不对？哎，现在的数据标注那种岗位，对吧？哎，给你们看一下数据标注岗位啊。我之前写过一些已经过时的课件，这个课件里边倒是有。看一下，在哪里啊？现在我没有按照那个课件的方式来讲了啊。哎，你看看一下这些课件。我一会儿呢，把这个标注这一块给你们截图啊，放到目前这节课下面啊。你们截图，你可以看一下啊。或者都不用截图，这有啥可看的嘛？这个就是数据标注嘛，对吧？这是人框出来的。

---

## Scene 18

Time: 00:31:27-00:31:55
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\keyframes\scene_018_00-31-55.png`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\1.Agents底层逻辑之AI的分类\work\codex-notes\scene_018.md`

Transcript:
数据标注嘛，对吧？这是人框出来的，人就可以告诉他：“哎，这是一个卡车，这是一个什么car，哎，这是一个小车，对吧？”告诉AI，对吧？哎，这就是标准答案。把文本标注也是一样，对吧？告诉你：“哎，这是一个什么，这是一个组织啊，标注一下。”有可能是AI分类出来，可能就有问题啊。告诉你正确答案是啥，就是人告诉他正确答案。比如说声音也可以做标注，一段混剪的音频，那么呃，表一第一秒到第二秒是“Speak二啊，第二个人说了一个“Alright啊，就这个意思。”

---
