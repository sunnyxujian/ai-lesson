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

Notes directory: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\codex-notes`

## Scene 1

Time: 00:00:00-00:01:40
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\keyframes\scene_001_00-00-50.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\codex-notes\scene_001.md`

Transcript:
其实你学完之后，你会发现整个神经网络就是在做一道一道的数学练习，这个习题非常非常庞大而已。好，我们上节课呢已经知道了，在这个神经网络当中呢，前向传播啊，从我们的输入开始，然后呢一层一层进行运算，最后呢运算到输出层，我们就会得到一个结果。通过分析这个结果呢，我们就可以得到哪个结果呢，几率最大。那么我们现在输入了一个样本四，得到的结果呢是。个样本四，得到的结果呢是他认为事实啊。当然，这个结果是完全不能看的啊，已经是错的离谱了。呃，那么现在接下来的问题呢，就是我们上节课说的，当我们输入固定的时候，是什么东西在影响这个结果呢？是不是就是参数？你脑袋里面要想到参数是什么意思啊？来回答我：参数是什么意思？是不是所有的整个神经网络的权重和整个所有的神经网络的偏置加起来，就是它的。之加起来就是它的参数，就它们的集合，就是它的参数。那些参数在影响着这个结果。那么我们要改变这个结果，使得这个结果正确，是不是就要去调整这些参数？对不对？那么怎么来调整呢？这里会涉及到几万个参数。像我们这个小例子的话，如果说这一块参开的话，是有很多个输入的，对吧？那么看看我们之前算过，是有两万多个参数的。这么多的参数，我们不可能像之前单个神经元的样子，通过手动的去调整。你可以脑袋里面想象这一块是有。你可以脑袋里来想象这一块是有两万多个，你怎么调呢？该怎么调？这个是很麻烦的事情。所以说呢，我们希望计算机能够自行去调整这个参数。那么接下来讨论的问题就是：我们如何根据这个结果，让计算机如何自行去调整这个参数，使得这个结果趋向于正确。对我们这节课要讲的反向传播。好，我们从头开始啊。现在呢，我们的情况是有一个样本输入了。那么这个样本呢，明显是一个数字一，对吧？我们人一眼一眼就看出来了。但是计算机它就做了一大堆的数学题，算出一个乱七八糟。

---

## Scene 2

Time: 00:01:40-00:03:24
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\keyframes\scene_002_00-03-21.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\codex-notes\scene_002.md`

Transcript:
大堆的数学题算出一个乱七八糟的结果。我们假设每一个结果呢是一个零到一之间的数字啊，这个数字呢越大，那么就表示说它的几率就越高。那么目前最大的是什么？是这个零点八六啊，他认为是它是一个数字六，不是啊，应该是零点七六啊，他认为是一个数字四，但明显不是，是吧？这些都是完全随机的权重，完全随机的偏置，导致了一个完全随机的这么一个结果。好，那么现在呢，问题就是我们如何来调整这个输出。那么要调整那个输出的话，我们得需要告诉他一个。要告诉他一个正确的值，应该是什么样子？我们可以通过数据标注，对吧？之前我们讲AI分类的时候，大家看过一些图片，对吧？那些数据标注，哎，标注好了这个图片，人类识别出来就是一，你这个明显不对呀。所以说，我们人类呢，就在这一块呢，计算机可以用一些自动化的程序，让它去读取一个正确的结果，就这是你算出来的，对吧？这是预测值。我们把这个玩意儿叫做预测值，就是通过这个神经网络算出来的一个结果，把它叫做预测值啊，预测。预测值啊，预测，呃，然后呢，接下来我们要给它一个真实值。真实值的话，我们把它叫做标签儿啊。那么真实值和标签儿之间肯定是有差距。你看标签儿里边，这就是一个典型的一。呃，我这里编号改了一下啊，之前的编号呢是按照神经元的顺序。那这里呢，为了让大家看得更清楚一点，所以说这一块的编号呢，我就让它用代表实际的数字啊，比方说第一个神经元代表数字零，第二个神经元代表数字一，一直到代表数字九啊。这样子的，同学们看得清楚一点。其实编号是啥，从哪个开始都无所谓的好。那么我们正确。无所谓的好，那么我们正确的结果应该是啥呢？是一。那么就意味着这个编号为一的这个神经元呢，应该是完全点亮，它的最大值就是一啊。当然，这个神经元的输出结果呢，我们这里也是人为规定啊，它应该是在零到一之间的范围内。就是你要把它做到零到一之间的范围，其实也很容易，有各种各样的数学工具啊。你想了解的话，去问一问AI，有哪些数学工具可以把压缩到零到一，那多的很。好，那么现在呢，我们给它的正确结果呢，就是只有一这个地方是点亮的，其他地方全是零，全是暗的，这才是正确结果。我们期望这套。

---

## Scene 3

Time: 00:03:24-00:05:34
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\keyframes\scene_003_00-04-29.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\codex-notes\scene_003.md`

