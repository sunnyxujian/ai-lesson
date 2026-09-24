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

## Scene 1

Time: 00:00:00-00:00:51
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_001_00-00-43.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_001.md`

Transcript:
实际上呢，现在的模型提供商啊，他的收费都已经很温柔了，知道吧？我这么跟你说啊，我不敢说百分之百啊，其实我认为就是百分之百，都是亏的钱给你做的，一点儿不夸张，他们赚不到钱的。好，咱们上节课呢讲完了这个裸model啊，就是裸模型，朋友们已经清楚啊，裸模型能干哪些事儿是吧？再回顾一下这张图哈，这就是裸模型能做的事儿，非常的简单，输入一串token，得到下一个token的概率分布。那么接下来我们来聊。那么接下来我们来聊裸模型的上一层，就是Model Service。这玩意儿呢，一般是由模型的服务商，他给你提供的一些接口。比如说谷歌的机器人，他做了一套模型出来，是吧？那么他如何对外发布呢？他往往是通过一个API的形式啊，一个API接口的形式给你发布出来的。那么当你要使用这个模型服务的时候呢，你往往需要通过一个HTTP协议啊去连接它的接口，得到它的模型服务。我们可以认为呢这个。

---

## Scene 2

Time: 00:00:51-00:03:02
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_002_00-02-54.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_002.md`

Transcript:
然后这一块呢，它是一个API接口的形式对外发布的。那么这个接口的规格呢，其实不同的模型服务商啊，它可能不太一样。呃，目前的主流的接口规格呢，分为三大类：一个是OpenAI这种，这种呢基本上现在是一个事实标准啊。因为这一块呢，就是模型服务商对外提供什么样的一个接口啊，通过什么样的地址得到什么样的数据，要传哪些东西，这种接口规。管用哪些东西？这种接口规格啊，目前没有一个权威的机构出来说啊。你们都按照我的来，不要自己去玩自己的。把这个接口规格统一啊，目前没有。说目前呢，遵循的是一个事实标准。因为OpenAI呢，虽然现在啊，它的模型能力啊已经不是排第一的，是吧？但是呢，我们依然尊重它的历史地位，它最早出现的。所以说，很多的大模型啊，包括国内的很多大模型，还有国外的很多大模型，他们对外发布接口的时候呢，都是依照这个OpenAI的这种API格式对外发布接口的。所以说，你看。对外发布接口的，所以说你看懂了这个open A I的接口规格呢，就已经掌握了绝大部分大模型的那个接口规格了。但是除了一些open A I的规格之外呢，还有一些特立独行的，像什么这个Cloud啊，他已经不让我访问了啊，我的地区又被限制了。还有就是谷歌的G P T，啊，他们有自己的接口规格。那么将来同学们如果说要去使用模型服务啊，就是通过API的形式，呃去对接这个模型服务的话，那么你要去自行阅读啊相关的官网的接口文档，看它的接口规格是什么。如果说官网文档。接口规格是什么？如果说它官网文档里面明确说了啊，我这套接口规格要兼容OpenAI，那你就去看OpenAI的接口文档就完事儿了。一般来说呢，呃，除了直接使用一个HTTP请求去请求这样的一个地址来拿到这个模型的返回，你看这里请求的是这个地址对吧？呃，发送一个消息啊，使用的模型呢是GPT五点四，然后呢发了一个消息过去，发那个消息过去呢，那边他就会收到一个响应啊，就是会给你返回一个响应，告诉你AI的响应结果是什么啊，就是这样子。那么就会完成了一次对。是什么啊？就是这样子，那么就完成了一次对话了，是吧？你刚发一个消息，然后呢得到一次对话，它里面咋说的？我们一会儿再说。但是我们使用上了就是发一段话，然后得到一个回复啊。这是不同的接口规格呢，就是像这些Cloud呀，还有就是Jetin来呀，它可能这里的给的呃路径不一样，或者头里边传的东西不一样，或者是这个请求体里边这些字段不一样啊。我希望啊，同学们看这个玩意儿要能看得懂啊。这个是啥？这个是原始的HTTP报文啊，请求行请求头。

