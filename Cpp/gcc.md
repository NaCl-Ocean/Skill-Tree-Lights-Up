# GCC 编译器 

- 使用 gcc 指令编译 C 代码
- 使用 g++ 指令编译 C++代码

## 编译过程

1. **预处理 Pre Processing**  **指示编译器仅对输入文件进行预处理**

   - 处理 `#include` 和` #define` ，把`#include`包含进来的`.h` 文件插入到`#include`所在的位置，把源程序中使用到的用`#define`定义的宏用实际的字符串代替
   - 生成的文件名为`test.i`

   ```bash
   # 产生的预处理后的cpp文件默认缺省扩展名为.i 
   g++ -E test.cpp -0 test.i 
   ```

2. **编译 Compling** **为C++代码产生汇编语言后停止编译**

   - 生成的文件名为`test.s`

   ```bash
   # g++产生的汇编语言文件的缺省扩展名是 .s
   g++ -S test.i -o test.s
   ```

3. **汇编 Assembling**  **告诉g++把汇编语言编译为机器语言的目标代码后停止编译**

   - 生成的文件名为`test.o`

   ```shell
   g++ -c test.s -o test.o
   ```

4. **链接 Linking  动态连接 静态连接**

   ```shell
   g++ test.o -o test
   ```

   

## g++ 重要编译参数

- `-g` 编译带调试信息的可执行文件

  - 告诉 GCC 产生能被GNU调试器 GDB 使用的调试信息，以调试程序

    ```bash
    # 产生带调试信息的可执行文件
    g++ -g test.cpp -o test
    ```

- `-O[n]` 优化源代码

  - **所谓优化**，例如省略掉代码中从未使用过的变量，直接将常量表达式用结果值代替等等，**这些操作会缩减目标文件包含的代码量，提高最终生成的可执行文件的运行效率**

  - -O 同时减小代码的长度和执行时间，等价于-O1

  - -O0 不做优化

  - -O1 默认优化

  - -O2 除了完成-O1的优化之外，还进行一些额外的调整工作，如指令调整等，一般使用-O2

  - -O3 包括循环展开和其他一些与处理特性相关的优化工作

    ```bash
    # 利用O2优化，产生优化后的可执行文件
    g++ test.cpp -o2 test
    ```

- `-l -L` 指定库文件 指定库文件路径

  - -l 指定程序要链接的库名，如果不利用-L指定库文件所在的目录名，那么库文件在默认搜索路径中，也就是这三个路径下：`/lib` ,`/usr/lib`，`/usr/local/lib` 。

  - -L 指定库文件所在的目录名 

    ```shell
    g++ -L/home/bing/Document/testlibfolder -lmytest test.cpp
    ```

- `-I` 指定头文件搜索路径

  - `/usr/include`是头文件的默认搜索路径

  - 如果使用的头文件不在`/usr/include`目录下，那么需要使用`-I` 参数去指定头文件的存放路径

    ```shell
    g++ -I/myinclude test.cpp
    ```

- `-Wall` 打印警告信息 `-w`关闭警告信息

- `-std=xxx` 指定编译标准

  ```shell
  # 指定使用c++11标准编译
  g++ -std=c++11 test.cpp
  ```

- `-o` 指定输出的可执行文件名

  - 不指定的话，默认输出名为`a.out`的可执行文件

- `-D` 使用gcc/g++ 编译的时候定义宏

  - 常用场景：`-DDEBUG`定义DEBUG宏，可能文件中有DEBUG宏部分的相关信息，用DEBUG来开启或者关闭DEBUG

  - ```c
    #include <stdio.h>
    int main(){
      #ifdef DEBUG
      	printf("DEBUG LOG\n");
     #endif
      	printf("in\n")
    }
    // 在编译的时候，使用g++ -DDEBUG main.cpp 那么就会输出 DEBUG LOG
    ```

    

- 使用`man gcc`来查看gcc英文手册



## 编译多个源文件

​	如果有多个源文件需要编译，比如`test.c`和`testfunc.c`，且这两个文件在一个文件夹下，那么有两种方法去编译

