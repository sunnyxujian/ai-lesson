# Video Notes Codex Batch

Inspect every referenced image and use the transcript as the factual source.
Write one file per scene to the notes directory. This is faithful light polish, not summarization or article rewriting.
Video mode: demo. Preserve the procedure in executable order. Describe the visible UI state, action, input, and resulting state; prefer a completed result frame over a transient cursor movement.
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

Notes directory: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes`

## Scene 7

Time: 00:10:30-00:13:06
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_007_00-12-50.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_007.md`

Transcript:
量啊，单个数字，他也不知道啥意思，反正就是说算出来的，好吧。好，那么现在我们就要研究了，是什么东西在影响这个结果。因为我希望的是啥呢？我希望给你一个数字，你要算出来一个东西，这个东西一定得有现实意义，对吧？你虽然不知道现实意义是啥，但是我们人知道啊，我在不同的领域里面，现实意义不一样，对吧？图像识别的领域和在我们这个心智预测的领域，它的意义不一样，每个领域的意义都是不一样的。但是呢，我就希望你给我这个东西呢，是符合我这个领域里面的预期的。不同的领域，他预期肯定是不一样的，所以不同的领域，他有自己的。预期肯定是不一样啊，所以不同的领域它有自己的模型啊，对吧？但是如果说我不加控制的话，你就说乱来了，就完全没有意义。所以说接下来我就要研究是什么东西在导致这个输出结果变化，对吧？哎，什么东西在变化，我就可以去调控那些东西，对吧？好，是什么东西在导致变化呢？首先输入值能不能调控，输入值是人给他弄进去了，对吧？那不同的情况，今天我问的是二零二五年程序员收入三十三万，哎，那我可能有一天问的是二四年做前台的他收入，然后请你预测下一年是啥？就每次给他输个东西。那下一年是啥？这每次给它输入的东西不一样，这个东西你打个调控的，没法调控。这是输入值，对吧？这是你不可控的。你可控的是什么呢？可控的是这个W一、W二，直到Wn。那么这一块叫做权重，它每个都是数字。权重代表是什么意思呢？代表的是每一个信息维度啊，它的重要程度。比方说这个年费有多重要。比方说你看我算出来啊，假设就是二十五，我们来算：第一个W一乘以二十五，然后呢加上呃W二啊乘以十一。w二啊，乘以十一啊，加上w三啊，乘以三十三啊，加上一个b啊，b我会再说。好，w一这一块，假设我们是一个零点三，那说明啥？它不是很看重年份，是不是？然后这一块，比方说是一点二，哎，它比较看重什么？比较看重你是什么行业的。啊，然后呢，这一块，假设是零点八，哎，比较看重你之前的薪资的水平啊。假设啊，假设是w一、w二、w三，是这个值，哎，是不是？通过这三个值就可以去调控它的输出，看到没？调控它的输出，看到没？哎，我只要改动一下这个，改小一点，是不是这个值的影响就很小了，对不对？对输出的影响很小。哎，这个值呢，调大一点，哎，这个对输出影响就很大，是不是这意思？我就是瞎写的啊，我就全是瞎写的，就是权重的含义。那么权重到底是取多少，不知道，不知道是多少，这个需要调控的。我们说一个神经元到底能不能输出一个正确的结果，很大程度上就取决于它的权重。为什么说它的结果对了，是因为它权重调对了，对吧？权重调对了，哎。重调对了，对吧？权重调对了，哎，我给他任何数据，好像这个结果都是对的，都是OK的，都是还比较接近现实情况的。哎，我给他任何一张图片，啊，图片的数字给他，哎，他都是能预测出来，给我一个正确的那个呃物体的ID啊。我去查那个ID，一查，哎，确实是，这是个图片是狗，那个图片是猫，哎，确实是对的。哎，我就希望这样子能懂那意思吧？哎，我就希望是能够去调控这个玩意儿，能够让这个神经元，哎，能够达到一个我们预期的一个。

---

## Scene 8

