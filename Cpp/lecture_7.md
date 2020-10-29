# 算法

- 算法主要由头文件`<algorithm>`  `functional`  `numeric` 三部分组成

- `<algorithm>`  是所有STL头文件最大的一个，范围涉及到比较，交换，查找，排序，复制，修改等

- `functional` 定义了一些模板类，用于声明函数对象

- `numeric`  体积很小，只包括几个在序列上面进行简单数学运算的模板函数

- 注：以下示例中自定义`Person`类定义如下

  - ```c++
    class Person{
    public:
        string name;
        int sex;
        int age;
        Person(string name, int sex, int age){
            this -> name = name;
            this -> sex = sex;
            this -> age = age;
        }
    };
    ```

    

## 遍历

- `for_each(iterator beg, iterator end, _func) `  遍历容器

  - beg 开始迭代器

  - end 结束迭代器

  - _func 函数或者仿函数

    - 函数不需要带`()`
    - 仿函数需要带`()`

  - ```c++
    void print1(int v){
        cout << v << endl;
    }
    
    class print2{
    public:
        void operator()(int v){
            cout << v << endl;
        }
    };
    int main()
    {
        vector<int> v;
        for (int i=0;i<7;i++){
            v.push_back(rand()%100);
        }
      	//函数，函数不需要带()
        for_each(v.begin(),v.end(),print1);
      	// 函数对象，函数对象需要带()
        for_each(v.begin(),v.end(),print2());
        return 0;
    }
    ```

  

- `transform(iterator begin, iterator end, iterator beg2, _func)`    **搬运容器到另一个容器中**

  - begin 源容器开始迭代器 

  - end 源容器结束迭代器

  - beg2 目的容器开始迭代器

  - _func 函数或者仿函数(该参数不可省略)

  - ```c++
    int Transform1(int v){
        return (v%10);
    }
    
    class Transform2{
    public:
        int operator()(int v){
            return (v%10);
        }
    };
    
    int main()
    {
        vector<int> v;
        for (int i=0;i<7;i++){
            v.push_back(rand()%100);
        }
        vector<int> v2;
        v2.resize(v.size());
        transform(v.begin(),v.end(),v2.begin(),Transform1);
        transform(v.begin(),v.end(),v2.begin(),Transform2());
        for_each(v2.begin(),v2.end(),print1);
      	return 0;
    }
    ```

## 查找

- `find(iterator begin, iterator end, value)` **查找指定元素，找到返回指定元素 的迭代器，找不到返回结束迭代器**

  - begin 开始迭代器

  - end 结束迭代器

  - value 要查找的元素

  - 要查找自定义的数据类型，需要重载`==`号

  - ```c++
    
    // Person 类重载 == 号
    bool operator==(const Person &person){
        if ((name == person.name) && (sex==person.sex) && (age=person.age)){
          return true;
        }else{
          return false;
        }
    
    int main()
    {
        vector<Person> v;
        
        v.push_back(Person("tom",1,20));
        v.push_back(Person("jack",1,19));
        v.push_back(Person("jessei",0,21));
        Person p1 = Person("jessei",0,21);
        vector<Person>::iterator it = find(v.begin(),v.end(),p1);
        cout << it->name << it->age << it-> sex << endl;
        return 0;
    }
    ```

- `find_if(iterator begin, iterator end, _Pred)`   **在前两个参数指定的范围内查找可以使第三个参数指定的谓词返回 true 的第一个对象，找不到返回结束迭代器**

  - begin 开始迭代器

  - end 结束迭代器

  - _Pred 函数或者谓词（函数需返回bool类型） 

  - 注：返回的迭代器无法通过++操作找到所有符合条件的对象

  - ```c++
    class Male{
    public:
        bool operator()(const Person &p){
            if (p.sex==1){
                return true;
            }else{
                return false;
            }
        }
    };
    int main()
    {
        vector<Person> v;
        v.push_back(Person("tom",1,20));
        v.push_back(Person("jack",1,19));
        v.push_back(Person("jessei",0,21));
        vector<Person>::iterator it = find_if(v.begin(),v.end(),Male());
        cout << it->name<<":" << it->age<<":" << it-> sex << endl;
        return 0;
    }
    ```

- `adjacent_find(iterator begin, iterator end`  **查找相邻重复元素，返回相邻重复元素的第一个位置的迭代器，找不到返回结束位置的迭代器**

  - begin 开始迭代器

  - end 结束迭代器

  - ```c++
    
    // Person 类重载== 号 
    // 注意这里加在函数后面的const，不加的话clang编译不了
    bool operator==(const Person &person) const{
      if ((name == person.name) && (sex==person.sex) && (age==person.age)){
        return true;
      }else{
        return false;
      }
    }
    int main()
    {
        vector<Person> v;
        v.emplace_back("tom", 1, 20);
        v.emplace_back("tom", 1, 20);
        v.emplace_back("jessei", 0, 21);
        vector<Person>::iterator it = adjacent_find(v.begin(),v.end());
        cout << it->name<<":" << it->age<<":" << it-> sex << endl;
        return 0;
    }
    ```

