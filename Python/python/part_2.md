# List

- 特点：通过索引访问列表中的元素，下标从0开始，有序存放
- 当索引为负值时，表示从索引的末尾开始，其中**-1表示最末尾**
- 增
  - 插入：`list.insert`，插入到指定位置，具体使用`insert(index,obj)`
  - 追加：`list.append`，只能插入一个元素
  - 合并：`list.extend(seq)`，插入多个元素，当插入seq是list时，每个元素分开插入，当seq是str时，每个字符分开插入，当seq是dict时，只插入key。
- 删
  - `del list[i]`	删除指定索引
  - `list.pop(i)` 	当`i`不指定时，删除最后一个元素，返回删除的值，当列表为空时，抛出error，`i`指定时，删除`list[i]`
  - `list.clear()`    清空列表
  - `list.remove(obj)`    删除某个元素（第一个匹配项）
- 查
  - `in`：查找某个元素是否在列表中，例 `if obj in list`
  - `list.index(obj)`：查找某个元素（第一个匹配项）的下标
  - `list.count(obj)`    统计某个元素出现次数
- 切片
  - 顾头不顾尾
  - `list[start:end:step]`   start省略不写默认为0，end省略不写默认为列表末尾，step省略不写默认为1
    - **step 为负数表示逆序**，例`list[::-1]`    创建一个逆序列表的副本
    - 切片出来的列表都是创建了一个新的对象，例`a is a[:] = False`
- 反转（逆序）
  - `list.reverse()`：直接在原对象上进行反转，不同于切片创造了一个新的列表副本
- `range(start,stop,step)`：创建整数列表，start默认为0，stop需指定，step默认为1
- 列表拼接：`+`
- 列表重复：`*`

# array

