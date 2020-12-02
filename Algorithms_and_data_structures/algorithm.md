# 递归

- 递归本质上是循环，只不过是通过调用函数体来循环

- ```python
  def recursion(level, param1, param2, ....):
    # recursion terminator  -->递归终止条件
    if level > MAX_LEVEl:
      process_result
     	return
    
    # process login in current level  -->处理当前层的逻辑
    process(level,data,...)
    
    # drill down  -->下探下一层
    recursion(level+1,p1,....)
    
    # reverse the current level status if needed
    
  ```

  

- 不要人肉递归

- 找到**最近重复子问题**

- 数学归纳法思维



# 分治

分治代码模版

```python
def divide_conquer(problem, data1, data2,...):
  # recursion terminator
  if problem is None:
    print_result
    return
  
  # prepare data
  data = prepare_data(problem)
  # how to split problem ?
  subproblems = split_problem(problem, data)
  
  # conquer subproblems
  subresult1 = self.divide_conquer(subproblem[1], p1,...)
  subresult2 = self.divide_conquer(subproblem[2], p1,...)
  subresult3 = self.divide_conquer(subproblem[3], p1,...)
  ...
  
  # process and generate the final result
  result = process_result(subresult1, subresult2, subresult3,...)
  
  # reverse the current level states
  
```



- 在这里的分治其实有两种思路
  - 先一直往下探，不做操作，探到最底层，开始返回，在返回的过程中操作，这样的话，传递的参数不需要''result"这个变量
  - 从第一层开始，每层开始操作，将"result"传递到下一层，直到最底层，之后一层一层逐级返回，不需要操作

# 回溯

- 采用试错的思想，尝试分布的去解决一个问题。在分布解决问题的过程中，当它通过尝试发现现有的分布答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其他的可能的分步解答再次尝试寻找问题的答案
- 回溯法通常使用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：
  - 找到一个可能存在的正确的答案
  - 在尝试了所有可能的分步方法后宣告该问题没有答案
- 最坏的情况下，回溯法会导致一次复杂度为指数时间的计算



# 动态规划

- 分治，回溯，动态规划本质上都是递归
- 如何人肉递归
  - **画出递归树**
- 动态规划和分治的区别在于
  - 动态规划需要一个最优的值
  - 分治需要保存所有的值
- **关键点**
  - **动态规划和 递归或者分治没有根本上的区别（关键看有无最优的子结构）**
  - **共性：找到重复子问题**
  - **差异性：最优子结构，中途可以淘汰次优解**
- **递推公式（状态转移方程 / DP方程）**
- **储存中间状态**
- **三个关键步骤**
  - **分解重复子问题**
  - **定义状态数组**
  - **DP方程**

# 搜索

- 遍历
- 保证每个节点遍历一次，且仅遍历一次

## 深度优先搜索

代码模版，利用递归

```python
def dfs(node, visited):
  visited.add(node)
  
  # process current node
  for next_node in node.children():
    if not next_node in visited:
      dfs(next_node, visited)
```

```python
def dfs(node, visited):
  if node in visited:
    return 
 	visited.add(node)
  for next_node in node.children():
    if not next_node in visited:
      dfs(next_node, visited)
```

```python
# 非递归写法
def dfs(tree):
  visited = []
  stack = [tree.root]
  while stack:
    current_node = stack.pop()
    visited.append(current_node)
    process(node)
    
    child_nodes = generate_related_nodes(current_node)
    stack.push(child_nodes)
    
```



## 广度优先搜索

代码模版

- 思想：利用一个（单端）队列，每处理一个节点，把这个节点的子节点放到队列里

```python
def BFS(graph, start, end):
  queue = []
  queue.append([statrt])
  visited.add(start)
  
  while queue:
    node = queue.pop()
    visited.add(node)
    process(node)
    nodes = generate_related_nodes(node)
    queue.push(nodes)
  
```

- 可以看到深度优先搜索的非遍历写法和广度优先搜索的写法是比较相似的，只不过一个是stack，一个queue



# 贪心

- 在每一步选择中都采取在当前状态下最好或者最优的选择，从而希望导致结果是全局最好或最优的算法
  - 不一定可以达到全局最优
- 贪心算法与动态规划的不同在于它对每个子问题的解决都做出选择，不能回退。动态规划会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。
- 贪心算法可以解决一些最优化问题，比如：求图的最小生成树，求哈夫曼编码等。然而对于工程或者生活的问题，贪心算法一般不能达到我们所要求的答案
- 一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效以及所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题
- 什么情况可以用贪心算法
  - 问题可以分解为子问题解决，子问题的最优解可以递推到最终问题的最优解



