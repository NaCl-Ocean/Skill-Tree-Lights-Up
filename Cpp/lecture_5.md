# STL

## STL的诞生

- 长久以来，软件界一直希望建立一种可重复利用的东西
- c++**面向对象和泛型编程**的思想，目的就是**复用性的提升**
- 大多数情况下，数据结构和算法都没有一套标准，导致被迫从事大量重复工作
- 为了建立数据结构和算法的一套标准，诞生了STL

## STL基本概念

- STL -> Standard Template LIbaray 标准模板库
- STL 从广义上分为
  - **容器 container**
  - **算法 algorithm**
  - **迭代器 iterator**

- 容器和算法之间通过迭代器进行无缝连接
- STL 几乎所有的代码都采用了**模板类或者模板函数**



## STL 六大组件

- **容器**：各种数据结构，如vector，list，deque，set，map等，用来存放数据
- **算法**：各种常用的算法，如sort，find，copy，for_each等
- **迭代器**：扮演了容器与算法之间的胶合剂
- **仿函数**：行为类似函数，可作为算法的某种策略
- **适配器/配接器**：一种用来修饰容器或者仿函数或迭代器接口的东西
- **空间配置器**：负责空间的配置与管理





## STL 容器，算法，迭代器

STL 容器将**运用最广泛的一些数据结构**实现出来

- 比如：数组(vector)，链表(linked list)，栈(stack)，队列，集合(set)，树，映射表(map)等等

容器一般分为两种

- **序列式容器**：强调值的排序，序列式容器的每个元素都有固定的位置，比如数组，
- **关联式容器**：二叉树结构，各元素之间没有严格的物理上的顺序关系



算法一般分为两种

- **质变算法**：运算过程中会更改容器中的元素的内容，比如拷贝，替换，删除等
- **非质变算法**：运算过程中不会更改容器中的元素的内容，比如查找，计数，遍历等等



迭代器：提供一种方法，使之能够依序寻访某个容器包含的各个元素，而又无需暴露该容器的内部表达式。

- **每个容器都有自己专属的迭代器**
- 迭代器使用非常类似指针

| 种类           | 支持运算                            | 功能                                                     |
| -------------- | ----------------------------------- | -------------------------------------------------------- |
| 输入迭代器     | 只读，支持++，==，!=                | 对数据的只读访问                                         |
| 输出迭代器     | 只写，支持++                        | 对数据的只写访问                                         |
| 前向迭代器     | 读写，支持++,==,!=                  | 读写操作，并能向前推进迭代器                             |
| 双向迭代器     | 读写，支持++,--                     | 读写操作，并能向前和向后操作                             |
| 随机访问迭代器 | 读写，支持++,--,[n],-n,+n,<,<=,>,>= | 读写操作，可以以跳跃的方式访问任意数据，功能最强的迭代器 |

- 常用的迭代器有双向迭代器和随机访问迭代器





## 容器算法迭代器初识

- **建立容器，遍历容器**

  - ```c++
    #include <vector>
    #include <algorithm>
    
    
    void print(int value){
        cout << value << endl;
    }
    int main(){
        // 建立容器
        vector<int> v;
        // push
        v.push_back(10);
        v.push_back(20);
        // 起始迭代器，指向容器中的第一个元素
        vector<int>::iterator itBegin = v.begin();
        // 结束迭代器，指向容器中最后一个元素的下一个位置
        vector<int>::iterator itEnd = v.end();
    
        // 遍历容器：方法一
        while(itBegin != itEnd){
            cout << *itBegin << endl;
            itBegin ++;
        }
        // 遍历容器：方法二
        for (vector<int>::iterator it = v.begin();it!=v.end();it++){
            cout << *it << endl;
        }
        // 遍历容器：方法三，遍历算法
        for_each(v.begin(),v.end(),print);
        return 0;
    }
    ```

    

