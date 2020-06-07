# 注释

- `//` 单行注释
- `/* */` 多行注释

# 变量

- `数据类型 变量名 = 变量值`

# 常量

- `# define 常量名 常量值`  宏常量

- `const 数据类型 常量名 = 常量值`



# 数据类型

- `sizeof(数据类型/变量)`  获取数据类型 或者 变量占据的内存空间

## 整型

| **数据类型**        | **占用空间**                                    | 取值范围         |
| ------------------- | ----------------------------------------------- | ---------------- |
| short(短整型)       | 2字节                                           | (-2^15 ~ 2^15-1) |
| int(整型)           | 4字节                                           | (-2^31 ~ 2^31-1) |
| long(长整形)        | Windows为4字节，Linux为4字节(32位)，8字节(64位) | (-2^31 ~ 2^31-1) |
| long long(长长整形) | 8字节                                           | (-2^63 ~ 2^63-1) |

## 浮点型

| **数据类型** | **占用空间** | **有效数字范围**  |
| ------------ | ------------ | ----------------- |
| float        | 4字节        | 7位有效数字       |
| double       | 8字节        | 15～16位有效数字- |

- 科学计数法
  - `3e2=300`  

## 字符型

- 单个字符
- `char ch = 'a'`  **单引号表示单个字符**
  - ASCII编码
- 占用1个字节



### 转义字符

- 用来表示无法一些不能显示出来的特殊字符

| **转义字符** | **含义**                                | **ASCII**码值（十进制） |
| ------------ | --------------------------------------- | ----------------------- |
| \a           | 警报                                    | 007                     |
| \b           | 退格(BS) ，将当前位置移到前一列         | 008                     |
| \f           | 换页(FF)，将当前位置移到下页开头        | 012                     |
| **\n**       | **换行(LF) ，将当前位置移到下一行开头** | **010**                 |
| \r           | 回车(CR) ，将当前位置移到本行开头       | 013                     |
| **\t**       | **水平制表(HT)  （跳到下一个TAB位置）** | **009**                 |
| \v           | 垂直制表(VT)                            | 011                     |
| **\\\\**     | **代表一个反斜线字符"\"**               | **092**                 |
| \'           | 代表一个单引号（撇号）字符              | 039                     |
| \"           | 代表一个双引号字符                      | 034                     |
| \?           | 代表一个问号                            | 063                     |
| \0           | 数字0                                   | 000                     |
| \ddd         | 8进制转义字符，d范围0~7                 | 3位8进制                |
| \xhh         | 16进制转义字符，h范围0~9，a~f，A~F      | 3位16进制               |

```c++
cout <<"today\t\t"<<'2020-6-6';
>>>today		2020-6-6
```

## 字符串

- **c语言风格**
  - `char 变量名[] = "字符串"`   **双引号表示字符串**
- **c++语言风格**
  - `string 变量名 = "字符串"`
  - 包含头文件`#include <string>`



## 布尔类型

- 占据**一个字节**
- `true`  or `false`
- `bool 变量名 = true/false`
- `false`实际上是0，非0为True



## 数据输入

- `cin>>变量名`   输入赋值给变量

## 数据输出

- `cout <<str1 <<str2<<endl`
- endl：换行 end of the line

# 运算

## 算术运算

- `+` `-` `*` `/` `%` 
  - 整数进行算术运算结果仍然为整数
  - 浮点数进行算术运算结果仍然为浮点数
  - 取模和除法 除数不可以为0
  - 浮点数不可以做取模运算
- `++`  `--`
  - `b = a++` **后置递增** 将a+1前的值赋给b，同时a=a+1
  - `b = ++a`  **前置递增**，将a+1后的值赋给b ,同时a=a+1



## 赋值运算

- `=` `+=` `-=  `   `*=` `%=`

## 比较运算

- `==`  `!=`  `<` `>` `<=` `>=`

- 输出true or false

## 逻辑运算

- `!`  取反    `&&` 与    `||` 或

```c++
char a = 'a';
!a
>>>0
int a = 1
!a
>>>0
int a = 0
!a
>>>1
char a[] = "abc";
!a
>>>0
float a =0;
!a
>>>1
```



# 程序流程结构

## if

- 单行格式 if 语句 

  - `if (条件){code}`

- 多行格式 if 语句

  - ```c++
    if (条件){
        code
    }else{
        code
    }
    ```

    

- 多条件 if 语句

  - 执行到某个条件成立即退出

  - ```c++
    if (条件){
        code
    }else if(条件){
        code
    }else{
        code
    }
    ```

    

