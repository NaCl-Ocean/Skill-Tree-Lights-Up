# 前引

- numpy中的核心是`ndarray`对象，类似于`array`对象，存储的是**相同格式**的数据。
- ndarray的size
  - <img src="F:\about study\07其他\Skill-Tree-Lights-Up\Python\numpy_shape.jpg" alt="numpy_shape" style="zoom:50%;" />

# 属性

- shape :以**tuple**的形式返回数组的形状
- ndim：返回数组的维数
- dtype：返回数组数据的格式
- size：返回数组的元素总数
- flags：更进一步详细的信息

# Universal function

- numpy内置函数
- `numpy.sin()`  `numpy.cos()`



# 查

- **索引**：`var[index]`

- **切片**：`var[start​：end：step​]`

  - 切片不会损失维度，索引会损失维度
  - 切片得到的是一个视图，修改切片得到的array会修改原array
  - 可以用`copy`来进行拷贝

- **花式索引**

  - 根据索引数组的值作为目标数组的某个轴的下标来取值。
  - 对于使用一维整型数组作为索引，如果目标是一维数组，那么索引的结果就是对应位置的元素；如果目标是二维数组，那么就是对应下标的行。
  - 花式索引得到的是一个副本，修改花式索引得到的array不会修改原array

- **布尔索引**

  - ndarray进行逻辑运算得到一个**布尔数组(mask)**

  - 布尔数组可以进行位运算 `&`，`|`，`^` ，`~`

  - 布尔索引是一种特殊的花式索引z

  - ```python
    a = np.array([4,7,8])
    >>>a<5
    >>>array([ True, False, False])
    >>>b, = (a<5).nonzero()
    >>>(array([0], dtype=int64),)
    >>>a[a<5]
    >>>array([4])
    >>>a[b]
    >>>array([4])
    ```

# 改

- 通过上述查的方法，进行修改

  - ```python
    a = np.arange(0,25).reshape(5,5)
    a[1,2] = 5 # 索引
    a[:,1] = 0 # 切片
    a[[2,4]] = 1 # 花式索引
    a[a<2] = 0   # 布尔索引
    ```

    



# 计算规则

- Operations between multiple array objects are first checked for **proper shape match**（可以广播，或者shape相同）

- Mathematical operators(+,-,*,/.......) apply **element by elemen**t, on the values.

- Reduction operations (mean,std,sum,prod.......) apply to the whole array, unless an axis is specified.

  - **指定的轴会退化掉（消失）**

  - ```
    4*5*3 --->sum(axis=-1)--->4*5
    4*5*3 --->sum(axis=-2)--->4*3
    ```

- Missing values **propagate** unless explicitly ignored.

  - ```python
    np.sum([1,np.nan,10])
    >>>nan
    np.nansum([1,np.nan,10])
    >>>11.0
    ```

    