- **建立自定义容器**

  - ```c++
    class Person{
    public:
        int age;
        string name;
        Person(string name,int age){
            this->age = age;
            this->name = name;
        }
    };
    
    
    int main(){
      
        vector<Person> v1;
        v1.push_back(Person("tom",3));
        v1.push_back(Person("jack",10));
        for (vector<Person>::iterator it=v1.begin();it!=v1.end();it++){
            cout << it->name << " " << it->age << endl;
        }
    
        vector<Person *> v2;
        Person p0 = Person("tom",3);
        Person p1 = Person("jack",10);
        v2.push_back(&p0);
        v2.push_back(&p1);
        for (vector<Person *>::iterator it=v2.begin();it!=v2.end();it++){
            cout << (*it)->name << " " << (*it)->age << endl;
        }
    
        return 0;
    }
    ```

- **容器嵌套容器**

  - ```c++
    int main(){
        vector<vector <int>> v;
        vector <int> v1;
        vector <int> v2;
        vector <int> v3;
        vector <int> v4;
        for (int i=0;i<5;i++){
            v1.push_back(i);
            v2.push_back(i+1);
            v3.push_back(i+2);
            v4.push_back(i+4);
        }
        v.push_back(v1);
        v.push_back(v2);
        v.push_back(v3);
        v.push_back(v4);
        for (vector<vector<int>>::iterator it = v.begin();it!=v.end();it++){
            for (vector <int> ::iterator it2=(*it).begin();it2!=(*it).end();it2++){
                cout <<(*it2)<< endl;
            }
        }
        
    
        return 0;
    }
    ```

    



# string 类

- `string` 是 c++风格的字符串，而`string`本质上是一个类
- `string ` 和` char* `的区别
  - `char *` 是一个指针，char * 就是单独定义一个字符串，比如`"hello"`
  - string 是一个类，类内部封装了char*，string类往往需要利用char *去构造
- string 类内部封装了很多成员方法，比如查找，拷贝，删除，插入等
  - string 负责管理char *所分配的内存，不用担心复制越界和取值越界等，由类内部进行负责

- `#include <string>`





## 构造函数

- `string() ` 创建一个空的字符串，例如：string str
- `string(const char* s) `  使用字符串s初始化
- `string(const string& str)`  拷贝构造
- `string(int n, char c)`    使用n个字符c初始化

```c++
 //string()
 string s1;
 // string(const char* s)
 string s2 = string("nihao");
 //string(const string& str)
 string s3 = string(s2);
 //string(int n, char c)
 string s4 = string(5, 'h');
```



## 赋值操作

- `string& operator=(const char* s)`  char* 类型的字符串赋值给当前的字符串
- `string& operator=(const string &s)`   把字符串s赋给当前的字符串
- `string& operator=(char c)`  字符赋给当前的字符串
- `string& assign(const char *s)` 把char* 类型的字符串s赋给当前的字符串
- `string& assign(const char *s,int n)` 把char* 类型的字符串s的前n个字符赋给当前的字符串
- `string& assign(const string &s)`    把字符串s赋给当前的字符串
- `string& assign(int n, char c)`  用n个字符c赋给当前字符串





## 字符串拼接

- `string& operator+=(const char* s)`
- `string& operator=(const string &s)`
- `string& operator=(char c)`
- `string& append(const char *s)`
- `string& append(const char *s, int n)` 把char* 类型的字符串s的前n个字符拼接到当前字符串之后
- `string& assign(const string &s)`
- `string& assign(const string &s, int pos, int n)` 从哪个位置开始截取，截取几个字符串



## string 查找和替换

- `int find(const string& str, int pos=0)`  查找str第一次出现位置，从pos开始查找，没有找到返回-1
- `int find(const char* s, int pos=0)`   查找s第一次出现的位置，从pos开始查找

- `int find(const char* s, int pos, int n)` 从pos位置查找s的前n个字符第一次出现的位置
- `int find(const char c, int pos=0)`查找字符c第一次出现的位置
- `int rfind(const string& str, int pos=0)`  查找str最后一次出现位置，从pos开始查找
- `int rfind(const char* s, int pos=0)`   查找s最后一次出现的位置，从pos开始查找
- `int rfind(const char* s, int pos, int n)` 从pos位置查找s的前n个字符最后一次出现的位置

