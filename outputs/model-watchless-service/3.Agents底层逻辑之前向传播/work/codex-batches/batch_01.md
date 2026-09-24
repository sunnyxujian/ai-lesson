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

## Scene 1

Time: 00:00:00-00:00:55
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_001_00-00-40.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_001.md`

Transcript:
在我们这个神经网络里边，一个非常简洁的神经网络里边，有多少参数呢？有两万六千多个参数，不多啊，不多。那么我们平时看到一些大模型有多少个呢？像那个DeepSeek，对吧？是有一点五万亿个参数。现在知道参数什么意思了吧？好，我们先回顾一下上节课的内容哈。上节课呢，我们讲了单个神经元，单个神经元呢，接收一个向量的输入，产生一个标量的输出。当我们输入的向量固定的时候，它的输出结。固定的时候，它的输出结果唯一的取决于它的参数，它的参数就是权重加上偏置。我们希望这个输出结果符合预期，就要不断的去调整这个权重和参数。我们当时是这样说的，对吧？我们希望调整到一个合适的位置，使得它可以在这个输入的情况下能够达到一个预期的输出。好，这就是我们上节课的内容。但是我们实际上啊，我们神经网络里边可不止一个神经元，它是有很多很多神经元连接起来的，因为一个神经元。

---

## Scene 2

Time: 00:00:55-00:02:11
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_002_00-02-03.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_002.md`

Transcript:
神经元连接起来的，因为一个神经元这个结构太简单了，也不符合人类大脑的结构，对吧？人类大脑结构呢是有很多的神经元。那么它怎么来连接的呢？就是我们这节课要学习的内容，叫前向传播。你看这个画面中的每一个小圆圈，它都是一个神经元。那么在这套神经元里边呢，它是分层次的啊，一层一层的可以看到啊，第一层、第二层、第三层、第四层。然后呢，这个层呢还有一些特殊的名字，我们可以看到第一层呢叫做输入层，然后呢。叫做输入层，然后呢，中间这两层呢，叫做隐藏层，然后呢，是最后一层呢，是输出层。那么输入层和输出层就很好理解，输入是什么呢？就是输入的一个向量，这里每一个神经元，你可以理解它会输出一个数字，这里就是输入啊，一个向量。我们以后会具体来讲。好，然后输出层呢，就是我们的结果。你可以把整个的过程呢，看上去是一个函数，输入一个东西，实际上是向量，然后吧啦吧啦吧啦吧啦，经过一系列的运算，最后呢，产生。一系列的运算，最后呢产生一个结果。那么中间这个隐藏层呢，就是一些中间的运算过程。整个其实神经网络，你就可以把它想象成一个函数，输入，刷刷刷算，算完了，过输出啊。就是它的整体的结构。我们先对它有一个整体的认识。然后呢，输入层呢，也叫做第零层。然后呢，从隐藏层开始，一二三，后边依次数。第一层、第二层、第三层啊，这也是一种叫法啊。也可以把它叫做输入层、隐藏层、输出层，也可以把它叫第零层、一二三层，这么个意思。

---

## Scene 3

Time: 00:02:11-00:03:52
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_003_00-03-49.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_003.md`

Transcript:
一二三层，这么个意思。而且呢，输入层和输出层呢，都是固定只有一层啊。输入层只有一层，输出层也只有一层。那中间的隐藏层有多少层呢？那就不好说了，那不一定了啊。那不同的模型呢，不同的神经网络架构呢，那隐藏层是不一样的啊。比方说像那个DeepSeek V四这个版本，它的隐藏层呢，呃，我们去说的话，好像有六十多的隐藏层，呃，GPT就。六十多的隐藏层，呃，GPT就不知道了，因为GPT的话，它是闭环的，闭环模型的话，你就不知道它有多少隐藏层的啊。不过业界猜测呢，它应该是有了一百多个隐藏层。但是隐藏层越多，不是说越多越好，隐藏层设置多少合适呢？不一定的啊，这个东西要看经验，看一些实际的工程经验。没有一个就是严格的数学论证说你一定要设置多少隐藏层才合适，这个东西纯看经验啊。太多了呢，会容易产生问题，太少了呢，又容易产生问题，都会容易产生问题的。要设置一个合适的值是最好的。那不同的模型。合适的只是最好的。那不同的模型架构呢？它的设置的，东西不一样啊。这个还跟你的训练的数据集有关系。然后每一层有多少个神经元呢？像这个隐藏层，每一层有，多少个神经元？你看，这一个个的都是神经元啊，我编了号的。那么这些神经元有多少个呢？也是不确定的。呃，像那个D P C可以有多少个？有七千多个啊。每个隐藏层有七千多个神经元。而且有些架构呢，隐藏层的神经元数量还不一致。那个超级T有多少个？我就不清楚了啊。因为它是闭源模型，你只能说开源。因为它是闭源模型，你只能说开源模型的，你能知道它有多少隐藏层啊，是这么个意思。好，那么接下来呢，我们就来研究的是这么多神经元它是怎么连接的，怎么运算的。我们从头到尾，比方说我们整个神经网络，要做一件事儿，从头到尾它是怎么来传递，怎么来输入，又怎么来输出的。你把这个过程理解了，我们这节课就结束了。好来吧，我们举一个例子啊，这里有个不着急去点下一步。假设我们的需求是什么呢？我们的需求呢是希望这个神经网络呢要产生这么一个智能，就是能够识别一张小图片。这个小图片呢，我们。

---

## Scene 4

Time: 00:03:52-00:06:23
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_004_00-05-07.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_004.md`

