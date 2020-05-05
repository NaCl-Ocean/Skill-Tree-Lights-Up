# docker 简介

- 解决环境的配置问题
- 一次封装 处处运行 
- 镜像（image）相当于类
- 容器（container）：相当于对象
  - 利用镜像创建的运行实例
  - 可以看作简易版的Linux环境（包括root用户权限，进程空间，用户空间和网络空间等），linux下可以用的命令docker也可以使用
- 仓库（repository）
  - 集中存放镜像文件的仓库
  - 分为公开库和私有库（相当于github和gitlab）



# 安装docker(Ubuntu)

- 以阿里云镜像为例

- ```
  sudo apt-get update ：更新源
  ```

- ```
	sudo apt install apt-transport-https ca-certificates software-properties-common curl ：安装需要的包
	```

- ```
	curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -:安装GPG证书
	```
	
- ```
	sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"：添加Docker-ce 软件源，为阿里云的镜像
	```
	
- ```
	sudo apt update：更新源
	```
	
- ```
	sudo apt install docker-ce：安装docker-ce
	```

- ```
  sudo systemctl start docker：启动docker
  ```

- ```
  sudo docker run hello-world：测试docker是否可以成功运行
  ```

- 配置镜像加速器（阿里云为例）

  - 通过[阿里云镜像控制台](https://cr.console.aliyun.com/?spm=a2c4g.11186623.2.11.19e611begDx0bH)获取独立分配的镜像加速地址
  - 根据[阿里云镜像控制台](https://cr.console.aliyun.com/?spm=a2c4g.11186623.2.11.19e611begDx0bH)给出的命令选择相应的系统进行配置

# 运行底层原理

- 与虚拟机的区别

  - docker不需要硬件资源虚拟化，不需要重新加载一个操作系统，通过一个docker引擎替代了虚拟机的Hypervisor和Guest OS。

  ![](http://image.haiyang1218.cn/images/docker_01.png)



# 常用命令
- 帮助命令

  - `docker version`
  - `docker info`
  - `docker --help`
- 镜像命令
  - `docker images [option]`：列出本地主机的镜像
    - 通过REPOSITORY:TAG来定义不同的镜像，默认TAG为latest
    -  -a：列出本地所有镜像（包括中间映射层）
    - -q：只显示镜像ID
    - --digests：显示镜像的摘要信息
    - --no-trunc：显示完整的镜像信息
  - `docker search xxx [option]`：在dockerhub上查找某个镜像
    - -s ：列出star数不少于指定值的镜像
    - -no-trunc：显示完整的镜像信息
      - -automated：只列出automated build的镜像类型
  - `docker pull xxx:tag`：拉取镜像
    - 不加tag默认为latest
  - `docker rmi xxx:tag`：删除镜像
    - 不加tag默认为latest
    - ``docker -f rmi xxx:tag`：强制删除镜像
    - `docker rmi -f $(docker images -qa)`：强制删除所有镜像，相当于管道操作
- 容器命令
  - `docker run [options] IMAGE [command] [arg...]`：新建并运行容器
    - -i：以交互模式运行容器，一般与-t结合使用
    - -t：为容器重新分配一个伪输入终端
    - --name xxx ：为容器指定一个名称
    - -d ：运行守护式容器
    - -p 主机端口:docker 容器端口 ：指定端口，将主机端口映射到容器端口，通过该主机端口即可放分容器端口
    - -P：随机分配端口
    - ![](http://image.haiyang1218.cn/images/docker_03.png)
  - `docker ps [option]`：列出当前运行的容器
    - -l：上一个运行的容器
    - -a：列出当前所有正在运行的容器+历史上运行过的
    - -n：显示最近创建的n个容器
  - -q：只显示容器ID
  - 交互式容器下退出容器：
    - `exit`：退出容器
    - ctrl+P+Q：暂时退出容器，容器没有被杀死
  - `docker start 容器ID或容器名`：启动容器
  - `docker restart 容器ID或容器名`：重启容器
  - `docker stop 容器ID或容器名`：停止容器
  - `docker kill 容器ID或容器名`：强制停止容器
  - `docker rm 容器ID`：删除已停止的容器
    - 删除多个容器：`docker rm $(sudo docker ps -aq)` 或者`docker ps -aq | xargs docker rm `
  - 守护式容器如果不是在运行一直挂起的命令，会自动退出
  - `docker log [option] 容器ID`：查看容器日志
    - -t：加入时间戳
    - -f：跟随最新的日志打印
    - -tail：显示最后多少条
  - `docker top 容器ID`：查看容器内的进程
  - `docker inspect 容器ID`：查看容器内部细节
  - `docker attach 容器ID` 或者`docker exec 容器ID /bin/bash`：重新进入正在运行的容器并以命令行方式运行
  - `dockrt exec -t 容器ID commond`：容器执行命令并返回结果，相当于先进入了容器并运行了命令
  - `docker cp 容器ID:容器内路径 主机路径`：将容器内的文件拷贝到主机

# 镜像原理

- 分层镜像
  - 好处：共享资源，多个镜像都从相同的 base 镜像构建而来，那么宿主机只需在磁盘上保存一份base镜像，同时内存中也只需加载一份 base 镜像，就可以为所有容器服务了。而且镜像的每一层都可以被共享。
  - ![一个深度学习的镜像示意图](http://image.haiyang1218.cn/images/docker_02.png)
- Docker 镜像都是只读的，当容器启动时，一个新的可写层被加载到镜像的顶部。这一层为“容器层”，“容器层”底下的为“镜像层”。

# docker commit

- 当根据镜像产生的容器进行了自定义的修改后，提交容器副本使之成为一个新的镜像。
- `docker commit -m "commit message" -a "author" 容器ID 要创建的目标镜像民:[TAG]`

# docker 容器数据卷

- 作用：docker中的数据持久化，容器/主机之间数据共享

- 不进行数据持久化的话，当容器删除后，数据就删除了

- `docker run -v 主机文件目录:docker文件目录 镜像 `：主机文件目录与docker文件目录绑定，进行容器和主机之间数据共享，当容器停止后，主机修改绑定的目录下的内容，该内容会自动同步到docker绑定的文件目录下。

  - `docker run -v 主机文件目录:docker文件目录:ro 镜像`：设置只读权限，容器对文件目录只有读权限。

-  编写docker file

  1. 新建一个Dockerfile

  2. 编写Dockerfile

     - ```dockerfile
       FROM centos
       # volume set ：给镜像添加多个数据卷
       VOLUME ["/dataVolumeContainer1","/dataVolumeContainer2"]
       CMD echo "finished,--------success1"
       CMD /bin/bash
       ```

  3. `docker build  -f Dcokerfile -t 镜像名`：根据Dockerfile生成镜像

  4. run

  5. `docker inspect 容器ID`：查看默认的主机对应地址

- 数据卷容器：用于多个容器之间数据共享
  - 根据Dockerfile生成的镜像配置数据卷（如上方步骤所示）
  - `docker run --volumes-from 父容器名/父容器ID IMAGE` ：新建子容器，此时子容器与父容器共享数据卷，也就是Dockerfile指定的 VOLUME。
  - 该数据卷的生命周期一直持续到没有容器再使用
  - 该数据卷可被多个容器使用，无论哪个容器再数据卷中修改了内容，都会同步到其他容器中。

# Dockerfile解析

- 用来构建镜像的文件，有一系列命令和参数构成
- 构建步骤
  - 编写dockerfie
  - docker build
  - docker run
- 基础规则
  - 每条保留指令都必须为大写字母且后面跟随至少一个参数
  - 指令从上到下依次执行
  - 每条指令创建一个新的镜像层，并对镜像进行提交

![Dockerfile,镜像与容器之间的关系](http://image.haiyang1218.cn/images/docker_04.png)

- 保留字指令

  | 指令       | 含义                                                         |
  | ---------- | ------------------------------------------------------------ |
  | FROM       | 基础镜像，当前镜像基于哪个镜像                               |
  | MAINTAINER | 镜像的维护者以及邮箱                                         |
  | RUN        | 容器构建时运行的命令                                         |
  | EXPOSE     | 当前容器对外暴露的端口，与容器运行时设置的端口转发可以看作一个功能 |
  | WORKDIR    | 指定在创建容器后，终端默认的进来工作目录                     |
  | ENV        | 用来在构建镜像过程中设置环境变量，相当于c语言中的宏定义      |
  | ADD        | 将宿主机目录下的文件拷贝进镜像且自动处理URL或者解压tar压缩包 |
  | COPY       | 类似于ADD，拷贝宿主机目录下的文件到镜像中，但是不会自动解压  |
  | VOLUME     | 设置数据卷，用于数据持久化                                   |
  | CMD        | 指定一个容器启动时要运行的命令                               |
  | ENTRYPOINT | 可以在指令中追加参数                                         |
  | ONBUILD    | 当构建一个被继承的Dockerfile时运行命令，相当于一个hook，当被继承时，触发 |


# 参考

[docker安装(阿里云镜像)](https://blog.csdn.net/qq_25135655/article/details/104296221)

[网课地址](https://www.bilibili.com/video/BV1Vs411E7AR)