- 嵌套 if 语句

  - ```C++
    if (条件){
        code ...
        if (条件){
            code...
        }
    }else{
        code
    }
    ```

## 三目运算符

- `条件 ? 表达式1 : 表达式2`
- 条件为真，执行表达式1，并返回表达式1的结果
- 条件为否，执行表达式2，并返回表达式2的结果
- 与python中三目运算符相同 `表达式1 if 条件 else 表达式2`



## Switch

```C++
switch(整型/字符型)

{

	case 结果1：执行语句;break;

	case 结果2：执行语句;break;

	...

	default:执行语句;break;

}
```

- 若case后不接break，则会一直向下执行

## while

```C++
while (条件){
	code...
}
```

## do while

```c++
do {
    code ...
} while(条件)
```

- 先执行一次 do 后判断while的条件

## for 循环语句

```C++
for (起始表达式;条件表达;末尾循环体){
    code ...
}
```

## break

- switch语句中，终止case，跳出switch
- 循环语句中，跳出当前的循环语句



## continue

- 循环语句中，跳出**本次循环**
- `continue;`

# 数组

- **创建数组**

  - `数据类型 数组名[数组长度]`
  - `数据类型 数组名[数组长度] = {值1,值2,值3.....}`
  - `数据类型 数组名[ ] = {值1,值2,值3.....}`

- 数组名

  - 指向数组首地址

    - ```C++
      int a[5];
          cout << a <<endl;
          cout << &a[0] <<endl;
      0x61fe00
      0x61fe00
      ```

      

  - 获取数组的长度

    - ```C++
      sizeof(a)/sizeof(a[0])
      ```

      

# 二维数组

- **创建二维数组**
  - `数据类型 数组名 [行数][列数]`
  - `数据类型 数组名 [行数][列数] = {数据1,数据2,....},{数据3,数据4,....}`    每个`{}`代表一行 **---》 推荐**
  - `数据类型 数组名 [行数][列数] = {数据1,数据2,数据3,数据4,....}`  根据行数和列数，将数据分为行和列
  - `数据类型 数组名 [][列数] = {数据1,数据2,数据3,数据4,....}`

- 二维数组名

  - 查看二维数组占用内存空间
  - 查看二维数组首地址

- **每一行都是一个一维数组**

  - ```C++
    int a[5][5];
    cout << a <<endl;
    cout << a[0]<<endl;   --》取到第一行为一维数组
    
    0x61fda0
    0x61fda0
    ```

    



# 函数

- 函数的定义

  - 返回值类型

    - 返回为空：`Void`

  - 函数名

  - 参数表列

  - 函数体语句

  - return 表达式

    - 和返回值类型挂钩
    - 返回为空时，可以省略return

  - ```
    返回值类型 函数名(参数列表){
    	函数体语句
    	return 表达式
    }
    ```

    

## 值传递

- 所谓值传递，就是函数调用时实参将数值传入给形参
- 值传递时，形参的改变不会引起实参的改变



## 函数的声明

- `返回值类型 函数名(参数列表);`
-  告诉编译器函数名称及如何调用函数。函数的实际主体可以单独定义
  - 函数定义写在主程序之后，函数声明写在主程序之前
- 函数的**声明可以多次**，但是函数的**定义只能有一次**



## 函数的分文件编写

- **四个步骤**
  1. 创建后缀名为 .h 的头文件
  2. 创建后缀名为 .cpp 的源文件
  3. 在头文件中写函数的声明
  4. 在源文件中写函数的定义
     - 包含对应的头文件 `#include "xxx.h"`
- 调用 其他文件的函数
  - `#include "xxx.h"`
  - **双引号 代表自定义头文件**

- 示例

- ```C++
  //swap.h文件
  #include<iostream>
  using namespace std;
  
  //实现两个数字交换的函数声明
  void swap(int a, int b);
  ```

- ```C++
  //swap.cpp文件
  #include "swap.h"
  
  void swap(int a, int b)
  {
  	int temp = a;
  	a = b;
  	b = temp;
  
  	cout << "a = " << a << endl;
  	cout << "b = " << b << endl;
  }
  ```

- ```C++
  //main函数文件
  #include "swap.h"
  #include <iostrem>
  using namespace std;
  
  int main() {
  
  	int a = 100;
  	int b = 200;
  	swap(a, b);
  
  	system("pause");
  
  	return 0;
  }
  ```

  

# 指针
