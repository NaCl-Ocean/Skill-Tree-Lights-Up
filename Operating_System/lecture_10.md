<center><font face="黑体" color=black size=7>文件管理</font></center>

# 前引

- **文件：存储在某种介质上并具有文件名的一组有序信息的集合**
  - 长期存在
  - 进程间可以共享
- **文件系统：操作系统的一部分**
  - 功能
    - 为文件分配磁盘空间
    - 管理文件集合
    - 数据可靠和安全
    - 提供的文件操作：打开，删除，创建……
- **文件结构**
  - 域：基本数据元素，包含一个值
  - 记录：若干个域组成记录
    - 记录的关键狱：通过关键域来唯一标识一条记录，相当于key
  - 文件：若干个记录组成文件
  - 数据库



# 文件组织

- 堆文件
  - 每条记录中域的个数可以不同，域的种类也可以不同
  - 按数据的到达时间堆放
  - 访问某条记录需从最开始穷举搜索
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527100856809.png" alt="image-20200527100856809" style="zoom:50%;" />
- 顺序文件
  - 记录的格式固定
    - 每条记录域的格式相同，个数相同，域同序排放
  - 插入记录不方便
    - 一般将新纪录放在日志文件或者事务文件中，之后通过批更新来合并日志文件或者事务文件
  - 访问记录：从顺序文件的开头进行穷举搜索
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527101845178.png" alt="image-20200527101845178" style="zoom:50%;" />
- 索引顺序文件
  - 基于顺序文件，建立一个index table，index table 中存放某条记录的关键域及指向该记录的指针
  - 一对一索引（个人感觉并不能真正提高查找记录的效率） or 一对多索引(大多采用一对多索引)
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527101708259.png" alt="image-20200527101708259" style="zoom:50%;" />
  - 新记录存放在overflow file中，通过批更新来合并overflow file和主文件
- 索引文件
  - 利用不同的关键域建立index table
  - 支持变长记录
- 散列文件
  - 通过关键域直接定位记录
  - $address = Hash(key)$



# 文件目录

- 包含了文件的相关信息，如文件名，文件所有者，文件权限，文件在磁盘上的位置等
- **本身是一个文件，提供了文件名到文件本身的映射**
- 简单目录结构
  - 每个文件拥有不同的文件名
- 两级目录结构
  - “文件名”=文件名+路径



# 组块分配

- 固定组块
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527110851757.png" alt="image-20200527110851757" style="zoom:50%;" />
- 可变长度跨越式组块
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527110906961.png" alt="image-20200527110906961" style="zoom:50%;" />
- 可变长度非跨越式组块
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527110925838.png" alt="image-20200527110925838" style="zoom:50%;" />

# 文件分配

- 连续分配
  - 将文件存放在连续的Block中
  - 会产生类似于外部碎片
    - 通过磁盘压缩去除外部碎片
  - 存取效率高
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527110029186.png" alt="image-20200527110029186" style="zoom:50%;" />
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527110054554.png" alt="image-20200527110054554" style="zoom:50%;" />
- 链式分配
  - 存取效率低，通过合并来提高存取效率
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527105912258.png" alt="image-20200527105912258" style="zoom:50%;" />
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527105940342.png" alt="image-20200527105940342" style="zoom:50%;" />
- 索引分配
  - 除了文件内容存放的块之外，申请一个新的块，用于记录文件存放的块
  - 磁盘利用率低
  - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200527105745814.png" alt="image-20200527105745814" style="zoom:50%;" />



# 空闲空间管理

- 磁盘分配表/位表

  - 外存上建立一张张位示图(Bitmap), 记录文件存储器的使用情况。每一位对应文件存储器上的一-个物理块，取值0和1分别表示空闲和占用。文件存储器上的物理块依次编号为0、1、 2……。假如系统中字长为32位，那么在位示图中的第一个字对应文件存储器上的0、1、2……31号物理块；第二个字对应文件存储器上的32、33、 34、……63号物理块，以此类推。
  - 位表大小：磁盘大小/(8*块的大小)
  - 缺点：位操作复杂，记录了所有的块，过大

- 链式空闲区

  - 每个空闲块中有指向下一个空闲块的指针，每次申请空闲块，只要找到链的头就可以。

- 索引空闲区

  - 申请一块block用于存放空闲表

  - | 序号 | 第一个空闲块号 | 空闲块数 | 状态 |
    | ---- | -------------- | -------- | ---- |
    | 1    | 18             | 20       | 可用 |
    | 2    | 56             | 7        | 可用 |

- 空闲块表

  - 给每个块分配一个固定大小的序号，所有空闲块的序号构成的空闲块表很大（相比于位表）
  - 空闲块表的一部分存放于主存中，空闲块申请释放优先对主存中的空闲块表进行操作
  - 存放于主存的空闲块表的组织形式
    - 栈（后进先出）
    - FIFO队列