# 二分查找

前提条件

- 目标函数单调性
- 存在上下界
- 能够通过索引访问

代码模版

```python
left, right = 0, len(array)-1
while left<=right:
  mid = (left+right) / 2
  if array[mid] == target:
    # find the target
    break or return result
  elif array[mid] < target:
    left = mid + 1
  else:
    right = mid - 1
```





# 排序算法

1. 比较类排序
   - 通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此成为非线形时间比较类排序
2. 非比较类排序
   - 不通过比较来决定元素间的相对次序，可以突破基于比较排序的时间下限，以线性时间运行，只适用于整形变量，无法适用于对象类的排序

## 比较类排序

### 初级排序

- 选择排序
  - 每次找最小值，然后放到待排序数组的起始位置（交换位置）

- 插入排序
  - 从前到后逐步构建有序序列，对于未排序数据，在已排序序列中从后往前扫描，找到相应位置并插入
- 冒泡排序
  - 嵌套循环，每次查看相邻的元素，如果逆序，则交换

### 高级排序

- 快速排序 O(nlogn)

  - 数组取标杆pivot，将小元素放在pivot左边，大元素放在右侧，然后依次对右边的右边的子数组继续快排，以达到整个序列有序

  - 代码模版

    ```python
    def quickSort(self, nums, begin, end):
        if begin >= end:
          return 
        pivot = self.partition(nums, begin, end)
        self.quickSort(nums, pivot+1, end)
        self.quickSort(nums, begin, pivot-1)
        return nums
    
    # 重点
    def partition(self, nums, begin ,end):
            pivot, counter = end, begin
            for i in range(begin, end):
                if nums[i] < nums[pivot]:
                    nums[counter], nums[i] = nums[i], nums[counter]
                    counter += 1
            nums[counter], nums[pivot] = nums[pivot], nums[counter]
            return counter
    ```

    

- 归并排序 O(nlogn)

  - 把长度为n的输入序列分为两个长度为n/2的子序列

  - 把这两个子序列分别采用归并排序

  - 将两个排序好的子序列合并为最终的序列

  - 代码模版

    ```python
    def mergesort(self, nums, begin, end):
            if begin >= end - 1:
                return
            mid = int((begin + end)/2)
            self.mergesort(nums, mid, end)
            self.mergesort(nums, begin, mid)
            self.merge(nums, begin, end, mid)
     
    # 重点
    def merge(self, nums, begin, end, mid):
      temp = []
      left, right = begin, mid
      while (left < mid and right < end):
        if nums[left] < nums[right]:
          temp.append(nums[left])
          left += 1
        else:
          temp.append(nums[right])
          right += 1
      if left < mid:
        temp.extend(nums[left:mid])
      if right < end:
          temp.extend(nums[right:end])
    	nums[begin:end] = temp
    ```

- 堆排序

  - 利用优先级队列

## 非比较类排序

- 计数排序
- 桶排序
- 基数排序







# 位运算

- 左移 <<
  - 补零
- 右移 >>
  - 补零
- 或运算 |
- 与运算 &
- 取反 ～
- 按位异或 ^ 
  - 相同为零，不同为一
  - x ^ 0 = x
  - x ^ 1s = ~x (1s也就是全一)
  - x ^(~x) = 1s 
  - x ^ x = 0
- 指定位置的位运算
  - 将x最右边的n位清零： x&(~0 << n)
  - 获取x的第n位值：(x>>n)&1
  - 获取x的第n位的幂值：x&(1<<(n-1))
  - 仅将第n位置为1：x|(1<<n)
  - 仅将第n位置为0：x&(~(1<<n))
  - 将x最高位至第n位（含）清零：x&((1<<n)-1)
  - 将第n位至第0位（含）清零：x&(~(1(1<<(n+1))-1))
- 实战运算要点
  - 判断奇偶
    - (x&1) == 1 判断最后一位是否为1，如果为1，则为奇数
    - (x&1) == 0 判断最后一位是否为1，不为1（为0），则为偶数
  - x >> 1 -> x/2
    - 二分查找时，mid = (left+right)>>1
  - x = x&(x-1) 清零最低位的1
  - x & -x = 得到最低位的1
  - x & ~x = 0
- 