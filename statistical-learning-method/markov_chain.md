# 隐马尔可夫模型

- 隐马尔可夫模型由三个参数确定
  - 假设给定隐状态的个数为N，**所有隐状态的集合为 $Q = \{q_1,q_2,...,q_N\}$**
  - 所有观测状态的个数的为M，**所有观测状态的集合为 $V=\{v_1,v_2,...v_M\}$**
  - **初始概率分布** $\pi = \{\pi_i\}, i=1,2,3,...,N$，
  - **状态转移概率(矩阵)** $A = [a_{ij}]_{N*N}, i=1,2,...,N, j=1,2,...,N$
  - **观测概率分布(矩阵)** $B = [b_{jk}]_{N*M} = [b_j(k)], j=1,2,...,N, k=1,2,...,M$
  - 至于状态转移概率的性质和观测概率分布矩阵的性质，随机过程中讲过，在此不再赘述

- 隐马尔可夫模型的两个假设
  - **齐次马尔可夫性假设**  （无后效性）
  - **观测独立性假设** 任意时刻的观测只依赖于该时刻的马尔可夫链的状态

- 马尔可夫模型的三个基本问题 : **定义模型的参数$\lambda = \{\pi, A, B\}$    观测序列 $O = \{o_1, o_2, ..., o_T\}$， 隐状态序列 $I=\{ i_1, i_2,...,i_T \} $ **

  - **概率计算问题**：***在给定模型参数和观测序列的情况下，计算观测序列出现的概率，***也就是计算
    $$
    P(O|\lambda)
    $$

  - **学习问题**：***在给定观测序列的情况下，估计出模型参数，***也就是计算
    $$
    arg \max_{\lambda} P(O|\lambda)
    $$

  - **预测问题**：***在给定模型参数和观测序列的情况下，计算最有可能的隐状态序列***，也就是计算
    $$
    arg\max_{I} P(I|O,\lambda)
    $$

- 马尔可夫模型实质上是一个概率有向图模型

## 概率计算问题

### 直接计算法

- 列举出所有可能的隐状态序列，对每一个可能的隐状态序列，计算观测序列出现的概率，之后进行求和

  - 序列长度为T，所有可能的隐状态数目为N，则共有$ N^T$种可能的隐状态序列。
  - 对每一个隐状态序列，计算观测序列出现的概率需要进行$2T$次乘法
  - 计算复杂度为$O(TN^T)$

  $$
  P(O|\lambda) = \sum_{I} P(O,I|\lambda) \times P(I|\lambda) \\
  = \sum_{i_1,i_2,...,i_T} \pi_{i_1} b_{i_1}(o_1) a_{i_1i_2} b_{i_2}(o_2)...a_{i_{T-1}i_{T} } b_{i_T}(o_T)
  $$

  

### 前向算法

- 定义**前向概率**： $\alpha_t(i) = P(o_1,o_2,...,o_T,i_t = q_i|\lambda)$，也就是到当前时刻$T$下观测序列为$\{o_1,o_2,...,o_t\}$且隐状态为$q_i$的联合概率

- 通过递推关系，我们可以求出$\alpha_{t+1}(j) = (\sum_i \alpha_t(i) \times a_{ij}) \times b_i(o_{t+1})$

  - 可以看到，在每一个时刻t，我们都要对所有的隐状态计算$\alpha_t(i)$，而每一个隐状态$\alpha_t(i)$的计算都需要前一个时刻所有隐状态的$\alpha_{t-1}(i)$，因此**计算复杂度为$O(TN^2)$**

- 算法流程

  1. 计算时刻1的各个隐藏状态前向概率：
     $$
     \alpha_1(i)=π_ib_i(o_1),i=1,2,...N
     $$

  2.  递推时刻 $2,3,...T$时刻的前向概率：
     $$
     \alpha_{t+1}(i)=[\sum_{j=1}^{N}α_t(j)a_{ji}]b_i(o_{t+1}),i=1,2,...N
     $$

  3. 计算最终结果：
     $$
     P(O|\lambda)=\sum_i^N \alpha_T(i)
     $$

- 推导：递推法，以下推导中省去$\lambda$

  - 首先推导一个公式：$a$与 $c$独立，
    $$
    P(a|b)P(bc) = P(a|b)P(c|b)P(b)=p(a,c|b)P(b)=P(a,c,b)
    $$
    

  - 先去推当序列长度为1时的情况
    $$
    \alpha_1(i) = \pi_i b_i(o_1) = P(i_1=q_i)P(o_1|i_1=q_i) \\
    = P(o_1,i_1=q_i) \\
    P(O) = \sum_{i=1}^{N} \alpha_1(i) =  \sum_{i=1}^{N} P(o_1,i_1=q_i)\\
    = P(o_1)
    $$

  - 序列长度为2的情况
    $$
    \alpha_2(i) = [\sum_{j=1}^{N}α_1(j)a_{ji}]b_i(o_{2}) \\
    =[\sum_{j=1}^{N} P(o_1,i_1=q_j)P(i_2=q_i|i_1=q_j)] \  \ \ \ b_i(o_2) o_1只和i_1有关，与i_2无关 \\
    =[\sum_{j=1}^{N}P(o_1,i_1=q_j,i_2=q_i)]b_i(o_2) \\
    = P(o_1,i_2=q_i)P(o_2|i_2=q_i) \ \ o_1,o_2无关 \\
    = P(o_1,o_2,i_2=q_i) \\
    \sum_{i=1}^{N}\alpha_2(i) = \sum_{i=1}^{N}P(o_1,o_2,i_2=q_i) = P(o_1,o_2)
    $$

  - 递推可证明

