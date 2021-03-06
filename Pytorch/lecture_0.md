# 张量是什么

- 多维数组
- 属性
  - `dtype`：数据类型，如`torch.FloatTensor`，`torch.cuda.FloatTensor`
    - ![](images/v2-95729ebb10269f807b0809fb09b125d0_720w.jpg)
  - `shape`：张量的形状
  - `device`：张量所在设备，GPU/CPU，加速的关键
  - `requires_grad`：是否需要求导
  - `grad`：导数/梯度
  - `grad_fn`：创建该Tensor的Function，是反向传播的关键
  - `is_leaf`：是否是叶节点
  - `ndim` : 有几维



# 张量的创建

## 直接创建

- `torch.tensor(data,dtype=None,device=None,requires_grad=False,pin_memory=False)`
  - 根据输入的data（list，numpy）创建tensor，数据类型默认与输入的data类型一致
  - device指定`tensor`所在设备，`cuda/cpu`
- `torch.from_numpy(ndarray)`
  - 根据`numpy.ndarray`创建`tensor`
  - 创建的`tensor`与原`ndarray`共享内存（视图），修改`tensor`也会修改`ndarray`的内容

## 依据数值创建

- `torch.zeros(size,out=None,dtype,layout,device,requires_grad)`
  - size：张量的形状
  - layout:内存中布局形式，`torch.sparse_coo`：稀疏张量 ，`torch.strided`：密集张量
  - out：将生成的全零张量 赋值给out指定的变量
- `torch.zeros_like(input,dtype=None,layout,device,requires_grad)`
  - 根据input的形状创建相同形状的全0张量
- `torch.ones_like(input,dtype,layout,device,requires_grad)`
- `torch.ones(size,out,dtype,layout,device,requires_grad)`
- `torch.full(size,fill_value,out,dtype,layout,device,requires_grad)`
  - 根据形状创建全为fill_value的张量
- `torch.full_like(input,fill_value,out,dtype,device,requires_grad)`
  - 根据input的shape创建全为fill_value的张量
- `torch.arange(start=0,end,step=1,out,dtype,layout,device,requires_grad)`
  - 创建等差的一维张量，数值区间为[start,end) 
- `torch.linspace(start=0,end,steps=1,out,dtype,layout,device,requires_grad)`
  - 创建均分的一维张量，数值区间为[start,end]，数列长度为steps
- `torch.eye(n,m=None,out,dtype,layout,device,requires_grad)`
  - 创建单位对角矩阵，n为矩阵行数，m为矩阵列数，不指定m默认为方阵



## 依据概率分布创建

- `torch.normal(mean,std,size,out,dtype,layout,device,requires_grad)`
  
  - mean 与 std都为张量（相同shape）：不需要指定size，生成的tensor shape与mean 和 std的形状相同，每个元素从对应的分布中采样得来
  
  - ```
    mean = [1,2,3,4]
    std = [0.1,1.2,2.3,3.4]
    
    ```
  
  - mean与std都为标量，可以指定size
  
  - mean 与 std一个为张量，一个为标量，将标量广播为张量，与上面都为张量的形式相同
  
- `torch.randn(size,out,dtype,layout,device,requires_grad)`
  
  - 生成标准正态分布的tensor
- `torch.randn_like(input,dtype,layout,device,requires_grad)`
  
  - 根据input的形状创建相同形状的正态分布张量
- `torch.rand(size,out,dtype,layout,device,requires_grad)`
  
  - 生成[0,1)区间上均匀分布的Tensor
- `torch.rand_like(input,dtype,layout,device,requires_grad)`
  
  - 根据input的形状创建相同形状的[0,1)区间上均匀分布张量