Transcript:
这才是正确结果。我们期望这套神经网络通过去调整参数去接近这个正确结果。那么这个时候呢，就肯定是有差距的，就是我们的输出层啊，就是预测值和我们的标签，它肯定有差距。第一个问题就是我们如何来衡量这个差距，这个差距到底有多大？我们肯定需要一个量化的衡量。那么这个衡量呢，叫做损失值啊，或者叫做损失度，都是一个意思。那么要衡量这个损失度的东西呢，叫做损失函数啊，或者叫做代价。叫做损失函数啊，或者叫做代价函数啊。有些教材呢把它翻译成为代价函数，有些教材呢把它翻译成为损失函数啊，都一个意思。那么无论是代价函数还是一个损失函数，它们产生的结果呢，都是一个损失值，损失值就是一个数字啊。一般来说呢是一个大于零的数字，最小的损失值是什么？就是零啊，就没有损失了，完全正确啊，就没有损失。但是你要把它调整到零是很困难，很困难的啊，呃，几乎是不可能的。就是我们尽量。呃，几乎是不可能的，就是我们尽量的小就行啊。这个是损失值。那么这个损失值是怎么算的呢？不同的神经网络呢，它的计算方式不一样。我在课件里边呢，给大家列举了一种算法，非常简单。你这个看的不是很清楚的话，你就看图啊，图上给你解释，非常简单。这两个相减求平方，然后呢，这两个相减求平方，这两个相减求平方。求平方的目的是要保证它是正数，对吧？你别给我减出来是负数了。哪个减哪个都无所谓，前面减后面，后面减前面，反正是求平方也无所谓。的好，求完平方过后全部把平方加起来，就是损失度啊。不对，把平方加起来就是损失度啊，就这么算啊，这块的损失度就是这样算出来的。那么总之呢，我们可以算出一个损失度。好了，接下来呢，就开始要进入到一些复杂的环节了啊。拿到这个损失度过后要怎么办？后边我们接下来要讲的东西，如果说同学们听着有困难，脑袋晕了一下，暂停视频，好好想一想，呃，因为这背后有一些数学的原理在。但是我数学不会讲很深啊，特别是涉及到微积分啊、呃偏导数这一块的话，我就完全不扯了啊。因为我们前面的讲这些概念的目的呢，是为了日常交流啊，扯犊子用的。比方说，给你蹦。啊，扯犊子用的，比方说给你蹦一些词儿出来，你完全听不懂，感觉很没面子啊。特别是在面试的时候，就觉得快要泄气了，心里面没底啊。还有包括平时刷一些短视频的时候，天天看别人不明智，觉得这个神经网络或者是那些模型啊，AI挺神秘的。我叫消除这个神秘感，没有啥神秘的。其实你学完之后，你会发现整个神经网络啊，就是在做一道一道的数学练习，这个是个习题，非常非常庞大而已啊，没有什么神秘的。好，那么拿到这个损失度怎么办呢？我们肯定是目标是为了减少损失度。好，接下来听我讲啊，看着。

---

## Scene 4

