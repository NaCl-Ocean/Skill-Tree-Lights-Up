# 线程

线程的作用

- 充分利用cpu资源（并行运行多个线程）



python 运行默认会产生一个主线程

## Threading

- python中多线程模块主要是`threading` 模块

- **创建线程**

  - `threading.Thread(target, args, name,daemon)`
    - target 是一个函数对象，args为其传入的参数（tuple），name为线程的名称，daemon为True表示设置为守护线程，为False表示设置为前台线程
    - 返回一个线程对象
  - 什么是守护线程（后台线程）
    - 当所有的前台线程结束后，会自动kill掉后台线程

- **join**

  - `thread.join()` 线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止，不设置的话，当主线程结束后，就会停止当前当前进程，也就是包含的所有线程都会结束
  - 守护线程不可以设置`join()`

- **start**

  -  `thread.start()`   开始运行线程

- **自定义thread**

  - 继承`threading.Thread` ，主要需要重写两个方法：`__init__` 和 `run`

  - 注意：启动线程仍然要调用`start`，虽然本质上start是在执行run中的代码

  - ```python
    class Mythread(threading.Thread):
        def __init__(self, name, delay):
            super(Mythread, self).__init__() --》Thead.__init__()中的参数全部是默认参数，因此在这里可以不穿入参数初始化
            self.delay = delay
            self.name = name
        
        def run(self):
            print('start run')
            display(self.name, self.delay)
            print('end run')
    ```

- 线程同步与锁（实现互斥操作）--》也就是操作系统中说的通过软件层面实现互斥

  - ```python
    lock = threading.Lock()
    
    def fun():
      # method 1
      lock.acquire() --》 上锁
      ... code 
      lock.release() --》 释放锁
      
      # method 2
      with lock:
        code ...
    ```

    

## pool