- `bool binary_search(iterator begin, iterator end, value)` **查找指定的元素是否存在，存在返回True，不存在返回False**

  - begin 开始迭代器
  - end 结束迭代器
  - value 查找的元素
  - **在无序序列中不可用**，利用的是二分查找

  

- `count(iterator begin, iterator end, value)` **统计指定元素出现的次数**

  - begin 开始迭代器
  - end 结束迭代器
  - value 查找的元素

- `count_if(iterator begin, iterator end, _Pred)` **按条件统计指定元素出现的次数**

  - begin 开始迭代器

  - end 结束迭代器

  - _pred 要统计的元素需满足的条件，谓词或者函数（返回bool）

  - ```c++
    
    class Male{
    public:
        bool operator()(const Person &p){
            if (p.sex==1){
                return true;
            }else{
                return false;
            }
        }
    };
    
    bool Male2(const Person &p){
        if (p.sex==1){
                return true;
            }else{
                return false;
            }
    }
    int main()
    {
        vector<Person> v;
        v.emplace_back("tom", 1, 20);
        v.emplace_back("tom", 1, 20);
        v.emplace_back("jessei", 0, 21);
      	// count
        cout << count(v.begin(),v.end(),Person("tom", 1, 20)) << endl;
      	// count_if 函数
      	cout << count_if(v.begin(),v.end(),Male2) << endl;
      	// count_if 谓词
      	cout << count_if(v.begin(),v.end(),Male()) << endl;
        return 0;
    }
    输出:
    2
    2
    2
    ```

    

  

## 排序

- `sort(iterator begin, iterator end, _Pred)` 对容器中元素进行排序

  - begin 开始迭代器

  - end 结束迭代器

  - _pred 谓词或者函数(返回bool)，指定排序的规则

  - ```c++
    class Mycompare{
    public:
        bool operator()(const Person &p1, const Person p2){
            if (p1.age > p2.age){
                return true;
            }else{
                return false;
            }
        }
    };
    bool Mycompare2(const Person &p1, const Person p2){
        if (p1.age > p2.age){
                return true;
            }else{
                return false;
            }
    }
    int main()
    {
        vector<Person> v;
        v.emplace_back("tom", 1, 20);
        v.emplace_back("tom", 1, 19);
        v.emplace_back("jessei", 0, 21);
      	// 函数（返回bool）
        sort(v.begin(),v.end(),Mycompare2);
      	// 仿函数
      	sort(v.begin(),v.end(),Mycompare());
        for (vector<Person>::iterator it=v.begin(); it!= v.end(); it++){
            cout << "姓名：" << it->name << " 年龄:" << it->age << "性别:" << it->sex << endl;
        }
        return 0;
    }
    
    ```

- `random_shuffle(iterator begin, iterator end)` 将指定范围内的元素随机打乱

  - begin 开始迭代器
  - end 结束迭代器

- `merge(iterator begin1, iterator end1,iterator begin2, iterator end2,iterator dest,_pred)`将两个容器中的元素合并后，存储到另一个容器中

  - begin 容器一的开始迭代器

  - end 容器一的结束迭代器

  - begin 容器二的开始迭代器

  - end 容器二的结束迭代器

  - dest 目标容器的起始迭代器

    - 如果是序列式容器(有迭代器)，目标容器需要先resize到指定的大小(容器一的大小+容器二的大小)

  - **要合并的两个容器必须有序**

  - ```c++
    // person 类重载< 符号
    bool operator<(const Person &person) const{
            if (age<person.age){
                return true;
            }else{
                return false;
            }
        }
    // 注意，这里在sort的时候也要按照升序sort
    // 因为merge默认认为升序的容器才是有序的，降序的容器同样是无序的
    // 所以对于降序的容器进行merge不会有希望的效果
    // 除非在merge时，传入一个谓词，让其按照降序排列
    class Mycompare{
    public:
        bool operator()(const Person &p1, const Person p2)const{
            if (p1.age < p2.age){
                return true;
            }else{
                return false;
            }
        }
    };
    int main()
    {
        vector<Person> v1;
        v1.emplace_back("tom", 1, 20);
        v1.emplace_back("tom", 1, 19);
        v1.emplace_back("jessei", 0, 21);
        sort(v1.begin(),v1.end(),Mycompare());
        vector<Person> v2;
        v2.emplace_back("tom", 1, 18);
        v2.emplace_back("tom", 1, 17);
        v2.emplace_back("jessei", 0, 16);
        vector<Person> v3;
        v3.resize(v1.size()+v2.size(),Person("jack",1,11));
        sort(v2.begin(),v2.end(),Mycompare());
        merge(v1.begin(),v1.end(),v2.begin(),v2.end(),v3.begin());
        for (vector<Person>::iterator it=v3.begin(); it!= v3.end(); it++){
            cout << "姓名：" << it->nam
              e << " 年龄:" << it->age << "性别:" << it->sex << endl;
        }
        return 0;
    }
    ```