- 多个文件一起编译

  - 重新编译时需要所有文件重新编译

  ```shell
  gcc testfun.c test.c -o test
  # 作用：将testfun.c和test.c分别编译后链接成test可执行文件。
  ```

- 分别编译各个源文件，之后对编译后输出的目标文件链接

  - 重新编译时可以只重新编译修改的文件，未修改的文件不用重新编译

  ```shell
  # 编译testfunc.c,生成testfunc.o
  gcc -c testfun.c -o testfun.o
  # 编译test.c，生成testfunc.o
  gcc -c test.c -o testfunc.o
  # 将testfun.o和test.o链接成test
  gcc testfunc.o test.o -o test
  ```

如果大型项目，源文件不在同一个目录下，且有复杂的依赖关系，那么就需要makefile了。

## 练习

编译 GCC_LEARN下的工程

- 因为头文件`swap.h` 在`/include`目录下，所以需要指定头文件所在的目录

```shell
g++ main.cpp src/swap.cpp -Iinclude
```

生成静态库，并链接静态库编译

```shell
cd src
# 编译，生成静态库
# -c表示编译生成二进制代码 -I表示头文件在../include目录下，-o表示输出的文件为swap.o
g++ swap.cpp -c -I../include -o swap.o
# 创建静态库
ar rs libswap.a swap.o
# 使用静态库（在编译时链接静态库）
cd ..
# -l表示要链接的库名为swap -L表示库文件所在路径为src/，-I表示有头文件在include/目录下
g++ main.cpp -lswap -Lsrc -Iinclude -o static_main
```



生成动态库，编译，并链接动态库运行

```shell
# Linux Version 
cd src
# 编译，生成动态库
# -c表示编译生成二进制代码 -I表示头文件在../include目录下
# -fPIC表示产生的代码中，没有绝对地址，全部使用相对地址
g++ swap.cpp -c -I../include -fPIC swap.o
# 创建动态库
g++ -shared -o libswap.so swap.o

cd ..
# 编译main.cpp
g++ main.cpp -lswap -Lsrc -Iinclude -o dyna_main

# 运行main.cpp
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Users/haiyang/Documents/Skill-Tree-Lights-Up/Cpp/gcc_learn/src
./dyna_main
```

```shell
# Macos Version 
cd src
# 编译，生成动态库
# -c表示编译生成二进制代码 -I表示头文件在../include目录下
# -fPIC表示产生的代码中，没有绝对地址，全部使用相对地址
g++ swap.cpp -c -I../include -fPIC swap.o
# 创建动态库
gcc -dynamic -o libswap.dylib swap.o

cd ..
# 编译main.cpp
g++ main.cpp -lswap -Lsrc -Iinclude -o dyna_main

# 运行main.cpp
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/Users/haiyang/Documents/Skill-Tree-Lights-Up/Cpp/gcc_learn/src
./dyna_main
```

- macos和linux的差距主要在于 创建动态库，macos下动态库的扩展名为.dylib，另外，macos下搜索dylib动态库需要设置的环境变量是`DYLD_LIBRARY_PATH`



# GDB调试器

- GDB（GNU Deubgger）用来调试C/C++程序的功能强大的调试器，是Linux系统开发C/C++最常用的调试器
- VSCode本质上通过调用GDB调试器来实现C/C++的调试工作
- GDB调试器功能
  - 设置断点
  - 单步执行程序
  - ......
- Macos 下 为  lldb

## 常用调试命令参数

调试命令：**gdb [exefilename] ** exefilename也就是要调试的可执行文件名

下面是调试时一些常用的操作

