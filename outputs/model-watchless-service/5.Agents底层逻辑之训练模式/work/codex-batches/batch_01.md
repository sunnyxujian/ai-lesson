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

## Scene 1

Time: 00:00:00-00:02:27
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_001_00-01-00.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_001.md`

Transcript:
我想说的是，就是那个神经元的设计的时候啊，啊，不是说层数越多越好，层数越多，神经元过量了，它会产生过拟合的问题，它只认识你训练的数据集，它不认识外面的。好，这节课就咱们就把那个神经网络就结束了啊，后面要讲那个全神folmer的。呃，这节课出现的主要目的呢，是因为还有一些杂七杂八的一些小概念啊，我给你讲到，就是有一些术语在里面。呃，主要讲几个点哈，一个点呢是提出。呃，主要讲几个点哈。一个点呢是梯度下降的训练模式，就是我们上节课呢讲的这个梯度下降的做法，对吧？其实做法呢就是反向传播，还记得吗？最终呢就会达到一个结果，就是每一个层。现在我们只有三个层嘛，对不对？啊，这看一下啊，是不是只有三个层？那输入层肯定不算了吧？输入层它没有权重啊，没有偏置啊，不用管它了啊。只有三个层，那么每一个层就是反向传播过后，就训练过后啊。以后我们就说训练完了过后啊，就这一次训练了过后，是不是每一层的权。量了过后，是不是每一层的权重啊、偏置，就是这些参数该怎么下降，怎么那个增加，是不是就明确了，对不对？那怎么弄呢？我现在是马上更新参数呢，还是怎么弄呢？哎，这一块呢，还有不同的模式啊。嗯，第一种模式呢，叫做随机梯度下降，那是早期的模式啊。现在基本上不会用这种模式啊，早期的一些示例代码里边会有这种模式，就是每一次呢，只取一个样本，比方说像我们这个演示里边，对吧？啊，每一次呢，我只取了一个样本，看到没？只有一个样本的输入啊，然后呢，拿到。只有一个样本的输入啊，然后呢拿到结果，就是这一次完了过后，哎，我就可以拿到这个结果，马上就更新参数，然后接下来下一个样本，下一个样本啊，循环往复。呃，这是以前的这种做法啊。这种做法有个什么样的问题呢？这种做法的问题呢，主要的问题就是容易导致那个梯度噪声过大。什么叫梯度噪声过大呢？那同学们要回想一下，梯度下降对吧？往那个坑里跳，一个小球往坑里滚，或者你站在山坡上往下降坡度，对不对？当时我们的前提条件是什么呢？前提条件是在这个输入。前提条件是在这个输入不变的情况下，你站在的是那个山脉。输入一遍，山脉全部变完。这个好理解吧？你输入变了呀，那最后的点亮的结构全部变完了。就是你现在闭上眼睛，或者说在黑夜伸手不见五指，你找到了一个坡度，好，你确实往下降了。然后呢，降了过后，接下来输入一遍，不好意思，对那个输入，你跑到山顶上去了，就会出现这种问题。那么你在这个坡度下，你又下降，在另一个输入下啊，比方说我们这里刷新一次，再刷新一次，哦，这里是固定的。再刷新一次啊，这里是固定的是吧？呃，那么比如说换了一个数字啊，就是这个数字，再换一个，换了一个数字，一路来跑一次这个训练，然后为这个数字又下降，为这个数字又下降了。过后呢，对于另外一边来说，那么那边又是升高，懂什么意思吧？它不同的输入，它那个整个三曼是不一样的，是完全不一样的。你如果说只用一个单一的数据集的话，你会导致参数东跑一下西跑一下，东跑一下西跑一下，就带来回震荡，这个东西就叫做。

---

## Scene 2

Time: 00:02:27-00:03:14
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_002_00-02-56.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_002.md`

