# 学习率调整

- Pytorch中学习率调整的对象在`torch.optim.lr_scheduler`中

  - scheduler的作用是调整学习率，也就是调整optimizer中的学习率，也就是`optimizer.param_groups['lr']`的值

  - 学习率在每个epoch后调整，而不是每个iteration调整

  - 在实际训练过程中，两步就可以了

    - ```python
      # 初始化scheduler
      scheduler = optim.lr_scheduler.StepLR(optimizer,...)
      ....
      for epoch in range(100):
          for data,label in dataloader:
              .....
           # 更新学习率
           scheduler.step()
      ```

- 父类`_LRScheduler`，具体的scheduler继承自该类，主要实现了一下几个方法

  - `step()` 更新学习率

    - ```python
      ....
      values = self.get_lr()
      for param_group, lr in zip(self.optimizer.param_groups, values):
          param_group['lr'] = lr
      ```

  - `__init__`初始化scheduler中的普遍参数

    - ```python
      self.optimizer = optimizer
      if last_epoch == -1:
          for group in optimizer.param_groups:
              group.setdefault('initial_lr', group['lr'])
      self.base_lrs = list(map(lambda group: group['initial_lr'], optimizer.param_groups))
      self.last_epoch = last_epoch
      ....
      ```

      

- 具体的scheduler（子类），主要实现以下方法

  - `get_lr()`  计算学习率更新的值，用于`step`调用
  - `__init__` 初始化特殊的参数



# StepLR

- 等间隔调整学习率
- `StepLR(optimizer,step_size,gamma=0.1,last_epoch=-1)`
  - step_size：调整间隔数
  - gamma：调整系数
  - 每隔step_size个epoch，利用$lr = lr*gamma$来调整学习率

# MultiStepLR

- 在给定epoch时刻，调整学习率

- `MultiStepLR(optimizer,milestones,gamma=0.1,last_epoch=-1)`

  - milestones：给定调整时刻数，list，eg

    - ```
      milestones = [50,70,90] 在第50个epoch，70个epoch，90个epoch调整学习率
      ```

  - gamma：调整系数

# ExponentialLR

- 按指数衰减调整学习率
- `ExponentialLR(optimizer,gamma,last_epoch=-1)`
  - $ lr = lr*gamma^{epoch}$
  - 每个epoch都调整学习率



# CosineAnnealingLR

- 按余弦周期调整学习率
- `CosineAnnealingLR(optimizer,T_max,eta_min=0,last_epoch=-1)`
  - T_max ：余弦周期的一半
  - eta_min：学习率的最小值，最大值为optimizer的初始学习率
- <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200603102801798.png" alt="image-20200603102801798" style="zoom:70%;" />



# ReduceLRonPlateau

- 监控某个指标，当指标不再变化时，调整学习率
- `ReduceLROnPlateau(optimizer,mode='min',factor=0.1,patience=10,verbose=False,threshold=0.0001,threshold_mode='rel',cooldown=0,min_lr=0,eps=1e-08)`
  - mode
    - min：当监控指标不下降时，调整
    - max：当监控指标不上升时，调整
  - factor：同上面的gamma
  - patience：当指标连续多少个epoch不变化时，调整学习率
  - cooldown：当调整学习率后，多少个epoch内不再调整
  - min_lr：学习率下限

# LambdaLR

- 自定义调整学习率

- `LambdaLR(optimizer,lr_lambda,last_epoch=-1)`

  - lr_lambda：function  or list

- 当lr_lambda为list时，可用于对不同的参数组进行不同的学习率调整策略

  ```python
  # 在第50个epoch后，每10个epoch调整学习率
  # 函数的input为学习率，output为学习率调整因子，也就是gamma
  lambda1 = lambda epoch:(epoch-50)//10 **0.1 if epoch>50 and epoch%10==0 else 1
  ```

  ```python
  def get_lr(self):
      .....
      return [base_lr * lmbda(self.last_epoch) --》lmbda也就是传入的函数
              for lmbda, base_lr in zip(self.lr_lambdas, self.base_lrs)]
  ```

  