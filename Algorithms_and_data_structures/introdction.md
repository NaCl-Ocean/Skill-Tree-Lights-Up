# 切题

- Clarification
- Possibile solutions
  - compare (time / space)
  - optimal
- Coding
- Test cases



# 刷题

- 第一遍刷题
  - 5分钟：读题+思考
  - 没有思路：直接看解法，多种解法，比较解法的优劣
  - 有思路：coding，之后看解法
- 第二遍刷题
  - 自己coding 
  - leetcode commit 
  - pass all test cases
  - 如果没有第一遍刷题看各种解法，则在第二遍刷题时看各种解法
- 第三遍刷题
  - 24小时之后，重复做题
- 第四遍刷题
  - 一周之后，重复做题
- 第五遍刷题
  - 面试前一周，重复做题



# 刷题准备

- [leetcode中国](https://leetcode-cn.com/problemset/all/)
- [leetcode国际](https://leetcode.com/problemset/all/)
  - 中国站网址 去掉cn就是国际站对应problem的网址
  - 看discussion board，most votes
- [Stackoverflow](https://stackoverflow.com)
- ide + leetcode plugin
- [数据结构以及算法的可视化](https://visualgo.net/en/bst)
- 小技巧
  - command + left/right 移动到行头行尾
  - option + left/right 以单词为单位移动
  - command + up/down 移动到文档的开头/末尾
  - shift + command + left/right 选中当前位置到本行开头/末尾的单词
  - shift + option + 左方向键← 选中当前位置到所在单词开头/末尾的文字
  - shift + command + up/down 选中当前位置到整个文档开头/末尾的文字
  - option + delete 删除单词
  - fn + delete 后删 
- search:  Top tips for  \<ide-name>
  - 熟悉自己使用的工具
- **自顶向下的编程方式**
  - 首先思考高层次（主干）逻辑
  - 之后再思考具体的实现
- 一个概念
  - 计算机很傻，只会做一下三种操作
    - if else
    - loop(while / for)
    - recursion
      - Loop 和 recursion 实际上就是在反复地重复一个单元
      - 能不能找到这个重复的单元是核心



# 时间复杂度

- 常见的时间复杂度

  - O(1) 常数复杂度
  - O(logn) 对数复杂度
  - O(n) 线性时间复杂度
  - O(n^2)  平方时间复杂度
  - O(n^3) 立方时间复杂度
  - O(2^n) 指数时间复杂度
  - O(n!) 阶乘时间复杂度

- 如何看时间复杂度

  - 只看最高复杂度的运算

  - 递归：状态树

    - |          Algorithm           |                   Recurrence relationship                    |                           Run time                           |                           Comment                            |
      | :--------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
      |        Binary search         | ![T(n)=T\left({\frac {n}{2}}\right)+O(1)](https://wikimedia.org/api/rest_v1/media/math/render/svg/a78716370c21c74f1808d4ca9fe1d7b2786986d5) | ![O(\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/aae0f22048ba6b7c05dbae17b056bfa16e21807d) | Apply Master theorem case, where![a=1,b=2,c=0,k=0](https://wikimedia.org/api/rest_v1/media/math/render/svg/f2febcf46a2897811ef7ab88631084fb7dfe4419)= |
      |    Binary tree traversal     | ![T(n)=2T\left({\frac {n}{2}}\right)+O(1)](https://wikimedia.org/api/rest_v1/media/math/render/svg/ce3306e42dc12660a749b44498cb94b0e496c225) | ![O(n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/34109fe397fdcff370079185bfdb65826cb5565a) | Apply Master theorem case  where![a=2,b=2,c=0](https://wikimedia.org/api/rest_v1/media/math/render/svg/fb42f5ac8573f25fcd0ada3b53a6618a076053df) |
      | Optimal sorted matrix search | ![T(n)=2T\left({\frac {n}{2}}\right)+O(\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/fa51b8f69be9eacd7ac514e93dae29735317f6c6) | ![O(n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/34109fe397fdcff370079185bfdb65826cb5565a) | Apply the Akra–Bazzi theorem for ![p=1](https://wikimedia.org/api/rest_v1/media/math/render/svg/c29a2f2fb3f642618036ed7a79712202e7ada924) and to get Θ(2n−log⁡n)![\Theta (2n-\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/64e79f6ddb2bea76af7ed8f3723cc5a9e17ed73d) |
      |          Merge sort          | ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/25880508f084e0d3d814505ec1a7b744e340ac81) | ![O(n\log n)](https://wikimedia.org/api/rest_v1/media/math/render/svg/9d2320768fb54880ca4356e61f60eb02a3f9d9f1) | Apply Master theorem case![c=\log _{b}a](https://wikimedia.org/api/rest_v1/media/math/render/svg/14dbd9a5745548d218886b959ce7f2d30df50e3b), where ![{\displaystyle a=2,b=2,c=1,k=1}](https://wikimedia.org/api/rest_v1/media/math/render/svg/32194b35cdfb9ab70167f83a55f9b4c27e7e9d45) |

#  空间复杂度



