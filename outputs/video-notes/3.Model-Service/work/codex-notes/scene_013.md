## 标题
选择、结束判断与自回归循环

## Light-plus
接下来，要从概率分布里面选一个 Token，是不是要选 Token？可以理解为封装了一个方法，叫 pickToken，传入概率分布，再传一些配置，就能从中挑选一个 Token。然后把这个 Token 追加到输出里，输出数组就加入了一个 Token，也就是 push。

当然，在这之前还要判断 isOver：这个 Token 是不是结束 Token？往往模型输出完了，会有一个结束标记。不同模型的结束符号、结束 Token 可能不同，总之这里会判断。如果是结束 Token，就 break；如果没有结束，就把它加入输出。同时，input 里面也要加进去。

我把它写完，你捋一下逻辑。这是模型的输出，加入输出数组；同时，把模型给出的下一个 Token 加入输入，input 是不是多了一个？接下来再循环，把新的 input 传进去，又拿到下一个 Token，再追加到 input，再下一次循环，再追加。

看上去像什么？比如用户的问题是“你是谁”，传进去的是这句话的 Token。预测的下一个 Token，可能取出来是“我”，就把“我”追加进去，再把整个东西传进去，又拿到下一个 Token——“是”。再传进去，再拿下一个 Token。懂意思吧？它这么玩，直到拿到一个结束 Token，那就 over 了，这一次交互结束。

结束以后，output 存的就是模型输出，对不对？因为 output 只存生成的这一部分。能看懂吧？好好捋一下。如果连这段代码都看不懂，我觉得现在还不适合玩 AI，先把这些东西搞定，那就是语言基础还有问题，福利课程看一看。

这个整体结构就是自回归。什么叫自回归？你看：输入，然后追加；追加后又作为输入，得到下一个，再追加，就是自回归。

按课堂板书整理，核心伪代码如下：

```javascript
const input = [/* 之前 Token 化的结果 */];
const output = [];

while (1) {
  const prob = raw_model(input); // 下一个 Token 的概率分布
  const token = pickToken(prob, options);
  if (isOver(token)) {
    break;
  }
  output.push(token);
  input.push(token);
}
```

理解了整体结构，接下来就可以解释一个现象：为什么输入 Token 比较便宜，输出 Token 比较贵。

## Visual explainer
最终伪代码明确保留两次 push：output.push(token) 收集生成结果，input.push(token) 将生成内容带入下一轮。raw_model、pickToken、isOver 与 options 都是课堂抽象，未提供可运行实现。代码块是对画面中代码的排版转录。
