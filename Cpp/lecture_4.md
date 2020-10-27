# 模板

- 模板不可以直接使用，只是一个框架
- c++的**泛型编程**思想，利用的技术就是模板
- c++提供两种模板
  - **函数模板**
  - **类模板**

## 函数模板

 函数模板的作用：

- 建立一个通用函数，其函数返回值类型和形参类型都可以不具体指定，用一个**虚拟的类型**来代表
- 类似于重载的加强版，提高代码的复用性



### 建立模板

```c++
template <typename T>
函数声明或定义
```

- `template`  声明创建模板
- `typename`  表明其后面的符号是一种数据类型，可以用`class` 来代替
- `T`  通用的数据类型，名称可以替换，通常为大写字母，一般为`T`



### 使用模板

- **自动类型推导：直接传入参数**
- **显式指定类型**

```c++
//不使用模板编程
void swapint(int &a, int &b){
    int temp = a;
    a = b;
    b= temp;
}
void swapdouble(double &a, double &b){
    double temp = a;
    a = b;
    b= temp;
}

int main(){
    int a = 10;
    int b = 20;
    swapint(a,b);
    cout << "a:" << a << " b:" << b << endl;
    double a_ = 10;
    double b_ = 20;
    swapdouble(a_,b_);
    cout << "a:" << a << " b:" << b << endl;
    return 0;
}

//使用模板编程
template <typename T>
void myswap(T &a, T &b){
    T temp;
    temp = a;
    a = b;
    b= temp;
}

int main(){

    int a = 10;
    int b = 20;
  	// 自动类型推导
    myswap(a, b);
  	// 显式指定类型
  	myswap<int>(a,b);
    cout << "a:" << a << " b:" << b << endl;
    return 0;
}
```



### 函数模板注意事项

- **自动类型推导，必须推导出一致的数据类型T，才可以使用**
- **模板必须要确定出T的数据类型，才可以使用**

```c++
template<typename T>
void myswap(T &a, T &b)
{
    T temp;
    temp = a;
    a = b;
    b= temp;
}
int main(){
    int a = 10;
    double b = 20;
    myswap(a, b); --> 出错，数据类型不一致
    cout << "a:" << a << " b:" << b << endl;
    return 0;
}
```

```c++
template<typename T>
void myfunc(){
    cout << "this is func" << endl;
}

int main(){
  	myfunc(); --> 出错，编译器无法确定T的数据类型
    myfunc<int>(); --> 正确，显式指定了数据类型
    cout << "a:" << a << " b:" << b << endl;
    return 0;
}
```



### 普通函数与函数模板的区别

- 普通函数调用可以发生隐式类型转换
- 函数模板，使用自动类型推导，不可以发生隐式类型转换
- 函数模板，使用显式类型指定，可以发生隐式类型转换



```c++
int myadd01(int a, int b){
    return a+b;
}
template <typename T>
T myadd02(T a, T b){
    return a+b;
}
int main(){
    int a =10;
    char c = 5;
    cout << myadd01(a, c) << endl; --> 普通函数调用，char变量被隐式转换为int
  	cout << myadd02(a, c) << endl; --> 自动类型推导，无法进行隐式转换，报错
    cout << myadd02<int>(a,c) << endl; --> 显式类型指定，可以发生隐式转换，正确
    return 0;
}
```



### 模板的局限性

- 上述模板只能针对built-in 的数据类型
- 针对特定的数据类型（class，list......）需要用具体化方式做特殊实现，进行重载

```c++
class Person{
public:
    int age;
    string name;
    Person(int age, string name){
        this -> age = age;
        this -> name = name;
    }
};

template <typename T>
bool myadd(T a, T b){
    cout << "function a" << endl;
    return true;
};

// 针对Person class 进行重载
template<> bool myadd(Person a, Person b)
{
    cout << "function b" << endl;
    return false;
}
int main(){
    int a =10; 
    char b = 5;
    Person c = Person(5, "tom");
    Person d = Person(5, "jack");
    myadd<int>(a,b);
    myadd(c,d);
    return 0;
}
输出：
function a
function b
```



## 类模板

类模板作用：

- 建立一个通用类，类中的成员，数据类型可以不具体指定，用一个**虚拟的类型**来代替



