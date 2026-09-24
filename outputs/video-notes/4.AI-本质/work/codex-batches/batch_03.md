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

## Scene 13

Time: 00:17:57-00:19:14
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_013_00-18-56.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_013.md`

Transcript:
那一条日志了。你可以看到，Cloud Code，他首先往这个模型这里发了这么一条消息啊，请出的是这个地址，请求头乱七八糟一大堆。然后看一下请求体，请求体传递的是一个json格式。首先，同学们看一下，我们现在有没有向那个Cloud Code在这里边写任何消息啊？没有是吧？说明啥？看一下之前这张图啊，说明我们上边的用户，不管你填没填消息，都要经过这个。填没填消息，都要经过这个AI application，就是AI应用给你进行封装一层，它有可能给你加入额外的消息，有可能你啥消息都没写，也会向模型给他发送一段消息。那我们可以简单的看一下啊，这个消息的内容是啥。好，走，我们把这个复制一份儿。好，然后这里去建立一个接生啊，走，保存一下啊，给他发送一个消息啊，简单看一下吧，这里边有啥东西。好，首先呢，给他传递了一个用户的消息啊，就是一个测试的赋，他测试一下这个模型通不通。然后呢，给他传递的。一下这个模型通不通？然后呢，给他传递了一下这个tools啊，这个tools的概念呢，我们后续会讲啊。好，在这些tools里边呢，我们可以看到啊，有这么一个tools叫做skill，它在描述啥呢？它在告诉AI模型，什么叫做技能，技能的是什么意思，技能的含义是啥？然后呢，同时也约定了AI模型说，如果说你要将来要使用一个技能，你要给我传递什么东西，肯定是要有技能的名字是吧？呃，然后呢，有一些参数怎么去传递，它就在描述这个。

---

## Scene 14

Time: 00:19:14-00:21:12
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_014_00-20-45.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_014.md`

Transcript:
怎么去传递？他就在描述这个。那么这个传递过去，AI模型是不是就知道了技能是啥？然后呢，如果说我要使用技能，应该怎么来回复消息，对吧？我们现在啥都没做。那么这个AI应用他就把这个消息传过去了。好，接下来我们来写个消息吧。你是谁？好，看他的回复啊。好，他说他是Cloud Code，啊，是一个什么CLI工具。但是这个信息是谁回复的？那肯定是模型回复的呀。但是我明明用的是。是模型回复的呀，但是我明明用的是T M模型，为什么他会回复我这个消息呢？是不是很奇怪？那你看一下他的请求啊，他给加了一大堆请求，没关系，我就随便看一个啊。好，我们把这个请求体啊，还是来复制一下，便于同学们看得清楚一点啊。我们这里乱七八糟一大堆，好，来看一下啊。我们在这里去搜索一下，你是谁？就是我们的题的问题，你看，这是给A I发的消息，你是谁？但是A I只收到这个消息了吗？并不止，他前面还有消息，你看这一段。它前面还有消息，你看这一段，这一段是啥呢？这一段是我们工程里边的那个Cloud M D五这个文件，看到没？是不是这个文件？之前是Cloud这个官方怎么说的，就是这个文件，是不是在每一次消息发送的时候都会带过去？你看是不是有有带过去？这是我文件里面写的一些规范之类的东西，它给带过去了。那么除此之外，还有没有带东西过去呢？还有，你看这个System Reminder，就是系统提醒，这就是Cloud Code这个工具给你加的消息。它这里边说，首先告诉了。他这里边说：“首先告诉了A I，我有哪些技能是可以用的。我有这么一个doctor compose的技能啊，还有这个skill create的技能，就是我写的那个技能的MD是可以用的。你看技能是怎么带过去的，技能就是提示词啊，给它带过去的。还有什么技能？还有这个web design guidelines。每个技能后面有描述，看后面都是描述。告诉A I，我有哪些技能，什么时候你要去使用那个技能。这个描述就是告诉A I，什么时候要去使用那个技能。至于说怎么去使用。”之后要去使用这个技能。至于说怎么去使用技能，所以之前告诉过A I了，要返回什么样的消息格式来去使用技能。说技能是不是非常简单，就是个提示词。好，除了这个消息之外，你看下边的系统提示词里面还有。这里又得告诉A I你是谁，你是一个可交互的可利用工具。是刚才我问他你是谁的时候，他是从这里边找到答案的。这是来自于Cloud Code的工具给A I喂的提示词。再回过头来想看一下，我们玩的那个。

---

## Scene 15

Time: 00:21:12-00:22:30
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_015_00-21-51.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_015.md`

Transcript:
看一下，我们玩那个Studio，包括什么那些工具在干啥，就在控制输入什么给模型。那么接来看第二个，它如何来处理模型的输出的。咱们又来一次啊，把这删了。呃，我举个例子哈，比方说，他怎么来调用技能的。呃，比方说这个技能吧，呃，他说，当你去使用这些语句的时候呢，他就会去调用这个技能。好，咱们就使用这个语句啊，走。走，来看一下。好，你看他现在调用技能是吧？他已经成功的加载了技能。我们看一下他这个过程是怎么样的啊。好，那么这里他在询问你啊，他肯定是读过这个技能文档过后，他才能知道应该询问你使用哪一种方案啊。我现在不去选择了啊，我们来看一下发那个请求是怎么发送的。好，来看一下啊，咱们的请求是那个review是吧？review邮箱。好，你看，都是我们用户发的请求，文本是review邮箱。现在首先问。是rev u u叉。现在首先问大家：AI，他知不知道有哪些技能？现在模型知不知道？模型它是知道的。之前是不是看过了？给他告诉他的对吧？我们系统里面有哪些技能？他是知道的。而且他也知道什么时候要去使用技能，对吧？那么现在用户发了这个消息，他是不是应该使用技能了？那你看一下AI给我们的是什么样的回复啊？呃，我们来收这个点赞啊。因为我们那个技能的名字叫做“web点赞”，是吧？来收一下这个点赞啊。好，你看一下这里啊，在这里，这是AI的响应。

---

## Scene 16

Time: 00:22:30-00:23:46
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_016_00-23-39.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_016.md`

