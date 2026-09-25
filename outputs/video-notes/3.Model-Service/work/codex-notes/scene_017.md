## 标题
top_k：按候选数量截断

## Light-plus
这两个参数是什么意思？就是在概率分布中截断。比如概率分布中有一百个 Token，每个对应一个概率。top_k 和 top_p 是先从一百个里面挑选，不要那么多，可能只选五个、十个。挑选完，再用 temperature 随机选择。懂意思吧？这两个作用很好理解，只是挑选规则不同。

看一下 top_k，搜一下。现在 OpenAI 这个接口里好像没有 top_k 了，只有 top_p。我还是都讲讲。

先讲 top_k，它是按数量取。比如下一个 Token 有一百种情况，每个有不同概率。我按概率从高到低排序，要取多少个？比如传 10，就是只取概率前十的 Token，再在这些 Token 里面使用 temperature 进行随机选择。排在十以后的 Token，绝对不可能出现在结果里。这就是 top_k 的做法。

top_p 则按概率选择，叫核采样。

## Visual explainer
便签写有 temperature、top_k 10、top_p，编辑器显示 pickToken(prob, options)。原课现场搜索后指出其所看的 OpenAI 接口未提供 top_k，因此不能假定三个参数在每家接口中都可直接使用。这里保留原课先截断、再选择的教学描述，未扩展底层采样处理顺序。
