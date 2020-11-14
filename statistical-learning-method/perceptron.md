# 感知机

## 概念

- 定义：
  - 输入空间 $X \sube R^n$ ，输出空间$Y={+1,-1}$，输入$x$表示实例的特征向量，$f(x)=sign(w\centerdot x+b)$
  - $sign(x) = +1 \ \ \ if \  x\ge 0 \ else -1$
  - 超平面 $w \centerdot x + b=0$ ，w是超平面的法向量，b是超平面的截距
- 线性分类模型，**二分类模型**，判别模型
- 损失函数
  - $L(w,b) = -\sum_{x_i \sub M}{y_i(w \centerdot x_i+b)}$
  - M表示所有误分类的点的集合
  - 对于误分类的点，$y_i(w \centerdot x_i + b) <= 0$

- 当数据集线性可分时，感知机学习算法可以收敛，反之，学习算法不会收敛，迭代结果会震荡



# 学习算法

- 原始形式

  - 选取初值$w_0 \ \ b_0$，学习率$\eta$
  - 在训练数据集中选取数据$(x_i,y_i)$
  - 如果$y_i(w \centerdot x_i + b) <= 0$，那么表示该点是误分类的点
    - $w \leftarrow w + \eta y_i x_i$
    - $b \leftarrow b + \eta y_i$
  - 循环上述步骤（除了初始化步骤），直到训练集中没有误分类点

  - 什么意思：
    - 回到熟悉的深度学习领域里，相当于batchsize=1，每次送入网络一个点，如果分类正确，不反向传播，分类错误，则进行反向传播

- 对偶形式

  - $w = \sum_{i=1}^{N}\alpha_iy_ix_i$，$b = \sum_{i=1}^{N}\alpha_iy_i$，$\alpha_i$表示训练数据集中的第i个数据被误分类的次数
  - 选取初值$\alpha = (\alpha_1, \alpha_2, ......., \alpha_N) = 0, b=0$
    - 其中N是训练数据集的size
  - 在训练数据集中选取数据$(x_i,y_i)$
  - 如果    $y_i(\sum_{j=1}{N}\alpha_jy_jx_j \centerdot x_i +b) \le 0$
    - $\alpha_i \leftarrow \alpha_i + \eta $
    - $ b \leftarrow b + \eta y_i$
  - 循环上述步骤（除了初始化步骤），直到训练集中没有误分类点