Transcript:
别一张小图片。这个小图片呢，我们可以看到啊，这里有很多的随机小图片，比方说，像这个手写的数字二、手写的数字三、手写的数字，就是这，这看上去好像是一啊，手写的数字四。它要能够识别这个数字，那么输入是什么？数字自然就是个图片本身，对不对？啊，它怎么来输入呢？它能接收图片吗？不能，整套神经网络只能接收数字，它不能接收别的玩意儿了，它只能接受数字。所以说，我们肯定要把这个图片干嘛要进行数字化，那怎么来数字化呢？拿手段多了去了啊，不同的那个。断多了去去了啊，不同的那个神经网络架构，它可能数字化的方式不一样。那比方说，我用最简单的方式，假设这个图片是四十乘以四十的，那有多少个像素点？就宽高都为四十，是不是？一千六百个像素点。好，那么输入层呢？我就要设计有多少？一千六百个神经元。那我这里实在画不下了啊，我不可能画一千六百画在这里，我就随便画了八个。那如果说你要训练的神经网络是基于四十乘四十的图片的，那么你就要设置一千六百个神经元，懂了意思吧？好，那么每一个神经元，它要接收输入嘛，对吧？呃，那么给它。它要接收输入嘛，对吧？呃，那么给它什么输入的东西呢？比方说这个图片，每个就是一个像素点嘛，一个像素点是个数字，对不对？哎，这个没问题吧？像素点是数字啊。比方说我们平时给一个东西设置颜色，对吧？不就是RGB嘛，三个数字嘛，对吧？三个数字是不是可以合并成一个？比方说这个数字，哎，它不就是个十六进制嘛？这个玩意儿，它是不是十六进制？是不是一个数字，对吧？好，那我们就可以把它来作为第一个数字啊，表示第一个像素点。哎，是这个东西啊，第二个像素点，第三个像素点。啊，第二个像素点，第三个像素点，是不是一共写一千六百个像素点？是不是可以这样子？好吧，那么你把这个东西是不是可以作为输入啊？那么输入层呢？那是不是这些神经元每个就点亮了？点亮是什么意思？就是激活值，那个值越高，它就越亮，就这个意思啊。点亮。啊，输入层比较特殊啊，我们之前讲那个神经元，呃，它有什么那个什么权重啊、偏置，但是输入层啥也没有。你可以把输入层想象成什么呢？把输入层就想象成就是用来提供用户的输入信息的，就是我们这个数据。的输入信息的，就是我们这个数据要训练的数据啊。这个数据的输入信息，那么就在输入层，假设这个一是比较亮的，对吧？那么我们就认为，哎，这个一呢，可能是一个这样的一个数字啊。这个二呢，要暗一些，哎，我们可以认为二是这么一个数字啊。这个三呢，它两个之巅，对吧？我们可以认为是这个数字。总的意思吧，总之的意思就是，把这个图片要训练的数据数字化过后，那么输入层就是显示的是那个数字化的结果。就输入层里边是不做任何转换的啊，它就表示的是原始输入。那么这里的每一个。是原始输入，那么这里的每一个神经元，它向后边传递的结果，因为每个神经元要往后传递嘛，是吧？传递一个弯过去，对吧？输出一个弯，那么向后面传递的结果就是我们的输入这一块，能理解吗？那如果说调训练这个图片的话，它就会有一千六百个输出，对吧？产生一千六百个结果，没问题吧？好，那么接下来这个结果怎么来传呢？就是输出了过后，谁来用呢？接下来到下一个，就是第一个隐藏层了啊，隐藏层我刚才说。

---

## Scene 5

