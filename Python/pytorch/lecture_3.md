# 模型构建

```python
class net(torch.nn.Module):
    def __init__(slef,...):
        super(net,self).__init__()
       	self.conv1 = conv2d()
    def forward(self,input,...):
        ....
        return output
```

- 继承自`torch.nn.Module`
- `__init__` 用于搭建子Module
  - 每一个子模型也继承自`torch.nn.Module`
  - 在赋值时`self.conv1 = conv2d()`，实际上时调用了`__setattr__`方法
    - 若是Module，则存储到`modules`属性中
    - 若是parameter，则存储到`parameters`中
- `forward` 用于前向传播
  - 当调用`net(input)`时，实际上是调用了`nn.Module`中的`__call__`方法，进而调用了`forward`方法



# nn.Module

**八大属性，全部为OrderDict**

- parameters：存储管理`nn.Parameter`类
  
  - **注意：Module类有一个方法`parametrs()`，返回module中所有可学习的parameters，与module.parameters的值可能不一样**
  
- modules：存储管理`nn.Module`类

- buffers：存储管理缓冲属性

  - buffer 和 parameter 的区别是 parameter 是可以进行学习的，而buffer是无法进行更新学习的，但是buffer仍然属于参数，比如batchnorm中的running_mean。
  - [参考](https://zhuanlan.zhihu.com/p/89442276)

- ***__hooks：存储管理钩子属性

- ```python
  class Module(object):
      dump_patches = False
      _version = 1
  
      def __init__(self):
          """
          Initializes internal Module state, shared by both nn.Module and ScriptModule.
          """
          torch._C._log_api_usage_once("python.nn_module")
          self.training = True
          self._parameters = OrderedDict()
          self._buffers = OrderedDict()
          self._backward_hooks = OrderedDict()
          self._forward_hooks = OrderedDict()
          self._forward_pre_hooks = OrderedDict()
          self._state_dict_hooks = OrderedDict()
          self._load_state_dict_pre_hooks = OrderedDict()
          self._modules = OrderedDict()
  ```

  

## Container

**封装多个子模型为一个子模型**

- **Sequential**

  - 按顺序封装一组网络层,常用于block构建

  - 内部实现了forward

  - ```python
    # 给每个子模型命名
    Sequential_1 = nn.Sequential(OrderdDict({
        'conv_1':nn.Conv2d(3,6,5),
        'relu1':nn.ReLu(inplace=True),
    }))
    # 不命名，利用数字0，1，...来命名
    Sequential_1 = nn.Sequential(
        nn.Conv2d(3,6,5),
        nn.ReLu(inplace=True),
    )
    ```

- **ModuleList**

  - 以迭代（for）的方式构建网络层，用于大量重复网络构建

  - ```python
    # 构建10个卷积层
    ModuleList_1 = nn.ModuleList([nn.Conv2d(1,1,3) for i in range(10)])
    ```

- **ModuleDict**

  - 以索引（key，value）的方式调用网络层，用于可选择的网络层构建

  - ```python
    Moduledict_1 = nn.ModuleDict({
        'conv':nn.Conv2d(10,10,3),
        'pool':nn.MaxPool2d(3)
    })
    # 调用
    Moduledict_1['conv'](input)
    ```

## Method

- `module.paramters()`
  
  - 返回module中可学习的参数
  
- `module.named_parameters()`
  
  - 返回module中可学习的参数及其名字（tuple）
  
- `module.modules()`
  
  - 返回module中所有的子module
  
- `module.named_modules()`
  
  - 返回module中所有的module（子module，子module的子module等等....）及其名字（tuple）
  
- `module.named_children()`

  - 返回module中所有的子module及其名字（tuple）

- ```python
  class net_test(nn.Module):
      def __init__(self):
          super(net_test, self).__init__()
          self.conv1=nn.Conv2d(3,3,3,1)
          self.relu = nn.ReLU()
          self.block1=nn.Sequential(nn.Conv2d(3,3,3,1),nn.ReLU())
  
      def forward(self,input):
          output_1 = self.conv1(input)
          output_2 = self.relu(output_1)
          output = self.block1(output_2)
          return output
  net = net_test()
  
  net.named_modules()
  >>>[('', net_test(  --》总的module
    (conv1): Conv2d(3, 3, kernel_size=(3, 3), stride=(1, 1))
    (relu): ReLU()
    (block1): Sequential(
      (0): Conv2d(16, 16, kernel_size=(3, 3), stride=(1, 1))
      (1): ReLU()))), 
      ('conv1', Conv2d(3, 3, kernel_size=(3, 3), stride=(1, 1))), --》子模型
      ('relu', ReLU()), --》子模型
      ('block1', Sequential((0): Conv2d(16, 16, kernel_size=(3, 3), stride=(1, 1))  (1): ReLU())), --》子模型
      ('block1.0', Conv2d(16, 16, kernel_size=(3, 3), stride=(1, 1))), --》子模型的子模型
      ('block1.1', ReLU())]  --》子模型
  
  net.named_modules()
  >>> ('conv1', Conv2d(3, 3, kernel_size=(3, 3), stride=(1, 1))), --》子模型
      ('relu', ReLU()), --》子模型
      ('block1', Sequential((0): Conv2d(16, 16, kernel_size=(3, 3), stride=(1, 1))  (1): ReLU())), --》子模型
  ```

- `module.train()`
  
  - 设置module为train模式
  
- `module.eval()`
  - 设置module为eval模式，对于Dropout，BatchNorm等有影响
  - 对于Dropout，BatchNormalization等，在训练时和测试时采取的策略不同
  
- `model.add_module(str,module)`

  - 添加子module，与`__init__`中`self.str = module`等价
  - 可以动态添加子模块

# nn.Parameter

- 可学习的参数

# nn.functional

- 函数的具体实现，如卷积，池化等

# nn.init

- 参数初始化方法



# 卷积层

- `Conv2d(in_channels,out_channels,kernel_size,stride=1,padding=0,dilation=1,groups=1,bias=True,padding_mode='zeros')`
  - in_channels：输入通道数
  - out_channels：输出通道数，等价于卷积核的数量
  - kernel_size：卷积核尺寸，int or (h,w) 
  - stride：步长，int or (h,w)
  - padding：填充像素数量，int or (h,w)
  - diltation：空洞卷积间隔数
  - groups：分组卷积设置
  - bias：是否需要偏置
- `ConvTranspose2d(in_channels,out_channels,kernel_size,stride=1,padding=0,output_padding=0,groups=1,bias=True,dilation=1,padding_mode='zero')`
  - 转置卷积，upsample
  - in_channels：输入通道数
  - out_channels：输出通道数，等价于卷积核的数量
  - kernel_size：卷积核尺寸
  - stride：步长
  - padding：填充像素数量
- **`Depthwise conv + Pointwise conv`**
  - `Depthwise conv `的groups 设为in_channels
  - `Pointwise conv`的kernel size设为1，
  - [参考](https://zhuanlan.zhihu.com/p/80041030)

# 池化层

- `MaxPool2d(kernel_size,stride,padding=0,dilation=1,ceil_mode=False,return_indices=False)`
  - kernel_size：卷积核尺寸
  - stride：步长
  - padding：填充像素个数，一般不填充
  - dilation：池化核间隔大小
  - ceil_mode：尺寸向上取整，计算输出的特征图大小时，当无法除整时，如何决定输出特征图的大小
  - return_indices：记录池化像素索引，也就是最大像素在原图中的位置，当设置为True时，返回indices
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200531182541998.png" alt="image-20200531182541998" style="zoom:70%;" />

- `AvgPool2d(kernel_size,stride,padding=0,ceil_mode=False,count_include_pad=True,divisor_override=None)`
  - count_include_pad：填充值用于计算（若进行了填充）
  - divisor_override：除法因子，一般情况下，计算平均值需要除以kernel的大小，当设置了该值后，除以的是该值divisor_override
- `MaxUnpool2d(kernel_size,stride,padding=0)`
  - 最大值反池化，up_sample
  - 在进行forward时，还需要传入`indices`参数，也就是前面最大池化`return_indices`

# 线性层

- `Linear(in_features,out_features,bias=True)`
  - in_features：输入的节点数
  - out_features：输出的节点数
  - bias：是否加偏置



# 激活函数层

- `Sigmoid()`
  - $f(x)=\frac{1}{1+e^{-x}}$
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200531184700276.png" alt="image-20200531184700276" style="zoom:50%;" />
  - 导数在[0,0.25]，容易导致梯度消失
  - 输出为非0均值，破坏数据分布

- `tanh()`
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200531184818218.png" alt="image-20200531184818218" style="zoom:40%;" />
  - 导数在[0,1]之间，易导致梯度消失
- `ReLU()`
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200531185111635.png" alt="image-20200531185111635" style="zoom:50%;" />
  - 负半轴导致死神经元
- `LeakyReLU(negative_slope=0.01)`
  - 负半轴加一个很小的斜率
- `PReLU(init=0.25，num_parameters=1)`
  - 可学习斜率（负半轴的斜率）
  - init：初始化斜率
  - If called with `nn.PReLU(nChannels)`, a separate a*a* is used for each input channel.
- `RReLU(lower,upper)`
  - 随机在[lower,upper]中选择一个数作为负半轴的斜率
- <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200531190003191.png" alt="image-20200531190003191" style="zoom:50%;" />



