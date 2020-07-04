

# 函数参数

- 实参

- 形参

  - **传参采用传对象的方式**，具体来说就是传入的都是变量（指向对象的指针）

  - ```python
    def test(name):
        print(id(name))
    name = ['mike']
    print(id(name))
    test(name)
    >>>2637467242888
    2637467242888
    
    name = 'mike'
    print(id(name))
    test(name)
    >>>1854626268336
    1854626268336
    ```

  - 那么这里就和part_1所说的可变数据和不可变数据就扯上关系了

    - 当传入的不可变数据时，函数内部修改数据不会影响到外部的数据

      - ```python
        def test(name):
            name = 'tom'
            print('函数内部：',name)
        name = 'mike'
        test(name)
        print('函数外部:',name)
        >>>函数内部： tom
        函数外部: mike
        ```

    - 当传入的是可变数据类型时，函数内部修改数据就会影响到外部的数据

      - ```python
        def test(name):
            name.append('tom')
            print('函数内部：',name)
        name = ['mike']
        test(name)
        print('函数外部:',name)
        >>>函数内部： ['mike', 'tom']
        函数外部: ['mike', 'tom']
        ```

- 传参

  - 将实参映射到形参上
  - 位置参数
    - 通过位置将实参与形参对应起来
    - 传参是只有`value`
  - 关键参数
    - 必须写在位置参数之后
    - 传参时`参数名=value`
  - **位置参数优先级最高，传参时写在最前面**
  - 当同时存在位置参数与关键参数时，注意一个形参被赋多个值的问题

- 定义参数

  - 默认参数   例 `def test(name='mike')`  ，name即为默认参数
  - 非默认参数
  - 默认参数写在非默认参数之后

- 非固定参数 `*args **kwargs`

  - 在定义函数时，不确定后面调用时，会传入多少个参数

  - 从下面的例子可以看出，**args参数为tuple，kwargs为字典**

  - ```python
    def test(name,*args,**kwargs):
        print(name,args,kwargs)
        
    >>>test('Mike',22,'Male')
    mike (22, 'male') {}
    >>> test('mike',age=22,sex='male')
    mike () {'age': 22, 'sex': 'male'}
    >>> test('mike',22,sex='male')
    mike (22,) {'sex': 'male'}
    ```
    

# 返回值

- 当遇到return语句时函数结束
- 没有指定return的值，返回None
- reutrn 多个值，以元组的形式打包

# 全局与局部变量

- 全局变量的作用域是整个程序，局部变量的作用域是函数内部，当函数结束后，销毁局部变量指向的对象
- 变量的查找顺序是**局部变量>全局变量**

  - 当函数内部定义了一个与全局变量同名的局部变量，函数内部生效的是局部变量，修改此局部变量不会影响到全局变量

  - 当函数内部没有定义局部变量时，函数内部使用的是全局变量
    
  - 此时函数内部能否修改全局变量还是要取决于是可变数据类型还是不可变数据类型
    
  - ```python
    def test():
        global_list = [1,2,3,4,5]
        global_list.append(7)
        print(global_list)
    
    global_list = [1,2,3,4,5]
    test()
    print(global_list)
       
    [1, 2, 3, 4, 5, 7]
    [1, 2, 3, 4, 5]
    ```
  
    

# 函数名

- **函数名同样是变量**

- 那么可以理解为定义函数实际上是在定义变量

  - ```python
    def bar():
        print("in the bar..")
    print(globals())
    >>>{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001BAE2920388>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'F:/about study/07其他/Skill-Tree-Lights-Up/Python/code/practice.py', '__cached__': None, 'bar': <function bar at 0x000001BAE29D3318>}
    ```

  - 从上面可以看出，定义的函数名（***'bar'***）（变量）是一个全局变量（当然，这取决于定义函数的位置，如果是嵌套函数，则应该是局部变量）



# 匿名函数

- `lambda arg1,arg2,...:code `

- 定义：`lambda arg1,arg2,...:code `

  - arg也就是传入的参数，可以有多个参数
  - code也就是具体的运算，运算的结果即为return，也就是只能return一个值
  - 这也就决定了运算不能太复杂，**可以写的最复杂运算是三元运算或者列表生成式**

- 调用：与正常函数调用没有区别，同样是传入参数，return结果

  - ```python
    >>> a = lambda x:x**2
    >>> a(2)
    4
    ```

  - 与其他函数结合

  - ```python
    a = [1, 2, 3, 4, 5]
    f = lambda x:x**2
    res = map(f,a)
    ```

# 高阶函数

- 接收函数作为参数

- return 返回另一个函数

- ```python
  def add(x,y,f):
      return f(x)+f(y)
  
  def get_abs(x):
      return abs(x)
  
  # 这里get_abs不可以加括号，加括号就是调用函数，
  print(add(1,-5,get_abs))
  >>>6
  ```

# 函数的递归
- 函数内部调用函数
- 需要有一个终止条件
  - 不设置终止条件的话，当达到最大递归层数，抛出error

```python
# 一个简单的利用递归实现二分查找的例子
a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107]

def half_search(a,target,index=0):
    if a[index]>target:
        index = int(index/2)
        half_search(a,target,index)
    elif a[index]<target:
        index = int(((len(a))+index)/2)
        half_search(a,target,index)
    else:
        print(index)

half_search(a,9)
```

# 内置函数

一些函数之前有用到，这里不再赘述

------

- `bool(obj)`   对于空list，空tupe，空set，空dict以及0，None返回False

