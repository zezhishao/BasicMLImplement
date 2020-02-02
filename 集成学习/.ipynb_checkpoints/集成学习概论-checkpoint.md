### 1. 什么是集成学习

集成学习是一类提升方法。**“团结就是力量”**就是他的宗旨。

**通过结合多个模型，可以产生一个更强大的模型。**是他的基本指导思想。

集成学习是在Kaggle或者天池等比赛中，想要达到最高名次时，几乎必用的手段。最朴素的想法是投票voting。Voting是最朴素的方法。鉴于过于简单朴素，效果提升有限，用得很少。

### 2. 集成学习主要方法
- Bagging
- Boosting
- Stacking

举个🌰：

Bagging：随机森林

Boosting：Adaboost

Stacking：Stacking的方法更加灵活，可以自定义层数、数据重采样方法。

### 3. 集成学习的特点

集成学习的特点是**使用多个模型**，与之相伴的另一个特点是**对数据集的各种使用方法**。

### 4. 设计一个集成学习模型时需要关注的问题：

(1). 如何设计弱学习器

> 通常这些学习器的形式是一致的

(2). 如何把这些弱学习器结合在一起

> 结合多个学习器的算法成为Meta-Algorithms，这个算法为了产生更好的效果，调用其他算法（若分类器）作为输入。

> what is meta-algorithms：
Loosely speaking, a meta-algorithm is an algorithm that wraps and executes other algorithms and might feed them input data or use their output data. A common goal is to achieve a better task performance compared to the performance of each of those algorithms on their own.