- `int rfind(const char c, int pos=0)`查找字符c最后一次出现的位置
- `string& replace(int pos, int n, const string& str) ` 替换从pos开始n个字符为字符串str
- `string& replace(int pos, int n, const char* s)`替换从pos开始的n个字符为字符串s

## string 字符串比较

- 按照字符的ASCII码进行比较，主要用来判断字符串是否相等
- `int compare(const string &s)`  与字符串s比较，相等返回0
- `int compare(const char *s)`  与字符串s比较，相等返回0



## string 字符存取

- 通过[] 来访问或者修改单个字符
- 通过at 方式来访问或者修改单个字符

```c++
string s1 = "nihao";
// 通过[] 来访问单个字符
for (int i=0; i <5; i++){
  cout << s1[i] << endl;
}
//通过at 方式来访问单个字符
for (int i=0; i< 5; i++){
  cout <<s1.at(i) << endl;
}
// 通过[] 来修改单个字符
for (int i=0; i <5; i++){
  s1[i] = 'h';
}
cout << s1<< endl;
```



## 字符串插入和删除

- 插入字符串
  - `string& insert(int pos, const char* s)`  在pos处插入字符串s
  - `string& insert(int pos, const string& str)  `  在pos处插入字符串str
  - `string& insert(int pos, int n, char c) ` 在pos处插入n个字符c
- 删除字符串
  - `string& erase(int pos, int n=npos)   `  删除从pos开始的n个字符



## string 子串

- 从一个字符串中截取一部分作为另一个字符串
- `string substr(int pos=0, int n = npos)`   返回从pos开始的n个字符组成的字符串





# vector 容器

- vector与数组的区别
  - 普通数组是静态的，而vector可以**动态扩展**
- **动态扩展**：**并不是在原空间之后续接空间，而是找一个更大的空间，然后将原数据拷贝到新空间，释放原空间**
- vector 容器的迭代器是支持随机访问的迭代器
- `#include <vector>`
- ![vector](images/vector.png)

## 构造函数

- `vector<T> v`   默认构造，无参构造 

- `vector<T>(v.begin(),v.end()) `  将v[begin(),end()) 区间中的元素拷贝给本身，v.begin()和v.end()是迭代器

- `vector<T>(int n, T elem)`   构造函数将n个elem拷贝给本身

- `vector<T>(vector<T> & v)`   无参构造

- ```c++
  //vector<T> v
  vector<int> v1;
  for (int i =0; i< 10; i++){
  v1.push_back(i);
  }
  //vector<T>(v.begin(),v.end())
  vector v2 = vector<int>(v1.begin(),v1.end());
  //vector<T>(int n, T elem)
  vector v3 = vector<int>(10,5);
  //vector<T>(vector<T> & v)
  vector v4 = vector<int>(v3);
  ```

  

## 赋值操作

- `vector& operator=(const vector &vec)`

- `void assign(begin,end)`

- `void assign(n,elem)`

- ```c++
  vector<int> v1;
  for (int i =0; i< 10; i++){
    v1.push_back(i);
  }
  vector<int> v2;
  //vector& operator=(const vector &vec)
  v2 = v1;
  vector<int> v3;
  //void assign(begin,end)
  v3.assign(v1.begin(),v1.end());
  vector <int> v4;
  //void assign(n,elem)
  v4.assign(5,10);
  ```

  

## vector 容量和大小

- `empty()` 判断容器是否为空
- `capacity()`    容器的容量
- `size()`  返回容器中元素的个数
- `resize(int num)`重新制定容器的长度为num
  - 若容器变长，则以默认值填充新位置
  - 若容器变短，则末尾超出长度的元素被删除 
- `resize(int num, T elem)`重新指定容器的长度为num
  - 若容器变长，则以elem值填充新位置
  - 若容器变短，则末尾超出容器长度的元素被删除