- `reverse(iterator begin, iterator end)` 对容器内的元素进行反转

  - `1 2 3 4 5 -> 5 4 3 2 1`
  - 不需要有序

## 拷贝和替换

- `copy(iterator begin, iterator end,iterator dest)` 将一个容器内的元素拷贝到另一个容器中

  - begin 源容器的开始迭代器
  - end 源容器的结束迭代器
  - dest 目标容器的开始迭代器
  - 同样需要给目标容器提前开辟空间(resize)

- `replace(iterator begin, iterator end,oldvalue,newvalue)` 将指定范围内的所有old value替换为new value

  - begin 开始迭代器
  - end 结束迭代器

- `replace_if(iterator begin, iterator end,_pred,newvalue)` 将指定范围内满足谓词的所有元素替换为new value

  - begin 开始迭代器

  - end 结束迭代器

  - _pred 谓词或者函数（返回bool）

  - ```c++
    class Myreplace{
    public:
        bool operator()(const Person &p1)const{
            if (p1.name == "tom"){
                return true;
            }else{
                return false;
            }
        }
    };
    int main()
    {   
        vector<Person> v1;
        v1.emplace_back("tom", 1, 20);
        v1.emplace_back("tom", 1, 19);
        v1.emplace_back("jessei", 0, 21);
        replace_if(v1.begin(),v1.end(),Myreplace(),Person("jack",1,18));
        for (vector<Person>::iterator it=v1.begin(); it!= v1.end(); it++){
            cout << "姓名：" << it->name << " 年龄:" << it->age << "性别:" << it->sex << endl;
        }
      return 0;
    }
    
    输出：
    姓名：jack 年龄:18性别:1
    姓名：jack 年龄:18性别:1
    姓名：jessei 年龄:21性别:0
    ```

- `swap(container c1, container c2) `  互换两个容器

  - 必须是同种类型的容器



## 算术生成算法

- `#include <numeric>`

- `accumulate(iterator begin, iterator end,value)` 计算区间范围内元素累计总和

  - begin 起始

  - end 结束

  - value 起始累加值

  - ```c++
    vector<int> v1;
    for(int i=0;i<100;i++){
    	v1.push_back(i+1);
    }
    cout <<accumulate(v1.begin(),v1.end(),0)<< endl;
    cout <<accumulate(v1.begin(),v1.end(),1000)<< endl;
    
    输出：
    5050
    6050
    ```

- `fill(iterator begin, iterator end,value)` 将区间范围内的元素填充为value



## 集合算法

- `set_intersection(iterator begin1, iterator end1,iterator begin1, iterator end1,iterator dest)` **求两个容器指定范围内的交集**

  - begin1,end1 容器1的起始与结束
  - begin2,end2 容器2的起始与结束
  - dest 目标容器的起始迭代器
  - 返回目标容器最后一个元素的迭代器地址
  - 注意：需要先给目标容器分配空间（resize）

- `set_union(iterator begin1, iterator end1,iterator begin1, iterator end1,iterator dest)` **求两个容器指定范围内的并集**

  - begin1,end1 容器1的起始与结束
  - begin2,end2 容器2的起始与结束
  - dest 目标容器的起始迭代器
  - **两个集合必须是有序序列**

- `set_difference(iterator begin1, iterator end1,iterator begin1, iterator end1,iterator dest)` **求两个容器指定范围内的差集**

  - begin1,end1 容器1的起始与结束
  - begin2,end2 容器2的起始与结束
  - dest 目标容器的起始迭代器
  - **两个集合必须是有序序列**

  

- ```c++
  int main()
  {   
      vector<int> v1;
      vector<int> v2;
      for(int i=0;i<10;i++){
          v1.push_back(i+1);
          v2.push_back(i+5);
      }
    	// 交集
      vector<int> v3;
      v3.resize(10);
      vector<int>::iterator end1 = set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),v3.begin());
      for_each(v3.begin(),end1,print);
      cout<<endl;
  		// 并集
      vector<int> v4;
      v4.resize(20);
      vector<int>::iterator end2 = set_union(v1.begin(),v1.end(),v2.begin(),v2.end(),v4.begin());
      for_each(v4.begin(),end2,print);
      cout<<endl;
    	// 差集
      vector<int> v5;
      v5.resize(10);
      vector<int>::iterator end3 = set_difference(v1.begin(),v1.end(),v2.begin(),v2.end(),v5.begin());
      for_each(v5.begin(),end3,print);
      cout<<endl;
  
      return 0;
  }
  ```

  

  



 