Time: 00:06:23-00:07:33
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_005_00-07-31.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_005.md`

Transcript:
一个隐藏层啊啊，隐藏层我刚才说了，设置多少个神经元，这个你就可以认为，我就随便设置，我就是随便设置的，怎么好看怎么画。在实际的工程落地的时候呢，多少个隐藏层，多少个神经元的要看一些经验。不过呢，你们也不是参与这个模型训练的，这个东西你不用去管它啊。反正他们会设置好，有哪些隐藏层，甚至呢，可能在训练的过程中发现，哎不太对劲儿，我可能要加一层，我可能要减一层，我可能要加点神经元，可能要减点神经元，他们会根据一些工程的经验慢慢去调。那么每一个神经元在干啥，没有人能清楚。每一个审计员在干啥？没有人能清楚，他这个审计员负责什么，这个审计员负责什么都不知道。谁都不知道他负责什么。最多最多只能管有多少层，每个层有多少审计员。具体每个审计员在负责啥，谁也不知道。智能是他自己产生的，不是我们人为给他规定的，规定不了啊。好，现在有输入了对吧？那么这里可以想象成什么？每一个审计员就产生一个数字，每个审计员就产生一个数字，那么就产生了一串数字。好，输入的时候，接下来下一步到达第一个隐藏层了。好，你可以看到。第一个隐藏层呢？好，你可以看到这里呢。我在图像上呢做了一个，就是直观的一个展示。你看，这里越亮的神经元，那么相当于它往后边传递的数字就越大。那么越暗的神经元呢，就是越不激活啊，越不活跃的神经元。那么它向后边传递的数字呢，就越小。我们就可以认为传递的数字越小呢，说明这个神经元不活跃啊，数字很小。数字越大呢，就说明这个神经元很活跃，传递的数字很大啊。其实就是数字大小的意思，活跃和不活跃呢。在这里，听到去。

---

## Scene 6

Time: 00:07:33-00:10:05
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\keyframes\scene_006_00-10-00.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\3.Agents底层逻辑之前向传播\work\codex-notes\scene_006.md`

Transcript:
活跃和不活跃呢，让你听上去呢比较直观一点。好，那么下一层是不是有很多的神经元？那么下一层的每一个神经元的运作方式就跟我们上节课讲的东西是一模一样的，上节课的课件拿出来啊，就是这个东西一模一样。好，比方说我们看下一层的第一个神经元，就是一啊，一这个神经元，那么它是怎么来算的呢？神经元啊，就是隐藏层第一层。好，然后第。乘第一层，好，然后第一个神经元，每个隐藏层有很多的神经元，对吧？好，第一个神经元它是怎么来算的？它全是数学运算，这里边没有什么神奇的，没有什么魔法，全是数学运算。就好比说一个小学生一样，大家说数学题，正儿八经的一个小学生跑来做这个数学题，他能做完，他可能花了非常非常长的时间，但是呢，能算完的，慢慢算呗，对吧？好，第一个神经元怎么算的？神经元的输出等于什么呢？等于前面的权重啊。好，那么第一个神经元。权重啊，好，那么第一个神经元的权重哪来的？全随机。这里边的所谓的神经元权重全随机啊，它的随机呢，它也有随机的方法啊，它随机的是通过一个正态分布来随机的。不过你不用去管它啊，反正它就是全随机的，随机的一个w一，随机的一个数字乘以x一。好，那么这个x一哪来呢？就来自于上面那一层、前面那一层的第一个神经元的输出乘以x一。好，然后加上w二随机的啊，乘以啥呢？乘以上。乘以啥呢？乘以上一个。你看，是全连接啊。我们这节课学的是全连接神经网络。神经网络呢，有全连接，也有非全连接。现在很多那个G P T都是非全连接的，但是无所谓。你理解全连接了，那其他非全连接的话就少算一些嘛，对不对？好，你看W二随机出来的啊。我们现在聊的是什么？第一个神经元它是怎么算的。这节课啊，可能很多同学数学这一块差一点的同学啊，就数量不太对的同学，可能要多次暂停，不断的去想，不断的去想，不断的去消化，才能理解这节课的东西啊。好，W二，呃，然后呢？好，W二，呃，然后呢，你看这个线啊，我这里重置一下啊，我指的这个神经元，你看是不是跟前面的所有神经元都是有连接的，每一个神经元跟前面全是有连接的，看到没？都是叫全连接，这里你看每一个神经元跟前面都是有连接的啊。所以呢，到这一层啊，现在穿的是第一个神经元啊，W二，呃，乘以什么呢？x二，x二来自什么？上一层的输出，对不对？把上一层的输出作为这一层的输入。好，然后一直加，是不是加到Wn乘以x减x八。乘以x减x八，对吧？其实不是八，是一千六。因为我们这个是四十乘四十，输入乘是一千六百个，就要进行这么多运算啊。等等，我这就写八吧，啊，是一个意思。然后呢，一直再加上一个b，b也是随机的。好，你看这些权重都是随机的。那么这些x呢，是来自于上一层的输入，是不是？b也是随机的。然后呢，这个激活函数也是固定的，叫sigmoid函数，对吧？sigmoid函数的实现有很多种，对吧？上节课我们是不是也是用的除最大值的那种方式，对不对？好，那把函数是固定的，是不是就可以算出来了？你做题嘛。做。

---
