# linux 文件目录

- 只有一个根目录，根目录下存在不同的目录，不存在windows下的c盘，D盘等分区。

- 级层式的树状目录结构，最上层的是根目录，同时各目录存放的内容都是具体含义的。

- **Linux世界里，一切皆为文件**

  ![img](https://www.runoob.com/wp-content/uploads/2014/06/003vPl7Rty6E8kZRlAEdc690.jpg)

  

- shell terminal的区别

  - shell 负责与kernel（也就是linux内核）交互，terminal 接收用户的输入，交给shell，shell解析后交给系统内核，执行结果返回给terminal，terminal显示结果。

- 远程操控

  - x shell   ssh 协议，linux机器开启sshd服务，默认端口22，主机地址为ifconfig命令输出的ip 地址。
  - Xftp 传输文件

# 设备驱动

- 设备分类
  - 字符设备
    - 映射为文件系统的一个文件对象，在/dev目录下
  - 块设备
    - 映射为一个特殊的文件对象，在/dev目录下
  - 网络设备
    - 无法映射为文件节点
- 可以映射为文件的设备都以文件的形式存放在/dev目录下
- 主设备号和次设备号
  - 主设备号相同的设备使用相同的驱动程序
  - 主设备号+次设备号可以唯一确定设备
- 设备号的分配方法
  - 静态分配设备号
  - 动态分配设备号