```shell
## 以下命令后括号内为命令的简化使用，比如run（r），直接输入命令 r 就代表命令run
$(gdb)help(h)        # 查看命令帮助，具体命令查询在gdb中输入help + 命令 
 
$(gdb)run(r)         # 重新开始运行文件（run-text：加载文本文件，run-bin：加载二进制文件）
 
$(gdb)start          # 单步执行，运行程序，停在第一行执行语句

$(gdb)list(l)        # 查看原代码（list-n,从第n行开始查看代码。list+ 函数名：查看具体函数）

$(gdb)set            # 设置变量的值

$(gdb)next(n)        # 单步调试（逐过程，函数直接执行）

$(gdb)step(s)        # 单步调试（逐语句：跳入自定义函数内部执行）

$(gdb)backtrace(bt)  # 查看函数的调用的栈帧和层级关系

$(gdb)frame(f)       # 切换函数的栈帧

$(gdb)info(i)        # 查看函数内部局部变量的数值

$(gdb)finish         # 结束当前函数，返回到函数调用点

$(gdb)continue(c)    # 继续运行

$(gdb)print(p)       # 打印值及地址

$(gdb)quit(q)        # 退出gdb

$(gdb)break(b)+num                 # 在第num行设置断点

$(gdb)info breakpoints             # 查看当前设置的所有断点

$(gdb)delete breakpoints num(d)    # 删除第num个断点

$(gdb)display                      # 追踪查看具体变量值

$(gdb)undisplay                    # 取消追踪观察变量

$(gdb)watch                        # 被设置观察点的变量发生修改时，打印显示

$(gdb)i watch                      # 显示观察点

$(gdb)enable breakpoints           # 启用断点

$(gdb)disable breakpoints          # 禁用断点

$(gdb)x                            # 查看内存x/20xw 显示20个单元，16进制，4字节每单元

$(gdb)run argv[1] argv[2]          # 调试时命令行传参

$(gdb)set follow-fork-mode child   # Makefile项目管理：选择跟踪父子进程（fork()）

$(gdb)quit                         # 推出gdb

$(gdb)print(p)                     # print出变量的值
```





# makefile

- 通过`make`命令编译工程时，需要一个脚本，也就是`makefile`或者`Makefile`

## 语法特性

**最基础的语法：**

```makefile
target ... : prerequisites ...
    command
    ...
    ...
```

- **target** ：可以是一个object file（目标文件），也可以是一个执行文件，还可以是一个标签（label）
- **prerequisites**：生成该target所依赖的文件或target
- **command**：该target要执行的命令（任意的shell命令）
- *prerequisites中如果有一个以上的文件比target文件要新的话，command所定义的命令就会被执行。*

**定义变量：**

- 声明变量 `OBJS = main.o kdd.o`
- 使用变量 `$(OBJS)`



## makfile如何工作

```makefile
edit : main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o
    cc -o edit main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o

main.o : main.c defs.h
    cc -c main.c
kbd.o : kbd.c defs.h command.h
    cc -c kbd.c
command.o : command.c defs.h command.h
    cc -c command.c
display.o : display.c defs.h buffer.h
    cc -c display.c
insert.o : insert.c defs.h buffer.h
    cc -c insert.c
search.o : search.c defs.h buffer.h
    cc -c search.c
files.o : files.c defs.h buffer.h command.h
    cc -c files.c
utils.o : utils.c defs.h
    cc -c utils.c
clean :
    rm edit main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o
```

以这个例子为例

1. 一般地，当在terminal中输入`make`指令后，make会在当前目录下寻找文件名为`Makefile`或者`makefile`的文件，当两者同时存在时，会优先根据`makefile`这个文件进行编译
2. 如果找到，它会找文件中的第一个目标文件（target），并把这个文件作为最终的目标文件。在上例中，最总目标文件也就是`edit`
3. 如果该最终的目标文件不存在，或是该最终的目标文件所依赖的后面的 `.o` 文件的文件修改时间要比 该最终的目标文件新，那么，他就会执行后面所定义的命令来生成该最终的目标文件。在上例中，也就是如果`edit`文件不存在，或者`edit`文件的依赖时间戳比`edit`文件更新，那么就会执行后面定义的命令。
4. 如果 `edit` 所依赖的 `.o` 文件也不存在，那么make会在当前文件中找目标为 `.o` 文件的依赖性，如果找到则再根据那一个规则生成 `.o` 文件。（这有点像一个堆栈的过程）