Time: 00:05:34-00:07:42
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\keyframes\scene_004_00-07-06.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\codex-notes\scene_004.md`

Transcript:
好，接下来听我讲啊。看着，减小损失度，在我们输入的固定的情况下，那么是不是这个标签也是固定的？想想这个问题，我们输入是固定的，标签是不是一定固定的？你输入是一标签，肯定只能是一样，只能是这个样子，这是我们人类给它标记好的，对吧？标记好的就是这个值啊，那肯定是一样。好，那么我们要改变那个损失度，是不是只能动输出？是不是只能动输出？但是输出能直接动吗？不能直接动。什么在影响输出？是不是参数？也就是说什么呢？我们现在有个损失度，什么在影响损失？我们现在有个损失度，什么在影响损失度？我们可以认为是参数在影响损失度。想一想啊，是不是这个样子？因为啥呢？这个逻辑推导啊，这个是固定的，这个是固定的。那么要改变损失度，只能改变它，对不对？要改变它的话，只能改变参数啊。所以说，间接的参数在影响损失度。哎，那么参数和损失度之间一定存在着某一种关系，只是这个关系太复杂了，因为参数有两万多个，在那个真正大模型里边，参数有一万多亿个。那这个影。一万多亿个，那这个影响到底是怎么影响水势度的？太复杂了。哎，在数学里边呢，遇到这种复杂度啊，就是有一个东西x，它通过一段计算，一段非常复杂的计算，得到了一个y。那么我们就说y这个东西呢，跟x有关系，对吧？有什么关系呢？如果说在数学里面，我们不知道的话，我们就这样来记，有一个函数y等于一个函数，只是这个函数是什么，我不知道，可能非常非常复杂，我们就可以这样记啊，在水势度度里面。我们。这样记啊，在水速度度里面，我们可以用cost这个单词啊，用c函数，用cost，有一个c函数传入的是什么呢？传入的是参数，当然这个参数你心里边要知道啊，是两万多个，在实际大模型里边是一点五万亿个，反正有这么多参数，这些参数的值经过一段复杂的运算，什么运算不知道，这个传来传去，传来传去，老瓜是传通了对吧？不知道，但是呢，最终会得到一个y啊，我们就可以这样来记。那这个东西写出来有什么意义呢？我们的目标。写出来有什么意义呢？我们的目标是什么呢？我们目标考虑的就是如何改变参数，使得y减少，就是损失嘛，损失减少，是不是就是我们的目的？好，那么我们考虑这么一种情况：假设参数只有一个，没有两万多个。假设参数一个，我们考虑最最简单的一个情况：假设参数只有一个，那么通过这个函数，一个非常复杂的函数得到一个y。那如何来改变x使得y减少呢？这里呢有一张示意图。好，假设。

---

## Scene 5

Time: 00:07:42-00:10:23
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\keyframes\scene_005_00-10-18.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\codex-notes\scene_005.md`

Transcript:
这里呢有一张示意图。啊，假设这是我们的画出来的结果啊，一个二维坐标系，横坐标是x啊，纵坐标是y。然后呢，这个函数太复杂了，不知道怎么画。但是画出来呢，可能是弯来扭曲的，弯来扭曲的一些曲线。那么现在呢，假设这个x x是我们的参数吧，假设是其中一个参数啊。我们就考虑整个神经网络只有一个参数啊，假设只有一个参数。那么参数的值是不是一开始是随机的，对吧？你随机到哪个点不知道，我不知道随机到哪个点，有可能x随机到这个点啊。我再说一次啊。x随机到这个点啊，我再说一次啊，我接下来要讲的东西，如果说你脑袋晕一下晕了，那么你可以暂停视频好好想一想啊。这个x表示什么意思？表示是我们的参数嘛。假设我们整个神经网络只有一个参数，我们简化模型，哎，x在这个位置。假设y是不是可以通过x一动啊？复杂的运算是不是可以算出一个y？对不对？只是呢，整个函数的曲线，就是个c函数的曲线，不知道是什么。我自己随便写了一个，就随便写了一个，不知道是什么。它有可能是这样的曲线。我可以随便乱画啊，它有可能是这样的曲线。我可以随便画啊，它有可能是这样的曲线穿过这个点，对吧？也有可能是这样的一个曲线，那它肯定不能小于零，因为一个损失最小值是零，对吧？也有可能是这样的一个曲线啊，也有可能是这样的一个曲线啊，搞不清楚它是什么曲线。我就随便瞎画了一个曲线，总之它穿过了这个点，能理解意思吧？好，那么现在我们的问题是啥呢？我虽然不知道你的曲线是啥，你的函数太复杂了，我不知道这个画出来在二维坐标系里边到底是一个什么东西，我不知道，但是呢。什么东西，我不知道。但是呢，你只要是一个曲线，一个光滑的曲线。哎，有人说：“我怎么来保证是一个光滑的曲线？”这背后有它的数学原理，几乎是光滑的曲线。我只能用“几乎”这两个字，不能说百分之百。即便是一些额外的地方，不是那么光滑，其实也无所谓啊，也影响不大。我们通过一些细微的手段去调整，也影响不大啊。那些都是小细节的东西，你不用去深究。我现在就告诉你，它几乎是光滑的曲线，它就是个光滑的曲线。我们不用那么严谨，对吧？我们是理解概念为。我们严谨，对吧？我们是理解概念为主。好，那现在你知道这个点在这个曲线上，请问你怎么走才能使得y减少呢？你怎么来调整这个x才能使得y减少呢？我是不是可以这样做？我只要能够求得这个点在这个曲线上，我不知道这个曲线整体的样子，但是呢，我能够求得这个点在曲线上那个斜率，对吧？我没有用导数啊，我怕有些同学听不懂斜率，都能听得懂吧？就是这个切线，我能求得这个切线。就是这个切线，我能求的这个切线。这个切线其实就是用微积分导数求出来的，这是能求的。只要能够知道这个切线是什么样子就可以了。我不用知道全局的曲线是什么样子，我只要知道这个切线长什么样子就行了。切线长这个样子，那么就应该往南边走，往右边走，是不是？让x增加，让x增加，我们的y就会减少。那反之，如果说它穿过的曲线不是我现在这个图中的样子，它可能是这个样子的。你不知道这个曲线什么样子，它可能是这个样子的。不知道这个曲线什么样子，它可能是这个样子的。那么同样的道理啊，我现说你这个点在这个曲线上的切线，切线是这个样子，对吧？那么切线是这个样子，我是不是就应该往左边走？所以说，虽然我不知道它整体的曲线画出来的曲线是什么样子，太复杂了，但是我只要知道这个切线就行，是不是？我就能知道我接下来该走往哪个方向走，走多远我都不知道。但是呢，我只能知道往哪个方向走了。好，那么这是一个参数的情况。

