# 张量是什么

- 多维数组
- 属性
  - `dtype`：数据类型，如`torch.FloatTensor`，`torch.cuda.FloatTensor`
  - `shape`：张量的形状
  - `device`：张量所在设备，GPU/CPU，加速的关键
  - `requires_grad`：是否需要求导
  - `grad`：导数/梯度
  - `grad_fn`：创建该Tensor的Function，是反向传播的关键
  - `is_leaf`：是否是叶节点



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
- `torch.fill(size,fill_value,out,dtype,layout,device,requires_grad)`
  - 根据形状创建全为fill_value的张量
- `torch.arange(start=0,end,step=1,out,dtype,layout,device,requires_grad)`
  - 创建等差的一维张量，数值区间为[start,end) 
- `torch.linespace(start=0,end,steps=1,out,dtype,layout,device,requires_grad)`
  - 创建均分的一维蟑螂，数值区间为[start,end]，数列长度为steps
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
- `torch,randperm(n,dtype,layout,device,requires_grad)`
  - 生成从0到n-1的随机序列
  - n为张量的长度
- `torch,bernouli(input,generator=None,out)`
  
  - 以input为概率，生成伯努利分布



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
  - split_size_or_sections：为int时，表示每一份的长度；为list时，按list元素切分
  - dim:要切分的维度

# 张量数学运算





