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

Notes directory: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes`

## Scene 7

Time: 00:10:05-00:11:19
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_007_00-11-11.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_007.md`

Transcript:
就可以算出来了。你做题嘛，做这个数学题，能不能做嘛？能做啊。那现在可以就是把这一千个值拿到，对不对？拿到这些像素点的颜色信息，还是很好拿的嘛。挨着的算，你算吧。你算个五六天，应该能把第一个神经元算完，然后接着算第二个。你计算吧。但是你是不是可以算嘛？好，那么这样子是不是可以算出这一层所有的数值，就是得到的结果，是不是可以算出来？对不对？好，又来这一层，每一个都是随机的啊。像这个第二个神经元同样的算法，第三个神经元同样的算法。神经元同样的算法，第三个神经元同样的算法。每个神经元它有自己的权重，不同的权重，不同的偏置。但是这个函数都是一致的。然后呢，输入都是来自于上一层的输入。也就是说，对于这一层的每一个神经元来说，它接收到的x一、x二到x八全是一样的。但是呢，每个有不同的权重和不同的偏置，所以说每个算出来的结果是不一样的。好，那么就算出来了这一层的所有的神经元，是不是全部算出来了？好，算出来了过后，接下来是不是又到下一层一样的过程？你可以暂停想一想啊。一样的过程，你可以暂停想一想啊。那下一层的是不是又来一次？好，下一层又来啊。那就是w e，就有他自己的权重，对吧？又是随机的啊。w二加到什么呢？加到w十六，是不是加到这里？因为上一层有十六个输出嘛，是不是加到乘x十六？我们可以看到，就是每一层的神经元它有多少个权重，等于什么呢？等于上一层有多少个输出。上一层有十六个输出，那么这一层每个的权重就得有十六个。上一层有八个输出，那么这一层的权重就得有八个。你可以暂停想一想啊。好，那么这样子是不是？

---

## Scene 8

Time: 00:11:19-00:12:31
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_008_00-11-55.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_008.md`

Transcript:
可以让你想一想啊。好，那么这样子是不是又算出这一层的结果，对吧？好，这一层的结果过后，又到下一层。那么下一层的话，是不是又可以重来一次，又来算出一个结果，对吧？又基于上一层，上一层就是输出层的啊，就最终结果了。那它也是一样的，没有什么特别的，也是权重乘以输入，对吧？输入就是上一层的输出嘛，上一层的输出就是下一层的输入。啊，那么这里就乘到它，也是乘到十六，对吧？一共有八个神经元嘛，就这个计算过程要八次。这第一次。Human Rights Watch is a non-profit organization that works to protect and promote human rights around the world.计算过程要八次：第一次、第二次、第三次、第四次、第五次、第六次、第七次、第八次，对吧？是不是可以把这一层的所谓的输出的东西算出来？对不对？好算出来过后，是不是数字有大有小？好，那么接下来就是要给输出层定义了。我们之前说过，对单个神经元，它输入到底什么意思啊？它输出的又是什么意思啊？还记得吗？我们上节课说的，它输入的到底这个玩意儿是啥意思？它输出的又是啥意思？谁都不知道，他自己根本不知道是啥玩意儿。反正他就接收数字，有输出，运算过后输出，他自己有智能吗？像我们人一样，有意识吗？你给我找上。我们人一样，有意思吗？你告诉我，长上哪来的意思呢？这就是输入、输出、输入、输出。它输出到底啥意思？是我们人为规定的。那么假设呢，我们这里呢，到最后一层，我们认为它的输出什么意思呢？越数字越大。你看，我这里输出层一共给它安排了十个神经元。为什么呢？输出层的神经元和这个输入层的神经元要设计，对吧？输入层的神经元，我们刚才说了，比如我们训练的图片像素多和点，我就设置多少个输入。那有些说，那有些图片像素尺寸不固定的图片，我要一起训练怎么办呢？那就要把归一化。

---

## Scene 9

Time: 00:12:31-00:13:19
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_009_00-12-55.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_009.md`

