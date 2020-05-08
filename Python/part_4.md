# 模块

- 一个.py文件就可以称之为一个模块

- 分类

  - 内置模块（标准库）  300个左右
  - 第三方模块   23万+
  - 自定义模块   自己写的.py文件

- 导入模块

  - `import module_a,module_b....`    导入多个模块，但是不建议一次性导入多个模块，最好每次仅导入一个模块
  - `from module import xxx,xxx`    从模块中导入某个部分
  - `from module.xxx.xxx  import xxx  as xxxx`        
  - 导入一个模块相当于执行了该.py文件

- **路径查找**

  - 导入某个模块需要查找到该模块所在的目录/路径
  - `sys.path`   路径查找列表，按照顺序依次在该列表列出的目录里查找某个模块
    - `site_packages` 第三方模块存放路径
    - 一般由当前目录`''`(空表示当前目录）和一些固定目录组成

- 如何下载第三方模块

  - 在[第三方模块仓库](https://pypi.python.org/pypi) 下下载某个模块，解压并进入目录，执行命令

    - ```python
      编译源码    python setup.py build
      安装源码    python setup.py install
      ```

  - `pip install package`  

    - `pip install  -i mirror_site package`   临时从镜像源下载

# os模块

- `os.getcwd()`  等同于linux下`cwd`
- `os.listdir()` 等同于linux下`ls`

------

- `os.path.isfile(path)`    检验该路径是否是文件
- `os.path.isdir(path)`      检验该路径是否是目录

- `os.path.exists(path)`   检验路径是否存在，也就是是否存在该文件或目录

- ------

  `os.path.spilt(path)`  将路径分割为dirname 和 basename  

- `os.path.dirname(path)`  返回dirname

- `os.path.basename(path)`  返回basename

------

- `__file__`   当前工作目录（相对目录）
- `os.path.abspath(path)`    通过相对路径返回绝对路径
- `os.system()`  执行shell命令

# sys模块

- `sys.platform`  返回操作系统的名称
- `sys.path`   返回文件搜索路径
- `sys.getrecursionlimit()`   获取最大递归层数

# time 模块

- python中表示时间的方式

  - 时间戳(timestamp)  表示的是从1970年1月1日00:00:00开始按秒计算的偏移量

  - 格式化时间字符串

    - ![](http://image.haiyang1218.cn/images/time_string.png)   

  - 元组（struct-time)

    - | Index |        Attribuate        |      Values      |
      | :---: | :----------------------: | :--------------: |
      |   0   |         tm_year          |                  |
      |   1   |          tm_mon          |       1-12       |
      |   2   |         tm_mday          |       1-31       |
      |   3   |         tm_hour          |       1-24       |
      |   4   |          tm_min          |       0-59       |
      |   5   |          tm_sec          |       0-61       |
      |   6   |         tm_wday          | 0-6（0表示周日） |
      |   7   |         tm_yday          |      1-366       |
      |   8   | tm_isdst（是否是夏令时） |     默认为-1     |

- `time.localtime([secs])`  将时间戳转换为当前时区的元组时间

- `timem.mktime(t)`  将元组时间转换为时间戳

- `time.strftime(format, t)`   将一个元组时间转换为格式化的时间字符串，t未指定为`time.localtime()`

- `time.strptime(string, format)`   将格式化时间字符串转换元组时间

- **元组时间是三种时间表示格式转换的中间站**

------

- `time.time()`  返回当前时间的时间戳
- `time.sleep(secs)` 程序停止secs秒钟



# datetime模块

几个常用的对象

- `datetime.date`   表示日期的类，常用的属性有`day`，`year`， `month`
- `datetime.datetime`：表示日期时间，常用的属性有`hour`，`second`，`minute`，`year`，`month`，`day`，`microsecond`
- `datetime.timedelta` ：表示时间间隔，可用于时间计算

------

`datetime.date`

- `datetime.date.today()`     返回一个`datetime.date`对象，用于表示当前时间
- `datetime.date.timetuple(obj)`  obj是`datetime.date` 对象，将`datetime.date`转换为元组时间
- `datetime.date.timetuple(timestamp)`   将时间戳转换为  ` datetime.date` 对象

------

`datetime.datetime`

- `datetime.datetime.now() `  返回一个`datetime.datetime` 对象，用于表示当前时间

------

`datetime`对象和`date`对象都有一个方法`replace`，可以修改属性`year` 等

- ```python
  >>> datetime.datetime.now().replace(year=2018)
  datetime.datetime(2018, 5, 7, 19, 50, 35, 245087)
  ```

------

`datetime.timedelta`

- `datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`     

- ```python
  >>> delta  = datetime.timedelta(days = 90)
  >>>datetime.datetime.now()
  datetime.datetime(2020, 5, 7, 19, 46, 56, 928211)
  >>> datetime.datetime.now()-delta
  datetime.datetime(2020, 2, 7, 19, 46, 24, 60378)
  ```

  

# random模块

- `random.randint(a,b)`  返回一个位于[a,b]区间的随机整数
- `random.randrange(start,stop,step=1)`  相当于利用range产生一个列表，在这个列表里随机选一个数
- `random.choice(iterable)`  从给定的序列中随机采样一个元素
- `random.sample(iterable,num)`  从给定的序列中随机采样num个元素  
- `random.shuffle(list)`  将列表随机打乱



# pickle模块

- 用于序列化操作，也就是将内存中的数据转为字符串存入内存中

- pickle模块可以序列化**任意对象**

- 序列化

  - `pickle.dumps(obj)`   将数据转换为特定的字符串，并编码为bytes
  - `pickle.dump(obj,file)`  将obj通过序列化后直接写入文件，注意：此时文件需要以二进制模式打开，因为写入的是bytes。

- 反序列化

  - `pickle.loads(bytes)`   将通过`dumps`的bytes反序列化
  - `pickle.load(file)`     从文件中加载经过`pickle.dump`的数据并进行反序列化
    - 先进先出，当同一个文件中先后存入了不同的数据，那么load时不会第一次就同时取出来，也是分次取出

  

# json模块

- 同样用于序列化

- 序列化

  - `pickle.dumps(obj)`   
  - `pickle.dump(obj,file)`  

- 反序列化

  - `pickle.loads(bytes)`   
  - `pickle.load(file)`    

  - 用法与pickle模块相同

- **无法序列化所有类型的对象**

- |   python    |  json  |
  | :---------: | :----: |
  |    dict     | object |
  | list, tuple | array  |
  |     str     | string |
  | int, float  | number |
  |    True     |  true  |
  |    False    | false  |
  |    None     |  null  |

  

- json文件解析

  - 对象(object)     以“{”（左括号）开始，“}”（右括号）结束。每个key后跟一个“:”；“‘名称/值’ 对”之间使用“,”（逗号）分隔。
  - 数组(array)  一个数组以“[”（左中括号）开始，“]”（右中括号）结束。值之间使用“,”（逗号）分隔。 
    - array中可以嵌套array，也可以嵌套object
  - 总的来说，概念与python中字典以及列表的概念相同

  

# Hashlib模块

  - `hash(obj)`   只能保证当前进程下同一对象hash出来的值相同，但是不同进程下hash出来的值一般不相同

  - **MD5算法**

    - 输入任意长度的信息，经过处理，输出128位的信息

    - 不同输入得到的输出不同

    - ```python
      import hashlib
      m = hashlib.md5()
      m.update(bytes)   # 传入经过编码后的bytes
      m.digest()  # 返回二进制的hash值
      m.hexdigest() # 返回十六进制的hash值
      
      
      m.update('test1')
      m.update('test2')
      '''
      上述两条命令等价于下面这一条命令，加盐操作
      '''
      m.update('test1test2')
      ```

      

  - **SHA-1算法**

    - 对于长度小于2^64位的消息，产生160位的消息

    - ```
      import hashlib
      m = hashlib.sha1()
      m.update(bytes)   # 传入经过编码后的bytes
      m.digest()  # 返回二进制的hash值
      m.hexdigest() # 返回十六进制的hash值
      ```

    - SHA-256：产生256位的消息

  

  # shutil模块

  - 用于文件操作，拷贝，删除，压缩，解压缩等

------

  - `shutil.copyfile(file_src,file_dst)`  创建dst，拷贝内容

  - `shutil.copymode(src, dst)`  仅拷贝权限，内容，组，用户不变，也就是dst文件已经存在，将dst文件的权限改为src文件的权限
  - `shutil.copystat(src, dst)`   仅拷贝状态的信息
  - `shulti.copy(src,dst)`  创建dst的同时，拷贝内容和权限  
  - `shutil.copy2(src, dst)`   拷贝内容和状态信息
  - `shulti.copytree(src, dst, symlinks=False, ignore=None)`   递归拷贝文件，相当于拷贝目录
    - `shutil.ignore_patterns(patterns)`     忽略一些文件，用在ignore参数
    - `shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))`    类似于于gitignore文件

------

  - `shutil.move(src, dst)`    移动文件
  - `shutil.rmtree(path)`   递归删除文件，相当于删除目录

------

  - `shutil.make_archive(base_name,format,...)`  创建压缩包并返回文件路径
      - `base_name`   压缩包的路径
      - `format`    zip,tar,gz等
      - `root_dir`    要压缩的文件夹路径（默认当前目录）
      - `owner`    用户，默认当前用户
      - `group`   组，默认当前组

- `shutil.unpack_archive(filename, extract_dir=None, format=None)`  解压缩
  - `filename`  压缩包
  - `extract_dir`    解压缩目的路径
  - `format`    zip,tar等，默认采用扩展名



# 正则表达式re模块

- 正则表达式是由普通字符（例如字符 a 到 z）以及特殊字符（称为"元字符"）组成的文字模式

- 匹配方法

  - `re.match` 从头开始匹配，类似于`str.startswith` 
  - `re.search` 匹配包含，也就是只要找到一个匹配的就返回并停止匹配
  - `re.findall` 把所有匹配到的字符以列表中的元素返回
  - `re.split` 以匹配到的字符当做列表分隔符
  - `re.sub` 匹配字符并替换
  - `re.fullmatch` 全部匹配

- 限定符：正则表达式的一个给定组件必须要出现多少次才能满足匹配

  - `*`  匹配`*`前的字符（规则）0次或多次
  - `+`  匹配`+`前的字符（规则）1次或多次
  - `?`  匹配`?` 前的字符（规则）0次或1次
  - `{m}`  匹配`{m}`前的字符（规则）m次
  - `{n,m}`   匹配`{n,m}` 前的字符（规则）n次到m次
  - `{n,}`  匹配`{n,}` 前的字符（规则）至少n次

- 定位符

  - `^`  匹配字符开头  
  - `$`  匹配字符结尾

- 元字符

  - `.`  匹配除`\n`之外的任意字符
  - `\w`  匹配字母或数字或下划线或汉字，相当于`[a-zA-Z0-9]`
  - `\d`  匹配数字，相当于`[0-9]`
  - `\s`  匹配任意空白符

- 转义符

  - `\`    

- 替换

  - `|`   匹配`|` 左或右的规则

- `[]`   匹配`[]`中的任意一个字符  `[a-z]` 表示任意一个小写字母，`[abc]`表示a或者b或者c

- `(pattern)`  分组匹配

- 优先级（从上到下递减）

  - |        运算符        |      描述      |
    | :------------------: | :------------: |
    |          \           |     转义符     |
    |        (),[]         | 圆括号和方括号 |
    | *,+,?,{m},{m,},{n,m} |     限定符     |
    |     ^,$,.,\w,...     | 定位符和元字符 |
    |          \|          |      替换      |



# 软件目录

```
Foo/
|-- bin/
|   |-- foo #可执行程序，启动foo调main.py
|
|-- foo/ #主程序目录
|   |-- tests/   #测试程序目录
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |
|   |-- __init__.py  #空文件，有这个文件就是包，没有就是目录
|   |-- main.py  #程序主入口
|
|-- docs/  
|   |-- abc.rst
|
|--conf/   
|
|--data/
|   
|-- setup.py  #安装部署脚本
|-- requirements.txt   #依赖关系，需要依赖的文件
|-- README
```

- `bin`下存放可执行的script，可以直接放在项目根目录下
- `docs`  下存放一些文档
- `conf` 存放配置文件
- `data`  需要用到的数据集
- `requirements.txt`   `pip install -r requirements.txt`   
  - `pip freeze > requirements`  将当前环境中的包及其版本号生成requirements.txt



# 包&跨模块代码调用

- 一个文件夹管理多个模块文件，则该文件夹可以称之为包

- 包下必须存在`__init__.py`

  - 当前包被调用时，先执行`__init__.py` 

- 跨目录调用

  - 由于`sys.path`一般只包含当前目录，所以跨目录调用需要更改环境变量

  - ```python
    my_proj
    ├── apeland_web
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── my_proj
        ├── settings.py
        ├── urls.py
        └── wsgi.py
        
    # 在views.py调用settings.py
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    ```

    

  - 官方推荐在项目根目录下放一个入口程序,类似于manage.py

    - 这样views.py调用settings.py就不需要再更改环境变量了  