# 内存分区模型

- 代码区：存放函数的二进制代码，编译后产生的二进制代码
  - 共享
  - 只读
- 全局区：存放全局变量和静态变量以及常量
  - 由操作系统负责全局区的分配释放
  - 静态变量：`static`修饰的变量
  - 常量分为
    - 字符串常量
    - const 修饰的全局变量
    - constt 修饰的局部变量 ---》**不存放于全局区**
- 栈区：由编译器自动分配释放
  - 局部变量以及形参
  - 当函数返回后，自动释放
- 堆区：由用户手动分配释放
  - 若一直不释放，则程序结束时由操作系统回收
  - 利用`new` 在堆区开辟空间
    - `int *p = new int(10)`  new关键字在堆区开辟空间，返回其在堆区的地址
    - `int *p_arr = new int[10]`  在堆区中开辟长度为10的数组空间，返回其首地址
  - 利用`delete`释放堆区中的空间
    - `delete p`   
    - `delete[] p_arr`   释放数组空间



# 引用

- 给变量起别名

- 与python中**“一切皆为对象，一切皆为对象的引用”**

- `数据类型 &别名 = 原名`

- **引用必须初始化**

- **引用一旦初始化，就不可以更改**

  - ```C++
    int a = 10;
    int &b = a;
    int c = 20;
    b = c; //赋值操作，而不是更改b的指向
    cout <<b<<endl;
    cout << c<<endl;
    cout << a<<endl;
    
    20
    20
    20
    ```

- **引用的本质**

  - **指针常量（指针的指向无法修改，指针指向的值可以修改）**

  - ```C++
    int &ref = a; --》int * const ref = &a
    ref = 10;     --》 *ref = 10
    ```

    

## 引用传递

- 通过引用参数产生的效果与地址传递是一样的，但是语法更加简洁

- ```C++
  void swap(int &a,int &b){
      int temp;
      a = temp;
      a = b;
      b = temp;
  }
  int main(){
      int a = 10;
      int b = 20;
      swap(a,b);
      cout << a <<endl;
      cout << b <<endl;
  }
  
  20
  10
  ```

  

## 引用做函数返回值

- 不要返回局部变量的引用

- ```C++
  int & swap(int a,int b){
      int temp;
      temp = a;
      a = b;
      b = temp;
      return temp; ----》错误，引用的本质是指针，当函数返回后，temp的空间被释放
  }
  
  int & swap(int a,int b){
      static int temp;
      temp = a;
      a = b;
      b = temp;
      return temp; -----》正确，静态变量存放于全局区，当函数返回后，temp的空间不会释放
  }
  ```

  

## 常量引用

- 如上篇文章所说，对于地址传递而言（引用传递也可以看作一种地址传递），传入的参数可以用const修饰，防止误操作，也就是防止函数内部修改实参

- ```c++
  //下述代码出错
  void swap(const int &a,const int &b){
      int temp;
      temp = a;
      a = b;
      b = temp;  
  }
  ```

-  对于const修饰的引用，可以直接传入数据

  - ```C++
    void swap(const int &a,const int &b){
        return a+b;
    }
    swap(10,20);
    ```

  - `const int &a = 10`  等价于 `int temp = 10, const int &a = temp`

  - `int &a = 10` 是错误的

  - `const int *a =10`也是错误的

# 函数提高

## 默认参数

- 定义的形参有两种
  - 默认参数
    - 默认参数在定义时写在非默认参数之后
  - 非默认参数
- 函数声明与函数实现 二者只能有一个定义默认参数

```c++
int func(int a=10,int b=20);
int func(int a,int b){
	return a+b;
}
int func2(int a,int b=10);
int func2(int a=10,int b);   ---》错误
```

## 占位参数

- 定义形参时，只定义数据类型

- 在调用函数的时候，需要传入其对应的实参

- ```C++
  void func(int a,int){
      cout<<"test"<<endl;
  }
  
  int main(){
      func(10,20);
      func(10);  ----》错误
  }
  ```

  

- 占位参数也可以有默认参数

## 函数重载

- 函数名相同，提高重用性

- 函数重载条件

  - 同一个作用域下
  - 函数名称相同
  - 函数**参数类型不同** 或者 **个数不同** 或者 **顺序不同**
  - 注意：返回参数的不可以作为重载的条件

- 注意事项

  - 引用作为重载条件

    - const修饰的引用 与 非const修饰的引用 可以作为重载条件

  - 函数重载遇到默认参数

    - 二义性

  - ```C++
    //函数重载注意事项
    //1、引用作为重载条件
    
    void func(int &a)
    {
    	cout << "func (int &a) 调用 " << endl;
    }
    
    void func(const int &a)
    {
    	cout << "func (const int &a) 调用 " << endl;
    }
    
    
    //2、函数重载碰到函数默认参数
    
    void func2(int a, int b = 10)
    {
    	cout << "func2(int a, int b = 10) 调用" << endl;
    }
    
    void func2(int a)
    {
    	cout << "func2(int a) 调用" << endl;
    }
    
    int main() {
    	int a = 10;
    	func(a); //调用无const
    	func(10);//调用有const
    	//func2(10); //碰到默认参数产生歧义，需要避免
    	system("pause");
    	return 0;
    }
    ```



# 类和对象

## 封装

- 定义类

  - ```C++
    class 类名
    {
    访问权限:
        定义属性 
        定义方法
    }
    int main(){
        类名 对象名;  --》实例化
    }
    ```

  - 通过`.` 操作符查看属性或者调用方法

