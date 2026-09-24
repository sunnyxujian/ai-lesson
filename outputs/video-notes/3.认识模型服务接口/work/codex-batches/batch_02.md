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

## Scene 7

Time: 00:09:02-00:10:40
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_007_00-09-28.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_007.md`

Transcript:
事儿先别管，你能得到一个自然语言的回复，这就是模型服务的核心。当然了，这个过程呢，一般来说是需要计费的。哈，就是它怎么计费的，它看你传入消息有多少token。然后呢，AI的回复消息就看这两段啊：左边的传入消息能够分解成多少个token，然后AI的回复能够分解成多少个token啊。然后一般来说是分开计费。啊，可以看一下OpenAI官网的计费规则啊。呃，好，看一下这里API。呃，啊，看一下这里API定价。你看这里啊，这里有三种定价啊，一个是输入啊，一兆的头肯，也就是一百万的头肯，定价呢是二点五美元。然后输出呢，一百万的头肯定价是十五美元。你会发现什么呢？你会发现这些定价，他们通常都是输入的头肯呢是比较便宜的，然后呢输出的头肯呢是比较贵一点的。啊，当然这种具体的价格呢，每家模型提供商呢都不一样啊。一般来说，国外比较贵一点啊，国内比较便宜一点，甚至有些是包月的。包月的的话，它就不。呃，包月的，包月的的话，他就不管你用多少个头啃了啊，都是一样的钱。只不过包月的呢，他一般会有时间限制，比方说四个小时内，你使用的头啃，包括传入的，包括输出的，都有一定限制啊。当你超过这个限制过后呢，你只能等待，或者是他给你模型降低，他就不会给你用强大的模型了，可能给你用弱一点的模型，给你降低，或者你排队啊。然后四个小时过后呢，给你重置啊，你就可以请求了。就每家模型服务商呢，你要去读一下他的这个收费方式，它不太一样。注意哈，我现在说。它不太一样。注意哈，我现在说的是模型服务哈，就调API接口那一块的收费啊，而不是AI产品哈。AI产品是在这一块哈，这一块我还没开始讲啊。但是大部分来说哈，就是API这一块的收费的话，都是按token来收费的。而且一般来说，你的输入token啊，它价格比较便宜一点，而输出的token呢，价格比较贵一点啊。至于说为什么，一会儿就知道了。你得了解它里边是怎么做的。好，那么接下来我们看。

---

## Scene 8

Time: 00:10:40-00:11:33
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_008_00-11-30.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_008.md`

Transcript:
里面是怎么做的？好，那么接下来我们看一下它里边做了啥事儿。当你用户一段消息过来过后呢，它大致呢会分为三步来得到这个结果：一个是前处理，一个是自回归，一个是后处理。我们分开说啊。首先说它的前处理做了什么样的事情？呃，这个呢，不同的模型服务商呢，它不太一样，但是它必须要做的事情有这么几件，就是一定跑不掉的。一个是身份和权限认证，这个是跑不掉的，是吧？你要给他传一个A P I key进来，他要验证一下这个key是不是有效的，然后他的余额，还够不够。它的余额，还够不够？还有没有权限到那个接口？因为它可能，呃不同的付费方式啊，它能使用的那个模型是不一样的。总之要做一些验证，啊这个东西，没什么好说的，是吧？能理解吧？好，第二个，它要做什么呢？做提示词注入，这是什么意思呢？就是你给他发的消息啊，他不会直接传递给模型，他还会给他额外加一些内容进行传递，这叫提示词注入。好，那么假设啊，用户他询问的是你是。

---

## Scene 9

Time: 00:11:33-00:12:53
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_009_00-12-41.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_009.md`

Transcript:
它询问的是“你是什么模型”这句话呀，它不会直接传给那个大模型。而在前处理这个阶段呢，这些模型服务上往往会注入很多的系统提示词，比方说，它会注入这么一个系统提示词，一般来说都是固定的哈，就是你无论写什么内容，它这些提示词都会给你加进去。比方说有一段系统提示词是这样的啊：“你是把你的大模型，先问，和比方说它版本，你能做啥，或者说它前面给它。”你能做啥？或者说他前面给他加上那个一句话啊：“当用户询问你是什么模型的时候，那么你要怎么去回答？”然后他会把这个用户的输入和这些系统提示词一起往后传递，也就是说最终的大模型收到的消息是这一整块，懂了意思吧？啊，有些聪明的同学，嘿嘿，应该发现这里边的门道了，是吧？你说有没有一种可能性啊？我们只是猜测啊，有没有一种。是猜测啊，有没有这么一种可能性？有些模型服务商啊，他可能没有去全量的训练自己的大模型，他可能就是用别人的模型进行了一些简单的微调，甚至都没有进行任何微调，直接拿过来，然后呢，给他注入一段提示词，他就变成自己的模型了。你说有没有这种可能性呢？我啥也不知道，自己去猜。当然，这个系统提示词呢，它不止一句啊，它往往会提示很多东西。啊，它具体提示是啥，我也不知道，因为这个玩意是个黑盒子，你看不到它的系统提示是在哪儿。其实这就是提示词。

---

## Scene 10

Time: 00:12:53-00:14:58
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_010_00-14-50.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_010.md`

