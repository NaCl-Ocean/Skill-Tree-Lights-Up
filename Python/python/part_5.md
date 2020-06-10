# 面向对象前引

- 编程范式
  - 面向过程编程  top-down lanuages
  - 面向对象编程  程序的维护和扩展更为简单

# 面向对象的核心特性

- 类（class)
  - 对一类拥有相同属性的对象的抽象、蓝图、原型。
  - 在类中定义了这些对象的都具备的属性、共同的方法
- 对象(object)
  - 一个类的实例化后的实例，每个对象有不同的属性
- 继承（Inheritance）
  - 一个类可以派生出子类，子类继承父类的属性和方法
- 封装（Encapsulation)
- 多态（Polymorphism）



# 属性

- 类属性，公共属性

  - 所有的实例（变量）共享该属性，也就是所有实例该属性的值都相同
  - 引用：可以通过类来引用，也可以通过实例来引用
  - 当通过实例引用来修改类属性时，不会改变类属性，此时相当于为实例创建了一个和类属性同名的实例属性
  - 当通过类引用来修改类属性时，创建的实例的类属性都会发生改变

- 实例属性

  - 通过构造函数来初始化
  - **实例化时，自动执行构造方法**`__init__`
  - 引用：只能通过实例来引用

- **self  是什么**

  - `self`   代表实例本身，也就是对象

- 属性实质上还是变量，既然是变量，那么也可以是对象变量

- ```python 
  class Test:
      d_type = 'test'  # 类属性
      
      def __init__(self,age):
          self.age = age  # 私有属性
          print(d_type)
  
  test1 = Test(16)   >>> 'test'
  # 引用类属性
  test1.d_type    >>> 'test'
  Test.d_type = 'modify'    
  test1.d_type    >>>'modify'
  # 引用实例属性
  test1.age       >>> 16
  Test.age        >>>error
  ```

- 属性分类

  - 静态属性
    - 除了函数变量以外可以看作静态属性
  - 动态属性
    - 方法（函数变量）可以看作实例的动态属性
    - 通过调用函数`obj.func()` 可以看出，func是一个函数变量，同时也是obj的属性

# 对象之间的交互

- **依赖关系**：单向关系

  - ```python
    class Dog:
        def __init__(self,name,age,d_type,master):
            self.name = name
            self.age = age
            self.d_type = d_type
            self.master = master  # 实例属性为对象
            self.bite()
        def bite(self):
            print('{} bites its master {}'.format(self.name,self.master.name))
    
    class Person:
        def __init__(self,name,age):
            self.name = name
            self.age = age
    
    mike = Person('mike',20)
    dog = Dog('dingding',2,'二哈',mike) # 传入了一个对象mike
    >>>dingding bites its master mike
    ```

- **关联关系**：双向关系

  - 单独构造一个对象属性来存储关系

  - ```python
    class Relation:
        def __init__(self):
            self.couple = list()
        def make_relation(self,obj1,obj2):
            self.couple.extend([obj1,obj2])
            print('{} and {} make relation'.format(self.couple[0].name,self.couple[1].name))
    
        def get_coule(self,obj_target):
            for obj in self.couple:
                if obj == obj_target:
                    pass
                else:
                    return obj.name
    class Person:
        def __init__(self,name,age,sex,relation):
            self.name = name
            self.age = age
            self.sex = sex
            self.relation = relation    
    
    relation = Relation()
    mike = Person('mike',20,'m',relation)
    jissca = Person('jissca',21,'f',relation)
    relation.make_relation(mike,jissca)
    print("mike's couple:{}".format(mike.relation.get_coule(mike)))
    >>>mike and jissca make relation
    mike's couple:jissca
    ```

- **组合关系**：由一堆组件构成一个完整的实体，组件本身独立，但不能自己运行，必须依赖于宿主发挥作用

  - 组件依赖于宿主，可以在宿主初始化时实例化一个组件

  - ```python
    class Brain:
        def __init__(self,IQ):
            self.IQ = IQ
    class Person:
        def __init__(self,name,age,sex,IQ):
            self.name = name
            self.age = age
            self.sex = sex
            self.Brain = Brain(IQ)  # 在宿主初始化时实例化组件
    
    mike = mike = Person('mike',20,'m',120)
    print(mike.Brain.IQ)
    >>>120
    ```