```c++
vector<int> v1;
//empty()
cout << "v1 是否为空:" << v1.empty() << endl;
for (int i =0; i< 10; i++){
v1.push_back(i);
}
//capacity()
cout << "v1的容量：" << v1.capacity() <<endl;
//resize(int num)
v1.resize(5);
print(v1);
// resize(int num, T elem)
v1.resize(15,3);
print(v1);

输出:
v1 是否为空:1
v1的容量：16
0 1 2 3 4 
0 1 2 3 4 3 3 3 3 3 3 3 3 3 3 
```





## vector 插入和删除

- `push_back(T elem)`  尾部插入元素 elem
- `pop_back()`   删除最后一个元素
- `insert(const_iterator pos,  T elem)`  迭代器指向位置pos插入元素elem
  - `const_iterator`只读迭代器   定义只读迭代器 `vector<T>::const_iterator it`
  - 通常如果传入的参数时只读的vector(deque,...等等)，函数内部的迭代器需要是只读迭代器
- `insert(const_iterator pos,  int count, T elem)`  迭代器指向位置插入count个元素elem
- `erase(const_iterator pos) ` 删除迭代器指向的元素
- `erase(const_iterator start, const_iterator end) `  删除迭代器从start到end之间的元素，相当于`clear()`
- `clear()`   删除容器中所有的元素

```c++
vector<int> v1;
for (int i =0; i< 10; i++){
v1.push_back(i);
}
cout << "origin:"<<endl;
print(v1);
v1.pop_back();
cout << "after pop_back:" << endl;
print(v1);
vector<int>::iterator it = v1.begin();
for (int i=0;i<3;i++){
it++;
}
v1.insert(it, 11);
cout << "after insert:" << endl;
print(v1);
v1.erase(it);
cout << "after erase:" << endl;
print(v1);
cout << "after insert:" << endl;
v1.insert(it,3,12);
print(v1);
cout << "after erase:" << endl;
v1.erase(it,v1.end());
print(v1); 
```





## Vector 数据存取

- `at(int idx)` 返回索引为idx所指的数据
- `operator[]` 返回索引为idx所指的数据
- `front()`  返回容器中第一个数据元素
- `back() `  返回容器中最后一个数据元素

```c++
vector<int> v1;

for (int i =0; i< 10; i++){
v1.push_back(i);
}
for (int i=0;i<10;i++){
cout << v1[i] << " ";

}
cout << endl;
for (int i=0;i<10;i++){
cout << v1.at(i) << " ";
}
cout << endl;
cout << v1.front() << endl;
cout << v1.back() << endl;

输出：
0 1 2 3 4 5 6 7 8 9 
0 1 2 3 4 5 6 7 8 9 
0
9
```





## vector 互换容器

- `swap(vector &vec)`  实现两个容器的互换
- 实际用途
  - `vector<T>(v).swap(v)`可以收缩内存，创建了一个大的vector(eg:len = 100000) ，当resize到小长度时，其capacity不会变化，仍然很大

```c++
vector<int> v1;

for (int i =0; i< 10; i++){
v1.push_back(i);
}
vector<int>v2;
v2.swap(v1);
```



## vector 预留空间

- `reserve(int len) `容器预留len个元素长度，预留位置不初始化，不可访问，写入元素后可以访问



# deque 容器

![deque](images/deque.png)

- **双端数组**，可以对头端进行插入和删除
- 内部工作原理
  - 内部有一个中控器，维护每段缓冲区中的内容，缓冲区中存放真实数据
  - 中控器维护的是每个缓冲区的地址，使得使用deque时像一片连续的内存空间
  - 读取时相比于vector更慢
- deque 容器的迭代器是支持随机访问的迭代器
- `#include <deque>`



## deque 构造函数

- `deque<T> v`   默认构造，无参构造 

