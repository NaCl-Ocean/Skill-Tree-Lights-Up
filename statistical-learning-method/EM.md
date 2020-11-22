# EM算法

- EM算法用于含有隐变量的极大似然估计

- 利用$Y$表示观测变量，$Z$表示隐变量，EM算法的思想是利用$\max_{\theta} P(Y,Z|\theta)$ 来近似 $\max_{\theta} P(Y|\theta)$（极大似然估计）

  - 注：$P(Y|\theta) = \prod_{i=1}^{N} P(y_i|\theta)$

  $$
  \max_{\theta} P(Y,Z|\theta) = \max_{\theta} \prod_{i=1}^{N}P(y_i,z_i|\theta) \varpropto \max_{\theta} \sum_{i=1}^{N} \ln (P(y_i,z_i|\theta)) \\
  $$

  - 所以这里$z_i$是极大似然估计的阻碍，也就是$Z$。

  - EM算法的另一个思想就是利用$E(z_i)$来代替$z_i$，这个$E(z_i)$也就是基于当前的$\theta_j$以及$y_i$，有了$P(z|y,\theta)$，那么就可以计算出在给定了$\theta_j$和$y_i$的条件下的$E(z_i)$
    $$
    E(z_i) = \sum_z P(z|y_i,\theta_j) \\
    ln(P(y_i, z_i | \theta)) = ln(P(y_i,E(z_i)|\theta)) = E_z[ln(P(y_i,z_i|\theta))|y_i,\theta_j] \\
    $$

  - 在这里了解得还很浅，有很多疑问。目前的理解是EM算法本质上还是一个极大似然估计，只是因为有了隐变量，无法直接利用极大似然估计去估计参数。EM算法在最大化的是Q函数，也就是上面的$\sum_{i=1}^{N}ln(P(y_i,z_i|\theta))$，***按照书上的说法，这里是完全数据的对数似然函数$logP(Y,Z|\theta)$关于在给定观测数据$Y$和当前参数$\theta_j$下对未观测数据$Z$的条件概率分布$P(Z|Y,\theta_j)$的期望***

    - 我们仔细地来看一下这个式子，当给定了当前观测数据$Y$和参数$\theta_j$的情况下，那么$Z$的分布就可以知道了，同理$E(z_i)$就可以算出，根据上述，我们要将$E(z_i)$代入$P(y_i,E(z_i)|\theta)$，求使该式子极大时的$\theta$，注意这里的$\theta$是我们要优化的变量，在给定了$P(Y,Z|\theta)$的条件下，$y_i,E(z_i)$都已知，只剩$\theta$一个变量。
    - 那么这个过程实际上就等价于给定了$Y和\theta_j$,知道了$z_i$的分布，将$z_i$代入$ln(P(y_i,z_i|\theta))$,之后再求期望，这样算下来后，最后只有一个参数$\theta$。
    - 所以实际上我们是利用上一步的参数，在上一步参数的基础上，再进行极大化的反复迭代过程

- EM算法与高斯混合模型中的作用
  - 具体的算法参考《统计学习方法》 P187