# Optimizer

- 管理并更新模型中可学习参数的值
- pytorch中optimizer相关的内容位于`torch.optim`模块中

## 属性

- defaults
  - 优化器的超参数，如learning rate，momentum等
- state
  - 参数的缓存，如momentum的缓存
- param_groups
  - 管理的参数组，`list[{'params':param_groups,'lr':lr,...}]`，Tensor
  - 每一组参数对应一组超参数
  - 根据python的语法，在这里存放的实质上是地址，因此与模型中的参数共享内存
- \_step\_count
  - 参数更新的次数



## zero_grad

- `optimizer.zero_grad()`

- 清空管理参数的梯度

- ```python
  def zero_grad(self):
      for group in self.param_groups:
          for p in group['params']:
              if p.grad is not None:
                  p.grad.detach_()
                  p.grad.zero_()
  ```

  

- 根据lecture_1 中，pytorch在自动求导后，不会清零每个tensor的梯度，这样之后自动求导的梯度会进行累加，因此需要清零



## step

- `optimizer.step()`
- **根据优化器的公式进行参数的更新**
- 根据lecture_1中，在backward之后，每个参数（requires_grad）的梯度存放于grad属性中，因此step做的就是根据公式和grad，对参数进行更新(sub)

## state_dict

- `optimizer.state_dict()`

- 当前优化器的状态，主要保存的是state(buffer)，不保存参数的值

- ```
  ’state':{orderdict}
  'param_groups':[{'params':[address1,address2,....],'lr':..,....}]
  param_groups 中params保存的是需要保存的buffer地址，真正的数据在'state'中，比如SGD中需要保存g(w_i)
  ```

- ![image-20200702163051170](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200702163051170.png)

- ![image-20200702163117166](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200702163117166.png)

- ![image-20200702163133627](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200702163133627.png)

- 从上面三幅图中可以看到是params中保存的是地址，真正的buffer在state中

## load_state_dict

- `optimizer.load_state_dict(state_dict)`
- 和前面的state_dict 相对应

## add_param_group

- `optimizer.add_param_group({'params:parameter,...'})`
- 额外添加一组参数，使用不同的超参数
- 对于fine_tune 是一个有用的功能

# SGD

- `SGD(params,lr,momentum=0,weight_decay=0,nesterov=False)`
  - params：管理的参数组
    - 通常用`module.parameters()`导入一个模型中的所有参数
  - lr：初始的学习率
  - momentum：动量系数
  - weight_decay：L2正则化系数
  - nesterov：是否采用Nesterov动量

​                          $ v_i = m \times v_{i-1} +g(w_i)$ 

​							$ w_{i+1} = w_i - lr \times v_i$