Transcript:
我要一起训练，怎么办呢？那就要把归一化。比方说，你假设你训练的神经网络，你最大可以接受的图片大小啊，比如说分辨率是幺九二零乘以幺零八零，那么应该有多少个神经元输入层？就应该有二百零七万个神经元。那个神经元确实有点大啊。所以说现在呢，训练图片的那一块，会做一些处理啊，就是把它变小。怎么变小呢？比方说举个例子，就题外话了啊。我训练图片的时候，干嘛一定要把整张图片拿来训练呢？我干嘛不把这个图片呢切分成很多小块来训练呢？是吧？我就可以把神经元缩小。小块儿来训练的是吧？我就可以把神经元缩小一点。那如果说你一定要整体训练的话，那你就得有二百零七万个神经元接收输入，那这个就很大很大了。有点太夸张了。呃，那么如果说它没有满足这个分辨率怎么办？拉伸，你拉到这个分辨率，或者你不拉伸。我点亮的时候，剩下的一些神经元就不点亮呗，对吧？就只点亮一部分。那超过这个分辨率，做什么呢？做裁剪、压缩。你压到这个分辨率，那些都是题外话。反正这个神经元的输入层的基本上是固定的啊。你有些特殊情况呢，不固定的，到不在我们这个讨论范围之内。好吧？呃，好。

---

## Scene 10

Time: 00:13:19-00:14:58
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_010_00-14-08.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_010.md`

Transcript:
我们在这个讨论范围之内，好吧？呃，好，这里说到哪儿了？就是输入层的神经元数量要设计，那么输出层也要设计，因为这个输出是结果，你要赋予它意义的。好，那么我们刚才看到，输出层它也就是按部就班的运算，对吧？得到一个结果。那么这个结果有大有小，我们就可以这样定义：这个结果越大的呢，比如七，这个第七个神经元它结果很大，最大的。那么我就认为这个数字识别出来是七的概率是最高的。哎，这个四，它很暗，它输出的数字不大。那么我就认为四。但是输出的数字不大，那么我就认为是这个数字呢，概率很小。我就给它人为定义，纯粹是人为定义啊，这个东西都是人为定义的，人为定义它的意义。比方说，给它一个数字七，我就期望说，哎，它输出七的概率是最大的。当然，它输出的是概率吗？输出的可能是一些几千、几万的数字啊，你不知道是什么数字，输出它不一定是个概率。那么这个时候呢，一般会用一些数学手段啊，用一些数学工具，比方说一个著名的数学工具叫softmax，这个函数。这个函数呢，可以把任何一组数据全部转换成百分比。你有兴趣的话，可以去。全部转换成百分比。你有兴趣的话，可以去了解一下这个工具是怎么去实现的。它可以把任何一组数据，不管那个数据有多大，它可以把它转换成百分比的格式。那么我这里呢，就用到了这个工具。它实际上输出的结果不是这个结果，但是呢，我就把转换成百分比显示到这儿了，懂我意思吧？啊，你就可以这样想象吧。假设它输出的是都是零到一的结果，那么七，那可能就是零点一四六，对吧？那么就是算出百分比的话，就是十四点六。那么它的可能性就最高的啊。当然这里是凑巧啊。嗯，实际上这里是全随机的。它怎么可能是编得出来的？全是简单的数学运算得出来的全是简单的数学运算，而且那个权重偏置全是随机的，他怎么可能识别准确的？他不知道在干啥，只管算，要算出来是是啥就是啥，完全是散裂的，完全没有任何意义。算出来的，那么只是说明他算错了嘛，对吧？我们告诉他算错了，怎么告诉他？那不是这节课要讨论的问题。我们这节课只讨论整个的神经元，从输入层一直传递到输出层的整个过程。我们就是演示这个啊。你可以在暂停视频，想一想啊，再回忆一下他是怎么做的。整个过程有一个专用名词。

---

## Scene 11

Time: 00:14:58-00:16:39
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_011_00-16-10.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_011.md`