- array与list类似，但是array更像C语言中的数组，只能存放相同类型的数据，通过类型字节码指定存放的数据类型
- [参考](https://blog.csdn.net/xc_zhou/article/details/88538793)



# String

- 定义：可以用单引号`' ' `，双引号` " "`，三引号`''' '''`，双引号中可以嵌套单引号，三引号可以用于多行字符串的定义

- 不可变-->不可修改字符串中的字符

- 通过索引和切片获取字符串中的元素（类似于列表）

- 字符串拼接：` + `

- 重复字符串：` * `

- **格式化字符串**

  - `str.format()`

    - ```python
      # 用法一
      >>>'{},{}'.format('hello','I am test')
      >>>'hello,I am test'
      # 用法二
      >>>'{0},{0},{1}'.format('hello','I am test')
      >>>'hello,hello,I am test'
      # 用法三
      >>>'hello,I am {name}'.format(name='test')
      >>>'hello,I am test'
      ```

    

  - `f-string`

- 转义字符不再转义，在字符串前+r，例`r"test\n"`，此时\n不再转义，打印时会打出\n

- **字符串扩充**

  - `str.center(width,fillchar)`    返回长度为width，str居中的字符串

  - `str.ljust(width,fillchar)`   返回长度为width，str靠左的字符串

  - `str.rjust(width,fillchar)`   返回长度为width，str靠右的字符串

  - ```python
    >>>“nihao".center(10,"-") 
    >>>--nihao---
    ```

- **判断字符串的开头与结尾**

  - `str.endswith(str)`    判断字符串是否以某个字符串结尾
  - `str.startswith(str)`    判断字符串是否以某个字符串开头

- **判断字符串**

  - `str.isdigit()`    判断字符串是否是数字

  - `str.isspace()`   判断字符串是否是空格

  - `str.isupper()`    判断字符串是否都是大写   ---------> `str.upper()`   将字符串中所有字符转为大写

  - `str.islower()`    判断字符串是否都是小写   ---------> `str.lower()`   将字符串中所有字符转为小写

  - `str.istitle()`    判断字符串是否符合title形式 -------> `str.title()`   将字符串中所有字符转为title形式(单词的首字母大写，其余字母小写)

    - 如何区分单词：以空格为分隔符来区分

    - ```python
      >>> "this is a test".title()
      >>>'This Is A Test'
      >>> "thisisatest".title()
      >>>'Thisisatest'
      ```

- **strip**

  - `str.strip([chars])`   移除字符串开头和末尾指定的字符或者字符序列，**默认为空字符和换行符**，当为字符序列时，匹配的不是字符序列整体

  - `str.lstrip([chars])`  移除字符串开头的字符或字符序列

  - `str.rsrip([chars])` 移除字符串末尾的字符或字符序列

  - ```python
    >>> str = "123abcrunoob321"
    >>> str.strip('21')
    '3abcrunoob3'
    ```

- `str.join(seq)`  将序列中的元素以指定的字符连接生成一个新的字符串

  - ```python
    >>>''.join(['1','2','3'])
    '123'
    ```

- `str.split(chars)`  根据指定的字符，分割字符串，以列表的形式返回

- 类似于列表的用法

  - `str.count(char)`  返回char在str中的出现次数
  - `len(str)`    返回str的长度
  - `max(str)`    返回str中最大的字母
  - `min(str)`    返回str中最小的字母

# Tuple

- `tuple = ()`

- Tuple中的元素不可修改，相当于只读列表

- 当tuple中存在可变数据时，可变数据仍然可以修改。因为此时tuple中存放的是可变数据的地址，该地址不可变，但是地址指向的对象可以变。

- 一个细节

  - ```python
    type((1))
    >>><class 'int'>
    type((1,))
    >>><class 'tuple'>
    ```

    



# Number

- 算数运算
  - 取模 `%`
  - 整除 `//`
  - 幂次 `**`
  - 其他的`+` 、`-`、 `*`、 `/` 不再赘述
- 比较运算
  - python 支持 `a<b<c` 这样的操作
  - 其他的`<` `>` `<=` `>=` 不再赘述
- 赋值运算
  - `+=`、`-=` 、`*=`、 `/=`、 `%=`、 `**=`、  `//=`  
- 逻辑运算
  - `and`：与
  - `or`：或
  - `not`：取反



# Dictionary

- `dict={key_1:value_1,key_2:value_2}`

- **特点**

  - **key必须为不可变数据类型，且唯一**
  - **value可以不唯一，可修改**
  - 查询速度快，不受字典的长度影响

- **创建dict**

- ```python
  >>>test = {'name':'test'}
  >>>test = dict(name = 'test')
  # 批量生成重复的值
  >>>test = {}.fromkeys([1,2,3,4,5,6],100)
  >>>test = {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100}
  ```

- **增 and 改**

  - 直接增加   `dict[key] = value_dst`   当dict中已经存在相应的key时，会将原来的value修改为value_dst

  - 保险增加  `dict.setdefault(key,value)`   当dict中存在相应的key时，不会修改原来的value，而是返回原来的value

  - ```python
    >>>test
    {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100}
    >>> test.setdefault(3,80)
    100
    >>> test
    {1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100}
    ```

  - 两个dict进行合并  `dict.update(dict2)`   将字典dict2中的键值对添加到字典dict中，若存在相同的key，则利用dict2中key的value去覆盖dict中key的原value

- **删**

  - `dict.pop(key)`   删除指定key
  - `del dict[key]`   删除指定key
  - `dict.clear()`    清空dict
  - `dict.popitem()`   删除字典的最后一个key及其value

- **查**

  - `dict[key]`   返回key对应的value ，若不存在key，则抛出error
  - `dict.get(key,default = None)`    返回key对应的value，若不存在key，则返回default的值
  - `dict.keys()`  返回一个对象`dict_keys`，包含dicy的所有key  **不是列表**
  - `dict.values()`   返回一个对象`dict_values`，包含dicy的所有value  **不是列表**
  - `dict.items()`   返回一个对象`dict_items`，包含dicy的所有items   **不是列表**

- **循环**

  - **官方推荐**

  - ```python
    for k in dict:
        print(k,dict[k])
    ```

# Set

- `set={}`
- **特点**
  - **Set中存放不可变数据**(无法修改set中的元素)
  - **Set中存放不重复的数据**
  - **无序**，不像列表通过索引来访问元素，集合{3，4，5}等同于{5，4，3}
- **增**
  - `set.add(obj)`  
- **删**
  - `set.discard(obj)`   删除指定obj，当不存在时，do nothing
  - `set.pop()`  随机删除
  - `set.remove(obj)`    删除指定obj，当不存在时，抛出error
- **去重**
  - 帮助列表去重，list转set，set再转list。`list_dst = list(set(list_src))`
- **关系运算**
  - `& 交集`   等价于 `set_a.intersection(set_b)`
  - `| 并集`   等价于`set_a.union(set_b)`
  - `- 差集`   等价于 `set_a.difference(set_b)`
  - `^ 对称差集`  等价于`(set_a - set_b) | (set_b - set_a)`    等价于`set_a.symmetric_difference(set_b)`
  - 判断两集合是否相交  `set_a.isdisjoint(set_b)`，相交返回False，不相交返回True
  - 判断某集合是否是另一集合的子集   `set_a.issubset(set_b)`，set_a 是set_b 的子集返回True
  - 判断某集合是否是另一集合的父集   `set_a.issuperset(set_b)`，set_a 是set_b 的父集返回True

# 深浅copy

- 对于可变数据类型，存在深浅copy的问题

- 首先说一下对于不可变数据类型

  - ```python
    >>> a = 'test'
    >>> b = a
    >>> a = 'test2'
    >>> b
    'test'
    ```

  - 这里符合