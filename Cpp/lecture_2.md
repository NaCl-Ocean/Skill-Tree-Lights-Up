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

### 构造函数的分类

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

### 调用构造函数

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

### 拷贝构造函数调用时机

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

  

### 构造函数调用规则

- 默认情况下，C++编译器至少给一个类添加3个函数
  - 默认构造函数（无参，函数体为空）
  - 默认析构函数（无参，函数体为空）
  - 默认拷贝构造函数，对属性值进行拷贝
- 调用规则：
  - 如果用户定义了有参构造函数，c++不再提供默认无参构造，但是会提供默认拷贝构造
  - 如果用户定义拷贝构造函数，c++不再提供其他构造函数

### 对象作为函数参数

- **可以值传递**
  - **值传递的情况下，会调用类的拷贝构造函数，通过实参，实例化一个新的对象，该对象作为形参**
- **也可以地址传递（引用传递）**

### 深拷贝 与 浅拷贝

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

    

### 初始化列表

- 用于初始化多个属性

-  `构造函数():属性1(值1),属性2(值2)... {}`

- ```C++
  class Person{
  public:  
      Person(int a,int b,int c):name(a),age(b),car(c){
          ....
      }
      //上述代码等价于
      Person(int a,int b,int c){
          name = a;
          age = b;
          car = c;
      }
  }
  ```

- **类对象作为类属性**

  - 构造时，先调用对象属性的构造方法，再调用本类的构造方法

  - 析构时，先调用本类的析构方法，再调用对象属性的析构方法

  - ```C++
    class Phone{
    public:
        string phone_name;
        Phone(string phone_name_input){
            phone_name = phone_name_input;
        }
    }
    class Person{
    public:
        Phone p_phone;
        string name;
        //p_phone(phone_name)  隐式转换法进行实例化
        Person(string name,string phone_name):name(name),p_phone(phone_name){
            ....
        }
    }
    ```

    

### 静态成员

- **静态属性**

  - **所有对象都共享同一份数据**

  - 类内声明，类外初始化

  - 编译阶段分配内存

  - 可以通过对象进行访问，可以通过类名进行访问

  - ```C++
    class man{
    public:
        int name;
        /*类内声明*/
        static int sex;
        /* 静态方法只能访问静态属性 */
        static void ser_sex(){
            sex = 0;
        }
    };
    /* 类外初始化 */
    int man::sex = 1;
    int main(){
        man jack = man();
        man mike = man();
        cout<<"before modify";
         /* 通过对象访问 */
        cout<<"\t"<<jack.sex;
        cout<<"\t"<<mike.sex;
        /* 通过类名访问 */
        cout<<"\t"<<  man::sex <<endl;
        mike.sex = 0;
        cout<<"after modify";
        cout<<"\t"<<jack.sex;
        cout<<"\t"<<mike.sex;
        cout<<"\t"<<man::sex<<endl;
    }
    输出：// 所有对象共享一份静态变量
    before modify   1       1       1
    after modify    0       0       0
    ```

    

- **静态方法**

  - **所有对象共享同一个静态方法**
  - **静态成员函数只能访问静态成员变量**

- 静态方法与静态属性同样有访问权限



### 属性和方法存储

- 属性和方法 分开存储
- 每个空对象占1个字节

- ```C++
  class man{
  public:
      int name;
      static int sex;   --》静态成员变量不在对象开辟的空间中存储
  	void func(){      --》非静态方法不在对象开辟的空间中存储
          
      }
  };
  int man::sex = 1;
  int main(){
      man jack = man();
      cout<<sizeof(jack)<<endl;
  }
  输出：
  4
  ```

  

### this 指针

- this 指针本质上是一个指针常量

- **this 指针指向被调用的方法所属的对象**

- 在类的非静态成员函数中返回对象本身，可使用`return *this`

- ```C++
  class Person
  {
  public:
  
  	Person(int age)
  	{
  		//1、当形参和成员变量同名时，可用this指针来区分
  		this->age = age;
  	}
  	
  	Person& PersonAddPerson(Person p)
  	{
  		this->age += p.age;
  		//返回对象本身
  		return *this;
  	}
  	void no_this(){
          cout<<"using no this"<<endl;
      }
  	int age;
  };
  ```

  

- 当空指针调用方法时，若用到了this指针，则会出错

  - ```C++
    Person * p =NULL;
    P.no_this();
    输出:
    using no this
    ```

    

### const 修饰

- **常函数**
  - 方法后加const称为常函数
  - 被调用方法所属的对象不可以进行修改
- 常对象