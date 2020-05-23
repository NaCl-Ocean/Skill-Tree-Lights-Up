<center><font face="黑体" color=black size=7>并发性：同步和互斥</font></center>

# 并发

- 单处理器，多道程序
  - 交替执行（伪并行）
- 多处理器，多道程序
  - 并行执行
- 并发导致的问题
  - 死锁：多个进程因相互等待所占用的资源而不能继续执行
  - 活锁：多个进程间为了响应其他进程中的变化而继续改变自己的状态，但不做有用的工作
  - 饥饿：可运行的进程尽管可以继续执行，但被调度器无限忽视而不能被调度执行
  - *竞争：多个线程或进程在读写同一个共享数据时，结果依赖于他们的相对执行时间*
    - 通过引入互斥来解决



# 进程同步和互斥

- 临界资源：一次只能被一个进程使用的资源
  - 被一个进程使用的意思是无论这个进程处于ready，blocked 还是running都不能被其他进程使用
- 临界区：一段代码用于访问临界资源，不能同时有两个以上的进程同时使用
- **互斥：多个进程不能同时访问临界资源的现象**
- **同步：多个进程之间为完成共同任务基于某个条件来协调执行先后关系而产生的协作制约关系**
  - **本质上来说，同步也是一种互斥，但是同步是更为严格的一种互斥，进程之间有顺序关系**





## 互斥的实现方法

- 原子操作：不能被打断的操作

- 中断禁用（硬件方式）

  - 进入临界区前禁用中断，离开临界区使能中断
  - 缺点
    - 无法适用于多处理器
    - 其他线程可能处于饥饿状态，处理器的效率降低

- 专用机器指令（软件方式）

- **信号量**

  - 整型变量

  - wait操作使信号量-1，如果信号量<0，执行wait操作的进程blocked

  - signal操作使信号量+1，如果信号量<=0，被wait操作阻塞的进程唤醒

  - **具体来说，进程进入临界区时，执行wait操作（加标签），出临界区时，执行signal操作（去标签）**

  - ```c
    struct semaphore{
        int count;
        queueType queue;
    }
    void semWait(semaphore s){
        s.count --;
        if (s.count<0){
            place this process in s.queue;
            block this process;
        }
    }
    void semSignal(semaphore s){
        s.count++;
        if (s.count<=0){
            remove a process P from s.queue;
            place process P on ready list;
        }
    }
    ```

- **互斥信号量**

  - 取值为0 和 1

  - Wait操作检查信号量的值

    - 为0，执行wait操作的进程blocked。
    - 为1，将互斥信号量的值置为0，执行进程后续的操作

  - Signal操作检查阻塞进程队列

    - 如果非空，被wait操作阻塞的进程唤醒
    - 如果为空，将互斥信号量的值置为1

  - **也就是说，互斥信号量为1代表当前没有进程在使用临界资源，为0代表有一个进程在使用临界资源，但是不知道是否有进程在处于阻塞状态**

  - ```C
    struct binary_semaphore{
        enum {1,0} value;
        queueType queue;
    };
    void semWaitB(binary_semaphore s){
        if (s.value == 1)
            s.value = 0;
        else{
            place this process in s.queue;
            block this process;
        }
    }
    void semSignalB(binary_semaphore s){
        if (s.queue.is_empty()==True){
            s.value = 1;
        }else{
            remove a process P from s.queue;
            place process P on ready list;
        }
    }
    ```

    

## 生产者/消费者问题

- 一个或多个生产者用于产生数据，存于缓冲区中。一个消费者从缓冲区中取数据

- ```c
  /*无限缓冲区*/
  semaphore n = 0; // 标识当前数据个数
  semaphore s = 1; //信号量，用于互斥操作
  void producer(){
      while(True){
          produce();//produce不需要使用临界资源
          semWait(s);
          append();
          semSignal(s);
          semSignal(n);//n++
      }
  }
  void consumer(){
      while(True){
          semWait(n);//如果n<=0,阻塞当前消费者
          semWait(s);//根据互斥条件阻塞该进程
          take();
          semSignal(s);
          consume();
      }
  }
  void main(){
      prebegim(produce,consumer)
  }
  ```

- ```c
  /*有限缓冲区*/
  semaphore n = 0; // 标识当前数据个数
  semaphore s = 1; //信号量，用于互斥操作
  semaphore e = sizeofbuffer;//标识缓冲区剩余空间大小
  void producer(){
      while(True){
          produce();//produce不需要使用临界资源
          semWait(e);//e--,如果e<0（缓冲区中没有空间），阻塞该进程
          semWait(s);
          append();
          semSignal(s);
          semSignal(n);//n++
      }
  }
  void consumer(){
      while(True){
          semWait(n);//n--,如果n<=0,阻塞当前消费者
          semWait(s);//根据互斥条件阻塞该进程
          take();
          semSignal(s);
          semSignal(e);//e++
          consume();
      }
  }
  void main(){
      prebegim(produce,consumer)
  }
  ```

  

# 信号量

# 管程



# 同步互斥的典型问题

# 进程间通信的方法