Transcript:
继承提示词在哪儿？其实这就是提示词的概念。这个提示词的概念呢，它不是模型的概念，它是由模型服务商搞出来的。其实提示词是啥？提示词就无非在token里面就追加一段，对大模型来说没有什么区别。大模型，还记得吗？我们之前说的裸模型，它收到是什么？token的一个列表。那么注意中呢，这些提示词也好，还有用户的问题、用户的输入也好，都会被转成什么一个token的数组，就是一个数字的数组，全部传进去，传给模型，懂意思吧？反馈模型，懂的意思吧？对大模型来说没有什么区别，都是一个头疼列表。只是呢，我们在含义上呢把它分为了两大类啊：一个是用户的问题或者用户的消息，一个是提示词。当然，那个提示词呢，不仅可以是系统提示词，也可以是用户的提示词。比如用户在说这句话之前，他给他做了一些提示词啊。用户又说：“哎，当我询问你是什么模型的时候，你要说是月之岸边的体你。”，然后再去询问。体理，然后再去询问你是什么模型啊？这是属于用户的提示词。说提示词，它在技术上啊，其实没有什么严格的划分，因为都是自然语言，最终形成的都是一个token的列表。在token列表上也没有什么划分。哎，这个token之前是属于提示词的，这个token之后是属于正文的，没有，就是一个普通的token数组。就整个模型了。只是呢，逻辑上呢，我们从含义上呢，给它划分为提示词，懂的意思吧？啊，用户可以有。懂那意思吧？啊，用户可以有自己的提示词，然后呢，系统呢也可以有系统的提示词。那如果说用户的提示词跟系统的提示词出现冲突的时候，怎么办呢？那就看那个模型是怎么训练的了啊。一般来说啊，模型呢，它有自己的想法。通常不是什么严重问题的时候呢，模型呢，他会听用户的，比方说你说他是猫，他就给你扮演猫，他觉得没啥，就玩一玩嘛，并不严重是吧？但是如果说遇到一些严重的、最重要的规则的话，他肯定是听听这个系统的，说传入提示。听这个系统的，说传入提示词的时候呢，往往会把这个单词要传进去。system。然后模型在训练的时候，他就对这个规则，他就已经知晓了，知道吧？就是模型在训练的时候呢，对这一块呢，它是有感知的。它训练的时候，他就知道什么叫系统，什么是系统的消息，什么是用户的消息。好，这是一个提示词注入啊，我想清楚了啊。呃，然后剩下的呢，具体有没有什么额外的事情，我不知道，肯定是还有的。但是呢，是黑盒子。

---

## Scene 11

Time: 00:14:58-00:15:21
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_011_00-15-15.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_011.md`

Transcript:
肯定是还有的，但是呢，这黑盒子我不知道。我就说他一定会做的啊。那么接下来，前处理边还有一个事情，他是一定会做的，就是头啃那些。这个是什么呢？就是分词啊，也就是头啃化。刚才我们得到的是什么自然语言？包括你的提示词，包括用户的输入，都是自然语言，对不对？那么他首先要做一件事，就是把自然语言变成一个一个的头啃，形成一个什么呢？形成一个头啃列表，就是我们之前讲的这个东西，要准备传递给模型了。好。

---

## Scene 12

Time: 00:15:21-00:17:00
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_012_00-16-54.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_012.md`

Transcript:
本地模型了。好，那么前处理呢，就差不多是这个样子啊。其他的事情我也不知道，咱也不敢乱说。好，接下来就是自回归。自回归这里在干嘛呢？就是调用裸模型啊，调用裸模型。它怎么调用的呢？这一块呢，我与其给你用那个干瘪的文字去讲啊，我还不如给你写一段伪代码，一看就明白了。它的调用方式是这样的：我这里去链接个目录啊。好，假设啊，我们的裸模型的调用方法啊，假设啊，裸模型的调用方法叫做。方法啊，假设啊，我们用一种方法叫做“model”，然后呢，这里是“token list”，是吧？“token list”是一个token的数组。假设啊，那么我们如何来在这一步去完成模型的输入和得到模型的输出的呢？它是这么一个逻辑。这里呢，我有一个input，这个input是什么呢？就是之前token化的结果，拿到是一个什么？拿到是一个token的数组，对不对？好，这里我就不写了。数组对不对？好，这里我就不写了啊。这里肯定有一堆的数字。好，接下来他会进入一个死循环。然后首先调用裸模型，把这个input传进去。这里边是不是包含了用户的输入，还有包括那个你的系统提示词，用户的提示词全在里边了，是吧？好，传进去过后是不是就开始进行模型的一个数学运算？我们之前说过，对吧？这个东西是一个理论上的纯函数，输入决定了输出。那么这里就可以拿到它了，是吧？output。好，这里改换成prob吧，啊，表示概率分布，根据输入。表示概率分布，根据输入计算下一个投坑的概率分布，这是我们之前讲的，是吧？这概率分布大概是长什么样子呢？大概长这个样子啊。一个对象，对象里边加上下一个投坑，然后它的概率是零点三，然后再下一个投坑，然后它的概率是零点二，大概就这个意思啊。那么后面不行了，我们就拿到了是什么？拿到是这么一个概率分布。好，那么接下来呢？

---
