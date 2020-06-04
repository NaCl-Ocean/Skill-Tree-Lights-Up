# 计算图

- 用来描述运算的**有向无环图**
- 由2个元素构成
  - **节点(Node) ：数据（Tensor）**
  - **边(edge)：运算（op）**

# 叶节点

- 用户创建的Tensor(通过lecture 0 中创建Tensor方法创建的Tensor)，叶节点的grad_fn为None
  
  - 对应来说，就是我们输入的input data，权重参数
  
- 非叶节点：运算过程中产生的Tensor
  
  - 拿CNN举例，就是运算过程中产生的heatmap，这部分众所周知，是不需要去更新参数的
  
- 非叶节点在反向传播`loss.backward`后会释放掉梯度，也就是无法进行更新，而叶节点的梯度在反向传播后会保存下来，进而可以更新参数
  
  - `tensor.retain_grad()`  保存非叶节点的梯度
  
- 注意：is_leaf 与 requires_gd 本质上是两个东西，叶子节点可以requires_gd，也可以不requires_gd，但是grad_fn为None

- **叶节点与requires_grad的区别与关联**

  - 叶节点当requires_grad为False时，不会对其进行自动求导，backward之后，grad自然为None

  - 叶节点requires_grad为True时，会对其进行自动求导，backward之后，grad为Tensor，也就是对应的梯度
  - 非叶节点requires_grad必然为True，但是反向传播后，grad为None



# 动态图 VS 静态图

- 动态图
  - 边搭建边计算
- 静态图
  - 搭建完成后进行计算
- 就像C语言是先编译后执行，而Python是边运行边解释，对应的优缺点也相似
  - 动态图 灵活
  - 静态图 性能更好



# autograd

- `torch.autograd.backward(tensors,grad_tensors=None,retain_graph=None,create_graph=False)`

  - **通过chain rule计算梯度，叶节点的grad属性自动更新为对应的梯度**

  - **Pytorch是动态图机制，也就是代码运行一步步从上到下，计算图也就搭好了，执行backward后，默认原计算图就销毁了。**

  - tensors：用于求导的张量，如loss

  - retain_graph：是否保存原计算图

    - 默认为False，则反向传播一次后，计算图buffer 释放掉，无法再次进行反向传播

  - create_graph：在原计算图上增加导数的计算图

    - 与retain_graph的差异

      - create_graph后去获取某个node的梯度，会发现这个梯度也是带有grad_fn的，而retain_graph后是不带有grad_fn的，也就是创建了导数计算图的差异

      - ```python
        loss.backward(gradient=torch.tensor([1.,1.]),create_graph=True)
        w.grad
        >>>tensor([6.], grad_fn=<CloneBackward>)
        loss.backward(gradient=torch.tensor([1.,1.]),retain_graph=True)
        w.grad
        >>>tensor([6.])
        ```

  - grad_tensors：多梯度权重

    - **当不指定grad_tensors时，只能对标量进行反向传播**

    - 只要loss不是一个标量，那么在求导的时候就会用到雅可比矩阵
    
    - **更一般地，当一个batch输入进网络，最终的loss一定是向量，当grad_tensors全1时，也就是SGD的实现，每个样本对于梯度的贡献相等**
    
    - ```
      eg:
      y (1*4)  x  (1*5)
      αy/αx (4*5) 那么怎样将这个梯度加到x上（维度不匹配）--》每一行加起来
      既然加起来就可以有权重，这也就是grad_tensors的权重分配，默认情况下为等权重
      ```
    
    

- `torch.autograd.grad(outputs,inputs,grad_tensors=None,retain_graph=None,create_graph=False)`
  - outputs：用于求导的张量
  - inputs：需要梯度的张量



- **梯度不会默认清零，而是会叠加（每次反向传播）**
  - 需要手动清零
- **叶节点不可以执行in-place操作**
  - 在反向传播时，梯度的值依赖于叶节点的值
  - 但是可以通过`tensor.data.op_()`曲线救国
  - **注：如果不进行自动求导（反向传播），叶节点是可以执行in_place操作的，或者在叶节点执行op时，进行in_place op也是可以的**
- **依赖于叶节点的节点默认requires_grad 为True**