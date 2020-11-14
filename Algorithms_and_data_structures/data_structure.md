

# Array

- 通过index索引数据，通过index访问数据的时间复杂度为O(1)
- 时间复杂度
  - append：O(1)
  - pop：O(1)
  - insert：O(n)
  - delete：O(n)
  - lookup：O(1)



# Linkedlist

- 链表，维护好头节点和尾节点

- 时间复杂度
  
  - prepend O(1)
  - append：O(1)
  - pop：O(1)
  - **lookup：O(n)** 通过index访问数据
  - delete：O(1)
  - insert O(1)
  
- 通常是通过定义**node类**来实现链表的连接

  - ```python
    class node:
      def __init__(self,data,next,prev):
        	self.data = data
          self.next = next
          self.prev = prev
    ```

    

- 按照每个node是否有prev指针分类

  - 无prev指针：单链表
    - 尾node的next指针指向头节点：循环链表
  - 有prev指针：双向链表

- [leetcode LRU缓存策略](https://leetcode.com/problems/lru-cache/)



# Skip list

- **类似于二分查找**，每一级索引的数量是上一级的1/2（或者1/3，1/4等等），每一级都构成了Linked list
- **空间换时间**
- 通过index进行lookup的时间复杂度：O(logn)
  - 索引有k级，时间复杂度为O(k)
  - 假设最高级的索引有2个节点，则$2*2^k=n, k=log_2n-1$
- insert O(logn)
- delete O(logn)
- 空间复杂度：O(n)
- <img src="images/第03课丨01数组、链表、跳表的基本实现和特性-0001.png" alt="第03课丨01数组、链表、跳表的基本实现和特性-0001" style="zoom: 25%;" />
- [leetcode LRU缓存策略](https://leetcode.com/problems/lru-cache/)





# stack

- First in - Last out
- Pop O(1)
- Lookup O(n)

# Queue

- First in - First out
- Lookup O(n)



# Double-End Queue

- 两端都可以进出的Queue
- Pop O(1)
- Insert O(1)

- 更加常用



# Priority Queue

- insert O(1)
- pop O(logn) 按照优先级pop出优先级最高的
- 底层具体实现的数据结构较为多样和复杂：heap，binary search tree，treap
- 一个概念
  - 这些数据结构都是对现实生活（或者业务）中某些逻辑的一种抽象
  - 设计出来都是有原因的





# Hash table

- 根据**关键码值（key value）**而直接进行访问的数据结构
- 通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度
- 映射函数称之为**散列函数(Hash function)** ，存放记录的数组叫做**哈希表**
- 哈希碰撞：对于不同存储的数据，经过哈希函数后得到相同的值
  - 哈希碰撞的解决办法：存储为列表形式，也就是哈希之后得到相同的值的所有元素存储为列表
  - <img src="images/第05课丨01哈希表、映射、集合的实现与特性-0001.png" alt="第05课丨01哈希表、映射、集合的实现与特性-0001" style="zoom: 25%;" />
  - 如果哈希函数选的不好，就会导致经常发生哈希碰撞，导致退化为链表



## Map

- 利用哈希表得到的一种data structure
- Java,python,cpp中都有实现
- 注意：set也可以

# Set

- 利用哈希表得到的一种data structure

- Java,python,cpp中都有实现



# Tree

- Tree 和 Graph的主要区别在于Tree不能有环

- 主要在用的是二叉树

- 示例代码

- ```python
  class TreeNode:
    def __init__(self,val):
      self.val = val
      self.left,self.right = None,None
  ```

  

- 为什么要用树

  - 状态转移，从一个初始状态开始，每次都不同的action，都是一个分支

- 遍历

  - 共有三种遍历方式，区别在于顺序不同，利用**递归**

    - 前序遍历（preorder） 根 左 右
    - 中序遍历（inorder）左 根 右
    - 后序遍历（post-order）左 右 根

  - ```python
    class preorder:
      def preoder(self,root):
        if not root:
          return
        self.traverse_path_list.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        
    class inorder:
      def inorder(self,root):
        if not root:
          return
        self.inorder(root.left)
        self.traverse_path_list.append(root.val)
        self.inorder(root.right)
    class postorder:
      def postorder(self.root):
        if not root:
          return
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path_list.append(root.val)
    ```

## 二叉搜索树

- 左子树上的所有节点均小于根节点的值
- 右子树上的所有节点均小于根节点的值
- 以此类推，左右子树也是二叉搜索树

- 查询 O(logN)
  - 查找的时候，每次操作 都可以筛掉一半节点
- 插入 O(logN)
  - 插入实际上，还是一个查找，没有查找到，那么最后到达的位置就是要插入的位置
  - 最后到达的位置的概念是如果要插入的元素小于该节点，而该节点的左子树为空，那么就是最终停留的位置，也就是元素要插入在该节点的左节点处。同理，如果要插入的元素大于该节点，而给节点的右子树为空，那么这个节点就是最终停留的位置，也就是元素要插入在该节点的右节点处。
  - 同样是不断地递归
- 删除
  - 同样需要查找节点，如果删除的是叶节点，那么直接删，没有影响
  - 如果删除的不是叶节点，那么在该节点的右子树中遍历寻找第一个大于该节点的元素，要删除的节点替换为该节点
- 遍历 O(N)