- `all(iterbale) `  对可迭代对象中所有的元素调用bool(obj)为True，则返回True
- `any(iterbale)`  与all 相对
- `exec(str)`   执行字符串形式的代码 `exec('pring('hello world)')`

------

- `filter(fun,iterable)`   过滤出iterabe对象中符合条件（fun）的元素  

- `map(fun,iterable)`     对iterbale中每个对象执行fun函数
- `zip(*iterables)`    将多个iterable对象打包为1个，其中长度取决于最短的iterable对象长度
- 上述函数返回一个特定的对象（filter对象，map对象，zip对象)，通常结合list或者dict等来进一步转换
  - 对于`filter`和`map` ，一般只能用list方法
  - 当iterable对象为dict时，循环的是key

------

- `help(obj)`    返回帮助信息
- `max()`   `min()`   `len()`  

# 名称空间

- 用于存放**变量**的地方
- 不同空间中相同名字的变量互相不影响
- 四种名称空间：LEGB
  - `locals`：函数的局部变量
  - `enclosing function`：在嵌套函数中外部函数的名字空间, 若fun2嵌套在fun1里，对`fun2`来说， `fun1`的名字空间就是enclosing
  - `globals`：全局变量
  - `__builtins__`：python内置变量或内置函数
- 不同名称空间中变量的作用域不同
- 作用域
  - 全局范围：全局存活，全局有效  `globals()`
  - 局部范围：临时存活，局部有效   `locals()`
- 作用域查找顺序：当使用某个变量的名字时，从当前空间开始查找，**即locals -> enclosing function -> globals -> \**builtins\****



# 闭包

- 函数定义和函数表达式位于另一个函数的函数体内(**嵌套函数**)。而且，这些内部函数可以访问它们所在的外部函数中声明的所有局部变量、参数。当其中一个这样的内部函数**在包含它们的外部函数之外被调用**（**外函数返回该内部函数**）时，就会形成闭包。

- 此时该内部函数不仅仅是一个函数对象，在外面包裹了一层作用域

- ```python
  def outer():
      name = 'test'
      def inner():
          print("在inner里打印外层函数的变量",name)
      return inner 
  f = outer() 
  f()
  >>>在inner里打印外层函数的变量 test
  ```

# 装饰器

- 软件开发的一个原则：开放-封闭

  - 已经实现的功能代码不应该修改
  - 对现有功能拓展开放

- 如何保持一个已经实现的功能代码块不修改，而对其进行扩展

- ```python
  def new_feature(func):
      def inner(*args,**kwargs):
          ......
          func()
          ......
       return inner
  
  @new_feature
  def old_feature(arg1,arg2,...):
      ......
  @new_feature
  def old_feature2():
      ....
  ```

- `@new_feature`   等价于  `old_feature = new_feature(old_feature)`

- 此时，调用`old_feature()`  就已经不再是执行`old_feature`下的code，而是`new_feature`中`inner`下的code

- 另外一个需要注意的是，`inner`的参数最好使用可变参数，这样`new_feature`可以为多个`old_feature`所使用，不会引发参数冲突的问题

- 从上面可以看出，装饰器本质上利用闭包，但是更多的感觉是语法糖。



# 列表生成式

- `a = [i+1 for i in range(10)]`     `a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- `a = [i for i in range(10) if i%2==0]`    `a = [0, 2, 4, 6, 8]`

# 生成器

- 边循环边计算后面元素

- **生成器在python 中的体现就是generator对象**

- 为什么需要生成器
  - 节省内存空间，不需要创建完整的list...
  - 当我们不需要完整的List，而只是关心list中部分元素
  
- **创建方式**
  
  - `(i+1 for i in range(10))`    将列表生成式的`[]`改为`()`
  
  - 函数式生成器
  
    - ```python
      def fib(max):
          a,b = 0,1
          n = 0
          while n < max:
              n = a+b
              a = b
              b = n
          	yield n
      
      g = fib(20) # 此时g就是generator对象
      next(g) # 程序停止到yield,下一次next 从yield下一行开始，到yield结束
      ```
  
- **使用**
  
  - `next(generator)`   每次next生成一个值
  - `for i in genarator:`    用于循环

# 迭代器

- **可迭代对象（Iterable)**
  - 可以利用`for`循环的对象，实际上在for循环时，隐式调用了`__iter__`方法，返回一个迭代器
  
    - ```python
      a = [1,2,3]
      for i in a:  ===> for i in iter(a)
      ```
  
    - 通过for循环对一个可迭代对象进行迭代时，for循环内部机制会自动通过调用iter()方法执行可迭代对象内部定义的__iter__()方法来获取一个迭代器，然后一次又一次的迭代过程中通过调用next()方法执行迭代器内部定义的__next__()方法获取下一个元素，在抛出StopIteration之前停止循环
  
  - 提供了`__iter__` 方法或者`__getitem__`方法的对象都是可迭代对象
  
    - `__iter__`返回一个实现了`__next__`方法的对象，可以是本身
  
    - ```python
      class A(object):
          def __init__(self,num):
              self.num = num
              self.start_num = -1
      
          def __iter__(self):
              return self
      
          def __next__(self):
              self.start_num += 1
              if self.start_num > self.num:
                  raise StopIteration
              return  self.start_num
      
      a = A(10)
      b = iter(a)
      next(b)
      # 实际上，直接iter(a)也可以
      ```
  
      
  
- **迭代器（Iterator)**
  - 可以调用next方法
  - Iterator都是Iterbale
  - 实现了`__iter__`和`__next__`都是迭代器
  
- `iter(Iterable)`   将Iterable转换为Iterator

  - 实际上调用了`__iter__`方法