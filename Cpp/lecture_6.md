

# 函数对象



- 重载**函数调用操作符**的类，其对象成为**函数对象**
- 函数对象**使用重载的`()`**时，行为类似函数调用，也叫**仿函数**
- **本质上仍然是一个类，而不是函数**
- **特点**
  - 函数对象在使用，可以像普通函数那样调用，可以有返回值
  - 函数对象超出普通函数的概念，函数对象可以有自己的状态
  - 函数对象可以作为参数传递

```c++
class Myadd{
public:
    int count=0;
    int operator()(int a,int b){
        count++;
        return (a+b);
    }
};
//函数对象可以作为参数传递
void add_print(Myadd add,string test){
    cout << test << add(10,20) << endl;
}
int main()
{
    Myadd myadd;
    cout<< myadd(10,20)<< endl;
    cout<<myadd(20,30) << endl;
  	//函数对象可以有自己的状态
    cout<<myadd.count<<endl;
    add_print(myadd, "test");
    return 0;
}
```



## 谓词

- **返回bool类型的仿函数**称为谓词
  - **一元谓词**：operator()接受一个参数
  - **二元谓词**：operator()接受两个参数

```c++
// 一元谓词
class GreatFive{
public:
    bool operator()(int v){
        return v>5;
    }
};

int main()
{
    vector<int> v;
    for (int i=0;i<7;i++){
        v.push_back(i);
    }
    vector<int>::iterator it = find_if(v.begin(),v.end(),GreatFive());
    cout << *it << endl;
    return 0;
}
```

```c++
class descend{
public:
    bool operator()(int v1,int v2){
        return v1>v2;
    }

};
int main()
{
    vector<int> v;
    for (int i=0;i<7;i++){
        v.push_back(rand()%100);
    }
  	// 默认排序(升序)
    sort(v.begin(),v.end());
    for (vector<int> ::iterator it=v.begin();it!=v.end();it++){
        cout << *it << " ";
    }
    cout << endl;
 		// 降序
    sort(v.begin(),v.end(),descend());
    for (vector<int> ::iterator it=v.begin();it!=v.end();it++){
        cout << *it << " ";
    }
    cout << endl;
    return 0;
}
```



## 内建函数

- STL内建的函数对象

- **分类**
  - 算术仿函数
  - 关系仿函数
  - 逻辑仿函数
- 用法
  - 与一般的仿函数使用方法相同
  - 需要引入头文件 `#include <functional>`

### 算术仿函数

- 实现四则运算
- negate 是一元运算，其余都是二元运算

- 仿函数原型
  - `template<class T> T plus <T> ` 加法
  - `template<class T> T minus<T>` 减法
  - `template<class T> T multiplies <T>` 乘法
  - `template<class T> T divides<T> ` 除法函数
  - `template<class T> T modules<T> `取模仿函数
  - `template<class T> T negate<T>` 取反仿函数

- ```c++
  negate<int> n;
  n(50);
  plus<int> p;
  p(50,10);
  minus<int> m;
  m(40,20);
  ```

  

### 关系仿函数

- 二元运算

- `template<class T> bool equal <T> ` 等于

- `template<class T> bool not_equal <T> ` 不等于

- `template<class T> bool greater <T> ` 大于 --》常用

- `template<class T> bool greater_equal <T> ` 大于等于

- `template<class T> bool less <T> ` 小于

- `template<class T> bool less_equal <T> ` 小于等于

- ```c++
  int main()
  {
      vector<int> v;
      for (int i=0;i<7;i++){
          v.push_back(rand()%100);
      }
    	// 默认排序(升序)
      sort(v.begin(),v.end());
      for (vector<int> ::iterator it=v.begin();it!=v.end();it++){
          cout << *it << " ";
      }
      cout << endl;
   		// 降序
      sort(v.begin(),v.end(),greater<int>());
      for (vector<int> ::iterator it=v.begin();it!=v.end();it++){
          cout << *it << " ";
      }
      cout << endl;
      return 0;
  }
  ```

  

### 逻辑仿函数

- `template<class T> bool logical_and <T> ` 与
- `template<class T> bool logical_or <T> `或

- `template<class T> bool logical_not <T> `非
- 一元运算