Transcript:
整个过程有一个专用名词，叫做前向传播。我们这里和讲的是什么？前向传播。前向传播是我们训练神经网络的第一个阶段。你先让它跑一次，对吧？给他一个数据，让他跑一次，跑出来，那肯定是乱七八糟的。跑的结果。那么后边我们再调。啊，这是你第一个要认识的名词啊。第二个，你会发现整个过程啊，从输入到最终输出。输入我们没法控制，对吧？整个神经网络，它能怎么知道它会输入啥呢？输入是我们的数据。当我们输入固定的时候，听好这句话啊。当我们。的时候，听好这句话啊。当我们输入是固定的时候，是什么东西在影响这个输出结果呢？是什么东西啊？想想上一课的神经元。当我们输入固定的时候，是什么东西在影响单个神经元的输出结果啊？是不是权重加偏置？那么在神经网络里面呢？神经网络里面，当输入固定的时候，是什么东西在影响这个结果呢？是不是整个网络里边每一个神经元啊？除了输入层，输入层是没有神经元的啊。第零层是不带神经元的啊。除了输入层。带神经元的啊，除了输入层之外，其他的隐藏层包含输出层，是不是每一个神经元都有自己的权重，自己的偏置，是不是？整个神经网络这些权重和偏置，整个的集合，它们在共同影响着注意中的输出结果。你要调整这个输出结果，你就可以想象得到，它有无数个这样的一个旋钮，非常非常多的旋钮，在进行调整。非常非常多的旋钮，在进行调整。调整每一个旋钮，都对整个神经网络的输出结果造成一定的影响。所以说，这个是人来调吧，肯定不是人来调啊，他会自己调。怎么来自己调？我们下节课再说。懂的意思吧？啊，这就是整个神经网络它的这个权重和偏置。当输入固定的时候，权重和偏置唯一的影响着输出的结果啊。因为一个神经元的亮度，对吧？是不是就会影响到后边的所有的神经元？同时后边的所有的神经元，它自己的权重和偏置又会影响到它的输出结果。然后它的输出结果又会。

---

## Scene 12

Time: 00:16:39-00:18:34
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_012_00-18-02.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_012.md`

Transcript:
它的输出结果，然后它的输出结果又会影响到后边，就是这种影响是传递性的。那最终呢，我们整个神经网络的权重偏置都影响到输出结果了。那么朋友们可以算一下啊，像我们这个简单的网络，有多少个神经元呢？就是你念一个四十乘四十的图片，那么输入层有多少？一千六百个，对吧？输入层有没有什么权重偏置？没有啊，它就是输入东西的，有一千六百个输入。好，我们算权重偏置，我们从这一层开始算。那么这一层有多少个权重偏置呢？能反应的过来吗？你。Humanoid Robot Design and Control有多少个权重？偏置呢？能反应的过来吗？你先看第一个神经元。第一个神经元有多少个权重？我们刚才说了，每个层的神经元的权重的数量等于什么？等于上一层有多少个输入，上一层有多少个传过来。它每一个传过来一个x，我们不就得搭配一个权重嘛，对不对？所以说这个由于上一层是1600个，所以说这一层的每一个神经元都是一千六百个权重。那么也就意味着一千六百乘以什么？几个神经元？有十六个。这就是这一层的权重。那么这一层的。这一层的权重，那么这一层的偏置呢？有几个？偏置呢？就是一个神经元一个嘛，那就是十六个。那就这一层的东西啊。那么下一层呢？是不是一样的？下一层等于什么？下一层等于每个神经元有多个权重，是不是？上一层有十六个，对吧？那么这里每一层就是十六个权重。有多个神经元呢，十六个，然后乘以十六。那有多个偏置呢，就是这个偏置b啊，那么也是十六个，对吧？加成十六。好，输出层呢？输出层每一个神经元多个权重，是不是？上一层有十六个，那么每个神经元有十六个权重。输出层有几个？一个神经元有十六个权重，输出层有几个？神经元呢？有十个啊。然后呢，再加上输出层的偏置，十个。这就是我们这个神经网络啊。因为这里输入层中只花了八个啊，没发多，一千六百个。在我们这个神经网络里边，一个非常简洁的神经网络里边，有多少参数呢？有两万六千多个参数，不多啊，不多。知道吧？我们平时看到一些大模型有多少个呢？像那个DeepSeek，对吧？是有一点五万亿个参数。现在知道参数什么意思了吧？参数就是什么。知道参数什么意思了吧？参数就是什么？参数就是权重加偏置，就是一个神经网络的参数，就是这个意思。啊，最后呢，我们来看一下一些数学公式。这个数学公式作为了解就行了啊。因为讲这个数学公式的主要目的呢，是我要引出一个点啊，其他不是很重要。因为你即便是不看这些数学公式的话，你看这个东西也能理解，对吧？也能理解的。好，首先单个神经元我们之前看到过的啊，之前是这个公式，对不对？见过吧？我不要再重复解释这个公式了啊。然后呢。

---