- `deque<T>(d.begin(),d.end()) `  将v[begin(),end()) 区间中的元素拷贝给本身，d.begin()和d.end()是迭代器
- `deque<T>(int n, T elem)`   构造函数将n个elem拷贝给本身
- `deque<T>(vector<T> & v)`   无参构造



## deque 赋值操作

- `vector& operator=(const deque &deq)`
- `void assign(begin,end)`
- `void assign(n,elem)`



## deque 大小操作

- `deque.empty()` 是否为空
- `deque.size() ` 容器中元素的个数
- `deque.resize(int num)`重新制定容器的长度为num
  - 若容器变长，则以默认值填充新位置
  - 若容器变短，则末尾超出长度的元素被删除 
- `deque.resize(int num, T elem)`重新指定容器的长度为num
  - 若容器变长，则以elem值填充新位置
  - 若容器变短，则末尾超出容器长度的元素被删除

- **没有容量的概念**



## deque 插入删除

- 两端操作
  - `deque.push_back(T elem) `   尾插
  - `deque.push_front(T elem) ` 头插
  - `deque.pop_back() ` 尾删
  - `deque.pop_front() ` 头删
- 指定位置操作
  - `deque.insert(const_iterator pos,  T elem)`  迭代器指向位置pos插入元素elem
    - `const_iterator`只读迭代器   定义只读迭代器 `vector<T>::const_iterator it`
    - 通常如果传入的参数时只读的vector(deque,...等等)，函数内部的迭代器需要是只读迭代器
  - `deque.insert(const_iterator pos,  int count, T elem)`  迭代器指向位置插入count个元素elem
  - `deque.insert(const_iterator pos, beg, end)`  在pos位置插入[beg,end)区间的数据
  - `deque.erase(const_iterator pos) ` 删除迭代器指向的元素
  - `deque.erase(const_iterator start, const_iterator end) `  删除迭代器从start到end之间的元素，相当于`clear()`
  - `deque.clear()`   删除容器中所有的元素

## deque 数据存取

- 同vector



# stack 容器

- **先进后出(First In Last Out;FILO) 数据结构**
- 栈不允许有遍历行为，只有栈顶元素可以被访问，也就没有迭代器
- ![](images/stack-3869496.png)

- `#include <stack>`

## stack 构造函数

- `stack<T>()` 无参构造函数
- `stack<T>(const stack & stk)` 拷贝构造

## stack 赋值操作

- `stack& operator=(const stack & stk)`  重载等号操作符

## stack 数据存取

- `push(T elem)` 入栈
- `void pop()`  出栈
- `top()` 查看栈顶元素



## stack 大小操作

- `int empty()` 栈是否为空，为空返回1
- `int size()` 栈的大小

```c++
stack<int> stk;
stk.push(10);
stk.push(20);
stk.push(40);
int size = stk.size();
for (int i=0;i<size;i++){
cout << "栈顶元素：" << stk.top() << endl;
stk.pop();
}
cout << "栈是否为空:" << stk.empty() << endl;
```



# queue 容器

- **先进先出(Firrst In First Out;FIFO) 数据结构**

- ![queue](images/queue.png)

- 队首只能出数据，队尾只能入数据

- 只有队尾和队首可以访问数据，同样没有迭代器
- `#include <queue>`



## queue 构造函数

- `queue<T>()` 默认构造函数
- `queue<T>(const queue &que)` 拷贝构造函数

## queue 赋值操作

- `queue& operator=(const queue & que)`  重载等号操作符

## queue 数据存取

- `void push(T elem)` 队尾添加元素
- `void pop()`  队首移除元素
- `T back()` 查看队尾元素
- `T front()` 查看队首元素

## queue 大小操作

- `int empty()` 栈是否为空
- `int size()` 栈的大小

```c++
queue<int> que;
que.push(10);
que.push(20);
que.push(30);
que.push(40);
int size = que.size();
for (int i=0;i<size;i++){
	cout << "队首元素：" << que.front() << " "<<"队尾元素："<< que.back()<< endl;
	que.pop();
}
cout << "队列是否为空:" << que.empty() << endl;

输出：
队首元素：10 队尾元素：40
队首元素：20 队尾元素：40
队首元素：30 队尾元素：40
队首元素：40 队尾元素：40
队列是否为空:1
```





