打开项目

- 拖拽： 拖拽项目目录到vscode中
- file 菜单栏 
- code命令
  - 安装code命令
    - Windows 和 Linux 默认可以安装
    - macos 安装： view -> command palette -> 输入 path -> install 'code' command in PATH
  - 使用code命令
    - `code 文件夹名称 `打开指定目录下的项目
    - `code .` 打开当前目录下的项目
    - `code -h`   code 命令帮助

## vscode 界面概览

共有五大部分

- 底部的Status Bar（状态栏），用于显示当前被打开文件的一些信息。
- 最左侧的Activity Bar（活动栏），它里面包含了VS Code五个重要功能的入口点。
- Activity Bar旁边的Side Bar（侧边栏），它里面包含了Activity Bar五个功能点的详细内容。
- 右侧，占据空间最多的Editor（编辑器），用于编写代码。
- 编辑器下方的Panels（面板），它包含了4个不同的面板，其中的Terminal面板我们会经常用到。

![vscode](images/vscode.png)

# Acivity Bar

<img src="images/截屏2020-10-11 上午10.48.16.png" alt="截屏2020-10-11 上午10.48.16" style="zoom: 50%;" />

## Explorer

功能：显示项目所包含的所有文件以及文件夹

包含三个部分（从上到下）：

- OPEN EDITORS：以列表的形式列出了当前打开的所有文件
  - 一键关闭打开的所有文件（最右侧叉叉图标）
    - ![截屏2020-10-11 上午10.58.45](images/截屏2020-10-11 上午10.58.45-2385169.png) 
- Project：当前项目中的所有文件
- OUTLINE：可以更容易理解代码的组织结构；很容易地跳转到指定代码块

## Search Tool

功能：文本的搜索和替换

包含两个部分（从上到下）：

- SEARCH，三个高级功能(从左到右)
  - 大小写敏感 Match Case
  - 匹配全单词 Match Whole Word 
  - 正则表达式 Use Regular Expression
- REPLACE 两个高级功能（从左到右）
  - 大小写不敏感 大写变小写 Preserve Case 
  - Toggle Search Details （三个小点） 指定在哪些文件中修改(files to include)，或者哪些文件排除，不进行修改(files to exclude)

## Source Control

- 基于git 进行版本控制， Git GUI
- 使用前提：
  - 搭建了git环境
  - 项目使用git进行管理(git init )
- 最基本的操作，修改了文件或者新增的文件，当保存后，会在Changes 部分显示，比如修改的文件会有`M` 的标示(modified)，新增的文件会有`U`的标示(untracked) ，此时点击文件旁边的`+` 号，即`git add` 添加到暂存区，或者点击文件旁边的撤销箭头，取消此次修改
- `commit ` 操作，在最上方的输入框中输入commit message后，有2种方法进行commit =，一种是点击最上方的 `对号` 进行commit，或者通过快捷键（输入框有提示快捷键）
- 智能`commit` ,  省去add 步骤，vscode完成git add 操作，直接进行commit。使用方法：不需要点击`+`，直接在输入框中输入commit message后进行commit，此时vscode会提示是否**automatically stage all your changes and commit them directly?** 点击yes即可，或者点击always，之后全部都进行智能commit
- git diff 修改文件时，vscode会根据修改的类型，出现不同颜色的指示，红色表示修改，绿色表示新增，蓝色表示修改
- 更多的git push ,git pull 可以点击最上方的`...` 



## Debug

需要满足的条件

- 搭建相应编程语言的开发环境
- 安装相应编程语言用于调试的扩展
- 配置launch.json

