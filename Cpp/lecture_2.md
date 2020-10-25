# 封装

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

    - 私有权限不可以被子类继承，保护权限可以被子类继承

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

- **将属性设置为私有权限**

  - **一般而言，常用的设计思路是，将属性设置为私有`private`，而提供一系列公共`public`接口`get` `set`去读写属性**

  - 好处：

    - 可以控制读写权限
    - 可以检查数据有效性

    

# 对象的初始化和清理

- **构造函数**

  - 相当于python 的`__init__`
  - 没有返回值，不写void
  - 函数名与类名相同
  - **构造函数可以有参数，可以发生重载**
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

## 构造函数的分类

- **按照参数类型**

  - 有参构造
  - 无参构造：默认构造函数

- **按照构造类型分类**

  - 拷贝构造

    - 常量引用传递：通过另一个对象初始化，往往需要和构造函数重载结合

      - ```C++
        class Person{
        public:
          // t
            Person(const Person &p){
                Person.age = p.age;
                ...
            }
          	Person(int age){
            	Person.age = age
            }
        }
        
        int main(){
          Person p1 = Person(12);
          Person p2 = Person(p1);
        }
        ```
  
  - 普通构造

## 调用构造函数

- 括号法
  - `Person p`  无参构造
  - `Person p(arg)`  有参构造
- **显式法---》prefer**
  - `Person p = Person(arg)` 有参构造
    - `Person (arg)` 匿名对象
    - 不能利用拷贝构造函数初始化匿名对象    `Person (obj)` 等价于  `Person obj`
  - `Person p `  无参构造
- 隐式转换法
  - `Person p = {args}`  等价于 `Person p = Person(arg)`

## 拷贝构造函数调用时机

- 使用一个已经创建的对象来初始化一个新的对象

- 值传递的方式给函数参数传值