# list 容器

- **双向链表** ，可以对任意位置进行快速插入或者删除元素
- **数据域 + 指针域**，双向链表的指针域包括前向指针和后向指针

- 缺点
  - 遍历数据的速度比数组慢
  - 占用空间比数组大
- 优点
  - 采用动态内存分配，不会造成内存溢出和浪费
  - 链表执行插入和删除方便，不需要移动大量元素
- **链表的迭代器是双向迭代器，**插入操作和删除操作不会造成list迭代器的失效，这在vector是不成立的
- ![list](images/list.png)

- `#include <list>`



## list 构造函数

- 类似于vector的构造函数
- `list<T> v`   默认构造，无参构造 
- `list<T>(l.begin(),l.end()) `  将v[begin(),end()) 区间中的元素拷贝给本身，l.begin()和l.end()是迭代器
- `list<T>(int n, T elem)`   构造函数将n个elem拷贝给本身
- `list<T>(const list<T> &l)`   拷贝构造

```c++
list<int> l1;
list l2 = list <int>(5,10);
list l3 = list<int>(l2.begin(),l2.end());
list l4 = list<int>(l3);
```





## list 赋值操作

- `list& operator=(const list &list)`
- `void assign(begin,end)`
- `void assign(n,elem)`



## list 交换

- `swap(list &l)`  实现两个容器的互换

## list 大小操作

- `empty()` 判断容器是否为空
- `size()`  返回容器中元素的个数
- `resize(int num)`重新制定容器的长度为num
  - 若容器变长，则以默认值填充新位置
  - 若容器变短，则末尾超出长度的元素被删除 
- `resize(int num, T elem)`重新指定容器的长度为num
  - 若容器变长，则以elem值填充新位置
  - 若容器变短，则末尾超出容器长度的元素被删除
- 没有capacity



## list 插入删除

- 两端插入和删除

  - `push_back(T elem)`
  - `pop_back()`
  - `push_front()`
  - `pop_front()`

- 中间插入

  - `insert(const_iterator pos,  T elem)`  迭代器指向位置pos插入元素elem
  - `insert(const_iterator pos, int n, T elem)`  迭代器指向位置pos插入n个元素elem

  - `insert(const_iterator pos, beg, end)`  在pos位置插入[beg,end)区间的数据

- 中间删除

  - `erase(const_iterator pos) ` 删除迭代器指向的元素
  - `deque.erase(const_iterator start, const_iterator end) `  删除迭代器从start到end之间的元素，相当于`clear()`
  - `clear()`  删除容器中的所有元素
  - `remove(T elem)` 删除容器中所有与elem值匹配的元素



## list 数据存取

- `front()` 
- `back()`
- 只能访问链表头和尾的元素

## list 排序和反转

- 所有不支持随机访问迭代器的容器，都不可以使用标准算法

- 不支持随机访问迭代器的容器，内部会提供一些标准算法

- `list.reverse()`链表反转

- `list.sort()`链表排序（升序）

  - 降序

    - sort + reverse

    - ```c++
      bool mycompare(T v1, T v2){
      	return v1>v2;
      }
      // 相当于自定义排序规则
      list.sort(mycompare)
      ```

      



# set/multiset 容器

- **所有元素都会在插入时自动排序**
- set/multiset 容器属于**关联式容器**，**底层结构用二叉树实现**
- set/multiset的区别
  - **set 不允许容器中有重复元素**
  - **multiset 容器中可以有重复元素**
- `#include <set>`



## set 构造方法

- `set<T>() ` 默认构造
- `set<T>(const set & s)`



## set 大小和交换

- `size()`
- `empty()`
- `swap(const set &s)`
- 不允许resize，没有capacity

## set 插入和删除

