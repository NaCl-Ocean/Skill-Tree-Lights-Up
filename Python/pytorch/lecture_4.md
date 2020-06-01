参数初始化相关函数在`torch.nn.init`模块中

# 参数初始化

- 为什么需要初始化

  - ![image-20200601142647262](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200601142647262.png)

  - 以上图为例，weight初始化为均值为0，方差为1，input 均值为0，方差为1

    则$D(H_1) = D(XW_1) = \sum_{i=0}^{n}D(X_i)D(W_{1i})=n$，这样，每一层的方差都是前一层的n倍(节点数)，网络越深，越容易NAN（方差很大），导致网络无法训练

  - 而我们需要的是**方差一致性，通常为1**

  - 上述是没有加激活函数的情况，而加上激活函数通常会导致方差更小
  
- **nn.Module中的模型在初始化的时候自动初始化，如Convnd利用kaiming.normal来初始化**

  - ```python
    class _ConvNd(Module):
    
        def __init__(self, in_channels, out_channels, kernel_size, stride,
                     padding, dilation, transposed, output_padding,
                     groups, bias, padding_mode):
            super(_ConvNd, self).__init__()
            ....
            self.reset_parameters()
    
        def reset_parameters(self):
            init.kaiming_uniform_(self.weight, a=math.sqrt(5))
            if self.bias is not None:
                fan_in, _ = init._calculate_fan_in_and_fan_out(self.weight)
                bound = 1 / math.sqrt(fan_in)
                init.uniform_(self.bias, -bound, bound)
    
    ```

    

# gain

- `calculate_gain(nonlinearity,param=Nonm)`
  - 计算激活函数的方差变化尺度
  - nonlinearity：激活函数名称，'tanh'，'sigmoid'等
  - param：激活函数需要的额外参数，如Leaky ReLU需要的negative_slop

# Xavier初始化

- **对于饱和的激活函数：Sigmoid，Tanh等**
- `xavier_uniform_(tensor,gain=1.0)`
  -  xavier 均匀分布$U(-a,a)$初始化
  -  gain为激活函数的方差变化尺度
  -  根据公式    $n_iD(w) =1,n_{i+1}D(w)=1$以及 $D(w) = \frac{1}{3a^2}$，   则$a = gain \times \sqrt{\frac{6}{n_i+n_{i+1}}}$
- `xavier_normal(tensor,gain)`
  - xavier 正态分布$N(0,std^2)$初始化
  - 同上，$D(w) = \frac{2}{n_i+n_{i+1}}$，$std = gain \times \sqrt{\frac{2}{n_i+n_{i+1}}}$

# Kaiming初始化

- **针对Relu 不饱和激活函数**
- $D(w) = \frac{2}{(1+a^2)*n_i}$
- `kaiming_uniform_(tensor,a=0,mode='fan_in',nonlearity='leaky_relu')`
  - kaiming 均匀分布$U(-a,a)$初始化
  - mode  'fan_in'选择 $n_i$，’fan_out'选择$n_{i+1}$
  - nonlearity：激活函数名称
  - a：当激活函数为LeakyReLU时，使用
- `kaiming_normal_(tensor,a=0,mode='fan_in',nonlearity='leaky_relu')`
  - kaiming 正态分布$N(0,std^2)$初始化



# 均匀分布

- `uniform_(tensor,a=0.0,b=1.0)`
  - 利用均匀分布[a,b]进行参数初始化

# 正态分布

- `normal_(tensor,mean=0.1,std=1.0)`
  - 利用正态分布$N(mean,std)$进行参数初始化

# 常数分布

- `constant_(tensor,val)`
  - 将参数初始化为常数val

# 正交矩阵分布

- `orthogonal_(tensor, gain=1)`
  - 将tensor初始化为正交矩阵或者半正交矩阵

# 单位矩阵初始化

- `eye_(tensor)`
  - 将tensor初始化为单位矩阵

# 稀疏矩阵初始化

- `sparse_(tensor, sparsity, std=0.01)`

  - 将参数初始化为稀疏矩阵
  - sparsity：tensor每一列中为0元素的比例
  - std：非0元素的分布$N(0,std)$

- ```python
  w = torch.empty(10, 5)
  nn.init.sparse_(w, sparsity=0.1)
  >>>tensor([[ 3.7671e-03,  1.3017e-02, -1.3105e-02,  1.3611e-02, -4.3414e-03],
          [-9.8588e-03, -1.6610e-03,  3.8819e-03, -6.8779e-03,  7.3079e-03],
          [-4.4903e-04, -5.3596e-03,  0.0000e+00, -5.1316e-04, -6.7473e-03],
          [-5.5754e-03,  6.5058e-03,  1.6620e-02,  6.2160e-04, -2.1154e-03],
          [ 0.0000e+00, -1.6751e-02, -3.2705e-04,  0.0000e+00, -1.4799e-02],
          [-1.5207e-02,  1.9744e-04, -3.9335e-05, -2.8865e-03,  3.4776e-03],
          [-1.1804e-03, -4.7845e-03, -6.3242e-03, -2.2384e-03, -2.6415e-03],
          [-1.3095e-02,  7.0139e-03,  1.4377e-02, -9.3868e-03,  0.0000e+00],
          [ 6.0244e-03,  0.0000e+00,  1.0333e-02,  1.9589e-03, -1.6687e-02],
          [ 7.7760e-03, -2.0742e-02,  9.3245e-03,  1.2779e-02, -8.9075e-03]])
  ```

  