---

## Scene 3

Time: 00:03:02-00:03:51
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_003_00-03-22.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_003.md`

Transcript:
B B报文啊，请求行、请求头、请求体，然后这边呢响应行、响应头、响应体啊，这里只给你列出来响应体，你要能看得懂哈。如果说你连这个都看不懂的话，我建议呢你现在还不是说学什么AI的问题了，你下来过后，先把这个东西搞定吧。这是咱们的福利课程哈，来你就完事儿了。我告诉你哈，无论你是学技术的哪个方向，前端也好，后端也好，还是什么测试运维也好，你这个网络层面你不搞定的话，你啥都玩不了，还学啥AI啊？跟AI就没啥关系了。这基础中的。跟一下就没啥关系了。这基础中的基础，核心中的核心哈。当然，除了这个网络课程之外啊，我们还有很多的其他的核心课程，都是咱们的福利课程。来领取完上了啊。这些核心课程你要先搞定了，过后，然后我们再去玩那些花里胡哨的。就好比说你要学框架，你得先学语言吧？你语言都不会，学啥框架呀？是吧？这些课程来找咱们领取啊。领取的方式，在咱们账号主页点击头像进入账号主页，根据提示领取完上了啊。好，这个玩意儿是。

---

## Scene 4

Time: 00:03:51-00:06:29
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_004_00-04-21.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_004.md`

Transcript:
你去玩笑了啊！好，这个玩意儿市场我就不解释了啊，我就假设你是懂网络的。呃，当然了，这些模型服务商啊，他除了对外提供这些API接口之外啊，他一般来说啊，还会给你提供SDK。啊，比方说非常著名的这个OpenAI的SDK，大家看一下吧。啊，都是OpenAI的SDK啊。呃，这套SDK呢，其实好处在于你就不用直接去写网络请求了啊，它被封装好了，你直接用就完事儿了。比方说你这里溜一个OpenAI的一个对象，然后呢，把API。再一个对象，然后呢，把API key啊，因为你要去调模型服务，肯定要去申请一个API key啊，它要基于这个key来付费的啊。再创建一个client之后呢，你就可以去用它来创建一次请求了啊。其实它就是给你封装了一次请求啊，你选择一个模型的名称，然后呢，这里呢，给它做一个提示词啊，怎么样怎么样，然后给它输入一句话，然后得到它的响应结果就是一句话啊，就是这样子。那我这里问大家一个问题啊，看大家能不能理解我刚才说的那些东西啊。假设啊，现在呢，你用的不是OpenAI，呃，你用的是什么呢？你用的是Timi啊。假设你用的是。是TMI啊，假设你用的是国内的模型，那么你通过TMI的官方文档已经知晓了，TMI是兼容OpenAI的接口的，它是兼容的。呃，当然它会给你提供它自己的API key啊，也会给你提供它自己的基地址。比方说它的基地址呢，我看一下我之前用的那个TMI的基地址啊。呃，比方说它的基地址呢是这个，啊，这是OpenAI的啊，自己看官网吧。好，比方说给大家看一下啊，它的说明。好。说明。好，你看，T M的官方说明里边，它明确说了，它提供基于A T T P的A P I服务，并且对于大部分A P I，它都兼容了Open A I。而且它可以提供了什么？它的基地址，就它的域名。因为我们知道Open A I那一块，它的域名是啥？域名是A P I点Open A I点com，对吧？那么你只需要把这个地方呢换成什么呢？换成它这个地方就行了。其他都一样，什么请求路径啊，还包括请求头啊、请求体啊，这些东西都是完全一样的。啊，当然模型的话要换一下啊。模型的话一般要去查阅一下它的模型列表。那么模型的话，你要。它的模型列表，那么模型的话你要填这些。好，你知道这些信息过后，我请问你，接下来你去请求的时候，你能不能参考open ai官网的请求接口来去发送TMI的请求，可不可以？是不是完全没问题啊？因为都是一样的呀，兼容的。你只需要把这个地方换了就行了，把这个模型换了就行了，其实都是一样的。好了，我再问你，他能不能去使用open ai的SDK？能不能？也可以。能不能？也可以，没有问题啊。因为open ai的SDK的话，它其实就是给你封装一个请求，你大配置一下一个请求基地址啊，在这里其实可以配置的啊，配置请求基地址，然后把kimi的API key写进去，然后创建请求的时候呢，你把这个模型给它更改一下，就完事儿了，是不是？所以说现在有那么多模型提供商，没有必要说一个模型提供商，你要把它官网文档全部读一遍，没必要啊，大部分都是支持open ai的SDK和open ai的API格式的，兼容的啊。

