# KNN

## 概念

- **多分类模型**，没有训练的显式过程，在test的时候仍然需要训练集的所有数据
- 输入：训练数据集 $ T = {(x_1, y_1), (x_2, y_2), ......, (x_N,y_N)}$
  
  - 其中$x_i \in X \sub R^n$，$ y_i \in Y \subset \{c_1,c_2,....,c_k\}$，$i=1,2,......, N$ 
- 输出：实例x所属的类y

- 步骤
  - 根据给定的**距离度量** 在训练集中找出与输入实例x**距离最近的k个点**，**涵盖这k个点的邻域**记作$N_k(x)$
  - 在$N_k(x)$ 中根据**分类决策规则**（如多数表决）决定x的类别y
- 三要素
  - **距离度量**
    
    - $L_p$距离 $L_p(x_i,x_j) = (\sum_{l=1}^n|x_i^{(l)} - x_j^{(l)}|^p)^{ \frac1p}$，l表示第l个维度
    - p等于2表示欧式距离
    - p等于1表示曼哈顿距离
    - p等于$\infty$时，表示各个维度距离的最大值
  - **k值的选择**
    
    - k值过小，模型过于复杂，对于邻近的点过于敏感
    - k值过大，模型过于简单，极端情况下，k取值为训练数据集的大小，那么无论输入什么，都分类为训练数据集中的多数类
    - 一般选择k比较小，采用交叉验证的方法选取最优的k值
  - **分类决策规则**

    - 多数表决：输入实例的k个近邻的训练实例中的多数决定输入实例的类别，多数表决等价于经验风险最小化

    - 经验风险：假设输入为$x$，其最近邻的k个训练实例点构成集合$N_k(x)$。如果涵盖$N_k(x)$的区域的类别是$c_j$,那么误分类率：

      - $$
        \frac1k \sum_{x_i \in N_k(x)} I(y_i \neq c_j)
        $$

        



## kd tree

- 对输入的实例搜索k个近邻点时，有两种办法
  - **线性扫描**：当训练数据量很大时，不可取
  - **kd tree**：当训练数据量很大（训练数据量>>2*dim)，优势明显
    - dim也就是输入数据x的维度

- **对于树，最常用的就是递归**

## 构造kd tree

- 输入：k维空间数据集 $T={x_1,x_2,......,x_N}$,其中$x_i = {x_i^{(1)},x_i^{(2)},......,x_i^{(k)}}$,$i=1,2,...N$
- 输出：kd tree
- 开始：构造根节点，根节点对应于包含T的k维空间的超矩形区域
  - 选择$x^{(1)}$为坐标轴，以T中的所有实例的$x^{(1)}$坐标的**中位数**为切分点，将根节点对应的超矩形区域切分为两个子区域
  - 由根节点生成深度为1的左、右子节点；子左节点对应坐标$x^{(1)}$小于切分点的子区域，子右节点对应坐标$x^{(1)}$大于切分点的子区域
  - 掉落在切分超平面上的实例点保存在根节点
- 重复：对深度为j的结点，选择$x^{(l)}$为切分的坐标轴，$l=j(mod k) +1$，以该节点的区域中所有实例的$x^{(l)}$坐标的中位数为切分点，将该点对应的超矩形区域切分为两个子区域，由该节点生成深度为1的左、右子节点；**子左节点对应坐标$x^{(l)}$小于切分点的子区域**，**子右节点对应坐标$x^{(l)}$大于切分点的子区域**

- 直到两个子区域没有实例存在时停止

## 搜索最近邻

- 输入：构造好的kd tree，目标点x
- 输出：x的最近邻
- 在kd tree中找出包含目标点x的叶节点：从根节点出发，递归地向下访问kd tree。**若目标点x当前维的坐标小于切分点的坐标，则移动到左子节点，否则移动到右子节点，直到子节点为叶节点为止。**
- 以此叶节点为“当前最近点”
- 递归地向上回退，在每个节点进行如下操作
  - 如果当前节点保存的实例点比当前最近点距离目标点更近，则以当前节点为“当前最近点”
  - 当前最近点一定存在于该节点一个子节点对应的区域。检查该子节点的另一子节点对应的区域是否有更近的点
    - 也就是判断当前节点切分点的维度与目标点x该维度的距离是否小于当前最近点距离目标点的距离
    - 如果小于，则移动到当前节点的另一个子节点，接着**递归地进行最近邻搜索**
    - 如果不小于，继续向上回退
- 当回退到根节点时，停止，"当前最近点"即为目标点的最近邻