- **访问权限**

  - **公共权限 public ：类内可以访问，类外可以访问**

  - **保护权限 protected：类内可以访问，类外不可以访问**

  - **私有权限 private：类内可以访问，类外不可以访问**

  - **当不标记权限时，默认为私有权限**

  - ```C++
    class Person
    {
    public:
        string name;
    private:
        string car;
    protected:
        string card;
    };
    
    int main(){
        Person p1;
        p1.name;
        p1.car;  --》私有权限，报错
        p1.card; --》保护权限，报错
    }
    ```

    

- **struct 和 class的区别**

  - **struct 中的所有成员都是公共权限，struct中也可以定义方法**

- 将属性设置为私有权限

  - **一般而言，常用的设计思路是，将属性设置为私有`private`，而提供一系列公共`public`接口`get` `set`去读写属性**

  - 好处：

    - 可以控制读写权限
    - 可以检查数据有效性

    

## 对象的初始化和清理

- **构造函数**

  - 相当于python 的`__init__`
  - 没有返回值，不写void
  - 函数名与类名相同
  - 构造函数可以有参数，可以发生重载
  - `类名(){}`

- **析构函数**

  - 将对象在堆区开辟的数据释放
  - 相当于python的`__del__`方法
  - `~类名(){}`
  - 不可以有参数，因此不可以发生重载
  - 在对象被销毁（手动 or 编译器自动）时，调用

- ```C++
  class Person{
  public:
      //构造函数
      Person(){
          ....
      }
      //析构函数
      ~Person(){
          .....
      }
  }
  ```

- 构造函数的分类

  - 按照参数类型

    - 有参构造
    - 无参构造：默认构造函数

  - 按照构造类型分类

    - 拷贝构造

      - 常量引用传递

      - ```C++
        class Person{
        public:
            Person(const Person &p){
                Person.age = p.age;
                ...
            }
        }
        ```

    - 普通构造

- 调用构造函数

  - 括号法
    - `Person p`  无参构造
    - `Person p(arg)`  有参构造
  - **显示法---》prefer**
    - `Person p = person(arg)` 有参构造
      - `person (arg)` 匿名对象
      - 不能利用拷贝构造函数初始化匿名对象 `Person (obj)` 等价于  `Person obj`
    - `person p `  无参构造
  - 隐式转换法
    - `Person p = arg`  等价于 `Person p = Person(arg)`

- 拷贝构造函数调用时机

  - 使用一个已经创建的对象来初始化一个新的对象

  - 值传递的方式给函数参数传值

  - 值方式返回局部对象--》**编译器不同，可能不会 调用拷贝构造函数**

  - ```C++
    class Cube
    {
    private:
    	int l;
    public:
    	void set_l(int l_input) {
    		l = l_input;
    	}
    	int get_l() {
    		return l;
    	}
    public:
    	Cube(const Cube &c) {
    		cout << "using reference construct" << endl;
    	}
    	Cube() {
    		cout << "using default construct" << endl;
    	}
    };
    
    
    Cube issame(Cube cube_1)
    {
    	cout << cube_1.get_l() << endl;
    	cube_1.set_l(20);
    	cout << cube_1.get_l() << endl;
    	Cube cube_2;
        cube_2.set_l(50);
    	return cube_2;
    }
    Cube test() {
    	Cube cube_3;
    	return cube_3;
    }
    int main() {
    	cout << "----init cube_1----" << endl;
    	Cube cube_1;
    	cout << "----using function----" << endl;
    	Cube cube_2 = issame(cube_1);
    	cout << "----exit function----" << endl;
    	cout << cube_2.get_l() << endl;
    }
    
    visual studio输出：
    ----init cube_1----
    using default construct
    ----using function----
    using reference construct
    -1965274831
    20
    using default construct
    using reference construct
    ----exit function----
    -858993460
    
    vscode输出：
    ----init cube_1----
    using default construct
    ----using function----
    using reference construct
    0
    20
    using default construct
    ----exit function----
    50
    ```

    

- **构造函数调用规则**
  - 默认情况下，C++编译器至少给一个类添加3个函数
    - 默认构造函数（无参，函数体为空）
    - 默认析构函数（无参，函数体为空）
    - 默认拷贝构造函数，对属性值进行拷贝
  - 调用规则：
    - 如果用户定义了有参构造函数，c++不再提供默认无参构造，但是会提供默认拷贝构造
    - 如果用户定义拷贝构造函数，c++不再提供其他构造函数
- **对象作为函数参数**
  - **可以值传递**
    - **值传递的情况下，会调用类的拷贝构造函数，通过实参，实例化一个新的对象，该对象作为形参**
  - **也可以地址传递（引用传递）**

- **深拷贝 与 浅拷贝**

  - **c++ 提供的默认构造函数是浅拷贝，**也就是仅做一个简单的赋值操作

    - 如果对象在堆区开辟了数据，浅拷贝会导致堆区数据释放的冲突

    - ```C++
      class Cube{
      private:
      	int * h;
      	int l;
      
      public:
      	Cube(int h_input, int l_input) {
      		h = new int(h_input);
      		l = l_input;
      	}
      	~Cube() {
      		if (h != NULL) {
      			delete h;
      			h = NULL;
      		}
      	}
      };
      
      
      void test() {
      	Cube cube_1 = Cube(10, 20);
      	Cube cube_2 = Cube(cube_1);  --》在函数返回时，会导致重复释放堆区中的内容，cube_1析构已经释放掉堆区中的内容，而cube_2 h仍然指向相同区域，释放时产生冲突
      }
      
      int main() {
      	test();
      }
      ```

      

  - 深拷贝

    - 在堆区重新申请一片区域

    - ```C++
      cube(const Cube &c){
          h = new int(*c.h);
          l = l_input;
      }
      ```

      

- 初始化列表
  -  