Transcript:
就要来回震荡，那个东西就叫做批度噪声。取单个样本算的话，就会有这样的一个问题。好，第二种做法呢，就是取全量批度下降。什么叫全量批度下降呢？比方说，我的训练数据集啊，因为我们要训练的话，肯定要标注很多很多的数据嘛，要拿数据给它训练，对不对？不同的数据来调整它的那个，就是呃各种各样的参数。比方说，我们以这个例子，我有很多的数字啊。其实网上有一个数据库，其实我这个例子呢，来自于就是一些呃，叫谁来着一个在。叫谁来着？一个在神经网络里边专门写各种各样的神经网络博客的一个国外哥们儿。来，他的一个教材里边的一些就是图片例子。我把这里的图片拿到了。他其实网上是有个数据库的，哈，有几万张这样的一个图片拿来进行训练啊。不同的手写的数字来进行训练，都标注好了的。就是训练的话，最麻烦的一个点就是能不能拿到一个好的训练数据啊。这其实是一个非常非常麻烦的一个点。嗯，不说别的了啊。就是我们拿到一个训练数据集过后呢，拿去训练。呃，每次训练就。

---

## Scene 3

Time: 00:03:14-00:04:55
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_003_00-03-56.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_003.md`

Transcript:
然后呢，拿去训练。呃，每一次训练就是一个前向传播，然后一个反向传播，对不对？啊，就完成了一个训练。但是呢，这样子的话，这种单一的样本来进行训练的话，就会导致梯度造成很大。那怎么办呢？有一种解决办法，就是全量训练。我把所有的一切拿来进行训练。哎，这所有的一切怎么训练呢？你可以这样理解啊，就是我先把第一个拿到，第一个数据的，第一个拿到，然后呢，跑一项正向，对吧？拿到预测值，然后呢，接下来跑反向，啊，是不是拿到这个第一个训练。好，是不是拿到这个第一个训练结果的这么一个参数的调整结果，对吧？这是第一个样本的最终结果，拿到了。现在不更新参数，不更新。然后呢，接下来拿第二个，也就是说，哎，这是第一个，对吧？拿到第一个了。接下来拿第二个，接下来拿第三个。拿到所有样本的结果过后，全量求平均。对于同一个，就是权重，可能有些是升高，有些是降低，求平均。这样子的话，东拉西扯吧。你往我这个方向拉一点，他又往那个方向拉一点。它是个高位空间啊，它可不是一个三维，它是有几百上千维、上千维的空间，东拉西。跑上前位，上弯位的空间，东拉西扯，东拉西扯，也拿到了一个合适的点，懂意思吧？啊，当然了，训练它不是一蹴而就的。那么这样子跑完一次全量的训练了，跑完了一次不够啊，他反复的跑，反复的跑，你再来跑一次全量训练，再来求平均，再来跑一次全量训练，再来求平均啊，每一次求完平均过后，更新参数啊，更新完了过后，又来跑全量训练，又来求平均啊，更新参数，又来跑全量训练，又求平均，又更新参数，懂意思吧？那么跑到什么时候为止呢？跑到你怎么弄？好像那个就是，呃，损失值都降不下去了，就很难降了下去了。损失值都降不下去了，就很难降了下去了。那么接下来就看那个损失度能不能接受了。比方说，像我们的图片识别，哎，能达到百分之九十八的准确率，能不能接受？哎，能接受了，啊，那就训练完毕了，就不训练了。如果说不能接受，比方百分之六十，但是损失度又降不下去的，那就是你的整个网络架构设计有问题。什么叫网络架构呢？就是你整个神经元的体系设计都有问题。就是比方说，我简单举个例子，隐藏层太少了，或者是那个神经元太少了，或者是太多了。那个时候你要去调试，要去考虑的啊，那是训练的事儿，那是算法工程师的事儿，跟你没关系了。好吧，呃，这是。

---

## Scene 4

Time: 00:04:55-00:05:46
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_004_00-05-22.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_004.md`

