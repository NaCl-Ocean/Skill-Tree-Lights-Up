# Stack and Queue

- 栈
  - 先入后出 FILO
  - 添加删除 O(1)
  - 查询 O(n)   --》遍历
- 队列
  - 先入先出 FIFO
  - 添加删除 O(1)
  - 查询 O(n)   --》遍历
- Python 实现
  - stack 通过list实现，pop，append操作
  - queue 通过`collections.dequeue`实现
    - append
    - popleft

# Deque

- 双端队列 
- 头和尾都可以push 和 pop
- 添加删除 O(1)
- 查询 O(n)   --》遍历
- python 实现
  - ``collections.dequeue`



# Pirority Queue

- 底层实现较为多样和复杂：heap，bst，treap
- 插入：O(1)
- 取出：O(logN)
  - 按照元素的优先级取出
- python 实现
  - `queue.PriorityQueue`实现，通过heap实现