Time: 00:13:06-00:15:08
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_008_00-13-36.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_008.md`

Transcript:
能够达到一个我们预期的一个输出结果，好吧，这是那个权重。那么这个B E是什么意思呢？这个B E呢叫做偏置，偏置又是什么含义呢？你看哈，我们最终的这个y哈，这个y值，它能代表什么呢？它代表是个标量，对吧？我们刚才说了，零点二，它是个标量。这个标量呢，我们要求它是不能小于零的，必须是正数。呃，为什么不能小于零呢？这也是背后有它的数学原理啊。但是呢，我不打算去讲它的数学原理，我讲一个比较直观的，你们能够理解的。什么呢？就像生物学一样。能够理解的什么呢？就像生物学一样，生物学呢，它就有这个特点，就是你给我输入没问题，我接收输入。但是呢，你输入过后，我发现哎，跟我没关系。因为大脑上有很多的神经元，对不对？现在你在听课，哎，一些跟逻辑、语言相关的，跟计算机相关的神经元，现在在疯狂的去工作，他们在激活，在做事情。但是有很多神经元是在休眠的，不干事儿的。比方说，跟你什么吃东西的神经元，跟饥饿相关的神经元，现在工作吗？不工作。跟玩游戏相关的神经元，现在工作吗？不工作。跟看小姐姐跳舞。现在的工作吗？不工作。跟看小姐姐跳舞的神经元，现在工作吗？不工作。那个是沉睡的。但是呢，他有没有接收到信息？他其实有接收到信息。我现在不停地跟你说话，通过声音一传播过去。他有没有接收到信息？他有。但是呢，他不输出，他不工作，他沉默。我们就把这种状态叫做未激活。这个神经元没有激活，它沉默的。你给我信息，但是那个信息好像跟我没关系。啊，我就沉默，懂了，意思吧？这叫激活状态。所以说，神经元的输出值呢，也叫做激活值啊。就是我们这里输出的Y。如果说你输出Y。我们这里，复数的y。如果说你复数y算出来，假设啊，假设这里的权重，权重是可以有负数的。假设算出来是一个零，那就表示你给我有信息，跟我没关系，我不啊，我不干活。只要未激活，那么也就是说，它有零就表示未激活了。那么负数，它就表示，比方说负负十，那跟零是不是一样的？跟零是一样的，它都表示不激活。所以说负数呢，容易干扰我们的运算啊。呃，因此呢，我们往往是要把一些负数去掉的啊。所以说呢，嗯，假设啊，我们现在一会儿再再说怎么来去掉啊。你理解激活的含义了吗？就是它有激活。激活的含义呢？嘛，就它有激活呃和不激活。当激活的时候有有多激活的吧，比如零点二，有点激活了；，哎，零点五，也比较激活了；，也可能一百，就相当激活了啊，就非常活跃了啊。当然一般来说，也不太会取到一百那么大的数字啊，一般就是几个数字。好，也就是说，它有一个激活度，要么就不激活，不激活就是零，完全不激活，完全休眠；，要么就是有一点点激活啊。这是激活的含义。好，你理解了激活的含义过后呢，你再来理解这个B，这个B是什么呢？

---

## Scene 9

Time: 00:15:08-00:16:22
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_009_00-15-45.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_009.md`

Transcript:
来理解这个B，这个B是什么呢？叫偏置，就是有些神经元啊，它可能有这么一个特点，就是我必须要大于十，就这个结果我算出来大于十，我才激活。哎，有些神经元它就有这个特点，有一个阈值，就像一道阀门一样，你没有超过阈值，我睡吧，睡吧。在现实世界，我怎么可以解释呢？呃，就是你要说饥饿的话，每一个点你可能都有都有点饥饿，对吧？刚刚吃完饭，你说能不能吃下东西，还是能吃得下的，对不对？但是呢，这个饥饿，它一定要达到一个阈值过后，你才能感觉到，才激活了，感觉到，哎，我要吃东西了，是不是？它有一个阈值啊，这个偏置呢，就可以。它有一个阈值啊，这个偏置呢，就可以这样理解。比方说，我要这个算出来的数字，我可能，当然在不同领域，它的含义不一样啊。我再说一次，我算出来一个数字，可能要达到某一个值过后，哎，我这个神经元才激活。那我这个偏置呢，我就可以把它设置为减十，你必须要大于十，你没有大于十。比方说，这里算出来值有个五，五减十，哦，不行，激活不了啊。就是可以通过这个偏置来进行调节。那比方说，有些神经元，我负十，我就可以达到激活状态了。那么就是假使，那前面哪怕一双。那么就是假使，那前面哪怕你算出来是一个负十，那我这里假使也可以到达零的状态，对吧？或者是呃你再多一点点，我就马上就可以激活了，是这个意思，能理解吗？能不能理解啊？这是偏置这个东西，你知道它是什么意思就行，大概知道什么意思。这个玩意你不能求甚解啊，因为一求甚解的话，我就得讲它的背后的数学原理了，这这就有点恼火了啊，没必要啊，没必要。你能大概理解它啥意思就行了。好，那么最后说一下这个激活函数是什么意思呢？这个激活函数其实就是对注意。

---

## Scene 10