- 值方式返回局部对象

  - **编译器不同，可能不会 调用拷贝构造函数**
  - 不调用拷贝构造函数会返回一个匿名对象

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
  ----exit function----      ---》vscode没有调用拷贝构造函数，而是直接将object返回
  50
  ```
  
  

## 构造函数调用规则

- **默认情况下，C++编译器至少给一个类添加4个函数**
  - 默认构造函数（无参，函数体为空）
  - 默认析构函数（无参，函数体为空）
  - 默认拷贝构造函数，对属性值进行拷贝
  - 赋值运算符，`operator=` 对属性进行值拷贝
- **调用规则：**
  - 如果用户定义了有参构造函数，c++不再提供默认无参构造，但是会提供默认拷贝构造
  - 如果用户定义拷贝构造函数，c++不再提供其他构造函数

## 对象作为函数参数

- **可以值传递**
  - **值传递的情况下，会调用类的拷贝构造函数，通过实参，实例化一个新的对象，该对象作为形参**
- **也可以地址传递（引用传递）**

## 深拷贝 与 浅拷贝

- **c++ 提供的默认构造函数是浅拷贝，**也就是仅做一个简单的赋值操作，进行成员变量的拷贝

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

    

## 初始化列表

- 用于初始化多个属性

-  `构造函数():属性1(值1),属性2(值2)... {}`

- ```C++
  class Person{
  public:  
      int name,age,car;
      Person(int a,int b,int c):name(a),age(b),car(c){};
     //上述代码等价于
      Person(int a,int b,int c){
          name = a;
          age = b;
          car = c;
      }
  };
  
  int main(){
    Person p = Person(10,20,30);
      return 0;
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



# C++ 对象模型

## 静态成员

- **静态属性**

  - **所有对象都共享同一份数据**

  - **类内声明，类外初始化**

  - 编译阶段分配内存

  - **可以通过对象进行访问，可以通过类名进行访问**

    - 通过对象访问：`obj.属性名`
    - 通过类名访问：`cls::属性名`

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

- 静态方法与静态属性同样可以设置访问权限



## 属性和方法存储

- 属性和方法 分开存储

- 每个空对象占1个字节

- [更详细的解释](https://www.cnblogs.com/HPAHPA/p/8339931.html)

- ```C++
  class man{
  public:
      int name;
      static int sex;   --》静态成员变量不在对象开辟的空间中存储
  	void func(){      --》方法不在对象开辟的空间中存储
          
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

  

## this 指针

- this 指针本质上是**一个指针常量**

- **this 指针指向被调用的方法所属的对象**

- **通过this 指针访问对象的属性**

  - `this ->属性名`

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

    

## const 修饰

- **常函数**
  - 方法后加const称为常函数
  
  - 被调用方法所属的对象不可以进行修改属性
  
  - 本质上是让this 指针 成为**指针常量+常量指针**
    
    - 也就是使得所属的对象的属性无法修改
    
    
  
- **常对象**
  - 在对象前加const关键字修饰，成为常对象
  - **常对象只能调用常函数**
  - 常对象的 属性 无法修改
  
- 关键字`mutable`
  
  - 属性在声明时利用`mutable`修饰，则该属性可以在常函数中修改，常对象也可以进行修改
  
- ```c++
  class man{
  public:
      mutable int name; --> 利用mutable声明属性
      int sex;  
  		void func() const {      
          this->sex = 2; --> 报错，无法修改
      }
      void func2() const{
          this -> name = 3;--> 可以修改
      }
  };
  int man::sex = 1;
  int main(){
      man m = man();
      m.func2();
      cout << m.name<<endl;
  }
  ```

  

- **指针**

  - 指针常量 `int * const ref = &a`    指针的指向不可以修改，但是指针指向的值可以修改
  - 常量指针 `const int * ref = &a`    指针的指向可以修改，但是指针指向的值不可以修改，也就是不能通过指针来修改指向的值
  - 常指针常量 `const int * const ref = &a`   指针的指向不可以修改，指针指向的值也不可以修改

# 友元

- **让一个函数或者类，访问另一个类中的私有成员（属性或者方法）**

## 全局函数做友元

- **在类的定义中进行声明函数，并且加上`firend`关键字**



## 类做友元

- 在被访问类的定义中声明访问类，并且加上`firend`关键字

## 成员函数做友元

- 在被访问类的定义中声明访问成员函数，并且加入`firend`关键字
- **访问成员函数所在的类在被访问的类之前定义，访问成员函数需要在被访问类之后单独定义**
  - *why? I don't know*

```C++
class Visit_friend;
class Room;
class roommate;
/*成员函数做友元，访问成员函数所在的类在被访问的类之前定义*/
class roommate {
public:
	void visit(Room &room);
};
class Room {
	/*类做友元*/
	friend class Visit_friend;
	/*全局函数做友元*/
	friend void visit(Room &room);
	/*成员函数做友元*/
	friend void roommate::visit(Room &room);
public:
	string sittingroom;
	Room(string sittingroom_name, string bedroom_name) :sittingroom(sittingroom_name), bedroom(bedroom_name) {}
private:
	string bedroom;
};

/*成员函数做友元，访问成员函数需要在被访问类之后单独定义*/
void roommate::visit(Room &room) {
	cout << "i am visting " << room.sittingroom << endl;
	cout << "i am visting " << room.bedroom << endl;
}
class Visit_friend {
public:
	void vist(Room &firendroom) {
		cout << "i am visting " << firendroom.sittingroom << endl;
		cout << "i am visting " << firendroom.bedroom << endl;
	}
};

void visit(Room &room) {
	cout << "i am visting " << room.sittingroom << endl;
	cout << "i am visting " << room.bedroom << endl;
}

int main() {
	Room room = Room("sittingroom", "bedroom");
	Visit_friend visit_friend;
	cout << "---类做友元----" << endl;
	visit_friend.vist(room);
	cout << "---全局函数做友元----" << endl;
	visit(room);
	cout << "---成员做友元----" << endl;
	roommate roommate_1;
	roommate_1.visit(room);
}
```



# 运算符重载

- 对已有的运算符进行重新定义，赋予其另一种功能，以适应不同的数据类型
- **相当于python中的魔法方法**

## 加号重载

- `operator*`：具体函数定义形式根据数据类型不同而不同，可以返回也可以不返回
- 类方法重载
  - `obj_a + obj_b`  等价于调用`obj_a.operator+(obj_b)`

- 全局函数重载
  - `obj_a + obj_b` 等价于调用`operator(obj_1,obj_b)`
- **运算符重载同样可以发生函数重载**
- **对于built in的数据类型的表达式不可以进行运算符重载**



## 左移运算符重载

- 可以输出自定义数据类型

- **利用全局函数来重载**

- `operator<<(Class_a &class_a,Class_b &class_b)` 

  - 当调用`class _a<<class_b` 时，相当于调用上述函数

- `cout` 是`ostream`对象

- 相当于python中的`__str__`

- ```C++
  void operator<<(ostream &cout,Person &p){
      cout<<p.name<<endl;
  }
  
  int main(){
      Person p;
      cout<<p;   --》等价于 operator<<(cout,p)
  }
  /* 当然也可以这样重载*/
  void operator<<(Person &p,ostream &cout){
      cout<<p.name<<endl;
  }
  /*调用的话这样调用, */
  p<<cout;
  ```



## 链式编程

- `cout << "test_1"<<"test_2"<<endl`

- 本质上链式操作的可行是因为调用 `cout<<"test_1"`  时（也就是重载的operator<<)时，又返回了一个`cout`对象，这样就可以重复下去

- **所以实现链式操作的核心是一定要返回对应的类型，不能返回void**

- ```C++
  ostream & operator<<(ostream &cout,Person &p){  --》当返回void时，无法链式编程
      cout<<p.name<<endl;
      return cout;
  }
  int main(){
      Person p;
      cout<<p<<endl;   
  }
  ```

  

## 递增运算符重载

- `operator++`

- 前置递增

  - `operator++()`

- 后置递增

  - `operator++(int)`   传入一个占位符

- ```C++
  class MyInteger {
  public:
  	int data = 0;
  	/*前置递增*/
  	MyInteger & operator++() {
  		data++;
  		return *this;
  	}
      /*后置递增*/
  	MyInteger& operator++(int) {
  		MyInteger temp = *this;
  		data++;
  		return temp;
  	}
  };
  
  int main() {
  	MyInteger integer;
  	++integer;
  	MyInteger temp = integer++;
  	cout << integer.data << endl;
  	cout << temp.data << endl;
  }
  输出：
  2
  1
  ```

- 递减运算符`operator--`同理

## 赋值运算符重载

- **c++默认提供的赋值运算符 是对属性值的拷贝**
- 主要用于深拷贝
- `operator=`

## 关系运算符重载

- `operator==`   == 运算符重载
- `operator!=`    != 运算符重载



## 函数调用运算符重载

- `()` 运算符重载，仿函数

- `operator()`

- **重载之后，通过`obj()` 调用，相当于python的`__call__`方法**

- 可以通过**匿名函数对象**直接调用  `class()()`调用

- ```c++
  void operator()(){
    code ....
  }
  ```

  

# 继承

- `class 子类: 继承方式 父类`

## 继承方式

-  **公共继承 public**
  - 父类中公共权限子类仍然是公共权限
  - 父类中保护权限子类仍然是保护权限
- **保护继承 protected**
  - 父类中公共权限与保护权限在子类中都变为保护权限
- **私有继承 private**
  - 父类中公共权限与保护权限在子类中都变为私有权限
- **父类私有权限 无论哪种继承方式都不可以访问，自然也就继承不了**



## 继承中的对象模型

- **父类中所有非静态成员属性都会被子类继承下去**
- **但是父类中私有属性会被编译器隐藏**
- 子类的成员会区分出哪个是继承下来的，哪个是自己又创建的





## 继承中构造和析构顺序

- 先构造父类，后构造子类，默认执行的是父类的无参构造函数
- 先析构子类，后析构父类
- [子类调用父类构造函数规则](https://www.cnblogs.com/fenghuan/p/4800199.html)

## 继承中同名成员

- **继承同名属性**
  
  - 子类访问子类属性 直接利用`.` 操作符即可
  - 子类访问父类属性：需要加作用域 `子类.父类::属性`
  
- **继承同名方法**
  
  - 子类调用子类方法 直接利用`.` 操作符即可
  - 子类调用父类方法：需要加作用域 `子类.父类::方法`
  
- 当子类通过`.` 调用方法时，所有父类同名方法被隐藏（所有重载的方法）

- ```c++
  class Base{
  public:
      int m_a = 0;
    	void test(){
          cout << Base::m_a << endl;
      }
  };
  
  class Son: public Base{
  public:
      int m_a = 1;
  
      void test(){
          cout << Base::m_a<<endl;  --> 通过类名::属性可以访问
          cout << Son::m_a << endl;
      }
  };
  
  
  int main(){
      Son s = Son();
      cout << s.m_a <<endl;  --> 子类访问子类属性
      cout << s.Base::m_a <<endl;  --> 子类访问父类属性
      s.test(); --> 子类访问子类方法
    	s.Base::test();  --> 子类访问父类方法
      return 0;
  }
  
  输出：
  1
  0
  0
  1
  0
  ```

  

## 继承中同名静态成员

```C++
class Base {
public:
	static int m_A;
};

int Base::m_A = 100;

class Son : public Base {
public:
	static int m_A;
};

int Son::m_A = 200;

//同名成员属性
void test01()
{
	//通过对象访问
	cout << "通过对象访问： " << endl;
	Son s;
	cout << "Son  下 m_A = " << s.m_A << endl;
	cout << "Base 下 m_A = " << s.Base::m_A << endl;

	//通过类名访问
	cout << "通过类名访问： " << endl;
	cout << "Son  下 m_A = " << Son::m_A << endl;
	cout << "Base 下 m_A = " << Son::Base::m_A << endl;
}

int main() {

	test01();
	system("pause");
	return 0;
}
```





## 多继承

`class 子类:继承方式 父类1 ,继承方式 父类2`

- 不建议使用多继承

## 菱形继承

- 两个派生类继承同一个基类，又有某个类同时继承者两个派生类

- 导致的问题是子类继承两份相同的数据，导致资源浪费以及毫无意义

- 利用虚继承可以解决菱形继承问题

- ```C++
  class Animal
  {
  public:
  	int m_Age;
  };
  
  //继承前加virtual关键字后，变为虚继承
  //此时公共的父类Animal称为虚基类
  class Sheep : virtual public Animal {};
  class Tuo   : virtual public Animal {};
  class SheepTuo : public Sheep, public Tuo {};
  
  void test01()
  {
  	SheepTuo st;
  	st.Sheep::m_Age = 100;
  	st.Tuo::m_Age = 200;
  	cout << "st.Sheep::m_Age = " << st.Sheep::m_Age << endl;
  	cout << "st.Tuo::m_Age = " <<  st.Tuo::m_Age << endl;
  	cout << "st.m_Age = " << st.m_Age << endl;
  }
  
  
  int main() {
  	test01();
  	system("pause");
  	return 0;
  }
  ```

  



# 多态

两类

- 静态多态：函数重载 运算符重载
- 动态多态：派生类 和 虚函数

**动态多态条件：**

- **有继承关系**
- **子类重写父类的虚函数**
  - **重写：函数返回值类型  函数名 参数列表 完全一致称为重写**

**动态多态使用条件**

- **父类指针或引用指向子类对象，之后该父类可以访问子类重写的虚函数**
- *需要区别于子类继承父类同名方法*

```C++
class father{
public:
    string name;
    void virtual test01(){
        cout << "father function"<<endl;
    }
};

class son:public father{

public:
    string n_class;
    void test01(){
        cout<<"son function"<<endl;
    }
};


int main(){
    son son_1;
    father & father_1 = son_1;
    father_1.test01();
}
输出:
son function
```



## 纯虚函数和抽象类

- **纯虚函数**

  - `virtual 返回类型 函数名(参数列表)=0`

- **抽象类**

  - **只要定义了纯虚函数，即为抽象类**
  - **无法实例化对象**
  - **抽象类的子类，必须要重写父类中的纯虚函数**

- 理解

  - 在实际工程实现中，往往会先抽象出一个基类，这个基类会定义一些子类会用到的通用函数
  - 但是不会在基类中实现这些函数，而是要在子类中根据每个子类的具体特点进行实现
  - 这样的好处是 抽象化，便于理解
  - 对于python 来说 ，往往在基类的这些函数中加一个`raise NotimplementError` 
  - 而在C++中，更为强大，通过虚函数，抽象类调用所有的这些子类接口

- ```C++
  // 计算器实现
  /* 抽象类 */
  class abstract_elevator{
  public:
      virtual int get_result(int ele_1,int ele_2)=0;
  };
  
  /* 子类实现具体的功能*/
  class addelevator:public abstract_elevator{
  public:
      /* 重写虚函数*/
      int get_result(int ele_1,int ele_2){
          return (ele_1+ele_2);
      }
  };
  /* 子类实现具体的功能*/
  class subelevator:public abstract_elevator{
  public:
      /* 重写虚函数*/
      int get_result(int ele_1,int ele_2){
          return (ele_1-ele_2);
      }
  };
  int main(){
      /* 通过一个 抽象类 来访问所有的子类接口 */
      abstract_elevator * base = new addelevator;
      cout <<base->get_result(10,20) <<endl;
      delete base;
      base = new subelevator;
      cout <<base->get_result(20,10) <<endl;
      delete base;
  }
  ```

  

## 虚析构 和 纯虚析构

- 父类指针指向子类，在析构的时候，不会调用子类中的 析构函数，导致如果子类在堆区开辟了数据，则不会释放

- 虚析构

  - 析构函数前用`virtual` 关键字修饰

- 纯虚析构

  - 类内声明：` virtual ~类名() = 0;`
  - 类外定义：`类名::~类名(){}`

- 虚析构和纯虚析构共性：

  * 可以解决父类指针释放子类对象
  * 都需要有具体的函数实现

- 虚析构和纯虚析构区别：
  * 如果是纯虚析构，该类属于抽象类，无法实例化对象

```C++
class Base{
public:
    virtual ~ Base(){
        cout << "virtual father func" << endl;
    }
};

class Son: public Base{
public:
    ~Son(){
        cout << "virtual son function" << endl;
    }
};

class Base2{
public:
    ~Base2(){
        cout << "father func" << endl;
    }
};
class Son2:public Base2{
public:
    ~Son2(){
        cout << "son function" << endl;
    }
};

int main(){
    Base *p = new Son();
    delete p;
    Base2 *p2 = new Son2();
    delete p2;
    return 0;
}

输出：
virtual son function
virtual father func
father func
```



# `::`

`::`的作用

- 作用域