- `insert(T elem)` set容器中插入元素
  - set 容器会返回插入是否成功
  - multiset 不会返回是否插入成功

- `clear()` 清空容器
- `erase(pos)` 删除pos迭代器指向位置的元素
- `erase(beg,end)` 删除区间[beg,end)中的所有元素，等价于`clear`
- `erase(T elem)` 删除容器中为elem的元素

```c++
set<int> s1;
pair<set<int>::iterator, bool>ret = s1.insert(10);
cout << ret.second << endl;
ret = s1.insert(10);
cout << ret.second << endl;
```





## set 查找和统计

- `find(T key)` 查找key是否存在
  - 若存在，返回该键的元素的迭代器
  - 若不存在，返回`set.end()`
- `count(key)` 统计为key



## set容器排序

- set容器排序规则默认为从小到大

- set容器存放自定义对象

  - ```c++
    class Person{
    public:
        int age;
        string name;
        Person(string name,int age){
            this->age = age;
            this->name = name;
        }
    };
    class Person{
    public:
        int age;
        string name;
        Person(string name,int age){
            this->age = age;
            this->name = name;
        }
    };
    int main(){
        
        set<Person,MyCompare> v1;
        Person p1 = Person("tom",28);
        Person p2 = Person("jack",29);
        Person p3 = Person("jessei",30);
        v1.insert(p1);
        v1.insert(p2);
        v1.insert(p3);
        for (set<Person,MyCompare>::iterator it = v1.begin();it!=v1.end();it++){
            cout << it->name << " "<< it->age<< endl;
        }
        return 0;
    }
    输出:
    jessei 30
    jack 29
    tom 28
    ```

    

- set容器排序规则改为从大到小(仿函数)

  - ```c++
    class MyCompare{
    public:
        bool operator()(int v1,int v2){
            return v1>v2;
        }
    };
    
    int main(){
      set<int,MyCompare> v1;
      v1.insert(10);
      v1.insert(30);
      v1.insert(20);
      for (set<int,MyCompare>::iterator it = v1.begin();it!=v1.end();it++){
              cout << *it << endl;
          }
    }
    输出:
    30
    20
    10
    ```

    

# pair

- 成对出现的数据，利用对组可以返回两个数据
- pair中第一个元素为key，起到索引作用，第二个元素成为value

  

## pair 构造函数

- `pair<T1,T2> (T1 value1, T2 value2)`
- `make_pair(T1 value1, T2 value2)`

```c++
pair p = pair<string,int> ("tom", 20);
pair p2 = make_pair<string,int>("tom", 20);
```



## pair 数据存取

- `pair.first` 访问对组中的第一个元素
- `pair.second` 访问对组中的第二个元素





# map/multimap 容器

- map中所有元素都是pair
- 所有元素会根据键值自动排序

- 属于**关联式容器**，底层结构是**二叉树实现**
- 优点
  - **可以根据key快速找到value值**
  - `map[key]` 返回对应的value
    - 通过此方式取值，如果是自定义对象，需要提供无参构造函数
- Map/multimap 的区别
  - map 不允许容器中重复key值的元素
  - multimap 允许容器中有重复key值的元素
- 类似于python中的dict



## map 构造函数

- `map<T1,T1>()` 默认构造

- `map<T1,T1(const map &m)` 拷贝构造

- ```c++
  map<string,int> t1;
  t1.insert(pair<string,int>("tom", 30));
  map t2 = map<string,int>(t1);
  ```

  



## map 插入删除

- `insert(pair<T1,T1>(key,value))` 插入的元素需要为pair
- `clear()` 清空容器
- `erase( pos) `  删除pos迭代器指向的元素 
- `erase(beg,end) ` 删除容器中区间为[begin,end)的所有元素
- `erase(key)` 删除容器中值为key的元素