Time: 00:16:22-00:17:12
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_010_00-17-07.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_010.md`

Transcript:
激活函数其实就是对最终的这个结果呢，来做一个简单的一个处理。这个处理的方式有很多，比方说之前最著名的一个激活函数，虽然现在不怎么用了啊，现在都是用一些更加复杂的函数了。但是这个函数其实很有用的，以前长期霸屏了很久的啊。这个函数的做法呢，就是激活函数有很多种啊，有非常多种。激活函数呢，就是把你最终这一坨的求的值，哎，跟一个零来求最大值，就是我刚才说的，以小于零的没意义，有啥意义呢？没意义，有啥意义呢？这个你负十，我就直接给你取零了，就这么简单。这激活函数，其实现在的做的这些激活函数呢，道理差不多啊，只是呢加了一些更复杂的一些东西在里边，比如用它也也没有啥问题，特别是训练一些小模型的时候，也没有啥问题。过去一直在用它，跟零其实最大值，负数不要了，直接给砍掉啊，直接给砍掉负数。长期在用这个啊，啊，这是激活函数，简单吧。再来看一下这个公式，是不是就没有那么复杂了？哎，权重乘以每一个输入加起来，然后呢加上一个。

---

## Scene 11

Time: 00:17:12-00:18:26
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_011_00-18-19.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_011.md`

Transcript:
输入加起来，然后呢加上一个偏置，然后呢通过一个激活函数就得到了最终的输出结果。这就是一个神经元的模型。好，接下来我给你看一个界面啊。我做了一个网页，这个网页呢我给你写到make file里边了啊。make file里边呢，你首先安装依赖啊，用那个make install安装依赖啊，在这里边啊，我是用R E X做的，因为之前呢我其实想用那个就是M S P L O T来做。Max Plus来做，但是发现了Max Plus做这个东西吧，有点实在太难为他了。我就用前端做了啊。不管你懂不懂前端都无所谓，的你直接运行出来看效果，只是为了学习方便的啊。Mac的来运行出来看效果啊。好，打开看一下，啊，这里，看一下单个神经元的工作原理。好，你可以把这个玩意儿呢理解成一个神经元。假设这个神经元它接收三个输入x一x二x三，啥意思不知道，对他来说他啥都不知道，他只知道我收到三个数字。好，但是。我收到三个数字，好。但是我们人可以规定啊，人可以规定。哎，你假设X一表示什么？表示你的年收入多少万一年啊，比如说这里呃三十万一年。好，然后呢，你的信用分是多少呢？比方说第二个参数，比如人为规定啊，信用分是那个，比如七百五十分。呃，负债率，你比方背负了房贷啊、车贷啊、贷款对吧？负债率啊，你不用管，负债率怎么算的，反正是个数字嘛，对吧？好，负债率的百分之三十。哎，我给你输入进去，那就作为X一、X二、X三。我给你输入进去了。好，那。

---

## Scene 12

Time: 00:18:26-00:20:04
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_012_00-19-15.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_012.md`

Transcript:
我给你输入进去了，好，那你内部在运算的过程中是不是要有这个权重，对不对？啊，有w一w二w三，是不是还有个偏置b，对不对？哎，这些东西就是你可以调节的了。你看看我们的公式，我把公式给你截图，所以说是解出来。啊，一起解吧。好，你看啊，这个公式里边x一。看啊，这个公式里边x一x二到xn是外界的输入，这个你咋调控呢？对不对？这个跟你的智能没有半毛钱关系，你咋调控呢？调控不了。你能调控的唯一的东西啊，只有w一w二一直到wn和这个偏置。那个激活函数是固定的，定下来的，定死的。在设计这个神经网络系统的时候，一开始有定死的，不可改变。所以说这个函数你就不用管了，你没法调，对吧？你能调的就是权重和偏置，你只只能调这个，只能调这个。那么现。只能调这个。那么现在我们要让这个神经元要有智能，得怎么办呢？是不是只能去调控这个？假设三个x是固定，输入固定，我希望这个输入里边产生一个预期的输出结果。啊，假设这个结果，哎，是什么意思呢？表示的是，哎，我的贷款的审批通过率应该是多少啊？这个值越高呢，就是我越应该给他通过贷款；这个值越低呢，我就越不应该给他通过贷款。假设小于百分之五。给他通过贷款，假设小于百分之五十，我就绝对不能给他通过了。哎，大于百百分之五十呢，我根据这个利率来看，能给他贷多少钱啊。假设我们是一个贷款的智能审批手续啊，啊，讲他带有智能的。哎，我们现在人为的一些专家肯定能够知道啊，你这个情况他到底应该是一个什么样的一个结果。但是呢，我现在要让这个审计员自己能够预测出来。那怎么来预测呢？我只能调这个，我发现他这个结果不对，我能调的只有一件事，只能调权重。我调第一个权重看一下，调第二个权重。

---
