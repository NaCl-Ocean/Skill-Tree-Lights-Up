# 基本名词

- index file 暂存区
- working tree 工作区
- commit 记录的commit 的版本只会增加，不会删除

![](http://image.haiyang1218.cn/images/git_07.png)



# 常用命令

- git help &lt;commond&gt; 查看命令的help
- **git init** : 初始化仓库
  - 本地库文件存放在/.git文件夹中
  - /.git 文件结构：
    - config
    - description
    - HEAD
    - hooks
    - info
    - objects
    - refs
- **git config**: 设置签名
  - **git config user.name / git config user.email** 设置项目级别/仓库级别的签名
  - **git config --global user.name/ git config --global user.email** 设置系统用户级别的签名
  - 这里设置的签名与远程仓库的登陆用户名以及密码无关
  - 项目级别的签名存放在/.git/config 中
  - 项目级别的签名与系统用户签名同时存在时，选择项目级别的签名
- **git status** 
  - No commits yet:  本地库中没有文件
  - nothing to commit:  暂存区中没有文件
  - untracked files: 工作区中的文件未提交到暂存区
  - modified files:  该文件曾经被添加到本地库中，现在被修改
  - deleted files: tracked files在工作区中被删除
  - Changes to be committed: 暂存区中的文件未提交到本地库
- **git rm --cached**  &lt;file &gt; ： 取消提交到暂存区中的文件
- **git add** 提交工作区中的文件到暂存区
  - git add . : 提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件
  - git add -u: 提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)
  - git add -A: 提交所有变化
  - git add &lt;file&gt;:  提交单个文件
- **git commit** 提交工作区的文件到本地库
  - git commit -m "commit message"
- **git log** : 查看所有commit 的信息
  - git log --pretty=oneline 每个commit 日志显示一行
  - git log --oneline 显示当前版本之前的版本
  - git refloq 有助于移动版本   HEAD@{移动到当前版本需要多少步}
- **git diff**
  - git diff &lt;file&gt; 表示工作区的文件与暂存区进行比较
  - git diff HEAD^ &lt;file&gt;  与本地库的某个版本进行比较

# 版本移动

- 基于索引：git reset --hard &lt;索引值&gt;  索引值: 哈希算法(reflog中显示的索引值即可)
- 版本后退： 
  - git reset --hard HEAD^^^ （^的个数为后退的步数）
  - git reset --hard HEAD~n （后退n步）
- git reset --soft 只移动本地库
- git reset --mixed 移动本地库，暂存区
- git reset --hard 移动本地库，暂存区与工作区
- 利用git进行删除文件找回：前提是被删除的文件曾经被commit
  - 通过版本移动到文件未删除的版本

# 分支

- **git branch -v** 查看现在的所有分支
- **git branch**  &lt;branch name&gt;  创建分支
- **git checkout** &lt;branch name&gt;  切换分支
- **git merge**  &lt;branch name&gt;  合并分支
- 冲突的merge
  - 文档的表现：![image-20200417212043595](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200417212043595.png)
  - 解决方法：
    - 编辑文件，删除特殊符号
    - 修改文件
    - git add &lt;文件名&gt;
    - git commit -m "commit message"(不带文件名)

# git 工作原理

- git object 有三种,每个object 都有一个Hash值

  - commit
  - tree
  - blob

  ![](http://image.haiyang1218.cn/images/git_01.png)

  

  

- git 提交的每个快照都有一个parent，parent指向上次提交产生的快照

![快照构成示意图](http://image.haiyang1218.cn/images/git-02.png)

- git 分支的切换以及版本的移动都是在移动**HEAD**.

![HEAD指向master](http://image.haiyang1218.cn/images/git_03.png)

![切换分支](http://image.haiyang1218.cn/images/git_04.png)

![提交新的版本HEAD的指向](http://image.haiyang1218.cn/images/git_06.png)

# 远程库交互

- 进行只读的操作时，不需要验证身份，比如Pull,fetch,clone

- git remote add &lt;远程库别名&gt;  &lt;address&gt;  关联远程库

  - address 有两种
    - https
    - SSH：使用SSH方式需要先设置SSH key。可以省去每次push的输入用户以及密码的操作

- git clone &lt;address&gt; 
  - 附带初始化本地库
  - 创建origin 远程仓库别名
  
- git push &lt;远程库别名&gt;  &lt;分支名&gt;

- git fetch &lt;远程库别名&gt;  &lt;分支名&gt;  fetch下来并没有写入到本地库现在HEAD指向的这个分支，实际上是写到了别名/分支名这个分支上。

- pull = fetch + merge

- git  pull  &lt;远程库别名&gt;  &lt;分支名&gt;

- 冲突的推送：当前本地库不是基于远程库的最新版进行修改，则不能推送，需要先拉取远程库的最新版，根据分支冲突的解决方法合并分支，之后进行提交

  


# 参考

[网课地址](https://www.bilibili.com/video/BV1pW411A7a5?p=42)

[生成SSH公钥](https://blog.csdn.net/u012037852/article/details/80756081)

[git book](https://git-scm.com/book/zh/v2)









