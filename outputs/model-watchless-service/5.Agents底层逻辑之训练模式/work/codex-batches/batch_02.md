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

Notes directory: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes`

## Scene 7

Time: 00:07:43-00:08:52
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_007_00-08-34.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_007.md`

Transcript:
训练数据集，你会发现有个特点，就全部是随机打乱了的，啥数字都有。哎，他为什么不先把零训练好？就是第一批各种各样的零，第二批各种各样的一。他为什么不这样子做呢？因为这样子做的话又会产生一个新的问题。这个问题呢，我这个课件里面没有啊，给你们说一下就行了啊，叫做灾难性遗忘。像你们以后如果说去做一些微调啊，微调的话，呃，还没有那么复杂啊，微调的话也是可以做的。如果说你们将来去做一些。如果说你们将来去做一些嗯微调之类的事情的话，就会遇到这个问题：灾难性遗忘。就是你先把零训练好了，各式各样的零训练好了。好，那个模型对零识别的非常准确啊，非常自信的去识别零。但其他数字没见过嘛。他把各种权重啊参数都往那个零方面靠了。好，这是一个极端的结果。他只认识零了啊。反正呢，他把零识别好了。接下来你去跑一，那一就是一塌糊涂了。那各式各样的一全是一塌糊涂的。那么你去跑一的时候呢，那肯定不行啊。他。那么，你去跑一的时候呢？那肯定不行啊，他又得重新训练，对吧？又得重新调整权重参数。一调整，好调整了一大堆，终于把一识别好了。好，一识别好了，零忘了，零又出问题了。你再去跑零，零又完完蛋了。懂这意思吧？这就是灾难性遗忘。所以说呢，我们在训练的时候呢，往往会打乱顺序啊。其实就为了就是东拉西扯，你往我这边拉一点，你往啊，他又往那边拉一点，拉到一个大家都能接受的一个结果。啊，模型训练就是这个样子的。呃，这个给大家说一下，嗯，还有。

---

## Scene 8

Time: 00:08:52-00:10:06
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_008_00-09-46.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_008.md`

Transcript:
这个给大家说一下，嗯，还有啥呢？还有啥呢？哦，还有两个概念啊，还有两个概念，就顺便说一下啊。这个我们那里面没有，一个是过拟合，一个是泛化啊。有的时候觉得这是，扯犊子的时候，有可能会提到这两个词啊。过拟合是什么呢？就是一个训练好的模型，就是我们来判断一个模型。我们先说泛化吧，判断一个模型是不是智能的。哎，我们比方说训练的数据集里边没有这个东西，但是呢，这个模型仍然认识。比方你看看图片，训练模型集里边没有，但是呢，它仍然认识。训练模型，集里边没有，但是呢，他仍然认识这个图啊，仍然能够识别出它的数字。那么我们就认为这个模型的泛化能力强，他能识别出一些他没见过的东西啊，他就是泛化能力强。反之呢，就是过拟合，过拟合的话就是泛化能力弱啊，就是过拟合，就只认识训练集里边的东西啊，也是训练集以外的，那就一塌糊涂了。那么这个模型训练就失败了，叫过拟合啊。还有一个叫欠拟合，欠拟合又是啥意思呢？他是这个意思，他指的是你都不是说过拟合的问题了，你连数据。说过拟合的问题了，你连数据集都没搞定，你数据集里面都还没有认识清楚。那就千里河啊。呃，为什么说这个呢？其实我想说的是，就是那个神经元的设计的时候啊，呃，不是说陈述越多越好，陈述越多，神经元过量了，它会产生过拟合的问题。它只认识你训练的数据集，它不认识外面的。神经元啊，陈述过多就会导致这个问题。那过少呢？又会导致千里河的问题，对吧？不够了啊，不够呢，智能程度不够，你连训练集都吃不下啊，就会导致这个结果。

---

## Scene 9

Time: 00:10:06-00:11:17
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_009_00-10-50.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_009.md`

Transcript:
支不下啊，就会导致这个结果。所以要调整到一个合适的值啊。好，这是那个极度下降的训练模式。这节课其实就是杂七杂八的一些东西啊，给大家说一下。然后呢，是网络架构。这个指的是什么呢？其实我们刚才之前讲的是神经网络的一个通用的做法，但是呢，不是唯一的标准做法。比如说简单理解，这个隐藏层设计多少层啊？每层有多少个神经元啊？这需要设计的。然后这个连接是全连接吗？那不一定啊，它可能不是全连接，一部分连接一部分。就是这些玩意。一部分连接一部分，就是这些画面具体的细节是需要去设计的。那不同的设计呢，就产生不同的网络架构，懂那意思吧？那么常见的两个网络架构，一个是卷积神经网络，但是现在呢用的已经很少了啊。呃，它以前呢主要是来处理图片的，现在处理图片啊、处理音频，全都是用卷积former的啊。现在主流的都是卷积former，我们后面会讲啊。它早期呢是用来处理这个NLP啊，就是神经语言城市学，就是处理语言起家的。本来是未来处理语言的，但是现在发现啥都可以用，都可以用它，像那个音频啊。啥都可以用，都可以用它，像那个音频啊、视频啊都可以用它啊。现在主流都是全，互联网全机都是过去式了啊。这网络架构你了解一下。然后呢，是学习框架。什么叫学习框架呢？你有了架构，架构市场呢，架构其实就是一张图纸。他告诉你那些算法工程师告诉你，他那个整个神经网络是怎么设计的。他告诉你过后，你要去实施啊，你要去真正的把线拿出来变成代码，然后运行起来，对不对？那么学习框架呢，其实就是训练框架啊。训练不就是学习吗？对吧？就是用来。