- make会一层又一层地去找文件的依赖关系，直到最终编译出第一个目标文件。在找寻的过程中，如果出现错误，比如最后被依赖的文件找不到，那么make就会直接退出，并报错，而对于所定义的命令的错误，或是编译不成功，make根本不理。**make只管文件的依赖性**。

## 标签

- 像`clean`这种，没有被第一个目标文件直接或间接关联，那么它后面所定义的命令将不会被自动执行，不过，我们可以显示要make执行。即命令—— `make clean` ，以此来清除所有的目标文件，以便重编译。



# CMake

- CMake 是一个跨平台的安装编译工具，可以用简单的语句描述所有平台的安装（编译过程）
- 已经成为大部分C++开眼项目标配



## 语法特性

- 基本语法格式 ：` 指令(参数1 参数2 ...)`
  - **参数用括弧括起**
  - **参数之间用空格 或者 分号 分开**
- **指令是大小写无关的，参数和变量是大小写相关的**
- 变量使用`${}`方式取值， 但是在IF控制语句中直接使用变量名



## 重要指令

- `cmake_minimum_required` 指定CMake的最小版本要求

  - `cmake_minimum_required(VERSION versionNumber [FATAL_ERROR])`

    ```cmake
    cmake_minimum_reuired(VERSION 2.8.2)
    ```

- `project` 定义工程名称，指定工程支持的语言

  - `project(projectname [CXX] [C] [Java]])`

    ```cmake
    # 指定工程名为HELLOWORLD
    project(HELLOWORLD)
    ```

- `set` 显式定义变量

  - `set(VAR [VALUE])`

  ```cmake
  # 定义变量SRC 其值为hello.cpp hellofunc.cpp
  set(SRC hello.cpp hellofunc.cpp)
  ```

- `include_directories` 向工程添加多个特定的头文件搜索路径

  - 相当于指定gcc编译时的`-I`参数
  - `include_directories(dir1 dir2 ...)`

  ```cmake
  # 将./include和/usr/include/myincludefolder添加到头文件的搜索路径
  include_directories(./include /usr/include/myincludefolder)
  ```

- `link_directories` 向工程添加多个特定的库文件搜索路径

  - 相当于指定gcc编译时的`-L`参数
  - `link_directories(dir1 dir2 ...)`

  ```cmake
  # 将./lib和/usr/lib/mylibfoler添加到库文件搜索路径
  link_directories(./lib /usr/lib/mylibfoler)
  ```

- `add_library` 生成库文件

  - `add_library(libname [SHARED]  [STATIC] source1 source2)`
  - SHARED 代表生成动态库
  - STATIC 代表生成静态库

  ```cmake
  add_library(hello SHARED ${SRC})
  ```

- `add_compile_options` 添加编译参数

  - `add_compile_options(<option> <option>)`

  ```cmake
  # 添加编译参数 -std=c++11
  add_compile_options(-std=c++11)
  ```

- `add_executable`生成可执行文件

  - `add_executable(exename source1 source2 ...)`

  ```cmake
  # 编译main.cpp生成main可执行文件
  add_executable(main main.cpp)
  ```

- `target_link_libraries` 为target添加需要链接的共享库

  - 相当于g++的`-l`参数
  - `target_link_libraries(target libaray1 <debug|optimized> library2 ...)`

  ```cmake
  # 将hello动态库链接到可执行文件main
  target_link_libraries(mian hello)
  ```

- `add_subdirectory` 向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制存放的位置

  - `add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])`

  ```cmake
  # 添加src子目录，src中需要有一个cmakeLists.txt
  add_subdirectory(src)
  ```

- `aux_source_directory` 发现一个目录下所有的源代码文件并将列表存储在一个变量中，这个指令临时被用来自动构建源文件列表

# 参考资料

[makefile](https://seisman.github.io/how-to-write-makefile/introduction.html)

[macos下编译使用动态库](https://blog.csdn.net/mydo/article/details/8907498)

