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





# 回溯

- 采用试错的思想，尝试分布的去解决一个问题。在分布解决问题的过程中，当它通过尝试发现现有的分布答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其他的可能的分步解答再次尝试寻找问题的答案
- 回溯法通常使用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：
  - 找到一个可能存在的正确的答案
  - 在尝试了所有可能的分步方法后宣告该问题没有答案
- 最坏的情况下，回溯法会导致一次复杂度为指数时间的计算