---

## Scene 10

Time: 00:11:17-00:12:10
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_010_00-11-44.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_010.md`

Transcript:
训练不就是学习嘛，对吧？就是用来真正的落地到代码层面。这个时候才是工程师出现了，对吧？戴个绿帽子啊，戴个红帽子吧，戴个红帽子开始干活了，开始敲敲打打，开始干活了啊。图纸都已经有了呀，我现在终于可以开始干活了。这个时候才是真正的落地啊。训练框架呢，也有两套比较知名，一个是 TensorFlow，过去呢很知名，但现在呢很少用了。现在他还在，但是他用在什么地方呢？他用在一些边缘计算。什么叫边缘计算呢？一般来说，大模型是跑在跑在云端的，对吧？也不可能自己在家里边摆一套那个就是那个 G P U 集群吧，对吧？不可能在家里边去。P P U集群吧，对吧？不可能在家里面去搭建那个训练集群的。这个玩意儿，是要正规的，就是那个训练机房的，有数据中心的，要去做这些事情。它肯定是在云端的。但是呢，有一些小的任务，呃，小的那些训练任务啊，或者是那个呃推理任务啊，以后我会讲训练推理啊。那么，你可以在一些手机上就可以完成，计算量不大，很小很迷你的东西。那么这个时候呢，哎，可以上这个TensorFlow啊。在这种场景下还有点用啊。一般来说，呃，现在大模型方面的话，都不会会使用它来进行训练学习的啊。现在都主流的都。

---

## Scene 11

Time: 00:12:10-00:12:57
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_011_00-12-45.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_011.md`

Transcript:
进行训练学习了啊，现在都主流的都是使用Python去，去拍成一套东西啊，拍成那个训练框架，主力训练框架，Python。现在主流的这些大模型都是通过它来训练的，懂了？意思吧？这是学习框架，就是真而八零落地的东西了。然后其实这两个玩意儿，它不仅是训练框架，它也是可以做推理的。什么叫推理呢？推理就是把那个现象传播走一次，现象传播完了过后，为什么要反向传播？是因为它预测的不对，对吧？预测对的还需要反向传播吗？就不需要了，它预测的不对，它预测值有问题。但是当我们把那些。它预测只有问题，但是当我们把那些模型的权重啊、偏置啊调整好了，训练完毕了过后，那还有问题吗？就没问题了，对吧？它就能够正确的出结果了。那我们后面怎么来用这个模型呢？那就把个权重啊，就是把那些参数填进去，直接前向传播就完事儿了，就不需要后面的东西了。这个过程就是推理。所以说训练框架，由于它是训练框架，它它肯定有前向传播啊，它同时也包含反向传播，对吧？那训练好了过后，我只需要用它前向传播的一个过程就行了，是不是这个道理？啊，你可以简单理解，前向传播就是推理过程，就是出结果的过程。

---

## Scene 12

Time: 00:12:57-00:14:38
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_012_00-13-50.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_012.md`

Transcript:
就是推理过程，就是出结果的过程。你输入，然后第一出结果啊。只是呢，以前在训练阶段呢，还需要这个过程，训练好了过后就不需要这个过程了，是这意思吧？好，下一个啊，模型啊，就可以解释模型了。模型到底是个啥呢？模型就是训练的结果。弄完了，啥都调整好了，到位了，那就出结果了呀。那这个结果到底是个啥呢？通常它是以多个文件的形式来存储的。文件里面主要是包含一个最核心的东西，就是呃权重文件，或者是我们把叫叫做核心参数文件，里面全是参数，就是权重加偏置，几万亿个权重偏。就是权重加偏置，几万亿个权重偏置啊，到那个文件里面去。这个主要是占了百分之九十九的体积，大部分体积都是他在占用。所以训练的结果其实就是产出那些权重偏置。那么下次要用的时候，把这些权重偏置读出来，放到网络里面去啊，就可以跑这个模型了，对吧？不，这个浅向传播就可以跑这个模型了。呃，然后呢，还有一些其他杂七杂八的文件，主要是一些配置文件，比如说他要描述一下啊，你光有一个权重参数，他得知道你这个网络架构啊，你用的是什么架构啊，你到底涉及到多少层数，那每个层数的这个神经元的数量，对吧？这些玩意儿，他才能复现这个网络结构啊，对不对？啊，要隐藏层的维度。这个网络结构啊，对不对？啊，然后隐藏层的维度、权重精度，就是每个权重它可能是有小数的，那小数去掉多好，对吧？那么这些额外的信息呢，需要用配置文件来描述啊。那么整个呢就形成了模型，模型就是这个意思啊。所以你们加一些本地模型，我们后边会下啊，会下载一些本地的模型去玩一玩，呃，就会发现模型它大，主要就是这个东西占体积，其他东西完全不占体积的，几乎是不占体积，好吧。后边下载过后呢，呃，使用的时候就是直接使用Python游戏，它是训练框架，那它也是一个什么推理框架呀，是一样的呀。一个什么推理框架呀，是一样的呀，就是把前项全部走一次嘛，不就得了嘛。啊，所以我们到时候跑一些本地模型的时候，就会用它去跑啊。但是正经的在生产环境里边，还是不会用它，因为生产环境里边还要考虑一个性能的问题啊，那就是部署工程师要搞定的事情啊，就是我们之前说的AI infra这样的工程师，他是要去搞定的问题的啊，那问题多了去了啊。但是我们本地玩的话，开发测试啊调试阶段，我们就可以玩一些本地模型就可以了。好了，这就是这节课补充一些那个专业术语啊，嗯，就是扯犊子用的，跟那个A I的开发也没多大关系。

---