Transcript:
这里啊，在这里，这是AI的响应啊，响应呢，它也是通过ATTP来响应的。为什么是这种格式呢？同学们，你们见没见过这种格式？这个东西格式叫啥呀？这个格式呢，叫做S S E啊。它是流式传输啊，它每次传输一段，你看，每次传输一段。呃，我将使用Web Design Guide，看到没？它这里对应到哪儿？是不是对应到这儿？啊，它只是一个回复而已。那么现在真正的技能调用，是不是要满足某一种格式？之前是不是看过的，见过某一种格式。之前是不是看过的，见过某一种格式的？就是当时我说，就在最开始的时候，是不是告诉过AI，当你要使用技能的时候，要给我返回一种节省格式，是吧？好，那你看一下啊，它节省格式在哪里调用的，就在这里。它继续响应。前面的是自然语言响应，完了过后，接下来它响应的一个是，通过use使用工具，什么工具呢？使用了一个技能工具。哎，这个东西是还记得不？不好意思啊，刚才把那个日志已经删了啊，看不到了。刚才那个日志里边，最开始的时候，是不是告诉他我有哪些工具？其。就是告诉他：“我有哪些工具？其中一个工具名字叫技能。当你要使用技能的时候，你要给我传一个接生，看到没？啊，因为它是牛式的啊，它隔开了。你看这个接生的大括号，看到没？然后呢，使用的是一个skill，然后后边肯定有skill的名字在哪里呢？在这里啊，web design guide，这是技能的名字，拼接好了。那这样子一来，这个clou code是不是就可以拿到这个模型的响应？来看一下这个流程啊，用户。”

---

## Scene 17

Time: 00:23:46-00:24:54
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_017_00-24-38.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_017.md`

Transcript:
流程啊，用户有一个输入，发给谁？发给Cloud Code了。Cloud Code接受到的输入加了一大堆系统提示词，发给什么模型？那么这里除了有用户的输入之外，还有什么？还有就是各种提示词。那么这个提示词里面就包含了技能，我有哪些技能？你到时候要使用技能的时候，你再给我回复什么。某些一起就传给模型了。好，模型这。就传给模型了。好，模型这个时候叫判断用户的输入，模型拿到的是什么，拿到什么输入，这个东西加上这个东西，对吧？那么这个时候模型就要进行判定了。那么这个时候到哪儿了？说到这儿了，到这个模型啊，模型最底层的模型层了啊。那么到这儿了过后，是不是还要判断我要不要使用技能？如果说不使用技能的话，比方说一开始我问的是你是谁，他跟技能没关系，他就正常输出就完事儿了。如果说要使用技能，要决定使用。要使用技能，要决定使用技能。过后，他会返回来是一个什么？返回来是一个接生。这个接生要告诉什么？告诉Cloud Code技能调用，我要使用某一个技能，传给谁了？又传给Cloud Code了。看到白，就是在这里进行响应的。我要使用这个Web Design Guide这个技能。好，那么接下来Cloud Code拿到这个响应过后，他又是怎么处理的呢？他不会直接给用户什么消息，他会进一步。

---

## Scene 18

Time: 00:24:54-00:26:27
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\keyframes\scene_018_00-26-05.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\4.AI-本质\work\codex-notes\scene_018.md`

Transcript:
库什么消息？他会进一步去读这个技能文档，这个能不能读？它是个本地程序啊，肯定能够把个技能文档读出来呀。你看一下有没有读到这个技能文档，咱们来搜一下这个技能啊。呃，这个技能，注意啊，看一下，可以进去。这个技能在这儿啊，我们就随便搜一句话吧，比如说这一句话啊，这是我们的一个技能，看到没？we be t in guidelines，技能文档里边复制一下，然后到。复制一下，然后到这边来搜索一下啊。你看，现在要使用技能了，看到没？那么这个时候，Cloud Code就会把技能的全文读出来。一开始有没有给他全文？没有。一开始只是告诉啊，我有哪些技能。你要使用的时候，就会把技能的全文告诉你。你看这里，这就是技能的全文，就把文档里边所有东西全部读出来，把文件内容读出来。读文件不复杂吧？然后一起扔给AI，让AI去进行后续的处理。那也就是说，Cloud Code会怎么样呢？会把技能。会把技能完整文档又传给模型，然后模型去进行后续处理，然后最后呢，模型的东西又传给cloud的，然后又传给用户。那么于是呢，用户就看到了这个提示啊。好，捋一下这个流程啊。整个流程，你看一下哪些是在给模型输入，这里是不是给模型输入？为提示词，哪些是在处理输出？这里是模型输出。再处理输出，这里是模型输出，然后克劳克的做后续处理。什么后续处理呢？又重新去调用模型，给它完整文档。然后这是模型的输出，输出给克劳克的，克劳克的再给用户。看到没？这就是个完整的闭环。你通过这个代理服务器就可以非常清楚的看到，它传了什么东西给模型，模型又吐出来啥，它又是如何来进行后续处理的。但我再次重申啊，我讲的是skill嘛，不是我后面讲的。

---