# 继承

- 节省代码

- 先抽象再继承      **共同点是什么，不同点是什么**

- 继承什么

  - 类属性
  - 类方法

- 重构父类的方法

  - 完全重构

  - 补充：既执行父类的方法，又执行子类新添加的方法

  - ```python
    class Person:
        def __init__(self,name,age,sex,IQ):
            self.name = name
            self.age = age
            self.sex = sex
            self.Brain = Brain(IQ)
    	def language(self):
            print('i speak English')
    class Chinese(Person):  # 表明继承了Person父类
        def __init__(self,name,age,sex,IQ,province):
            # 执行父类的方法，三种方式
            # 1. super().__init__(name,age,sex,IQ)  # 只支持单继承
            # 2. super(Chinese,self).__init__(name,age,sex,IQ)
            # 3. Person.__init__(self,name,age,sex,IQ)
            # 执行子类的方法
            self.province = province
            
        def language(self):
            # 完全重构
            print('我说汉语')
    ```

- 多继承

  - `class test(father1,father2)`   从左到右依次继承，先继承father1，fanter1没有的再继承father2
  - 查找属性或方法的顺序：
    - 深度优先    
    - 广度优先
    - py3.x 默认采用c3算法
    - `class.mro()`   查找顺序

# 封装

- 保护屏障，防止该类的代码和数据被外部类定义的代码访问
- 私有属性：在变量前加双下划线`__`，外部无法获取，
  - 类属性与实例属性都可以设置为私有属性
- 私有方法：在方法前加双下划线`__` ,  外部无法调用
- 如何强制查看私有属性或调用私有方法
  - `实例名.__类名+方法名`  强制调用私有方法
  - `实例名.__类名+属性名`  强制查看私有属性
- 私有属性必须是在定义类的时候进行定义
  - 当实例化的实例添加一个`__`开头的属性时，此时该属性不是私有属性

# 多态

- 同一个接口，使用不同的实例而执行不同操作



# 类方法

- `@classmethod`  装饰器

- 不能访问实例变量，只能访问类变量

- 为什么不能访问类变量

  - 此时传入的参数不是实例，而是类

- 类和实例都可以调用

- ```python
  @classmethod
  def test(cls):
      pass
  ```

  

# 静态方法

- `@staticmethod`   装饰器

- 不能访问类变量，也不能访问实例变量

- 类和实例都可以调用

- ```python
  @staticmethod
  def test():
      pass
  ```

# 属性方法

- `@property`    将一个方法转换为属性

- 可以访问实例变量和类变量

- 调用
  
  - `obj.func`   不用加括号`()`
  
- 既然是变量，能否修改其值

  - ```
    
    ```

    

# 反射

- 通过字符串的形式来操作对象的属性（增，删，改，查）

- 下面的obj可以是obj也可使class

- 查

  - `hasattr(obj,str)`    判断obj是否有str代表的属性

  - `getattr(obj,str)`     获取obj 中str代表的属性的value(包括静态属性和动态属性)，以字符串的形式返回属性的value

- 增

  - `obj.name = value`   直接增加

- 删

  - `delattr(obj,str)`  等同于 `del obj.name`  

- 改

  - `setattr(obj,name,value)`   给obj的'name'属性设置为value

    - 设置静态属性 

    - ```python
      setattr(test,'name','test2')
      print(test.name)
      >>>test2
      ```

    - 设置动态属性

    - ```python
      def new_func(self):
          print(self.name)
      
      setattr(test,'speak',new_func)
      test.speak(test)
      >>>test2
      ```



# 动态加载模块

- 一般我们导入模块需要在程序的开头都写好，但是也可能存在 动态加载模块的情况

- `__import__(str)`    导入str代表的模块

- 官方推荐

  - ```python
    import importlib
    importlib.import_module(str)
    ```

  

