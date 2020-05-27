<center><font face="黑体" color=black size=7>设备驱动</font></center>

# 驱动程序

- 概念：驱使硬件设备工作的**软件**
- **提供了操作硬件设备的接口（API/函数）**
- 与设备控制器的关系
  - 设备控制器是一个硬件设备，相当于一个小型处理器，而*驱动程序相当于编译器*，将用户I/O指令转换为设备控制器可以读懂的指令，也就是I/O进程与设备控制器之间的通信程序
  - [设备驱动程序参考讲解](https://blog.csdn.net/dongyanxia1000/article/details/51878467?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.nonecase)
  - [设备控制器讲解](https://blog.csdn.net/dongyanxia1000/article/details/51775723)
- 设备驱动程序的处理过程
  - 接到抽象的要求转换为具体要求
  - 检查用户I/O请求的合法性：是否有权限等
  - 读出和检查设备的状态
  - 传送必要的参数（在读写前，传递参数到设备控制器的寄存器中）
  - 完成I/O操作
- 设备驱动与软硬件的关系
  - 无操作系统：应用软件直接调用驱动程序提供的接口，操纵硬件，例：单片机，STM32等
  - 有操作系统：操作系统进一步封装驱动程序提供的接口，向应用程序提供统一的接口操纵硬件
  
  