Transcript:
的事儿跟你没关系了，好吧？呃，这是全量的训练，全批量梯度下降，全批量梯度下降肯定是最好的、最理想的。但是呢，烧硬件啊，烧成本呢，这个受不了的啊。现在大模型那么多参数，那么庞大的训练集，两百多个T B的训练数据集啊，那收得了吗？受不了啊。这个从成本上来讲的话，而且训练很慢，很慢啊，几乎不会用这种方式。现在的主流方式呢是小批量梯度下降，这是怎么做的呢？它其实就是切片啊，比方说我这一块训练数据集啊。比方说，我这一块训练数据集啊，拿过来，哎，拿过来过后呢，我把这一批跑完，就跑这一批啊。然后呢，还是一样的啊，把这一批来过后，跑出一个，对吧？跑出来第一个啊，然后跑出来第二个，然后跑出来第三个，直到把这一批跑完啊，全部跑完，然后来求平均。好，然后直接更新参数，更新了过后再跑下一批，对吧？批量跑啊，总的意思吧。这是目前的主流的训练方式。嗯，但是我这里说一下啊，我这里演示的时候，给你们让你们好理解，是一个一个写的一个一个说，哎，先跑第一个，再跑第二个，实际上它是一起跑的啊，它怎么一起跑的。

---

## Scene 5

Time: 00:05:46-00:06:30
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_005_00-06-14.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_005.md`

Transcript:
实际上它是一起跑的啊，它怎么一起跑的？这个东西呢，它是靠张量啊，它是会把这个批量的数据组成张量。什么叫张量呢？张量呢，你可以把它想象成几维的数组，比方说零维张量，零维张量的话就是标量，就是一个数字啊；一维张量的话，那么就是一个数组啊，就是个向量，对吧？二维张量呢，就是二维数组，二维数组是什么？就是矩阵，对吧？三维张量呢，那就是多维矩阵啊，它就是个三维张量，多维矩阵，对吧？因为你每一个。多维矩阵，对吧？因为你每一个训练集不是有很多样本嘛，每个样本它就是一个向量输入，对吧？那么它调整参数的时候就是一个矩阵，对不对？那么单位向量呢，就是多维矩阵啊。你这个了解就行了啊，因为这一块又涉及到数学的，你了解就行了。呃，为什么要弄成张量呢？因为对于GPU来说，张量本质上它的运算规则跟向量是一样的，没有本质的区别。所以说仍然可以用GPU瞬间完成啊，并行完成，一起跑。它不是说一个一个跑啊，它实际上是一起跑的。嗯，你这个。

---

## Scene 6

Time: 00:06:30-00:07:43
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\keyframes\scene_006_00-07-32.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\5.Agents底层逻辑之训练模式\work\codex-notes\scene_006.md`

Transcript:
啊，它实际上是一起跑的。呃，你这个了解就行了。啊，一次跑一批，跑一批，更新参数，再跑下一批，然后再更新参数，然后再跑下一批，然后循环往后。跑完，跑完过后，然后再重来，跑跑跑，跑跑跑，跑跑。啊，跑跑跑，对吧？呃，它具体的做法呢，它有非常丰富的做法啊。呃，总之它是分批次的来去更新这个呃权重和偏置啊，都是求平均值的。东拉西扯，就是说我们训练模型的话，并不是要求一道一个完美的结果。这个完美的结果谁是达不到的啊？你要像。这结果谁都达不到的啊！你要像模型，真正的像人这样子，其实很难的。我们尽管呢是用计算机来模拟它的神经元，模拟人类的神经元，但是呢，人类的神经元要比计算机那个数学公式要复杂得多得多得多。甚至到现在，人都还远远没有完全清楚人类的神经元到底是怎么工作的，它背后还有哪些东西，根本就不清楚。所以说，哥们，人才是最复杂的，你才是最复杂的，对吧？你计算机要好多好多点才能训练一个模型出来，你两个晚头干两天，一点问题都没有，是不是？你才是最复杂的。嗯，所以说。不是你才是最复杂的，呃，所以说他这一块训练的话，你他不是要求一个完美的结果，他是很难找到一个完美的结果的。就是说，在这个东拉西扯的时候，求平均的时候，往这个方向拉一点，你往那个方向拉一点，拉到大家都能接受，对吧？照顾一下你也照顾一下这位啊，大家都照顾一下，有这么多人啊，都要照顾一下。那么就求得这么一个能接受的结果，那就OK了啊，就训练完成了啊。这种训练模式，然后那个训练模式里边呢，还有一个现象哈，你看哈，每一批的训练数据集，你会发现一个特点。

---