---

## Scene 6

Time: 00:10:23-00:12:29
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\keyframes\scene_006_00-11-54.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\4.Agents底层逻辑之梯度下降\work\codex-notes\scene_006.md`

Transcript:
那么这是一个参数的情况，那两个参数呢？哎，那如果说是这种情况呢，那这种情况呢就不能再二维平面化了，那就是一个三维平面了。好，来看一下，这里呃，我这个玩意用什么软件打开的？是在麦克系统上有个Grapher软件啊，你在麦克系统上直接可以打开，你在Windows系统上是打开的啊，打开也没关系，反正这个玩意是课件啊，是那个教学工具教学用具，打开就打开吧。好，在三维曲面上，你看哈，假设这里这是一个x轴，然后呢这边是y轴，然后呢这个是什么z轴，z轴表示损失度，我要是。也就表示损失度，我要使损失度最小，什么意思呢？讲个三问题：我们这样倒着看啊，倒着看，就这样看吧。现在我们人站在这个像山一样的地方，你现在想象啊，你人站在上面啊，你的脚下一个方向是x，一个方向是y，这是你的脚下的坐标系，垂直于你的身体，就是上下的坐标系呢，就是你的损失度。接下来干嘛？你要想使得损失度减少，是不是要下坡呀？是不往下坡路走？那往哪个方向下坡路走呢？你可以这样想象啊，你在一个伸手不见五指的黑夜里边，站在一些。无止的黑夜里边，站在一些连绵起伏的山脉中，你不知道站在山的什么位置，你不知道山的整体什么样子，你看不见。你是不是可以通过脚底去感受哪个地方的坡度最陡？是不是你往最陡的那个方向走一点，是不是就在下坡？那下坡是，是不是就让损失度减少？那么你下坡的那个方向，就是你要走的方向。明白了吧？这个过程就叫做梯度下降，非常形象，像楼梯一样，往最陡的那个方向走，这就是梯度下。最陡的那个方向走，这就是梯度下降。梯度下降是一个整体的思维，它不是说一个具体的数学算法。因为那个函数具体长什么样子，确实不知道。它是一个整体的思维，就是我的思想上应该沿着这个思路去走。我要想办法找到一个最陡的那个坡度，往下降。当然，这我们现在写的是什么？两个维度。那参数是多少维度呢？啊，这个参数是两万多个维度。那是一个高维空间吗？高维空间我们画不出来，没法画。但是呢，我们可以想象到，在一个高维空间中，一定存在一个最陡峭的。中一定存在一个最陡峭的方向，往最陡峭的那个方向走就可以下坡。那具体怎么走，我看现在还没开始讲啊，不着急。但是你要有整体的这么一个感觉，这就是梯度下降。梯度下降就是为了让损失度降到最低，就调整参数，让损失度降到最低，就是梯度下降，沿着最陡峭的一个方向走啊。所以说我们这个环节呢，有的时候有把叫做梯度下降。那么接下来就是怎么实现梯度下降的问题啊？那我们一会儿再说。

---