- `torch.randint(low=0,high,size,out,dtype,layout,device,requires_grad)`
  
  - 创建[low,high）区间均匀分布的，形状为size的整数Tensor
- `torch.randint_like(input,low=0,high,out,dtype,layout,device,requires_grad)`
- `torch.randperm(n,dtype,layout,device,requires_grad)`
  
  - 生成从0到n-1的随机序列， permutation （置换），索引随机打乱
  - n为张量的长度
- `torch.bernouli(input,generator=None,out)`
  
  - 以input为概率，生成伯努利分布



## new 创建

- 创建一个和原tensor同`dtype`，同`device` ，但是`size`以及其中的值不同的tensor

- `new_zeros(size, dtype=None, device=None, requires_grad=False)`

- `new_ones(size, dtype=None, device=None, requires_grad=False)`

- `new_full(size, fill_value, dtype=None, device=None, requires_grad=False)`

- `new_empty(size, dtype=None, device=None, requires_grad=False) `

- `tensor.new_tensor(input,dtype,device,require_grad)`

  - Returns a new Tensor with `data` as the tensor data. By default, the returned Tensor has the same [`torch.dtype`](https://pytorch.org/docs/stable/tensor_attributes.html#torch.torch.dtype) and [`torch.device`](https://pytorch.org/docs/stable/tensor_attributes.html#torch.torch.device) as this tensor.

  - 通常用来根据list或者tuple来构造tensor，十分简单

  - ```
    tensor = torch.tensor([2,3,4])
    tensor.new_tensor([7,8])
    
    >>>tensor([7,8])
    ```

    



# 广播机制

当tensor需要进行element-wise操作时，当tensor size不一致时，自动触发广播机制，可以进行广播有2种情况

- **A.ndim > B.ndim, 并且A.shape最后几个元素包含B.shape,** 比如下面三种情况, 注意不要混淆ndim和shape这两个基本概念
  - `A.shape=(2,3,4,5), B.shape=(3,4,5)`
  - `A.shape=(2,3,4,5), B.shape=(4,5)`
  - `A.shape=(2,3,4,5), B.shape=(5)`
- **A.ndim == B.ndim,** 并且A.shape和B.shape对应位置的元素要么相同要么其中一个是1, 比如
  - `A.shape=(1,9,4), B.shape=(15,1,4)`
  - `A.shape=(1,9,4), B.shape=(15,1,1)`



那么所谓的广播机制，也就是沿着某一维度重复，可以参照下面 的repeat以及expand（实际上expand更符合广播机制）



# 张量操作

## 张量拼接

- `torch.cat(tensors,dim=0,out)`

  - 将张量按维度dim进行拼接
  - tensors：张量序列
  - dim：要拼接的维度

- `torch.stack(tensors,dim=0.out)`

  - 在新创建的维度 dim上进行拼接

- ```
  (2*3)+(2*3) --> cat dim=0 ---> (4*3)
  (2*3)+(2*3) --> stack dim=0 ---> (2*2*3)
  ```

## 张量切分

-  `torch.chunk(input,chunks,dim=0)`
  - 将张量按照维度dim 进行平均切分
  - input：要切分的张量
  - dim：要切分的维度
  - chunks：要切分的份数
- `torch.split(tensor,split_size_or_sections,dim=0)`
  - 将张量在维度dim上进行切分
  - split_size_or_sections：为int时，表示每一份的长度；为list时，按list元素切分，sum(list)等于该维度的长度
  - dim:要切分的维度

## 张量判断

- `torch.nonzero(input,out,as_tuple=False)`

  - 查找tensor中不为0的元素，并返回这些元素在tensor中的坐标

  - as_type 为 False , 返回张量的shape为（N,ndims)

  - as_type为True，返回tuple，len(tuple)=ndims

  - ```python
    >>> torch.nonzero(torch.tensor([1, 1, 1, 0, 1]))
    tensor([[ 0],
            [ 1],
            [ 2],
            [ 4]])
    >>> torch.nonzero(torch.tensor([[0.6, 0.0, 0.0, 0.0],
                                    [0.0, 0.4, 0.0, 0.0],
                                    [0.0, 0.0, 1.2, 0.0],
                                    [0.0, 0.0, 0.0,-0.4]]))
    tensor([[ 0,  0],
            [ 1,  1],
            [ 2,  2],
            [ 3,  3]])
    >>> torch.nonzero(torch.tensor([1, 1, 1, 0, 1]), as_tuple=True)
    (tensor([0, 1, 2, 4]),)
    >>> torch.nonzero(torch.tensor([[0.6, 0.0, 0.0, 0.0],
                                    [0.0, 0.4, 0.0, 0.0],
                                    [0.0, 0.0, 1.2, 0.0],
                                    [0.0, 0.0, 0.0,-0.4]]), as_tuple=True)
    (tensor([0, 1, 2, 3]), tensor([0, 1, 2, 3]))
    >>> torch.nonzero(torch.tensor(5), as_tuple=True)
    (tensor([0]),)
    ```

- `torch.topk(input, k, dim=None, largest=True, sorted=True, out=None)`

  - 在指定维度上查找最大的k个值，返回其value 和 indices

  - dim 默认为tensor最后的维度

  - ```
    a = torch.tensor([[1,2,3],[4,5,6]])
    >>>tensor([[1, 2, 3],
            [4, 5, 6]])
    a.topk(2)
    >>>torch.return_types.topk(
    values=tensor([[3, 2],
            [6, 5]]),
    indices=tensor([[2, 1],
            [2, 1]]))
    ```

- `tensor.kthvalue(input, k, dim=None, keepdim=False, out=None)`

  - 返回第k小元素的value与index，如果dim未指定，选定为最后一维

  - ```
    >>> x = torch.arange(1., 6.)
    >>> x
    tensor([ 1.,  2.,  3.,  4.,  5.])
    >>> torch.kthvalue(x, 4)
    torch.return_types.kthvalue(values=tensor(4.), indices=tensor(3))
    
    >>> x=torch.arange(1.,7.).resize_(2,3)
    >>> x
    tensor([[ 1.,  2.,  3.],
            [ 4.,  5.,  6.]])
    >>> torch.kthvalue(x, 2, 0, True)
    torch.return_types.kthvalue(values=tensor([[4., 5., 6.]]), indices=tensor([[1, 1, 1]]))
    ```

    

## 张量索引

- `torch.index_select(input,dim,index,out)`
  - 在维度dim上，按index索引数据，返回根据index索引得到数据拼接而成的张量 
  - index type 需要为int
- `torch.masked_selct(input,mask,out)`
  - 按照mask为True进行索引（Numpy中的布尔索引）
  - 返回一维张量
  - 布尔索引类似于Numpy中布尔索引，通过`tensor>10`类似即可获得一个布尔索引
- 同样支持切片，切片得到的同样是一个视图，修改切片得到的张量同样会修改原张量
- `tensor_a[tensor_b]`  花式索引

  - [ ] 待补充

## 张量变换

- `torch.reshape(input,shape)`
  - reshape 后的张量与原张量共享内存
  - shape 中某一维度为-1 表示该维度大小根据其他维度的大小进行推断

- `torch.transpose(input,dim0,dim1)`
  
  - 交换张量的两个维度，dim0 与 dim1即为要交换的维度
  
- `torch.t(input)`
  
  - 二维张量的转置
  
- `torch.squeeze(input,dim=None,out)`
  
  - **压缩（移除）**长度为1的维度（轴）
  - 当dim为None时，移除所有长度为1的轴，若指定维度，当且仅当该轴长度为1时，可以被移除
  
- `torch.unsqueeze(input,dim,out)`
  
  - 依据dim扩展维度，dim维度的长度为1
  
- `None`

  - 类似于unsqueeze的做法，但是比较方便，返回view

  - ```python
    tensor = torch.randn(3, 4)
    print('tensor size:', tensor.size())
    tensor_1 = tensor[:, None]
    print('tensor_1 size:', tensor_1.size())
    tensor_2 = tensor[:, :, None]
    print('tensor_2 size', tensor_2.size())
    
    tensor size: torch.Size([3, 4])
    tensor_1 size: torch.Size([3, 1, 4])
    tensor_2 size torch.Size([3, 4, 1])
    ```

    

- `torch.permute(*dims)`

  - 将张量的dim进行变换，返回其view

  - ```python
    >>> x = torch.randn(2, 3, 5)
    >>> x.size()
    torch.Size([2, 3, 5])
    >>> x.permute(2, 0, 1).size()
    torch.Size([5, 2, 3])
    ```

- `torch.repeat(*sizes)`

  - 将张量重复，进而**扩展维度**

  - *size(torch.Size or int) - The **number of times** to repeat this tensor along each dimension
  
  - ```python
    >>> x = torch.tensor([1, 2, 3])
    >>> x.repeat(4, 2)
    tensor([[ 1,  2,  3,  1,  2,  3],
            [ 1,  2,  3,  1,  2,  3],
            [ 1,  2,  3,  1,  2,  3],
            [ 1,  2,  3,  1,  2,  3]])
    >>>x.repeat(4, 2).size()
    torch.size([4,6]) # 6 = 2*3
    >>> x.repeat(4, 2, 1).size()
    torch.Size([4, 2, 3]) # 3=3*1
    ```
    
  
- `torch.expand`(*sizes)`

  - *sizes(torch.Size or int) - the desired expanded **size**
  - Returns a new **view** of the self tensor with singleton dimensions expanded to a larger size.
  - 和repeat不同的是，这里的size需要和原size匹配，比如原size （1，3），那么expand size(n,3)
    - 因为只沿着dim=1的维度进行扩展

# 张量数学运算

- 下面这些数学运算有3个版本

  - `torch.op()`：函数

  - `torch.tensor.op()`：方法

  - `torch.tensor.op_()`：In_place op，加后缀`_`

  - ```python
    a = torch.rand((1,5))
    b = torch.ones(1,5)
    c = torch.add(a,b)
    >>>c = tensor([[1.5135, 1.6267, 1.7241, 1.7989, 1.6269]])
    d = a.add(b)
    >>>d = tensor([[1.5135, 1.6267, 1.7241, 1.7989, 1.6269]])
    a.add_(b)
    >>>a = tensor([[1.5135, 1.6267, 1.7241, 1.7989, 1.6269]])
    ```

    

## 加减乘除

- 加
  - `torch.add(input,alpha=1,other,out)`  
    -  element by element
    - $out= input+alpha*other$
  - `torch.addcmul(input,value=1,tensor1,tensor2,out)`  
    - element by element
    - $out = input+value * tensor1 *tensor2$
  - `torch.addcdiv(input,value=1,tensor1,tensor2,out)`
    - element by element
    - $out = input+value * tensor1 /tensor2$
- 除
  - `torch.div(input, value, out=None)`
    - value 为scalar
  - `torch.div(input, other, out=None)`
    - element by element
    - other 为 tensor
- 乘
  - `torch.mul(input, value, out=None)`
    - value 为scalar
  - `torch.mul(input, other, out=None)`
    - element by element
    - other 为 tensor

## 对数，指数，幂

- 对数
  - `torch.log(input, out=None)`
    - element by element
    - $out_i=log_e(input_i)$
  - `torch.log1p(input, out=None) `
    - $y_i=log_e(x_i+1)$
  - `torch.log2(input, out=None)`
    - $y_i=log_2(x_i)$
  - `torch.log10(input,out=None)`
    - $y_i=log_{10}(x_i)$
- 幂
  - `torch.pow(input, exponent, out=None)`
    - $y_i=input^{exponent}$
- `torch.sqrt(input,out)`
  
- 指数运算
  - `torch.exp(tensor, out=None)`
    - $y_i=e^{x_i}$
  - `torch.expm1(tensor, out=None)`
    - $y_i=e^{x_i} -1$

## 三角函数

- `torch.cos(input,out)`
- `torch.sin(input,out)`
- `torch.tan(input,out)`
- `torch.tanh(input.out)`

## 比较大小

- `torch.min`

  - `torch.min(input)`  返回该张量中所有元素中最小的元素

  - `torch.min(input,dim=0,keepdim=False)`   

    - 返回一个namedtuple (value,indices)

    - value为最小的元素值

    - indices为其的索引，注意该索引不包括当前维度

    - ```
       >>> a = torch.randn(4, 4)
       >>> a
       tensor([[-0.6248,  1.1334, -1.1899, -0.2803],
                      [-1.4644, -0.2635, -0.3651,  0.6134],
                      [ 0.2457,  0.0384,  1.0128,  0.7015],
                      [-0.1153,  2.9849,  2.1458,  0.5788]])
      >>> torch.min(a, 1)
      torch.return_types.min(
      values=tensor([-1.1899, -1.4644,  0.0384, -0.1153]), 
      indices=tensor([2, 0, 1, 0]))
          
      ```

  - `torch.min(input,other)`

    - 将input和other 按照elemnt-wise 的原则比较大小，取最小，返回value
    - input 和 other 不需要size一致，但是需要满足广播机制
    - 

## 其他

- `torch.sigmoid(input, out=None)`
  - $out_i = \frac{1}{1+e^{-input_i}}$



# 张量属性相关

- `torch.numel(input)`
  - 返回input中所有元素的个数
- `tensor.float()` or other types
  - 转换tensor的dtype
- `tensor.item()`  
  - 当只有一个元素时，以python数据类型返回该值
- `tensor.tolist()` 
  - 将tensor转为列表，对于scalars等同于`item()`

 # 其他实用操作

- `tensor.data.numpy`  tensor 转为ndarray

- `tensor.new_tensor(input,dtype,device,require_grad)`

  - Returns a new Tensor with `data` as the tensor data. By default, the returned Tensor has the same [`torch.dtype`](https://pytorch.org/docs/stable/tensor_attributes.html#torch.torch.dtype) and [`torch.device`](https://pytorch.org/docs/stable/tensor_attributes.html#torch.torch.device) as this tensor.

  - 通常用来根据list或者tuple来构造tensor，十分简单

  - ```
    tensor = torch.tensor([2,3,4])
    tensor.new_tensor([7,8])
    >>>tensor([7,8])
    ```

- `torch.clamp(input,min,max,out)`
  
  - 将input 的范围限制在[min,max]