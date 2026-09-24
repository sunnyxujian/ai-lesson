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

## Scene 13

Time: 00:20:04-00:20:53
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_013_00-20-29.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_013.md`

Transcript:
调权重，看一下；调第二个权重，看一下；调第三个权重，看一下。呃，我用这个明暗度啊，来表示它的激活程度。这个Y值越大，它就越亮，它就越激活；Y值越小，比方说Y值小，到最后你就往往下按下去，这就完全不激活了啊，它不可能是负数的。能看到吧？哎，我调这个权重，调这个权重，调这个偏置。哎，我就可以调它的激活状态。哎，我觉得调调调调调到一个合适的东西。哎，比方说啊，调到一个一点七一。哎，我觉得哎这就符合现实情况了。哎，我们人类。哎，这就符合现实情况了。哎，我们人类做出了一个审批，也就是这个情况。假设吧，假设，我们再随便说一个吧。假设这个值，就表示能给他贷几万块钱。啊，假设我们随便假设嘛，啊，假设这个值是这个意思。啊，就不是什么通不通过了，就是能贷多少钱。好，那么调到这，哎，哎，我觉得符合现实情况。好，你就记住啊，在这种情况下应该是这个，这个，这个权重，这个偏值。好，然后呢，我们换个。

---

## Scene 14

Time: 00:20:53-00:22:33
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_014_00-21-01.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_014.md`

Transcript:
好，然后呢，我们换了一个。我希望的是啥？不是对这个输入就行，还要去对其他输入也可以。比如三十五万，这里信用分变成三百五十分。哎，它不能是一点二六，它可能得是别的值。那你要重新去调，而且调的时候呢，你还不能尽量不要影响刚才这个结果，尽量不要影响这个过程，不是人来参与去调的，人没法调这个。你知道最终这个东西叫什么名字吗？就是权重加偏置，它的一个名字加起来啊，就叫做参数。多参数，参数是什么？就是权重加偏置，就是一起同称为参数。你们知道现在的神经网络有多少参数吗？哎，你们平时看新闻都知道是吧？现在都到多少参数啊？几万亿的参数了，人咋调啊？人咋调啊？调这个没法调啊，调不了啊，这个得靠机器自己去调。那么具体它是怎么调的，就是我们后边课程要说的啊。但是呢，你现在要清楚的是，对于单个神经元，它能调的。单个神经元，它能调的只有这个东西，就是叫参数，统称为参数啊。它能调整的只能这个东西，它是输入，跟它没关系，是外界传过来的，跟它没关系。它能影响这个输出结果的只有这些参数。问题研究的关键就在于我怎么样去调整这个参数，让这个神经元带有智能。好像你任何的输出都应该得到一个预期的结果。能明白这个意思吗？我们训练整个什么训练模型啊，训练这个神经网络啊，其实本质上是一个意思。关键就在于。就是本质上是一个意思，关键就在于我们怎么去调控这些参数，让他随便给他什么输入。就在这个行业里边，这个领域里边，给他输入，他都能得到一个我们看上去是正确的结果。就在做这个事儿，就在调这些东西。能听懂吧？现在我们要讲的是单个神经元啊，后边我们会讲多个神经元是什么情况。但是呢，前提条件必须要把单个神经元理解清楚，什么叫参数，他能调的就是这些东西，他调不了别的了，你没有别的东西可调了，只能调这个。通过。

---

## Scene 15

Time: 00:22:33-00:23:25
Image: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\keyframes\scene_015_00-23-10.jpg`
Output: `C:\Users\micro\Desktop\ai-lesson\outputs\model-watchless-service\2.Agents底层逻辑之神经元\work\codex-notes\scene_015.md`

Transcript:
你没有别的东西可聊了，只能调这个。通过调这个，调这些旋钮开关，你可以把它像一个仪表盘上的各种各样的旋钮去调，怎么去调它，让它这个结果符合我们的预期。不但这个结果符合预期，其他的结果都是符合预期的。怎么去调整它？就这个问题，好吧。好，最后呢，我们来总结一下这节课学到东西：单个神经元接收一个向量，一个向量啊，是不是一个向量？多维数字对吧？传进来，输出一个标量，输出的是不是个标量？单个神经元对吧？输出的是标量。然后呢，激活函数是固定的，定死的。就这个东西，你不用去考虑。这个东西，这个东西它具体。你不用去考虑这个东西，这个东西它具体是什么函数，反正跟你没关系。定值额的，一开始定值额的，它不影响输出的。因为定值额的嘛，然后呢，你能调的只有参数，就是权重加偏置。唯一的决定了该神经元的输出是否正确。这个神经元的智能程度，就是看它的权重和偏置到底取值为多少。它是智能的。就这个问题，好吧？好，这个单个神经元的概念啊，脑袋里面过一下啊。这些可以没有理解清楚的话，你下节课就懵逼了啊。

---