# 类的双下划线方法

- `__len__(self)`    定义了该方法后，可以调用`len(obj)`  ,返回必须是整数
  
  - 常见的是pytorch中dataset定义的`__len__`
  
- `__hash__(self)`  定义了该方法后，可以调用`hash(obj)`  ，返回必须为整数

- `__equal__(self,other)`  定义了该方法后，可以调用`obj_a == obj_b`，obj_b即为传入的参数other

- **item系列：将对象变成dict**
  - `__getitem__(self,item)`   定义了该方法后，可以通过`obj[item]` 调用该方法（pytorch中的dataset）
  - `__setitem__(self,key,value)`    定义了该方法后，可以通过`obj[key] = value`调用该方法
  - `__delitem__(self,key)`      调用`del obj[key]` 时，调用该方法
  - `__delattr__(self, key)`    调用`dek obj.key`时，调用该方法

- **str & repr**
  - `__str__`   当str函数调用`str(obj)`或者print函数调用时，调用`obj.__str__`
  - `__repr__`   当repr函数调用`repr(obj)`或者交互解释器中调用时，调用`obj.__repr__`
  - 上述两方法返回字符串
  
- **del**
  
  - `__del__` 当`del obj`调用时，执行该方法，一般没有明确调用`del obj`时，在程序末尾执行`del obj`
  
- **new**

  - `__new__`  在`__init__`之前执行，作用是创建实例

  - ```python
    class test(object):
        def __new__(cls,*args,**kwargs):
            return object.__new__(cls)
        def __init__(self,name):
            self.name = name
    ```

  - `__new__`必须有返回值，返回实例

    - 如果`__new__`创建的是当前类的实例，会自动调用`__init__`函数，通过return语句里面调用的`_object.__new__(cls)`函数的第一个参数是 cls 来保证是当前类实例，如果是其他类的类名，那么实际创建返回的就是其他类的实例，其实就不会调用当前类的`__init__`函数，也不会调用其他类的`__init__`函数。

  - **单例模式**

  - ```python
    class Printer(object):
        __instance = None
    
        def __new__(cls, *args, **kwargs):
            if cls.__instance == None:
                obj = object.__new__(cls)  # 只有当第一次实例化时，进行正常的实例化
                cls.__instance = obj
            return cls.__instance  # 之后的每次实例化，返回之前的实例化对象
        						   # 由于创建的是当前类的实例，因此接下来会调用__init__
    
        def __init__(self,name):
            self.name = name
            print('create:{}'.format(self.name))
         
    word = Printer('word')
    excel = Printer('excel')
    print('word:',word.name,'excel:',excel.name)
    print(id(word),id(excel))
    >>>create:word
    >>>create:excel
    >>>word: excel excel: excel
    >>>2946329312840 2946329312840   #可以看到上述两个实例实际上是同一个实例，并没有创建新的实例
    ```

- **call**

  - `__call__`
  - 通过`obj()`或者`cls()`调用
  
- **attr**

  - `__setattr__`  当调用`obj.xx= xxxx`时，调用该方法，也就是给属性赋值时

  - `__getattribute__(self,item)`  当调用`obj.xxx` 时，调用该方法，也就是获取属性的值时

  - `__getattr__(self,item)`  

    - 若没有重写`__getattribute__`时，先去查询对象是否有此属性，若有，则不调用该方法，若没有，则调用该方法
- 当重写了`__getattribute__`时，不调用该方法
  
- **运算符相关**

  - [魔法方法大汇总](https://www.cnblogs.com/zhouyixian/p/11129347.html#_label6)



# 动态创建一个类

- `type(object_or_name, bases, dict)`   动态创建一个类

  - object_or_name 为类的名称
  - bases 为继承的类
  - dict 属性，包括动态属性以及静态属性

- ```python
  def __init__(self,name,age):
      self.name = name
      self.age = age
      print('create test obj')
  
  test_cls = type('test',(object,),{'d_type':'test','__init__':__init__})
  test_obj = test_cls('test_obj',1)
  >>>create test obj
  ```





