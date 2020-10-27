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

- 不需要通过取址符来传入地址

- ```C++
  void swap(int &a,int &b){
      int temp;
      temp = a;
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

- 不需要return 地址，只要return 对应类型的变量即可

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
  - *注意：返回参数不可以作为重载的条件*

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



## 函数传参的类型

- **值传递**
  - 函数接收到了传递过来的参数后，将其拷贝一份，其函数内部执行的代码操作的都是传递参数的拷贝。
  - 函数内部修改参数的值，不会影响外部参数的值。
  - 比较浪费资源
  - `func(int a, int b)`
- **引用传递**
  - 函数内部修改参数的值，会影响外部参数的值
  - 传进来的实质上是地址
  - `func(int &a, int &b)`
- **常量引用传递**
  - 函数内部不允许修改参数的值
  - `func(const int &a, const int &b)`