### 创建模板

```c++
template <typename T>
类
```

- `template`  声明创建模板
- `typename`  表明其后面的符号是一种数据类型，可以用`class` 来代替
- `T`  通用的数据类型，名称可以替换，通常为大写字母，一般为`T`

```C++
template <class NameType, class AgeType> --> 可以一次性定义多个虚拟类型
class Person{
public:
    NameType name;
    AgeType age;
    Person(NameType name, AgeType age){
        this -> age = age;
        this -> name = name;
    }
};

int main(){
    Person p = Person("jack", 2);
    cout << p.name <<" "<< p.age << endl;
    return 0;
}
```



### 类模板与函数模板的区别

- 有参构造可以使用自动推导，无参构造必须使用显式类型指定



### 类模板成员函数调用时机

- 类模板中的成员函数并不是一开始就创建好的，而是在调用时才去创建，因为无法确定数据类型

```c++
template <class NameType, class AgeType>
class Person{
public:
    NameType name;
    AgeType age;
    Person(NameType name, AgeType age){
        this -> age = age;
        this -> name = name;
    }
    void test(){
        age ++;
        name = name*2;
    }
};
int main(){
    Person p = Person("jack", 2);
    p.test();//注释掉，可以正常运行，不注释，编译失败，表明只有在调用的时候，才会去创建该成员方法，从而检查到string类型的变量无法++
    return 0;
}
```





### 类模板对象做函数参数

1. **指定传入的类型 --> 最常用**
2. 参数模板化
3. 整个类模板化



```c++
template <class NameType, class AgeType>
class Person{
public:
    NameType name;
    AgeType age;
    Person(NameType name, AgeType age){
        this -> age = age;
        this -> name = name;
    }
    void show(){
        cout << name <<" "<< age << endl;
    }
};

// 方法1:指定传入的类型
void test01(Person<string,int> &p){
    p.show();
}

// 方法2:参数模板化
template <typename T1, typename T2>
void test02(Person<T1,T2> &p){
    p.show();
}
// 方法3:整个类模板化
template <typename T>
void test03(T &p){
  	/* 查看编译器推导出的类型 */
    cout << "T的数据类型：" << typeid(T).name() << endl;
    p.show();
}
int main(){
    Person p = Person<string,int>("jack", 2);
    test01(p);
    test02(p);
    test03(p);
    return 0;
}
```



### 类模板与继承

- 当子类继承的父类是一个类模板时，子类在声明的时候，要指定父类中T的类型
- 如果不指定，编译器无法给子类分配内存
- 如果想灵活指定出父类中T的类型，子类也要变为类模板

```c++
template <class NameType, class AgeType>
class Person{
public:
    NameType name;
    AgeType age;
    Person(NameType name, AgeType age){
        this -> age = age;
        this -> name = name;
    }
  	Person(){}
    void show(){
        cout << name <<" "<< age << endl;
    }
};

// 指定父类中T的类型
class MyMan:public Person<string,int>{ --> 指定父类中T的类型
public:
    MyMan(string name, int age):Person(name, age){}
};
// 子类变为类模板
template <typename NameType, typename AgeType>
class MyMan2:public Person<NameType,AgeType>{
public:
  	// 注意：这里调用父类的有参构造方法会出错，推测是因为这样先调用父类的构造方法时，编译器无法推断虚拟的类型究竟是什么类型，调用父类的无参构造方法不会出错
    //MyMan2(NameType name, AgeType age):Person(name, age){}  
  	MyMan2(NameType name, AgeType age){
        this -> age = age;
        this -> name = name;
    } 
};
```



### 类模板成员函数类内实现

- 如果成员函数传入的参数是该类模板实例化的对象，可以不用指定类型

- ```c++
  template <typename T>
  class MyArray{
  public:
  
      MyArray(int capacity){
          this->capacity = capacity;
          this->size = 0;
          this->address = new T[this->capacity];
      }
  		// 不指定类型
      MyArray(const MyArray &arr){
          this->capacity = arr.capacity;
          this->size = arr.size;
          this->address = new T[this->capacity];
          for (int i=0;i<this->capacity;i++){
              this->address[i] = arr.address[i];
          }
      }
  ```

  

