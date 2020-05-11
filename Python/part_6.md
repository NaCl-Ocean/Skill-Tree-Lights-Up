# 异常处理

- ```python
  try:				
      code 
  except ValueError as e:  # 不同的error执行不同的code
      code
  except (NameError,TypeError) as e:  # 捕捉到NameError或TypeError
      code  
  except Exception as e: 
      code
  else:
      code  # 当程序正常运行时，执行完try下的code后执行这里的code
  finally:
      code  # 不管程序是否正常运行，都会执行这里的code
  ```

- `Exception`  万能错误，可以捕捉到所有的error，一般不要使用，或写在最后的except
- `ValueError`  
- `ArrtibuteError`  试图访问一个对象不存在的属性
- `IdentationError`  代码没有正确对齐，实际上捕捉不到，因为没有正常缩进的话，代码相当于无法执行



# 自定义异常

- `raise`  主动触发异常

- ```python
  class TooLongExceptin(Exception):
      "this is user's Exception for check the length of name "
      def __init__(self,leng):
          self.leng = leng
      def __str__(self):
          print("姓名长度是"+str(self.leng)+"，超过长度了")
  ```

- 自定义异常自己指定什么时候触发，也就用到了`raise`

  - `raise TooLongException(len('this is a test'))`

# 断言

- `assert `  ,判断一个表达式，表达式条件为False 时触发异常
- `assert experssion`  等价于  `if not expression:raise error`