---

## Scene 5

Time: 00:06:29-00:07:21
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_005_00-07-13.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_005.md`

Transcript:
A P I格式的，兼容的啊。甚至呢，有些模型服务商啊，它不仅兼容Open A P I，它还可以兼容几个，比如说这个Kimi，它还可以兼容一个Answorpic。啊，在这里可以去搜索一下，就是Cloud。啊，你看这里，他说在编程工具里边去使用那个K two。那么在这里边呢，你看，它给你提供了这么一个地址，它把这个基地址呢给你换成了这个啊，后面给了一个后缀叫做Answorpic。也就是说，这个模型服务商啊，它既兼容。模型服务商啊，它既兼容OpenAI，同时呢，在另一个基地址，你只换成这个基地址。那么基于这个基地址的请求呢，它就兼容这个S R P。也就是说，它的请求呢，跟那个Cloud S N E T和Cloud O P U S，它的请求规格是一样的，都是兼容的。因此呢，将来你又去用一些别的模型的时候，你去读一下它官网的文档哈。关键是看它兼容哪些接口规格。兼容OpenAI，你就可以使用OpenAI的SDK；兼容那个S R P，呢，你就可以使用S R P的SDK，都可以啊。好，这些都是。

---

## Scene 6

Time: 00:07:21-00:09:02
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\keyframes\scene_006_00-08-36.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\3.认识模型服务接口\work\codex-notes\scene_006.md`

Transcript:
都可以啊，好，这些都是实操的层面哈，大概讲一下就行了。然后核心点来了，核心点是啥呢？就是说我们要聊的是这个模型服务，它模型服务它到底做了什么样的事情。现在的模型服务啊，它的这个接口啊，变化的非常的快，可能我今天录的视频，明天它又变了，它是处于一个不稳定的状态。而且呢，不同的模型提供商呢，它的接口呢又不一样，它能干的事呢也不一样。比方说现在OpenAI，它能干的事特别多，特别多，除了跟模型相关。多特别多，除了跟模型相关的一些服务之外呢，它还允许你上传文件，还允许你去创建什么skill。而且现在很多的模型提供商都可以允许你使用to，就是杂七杂八的一大堆。那么这一块，我要按照它的特性去讲的话，那就没有什么意义了。这些玩意儿，你们随随便便去看一下官网文档都能看得懂。我们学东西啊，一定不要去学细枝末节，细枝末节的话，需要的时候再去看，一定要抓住核心。那什么是核心呢？当我在学习的。什么是核心呢？当我在学习的时候，遇到这些问题的时候，我一般会这样处理：这是open ai的提供的服务内容，通过API暴露出去的。好，这是S R P K提供的服务内容。好，这是这个G M D提供的服务内容。我看啥，我只看这一部分，就是他们的交集。交集意味着啥？就是核心。就是你无论怎么玩，你百分之百一定会做的事情。这就是交集。其他杂七杂八的，变动也比较大。它杂七杂八的，变动也比较大。那么同学们可以根据你到时候实际的需求去查询一下相关文档，就完事儿了。那么这些模型服务商他们提供的核心是什么呢？自然就是封装模型的能力。它有很多接口，其实跟模型没有什么关系的，跟A S也没有什么关系，只是创建一些边缘的一些事情。好，我们来看一下它的核心在什么地方。就这个东西，它的核心能力就是：用户传入一段消息，用自然语言传入，然后呢，经过这个模型服务的A P I，里面装的啥事儿，先别管，你就能得到。

---
