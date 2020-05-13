# 前引

- argparse模块用于在终端运行python程序时，处理终端接收的参数
- 所有的方法都是围绕ArgumentParser 对象的
- 处理流程如下：
  - 创建解析器
  - 添加参数
  - 解析参数
- 通过终端运行命令`python xxx.py -h` 或者`python xxx.py --help`可以列出关于python程序的帮助信息
- 参数有两种
  - 位置参数
  - 选项参数：一般用前缀加以区分，缩写和全写
- 传参（命令行）
  - **位置参数在前，选项参数在后**
  - **选项参数必须加参数名，位置参数不加参数名**

# 创建解析器

- `parser = argparse.ArgumentParser(prog=None,usage=None,description=None,epilog=None, parents=[], prefix_chars='-',)`

- ```
  # 一个help信息示例
  usage:pratice_argparse [-h] [--foo FOO] f   《=== usage
        |-----  ===》prog            |- ===》metavr
  this is a script for parcitce   《=== description
  
  positional arguments:     ====》位置参数
    f                  test help 
  
  
  optional arguments:     ====》可选参数
    -h, --help  show this help message and exit
    --foo FOO   foo help     《=== help
  
  after args help    《==== epilog
  
  ```

  

- 从上面可以看到，不同的参数指定不同的分区内容
- `usage`不指定时，按照默认的格式，包括prog以及其他的参数名
- `prefix_chars`  指定区分位置参数和可选参数的前缀，默认为`-`
- `parents`  传入`ArgumentParserxiang`对象，此时可以使用相同的参数



# 定义参数

- `parser.add_argument(name or flags,action = None,default=None,type=None,help=None,metavar=None,dest=None)`
- 对于可选参数
  - `default` 设置当可选参数的值未指定时的值
  - 利用前缀加以区别，可以同时设置缩写和全写`parser.add_argument('-f,'--foo')`
- 位置参数的顺序
  - 位置参数传入需要顺序，如何去区分顺序
    - 按照定义参数的前后顺序
- `dest`   定义如何获取参数的值
  - 对于可选参数，默认为取最长的字符（全写），去掉`prefix_chars`指定的字符。



# 解析参数

- `args = parser.parse_args([args])`
  - `[args]`  字符串列表
- 最终返回一个namespace对象
- 通过`args.name`来获取参数的值
  - 通过上述的`dest`可以定义`name`
  - 其中值的类型通过`type`来指定

# 示例

```python 
import argparse
parser = argparse.ArgumentParser(prog='pratice_argparse',
                                description='this is a script for parcitce',
                                 epilog='after args help')
parser.add_argument('-f','--foo', help='foo help',metavar='foo',
                    type = int,default=10,dest='f_test')
parser.add_argument('pos_1',help='first pos arg',type = str)
parser.add_argument('pos_2',help='second pos arg')

 
args = parser.parse_args()
print('f:',args.f_test)
print('pos_1:',args.pos_1)
print('pos_1:',args.pos_2)
```

```shell
>>>python practice_argparse.py -h
usage: pratice_argparse [-h] [-f foo] pos_1 pos_2

this is a script for parcitce

positional arguments:
  pos_1              first pos arg
  pos_2              second pos arg

optional arguments:
  -h, --help         show this help message and exit
  -f foo, --foo foo  foo help

after args help

>>>python practice_argparse.py ni wo
f: 10
pos_1: ni
pos_1: wo

>>>python practice_argparse.py ni wo -f 12
f: 12
pos_1: ni
pos_1: wo
```