### 类模板成员函数类外实现

- 构造函数类外实现
  - 有参构造
  - 无参构造
- 成员函数类外实现

```c++
template <class NameType, class AgeType>
class Person{
public:
    NameType name;
    AgeType age;
    Person();
    Person(NameType name, AgeType age);
    void show();
};

//有参构造
template <class NameType, class AgeType>
Person<NameType,AgeType>::Person(NameType name, AgeType age){
    this -> age = age;
    this -> name = name;
};

//无参构造
template <class NameType, class AgeType>
Person<NameType,AgeType>::Person(){
    this->age = 10;
    this->name = "tom";
};

//成员函数
template <class NameType, class AgeType>
void Person<NameType,AgeType>::show(){
    cout << name << " " << age << endl;
}

int main(){
    Person p1 = Person("jack", 2);
    p1.show();
    Person p2 = Person<string,int>();
    p2.show();
    return 0;
}
```

### 类模板份文件编写

一般来说，`.h`  文件写声明，`.cpp` 文件写实现，在其他文件中需要使用该类时，一般直接`#include ***.h` 就可以

但是，类模板文件如果`#include ***.h`，是不会创建成员函数的，因此相当于没有include进来成员函数。

**解决办法**

- include cpp 源文件 `#include ***.cpp`
- 将`.h` 文件和`.cpp`文件中的内容写到一起，将后缀名改为`.hpp`文件（该后缀名是约定俗成），也就是声明和实现写到一起

### 类模板与友元

- 全局函数做友元
  - 类内实现
  - 类外实现，非常复杂，***不建议***
    - 需要在最开始声明类模板
    - 声明类模板之后，紧接着实现该全局函数
    - 在类内声明该函数

```c++
template <class NameType, class AgeType>
class Person;

// 最开始声明类模板
template <class NameType, class AgeType>
void show(Person<NameType,AgeType> p){
    cout << p.name << " " << p.age << endl;
}
// 紧接着实现该全局函数
template <class NameType, class AgeType>
class Person{
public:
    NameType name;
    AgeType age;
    Person();
    Person(NameType name,AgeType age){
        this -> name = name;
        this -> age = age;
    }
  	// 类内声明该全局函数
    friend void show<>(Person<NameType,AgeType> p);
  
  	// 全局函数类内实现，只需要在类内实现就好
  	friend void show2(Person  p){
        cout << p.name << " " << p.age << endl;
    }
};

int main(){
    Person p1 = Person("jack", 2);
    show(p1);
    return 0;
}
```



## Exercise: 数组类封装

```c++
template <typename T>
class MyArray{
public:

    MyArray(int capacity){
        this->capacity = capacity;
        this->size = 0;
        this->address = new T[this->capacity];
    }

    MyArray(const MyArray &arr){
        this->capacity = arr.capacity;
        this->size = arr.size;
        this->address = new T[this->capacity];
        for (int i=0;i<this->capacity;i++){
            this->address[i] = arr.address[i];
        }
    }
    ~MyArray(){
        if (this->address != NULL){
            this->capacity = 0;
            this->size = 0;
            delete[] this->address;
            this->address = NULL;
        }
    }

    MyArray & operator=(const MyArray & arr){
        if(this->address !=NULL){
            delete[] this->address;
        }
        this->capacity = arr.capacity;
        this->size = arr.size;
        this->address = new T[this->capacity];
        for (int i=0;i<this->capacity;i++){
            this->address[i] = arr.address[i];
        }
        return *this;
    }

    void show(){
        if (this->address != NULL & size >0){
            for (int i=0;i < this->size; i++){
                cout << this->address[i]<< " ";
            }
            cout << endl;
        }
    }

    void push(const T & value){
        if (size == capacity){
            cout << "无法再插入元素"<< endl;
            return;
        }
        address[size] = value;
        size ++;
    }

    void pop(){
        if (size == 0){
            return;
        }
        size -- ;
    }

    T& operator[](int index){
        return address[index];
    }

    int get_capacity(){
        return capacity;
    }

    int get_size(){
        return size;
    }

private:
    int capacity;
    int size;
    T *address;
};
```

