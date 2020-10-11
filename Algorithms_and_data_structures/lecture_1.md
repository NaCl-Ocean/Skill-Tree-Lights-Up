# Array

- 通过index索引数据
- 时间复杂度
  - append：O(1)
  - pop：O(1)
  - insert：O(n)
  - delete：O(n)
  - lookup：O(1)



# Linkedlist

<img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200605203739473.png" alt="image-20200605203739473" style="zoom:50%;" />

- 链表，维护好头节点和尾节点
- 时间复杂度
  - append：O(1)
  - pop：O(1)
  - **lookup：O(n)**
  - delete：O(1)
- 通常是通过定义**node类**来实现链表的连接
- [leetcode LRU缓存策略](https://leetcode.com/problems/lru-cache/)



# Skip list

<img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200605204430838.png" alt="image-20200605204430838" style="zoom:50%;" /> 

- **类似于二分查找**，每一级索引的数量是上一级的1/2，每一级都构成了Linked list
- **时间换空间**
- 查询的时间复杂度：O(logn)
- 空间复杂度：O(n)