### 后向算法

- 前向算法与后向算法本质上是相同的，只是一个是从前往后算，一个是从后往前算，同样计算复杂度是$O(TN^2)$

- 定义**后向概率**：$\beta_t(i) = P(o_{t+1},o_{t+2},...,o_T｜i_t=q_i)$ ，在时刻$t$状态为$q_i$的条件下，从$t+1$到$T$时刻的部分观测序列为$\{o_{t+1},o_{t+2},...,o_T\}$的条件概率

- 算法流程

  1. 初始化时刻T下的各个隐藏状态的后向概率
     $$
     \beta_T(i) = 1,i=1,2,...,N
     $$

  2. 递推时刻$T-1, T-2,...1$时刻的后向概率：
     $$
     \beta_t(i) = \sum_{j=1}^{N} a_{ij} b_{j}(o_{t+1}) \beta_{t+1}(j) ,i=1,2,...,N
     $$

  3. 计算最终结果：
     $$
     P(O|\lambda) = \sum_{i=1}^{N} \pi_i b_i(o_1)\beta_1(i)
     $$
     

## 学习问题

### 监督学习方法

- **在给定了观测序列的同时，给定了隐状态序列，*给定了S个观测序列及其对应的隐状态序列***

- 利用极大似然估计

- 转移概率的估计$\hat a_{ij}$（利用隐状态序列）

  - $A_{ij}$  **所有序列中 由隐状态$i$转到隐状态$j$的频数** 
    $$
    \hat a_{ij} = \frac{A_{ij}}{ \sum _{j=1}^{N} A_{ij}}
    $$
    

- 观测概率的估计$\hat b_j(k)$（隐状态序列+观测序列）

  - **$B_{jk}$ 所有序列中 隐状态为$q_j$且观测为$v_k$的频数**
    $$
    \hat b_j(k) =\frac{B_{jk}}{\sum_{k=1}^{M} B_{jk}}
    $$
    

- 初始概率的估计（利用隐状态序列）

  - S个隐状态序列中初始状态为$q_i$的频率即为估计的$\hat \pi_i$

### Baum-Welch算法

- 只给定了观测序列
- 无监督学习方法，本质上是EM算法
- 

## 预测问题

### 近似算法

- 定义$\gamma_t(i)= P(i_t = q_i|O,\lambda)$ ，也就是给定观测序列和马尔可夫模型参数，在时刻$t$时，隐状态为$q_i$的概率

  - 以下推导中省去$\lambda$

  $$
  \alpha_t(i) \beta_t(i) = P(o_1,...,o_t,i_t=q_i)P(o_{t=1},...,o_T|i_t=q_i) \\
  = \frac{P(o_1,...,o_t,i_t=q_i) P(o_{t+1},...,o_T,i_t=q_i)}{P(i_t=q_i)} \\
  = \frac{P(o_1,...,o_t|i_t=q_i) P(o_{t+1},...,o_T|i_t=q_i) P(i_t=q_i) P(i_t=q_i)}{P(i_t=q_i)}\\
  = P(o_1,...,o_t|i_t=q_i) P(o_{t+1},...,o_T|i_t=q_i) P(i_t=q_i) \\
  = P(o_1,...,o_t,o_{t+1},...,o_T|i_t=q_i)P(i_t=q_i) \\
  = P(o_1,...,o_t,o_{t+1},...,o_T,i_t=q_i)\\
  \frac{\alpha_t(i) \beta_t(i)}{P(O)} = P(i_t=q_i|O) = \gamma_t(i)
  $$

- 近似算法的思想就是对每一个时刻，分别求使$\gamma_t(i)$最大的隐状态$q_i$，这样就得到了最后的隐状态序列。

### 维特比算法

- 核心思想是用动态规划求解概率最大的路径

- 在时刻t状态为$i$的所有单个路径中最大的概率值
  $$
  \sigma_t(i) = \max_{i_1,i_2,...,i_{t-1}} P(i_t=i, i_{t-1},...,i_1,o_1,...,o_t|\lambda)
  $$

- 时刻t+1时状态为$i$的所有单个路径中最大的概率值可以由$\sigma_t(i)$推出来
  $$
  \sigma_{t+1}(i) = \max_{1\leq j \leq n} [\sigma_{t}(i)a_{ji}] b_i(o_{t+1})
  $$
  

- 算法流程

  1. 初始化 $\Psi$记录的是最大概率的路径，$\sigma$记录的是最大概率
     $$
     \sigma_1(i) = \pi_i b_i(o_1)i =1,2,...,N \\
     \Psi_1(i) = 0,i =1,2,...,N
     $$

  2. 递推 对$t=2,3,...,T$
     $$
     \sigma_{t}(i) = \max_{1\leq j \leq n} [\sigma_{t-1}(i)a_{ji}] b_i(o_{t-1}),i=1,2,...,N \\
     \Psi_{t}(i) = argmax_{1\leq j \leq n} [\sigma_{t-1}(i)a_{ji}]
     $$

  3. 终止
     $$
     P^{*} = \max_{1\leq i \leq N} \sigma_T(i) \\
     i^*_T = argmax_{1\leq i \leq N} [\sigma_T(i)]
     $$
     

- 推导：递推法，以下推导中省去$\lambda$

  - 先去推当序列长度为1时的情况
    $$
    \sigma_1(i) = \pi_i b_i(o_1) = P(i_1=q_i)P(o_1|i_1=q_i) \\
    = P(o_1,i_1=q_i)= P(i_1=q_i|o_1)P(o_1) \\
    = P(i_1=q_i|o_1); \  \ \ \ ( P(o_1)=1) \\
    $$
    