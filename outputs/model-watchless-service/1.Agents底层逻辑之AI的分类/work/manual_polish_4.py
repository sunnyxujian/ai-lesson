from pathlib import Path
import json,re
p=Path(__file__).resolve().parents[1]
bodies={
23:'''实现手段有很多。网上常刷到“线性回归”，这就是一种实现手段。讲的是什么？数学原理：空间上有一些散列的点，怎样做出一条线，让它尽量穿过更多点？得到这条线的过程，就是一个学习过程。这里也还没到代码，只是朝落地又推进一大步。

过去用线性回归，还有一些方法曾火过一段时间。这些先不用逐个了解，实现手段太多。现在最流行的是神经网络。你看，图里加黑的都是重要部分。神经网络就是实现机器学习的一种具体手段。''',
24:'''神经网络是实现机器学习的一种具体手段，但这里落地了吗？也没有，只是设计一套方法，用这套方法可以实现机器学习。这套方法很巧妙，后面会学到。

在神经网络里面，还有一个叫深度学习。深度学习其实就是神经网络。不要把“深度学习”和“强化学习”这两个词搞混，有同学容易混淆。

深度学习属于神经网络的一种实现，强化学习则是训练方法。深度学习是实现机器学习的手段，属于神经网络。深度学习一定是神经网络，只是在神经网络基础上，层变得更多、更复杂。后面讲神经网络，就知道了。

最后总结一下。今天聊了很多，实际上没有那么复杂。哲学流派当作历史知识了解就行，没人会专门问某个 AI 属于哪个哲学流派。''',
25:'''没人会专门这样问。要解决的问题，就是各个领域里的问题。各领域有各自的问题，但遇到一个共性问题：没有智能，就解决不了。领域中那些不同的东西研究清楚后，智能由谁提供？

于是讨论智能的实现方法。曾经有很多方法，机器学习是其中一种，也是现在最流行的一种。它想的是：要实现智能，得学习，不学习哪有智能？

但其他路线不一定这样想，它们认为不学习也可以有智能，而且那些方案做出过成绩。机器学习是这些年才占主流，以前主流不是它。

现在这条路强调通过学习获得智能。那么怎么训练？有一些方法，提出这些范式时仍在讨论、不负责落地。怎么落地？落地也需要方法，也需要讨论，慢慢接近，不是一下就能落地，哪有那么容易。

比如做一套系统，得做架构设计。架构设计已经落地了吗？出来的是图纸。神经网络就像一套图纸，告诉你这样可以实现。以前神经网络有比较简易的实现，现在基本是深度学习的实现。

有同学问：“袁老师，不是要讲 Transformer 吗，Transformer 在哪？”它就是深度学习的一种具体实现。Transformer 本身也还不是工程落地，只是后来工程师把它落地了。''',
26:'''这应该是什么关系？给工科生讲这一部分比较恼火。如果给高中生讲，可能会觉得老师这样说有道理，背下来就行。工科生更在意它落不落地，但这里确实还没落地。

工科生说的落地，有点像做一个功能。先做什么？需求分析。产出是文档，哪里有代码？需求分析之后，做架构设计，出来的是图纸。架构设计之后，还要进一步设计。大学里学过，我都快忘了：以前瀑布流程里，Java 那里有类设计、类图设计，出来也还是图。实现要一步一步推进，不是一下就能实现。

现在更多用敏捷开发，没有经过那么长的流程；以前大项目的瀑布式推进，就是这样一层层走。这里也是一样。机器学习是在聊实现，但实现也得逐步推进。

提出实现方案，其中有一套叫神经网络，往前推了一大步；深度学习又推进一步；Transformer 再推进一大步。接下来还需要算法工程师，基于不同行业特点具体设计，还要设计，然后才是落地。是一步一步落地的。

好，这节课讲到这里。能够认识清楚它们的关系就可以，特别是机器学习、神经网络、深度学习之间的关系。对神经网络、深度学习本身还没认识得很清楚也没关系，后面会细化讲，讲了就明白。

但至少要清楚机器学习本身与神经网络、深度学习的关系，还包括前面的分类到底是怎样一种分类。''',
27:'''把这些认识清楚，以后别人给你蹦词儿、蹦各种名词，你就不会慌了。就是这么一些东西。''',
}
for sid,body in bodies.items():
 f=p/f'work/codex-notes/scene_{sid:03d}.md';s=f.read_text(encoding='utf-8');f.write_text(s.split('## Light-plus')[0]+'## Light-plus\n'+body+'\n\n## Visual explainer'+s.split('## Visual explainer')[1],encoding='utf-8')
logpath=p/'work/correction-log.json';log=json.loads(logpath.read_text(encoding='utf-8'))
log['final_method']='All 27 scene notes manually light-polished in order. Repeated partial chunk tails joined at their original sentence position; substantive rhetorical repetitions, examples, questions, caveats and argument order retained. No algorithmic overlap deletion. Raw 101 chunks are immutable and exactly mapped.'
log['corrections'].append({'scene':15,'removed_from_teaching_text':'Human Rights Watch is a human rights organization that works to protect human rights around the world.','basis':'The original JSON has an endoftext marker before this unrelated ASR suffix. Original visual captions at 1755, 1758, 1759 and 1761 seconds continue chess and performance. The plain transcript parser had already stripped the marker. Manual polish removes only the unrelated suffix; raw original and service-audio clip retained.','verification':'visual subtitle comparison, not listening'})
log['corrections'].append({'scene':4,'from':'GPT六','to':'GPT Live','basis':'Original visible caption at 482 seconds reads 叫GPT live对吧. This preserves the source wording, not a claim about a current official product name.'})
logpath.write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
coverage=json.loads((p/'verify/content-coverage.json').read_text(encoding='utf-8'))
for row in coverage['scenes']:
 text=(p/f'work/codex-notes/scene_{row["scene"]:03d}.md').read_text(encoding='utf-8').split('## Light-plus')[1].split('## Visual explainer')[0].strip();row['note_characters']=len(text)
coverage['notes_status']='All 27 manually light-polished, no condensed substitute; chunk overlap and meaningless filler reduced; 101 raw chunks remain exactly covered in source manifest.'
(p/'verify/content-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
print('manually polished',list(bodies),'total note characters',sum(r['note_characters'] for r in coverage['scenes']))