```c++
int main(){
    map<int,int> t1;
  	//inset method 1
    t1.insert(pair<int,int>(20, 30));
  	//inset method 2
    t1.insert(make_pair(30,40));
  	//inset method 3
    t1.insert(map<int,int>::value_type(40,30));
  	//inset method 4(不建议，最好用在访问元素时用这种写法)
    t1[50] = 50;
    print(t1);
    cout<<"删除key=20之后"<< endl;
    t1.erase(20);
    print(t1);
    cout << "删除第一个元素后" << endl;
    t1.erase(t1.begin());
    print(t1);
    cout << "删除所有元素后" << endl;
    t1.clear();
    print(t1);
  	return 0;
}
输出:
20 30 
30 40 
40 30 
50 50 
删除key=20之后
30 40 
40 30 
50 50 
删除第一个元素后
40 30 
50 50 
删除所有元素后
```



## map 大小和交换

- `size()`  容器的大小
- `empty() ` 判断容器是否为空
- `swap(const map &m)`  交换两个map



## map 查找统计

- `find(key)` 查找键为key的元素是否存在
  - 若存在，返回指向该键的元素的迭代器
    - 若为multimap，该迭代器通过++操作可以指向所有该键的元素
  - 若不存在，返回`map.end()`
- `count(key)`  统计键为key的元素的个数
  - 对于map而言，为1或者0
  - multimap 可能大于1

```c++
multimap<string,int> m;
m.insert(make_pair("tom",12));
m.insert(make_pair("jack",30));
m.insert(make_pair("tom",15));
multimap<string,int>::iterator it = m.find("tom");
while (it!=m.end()){
  cout << (*it).first << " " << (*it).second << endl;
  it++;
}

输出:
tom 12
tom 15
```



## map 排序

- 默认排序是从小到大

- ```c++
  class MyCompare
  {
  public:
      bool operator()(string s1, string s2) const
      {
          return s1 > s2;
      }
  };
  
  int main()
  {
    	// 更改排序为从大到小
      map<string, int, MyCompare> m;
   
   
      m.insert(make_pair("Tom", 18));
      m.insert(make_pair("Anthony", 23));
      m.insert(make_pair("Bob", 24));
      m.insert(make_pair("Sunny", 19))；
      
      return 0;
  }
  ```
```
  
  

# 案例

* 公司今天招聘了10个员工（ABCDEFGHIJ），10名员工进入公司之后，需要指派员工在那个部门工作
* 员工信息有: 姓名  工资组成；部门分为：策划、美术、研发
* 随机给10名员工分配部门和工资
* 通过multimap进行信息的插入  key(部门编号) value(员工)
* 分部门显示员工信息

​```c++
class Person{
public:
    string name;
    int sallary;
    string depart;
    Person(string name, int sallary,string depart){
        this->name = name;
        this->sallary = sallary;
        this->depart = depart;
    }
};


int main()
{
    vector<Person> persons;
    string name;
    int sallary,depart_num;
    map<int,string> depart_map;
    depart_map.insert(make_pair(0,"策划"));
    depart_map.insert(make_pair(1,"美术"));
    depart_map.insert(make_pair(2,"研发"));
    for (int i=0;i<10;i++){
        cout << "请输入姓名:"<< endl;
        cin>> name;
        cout << "请输入薪水:" << endl;
        cin>>sallary;
        depart_num = rand()%3;
        persons.push_back(Person(name,sallary,depart_map[depart_num]));
    }
    map<string,vector<Person>> depart;
    depart.insert(make_pair("策划",vector<Person>()));
    depart.insert(make_pair("美术",vector<Person>()));
    depart.insert(make_pair("研发",vector<Person>()));
    for(vector<Person>::iterator it=persons.begin();it!=persons.end();it++){
        depart[it->depart].push_back(*it);
    }
    for(map<string,vector<Person>>::iterator it=depart.begin();it!=depart.end();it++){
        cout<<(*it).first<< ": "<< endl;
        for(vector<Person>::iterator it2=(*it).second.begin();it2!=(*it).second.end();it2++){
            cout << it2->name << " "<< it2->sallary<< endl;
        }
    }
    return 0;
}
```

