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