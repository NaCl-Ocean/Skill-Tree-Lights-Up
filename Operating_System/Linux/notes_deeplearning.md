- 深度学习使用的服务器一般是ubuntu。

# Ubuntu

- ubuntu下安装后都是普通用户权限，没有root权限
- 使用root权限有以下几种方式：
  - sudo 命令：使用root权限执行命令
  - 切换到root用户，需要先设置root用户密码
    - sudo passwd：设置root用户密码
    - exit：退出root用户
- Ubuntu下一般内置了python
- Ubuntu下没有内置sshd，需要手动安装sshd
  1. `sudo apt-get install openssh-server`
  2. service sshd restart
- linux 下远程登陆另一台linux服务器
  - `ssh 用户名@ip地址`

## apt软件管理

- Advanced Packing Tool
- /etc/apt/sources.list 存放官方的软件仓库地址
- `apt-get update`：更新源
- `apt-get install package`：下载软件包
- `apt-get removre package`：删除包
- `apt-cache search package` 搜索软件包 
- `sudo apt-cache show package`  获取包的相关信息，如说明、大小、版本等
- `sudo apt-get install package --reinstall` 重新安装包
- `sudo apt-get -f install`   修复安装
- `sudo apt-get remove package --purge` 删除包，包括配置文件等
- `sudo apt-get build-dep package` 安装相关的编译环境
- `sudo apt-get upgrade` 更新已安装的包
- `sudo apt-get dist-upgrade` 升级系统
- `sudo apt-get dist-upgrade` 升级系统
- `sudo apt-cache depends package` 了解使用该包依赖那些包
- `sudo apt-cache rdepends package` 查看该包被哪些包依赖
- `sudo apt-get source package`  下载该包的源代码
- 设置镜像源
  1. 备份/etc/apt/sources.list
  2. 在[阿里云镜像](https://developer.aliyun.com/mirror/ubuntu) 查找对应版本的镜像源配置
  3. `echo '' > /etc/apt/sources.list` 清空/etc/apt/sources.list中的内容
  4. 修改/etc/apt/sources.list中的内容位阿里云镜像的镜像源配置
  5. sudo apt-get update 更新源

# 深度学习相关

## 睡觉调参

- 训练一个模型通常需要很长时间
- 当由于网络原因突然断开ssh或关闭ssh时，此终端下运行的所有任务都会被杀死。
- **screen** 在一个终端下创建多个screen窗口，这样当突然断开ssh时，screen窗口下的任务不会被杀死。
  - screen -S xxx：创建一个xxx的screen窗口
  - screen -r xxx ：切换到xxx screen窗口
  - screen -ls：查看已经创建的screen 窗口
  - exit：进入到screen窗口后，使用exit退出screen窗口

## 查看GPU使用情况

- `watch -n 10 nvidia-smi` 
  - watch 命令类似于top命令，使用方法 `watch [选项] [命令]`，周期性监测一个命令的运行结果
  - 上述命令即为每10s更新GPU使用情况，包括显存占用，利用率等
  - `nvidia -smi` 是nvidia官方提供的用来查看GPU状态的命令



## 参考

[搜狗拼音输入法乱码](https://blog.csdn.net/a6333230/article/details/95305918?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1)

[apt安装本地软件包](http://blog.lujun9972.win/blog/2018/11/18/ubuntu%E4%BD%BF%E7%94%A8apt%E5%AE%89%E8%A3%85%E6%9C%AC%E5%9C%B0deb%E8%BD%AF%E4%BB%B6%E5%8C%85/index.html)

[ubuntu安装搜狗拼音输入法](https://www.bilibili.com/video/BV1UW411S7nu?from=search&seid=10871947589641994248)



