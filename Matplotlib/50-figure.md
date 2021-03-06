

以下都用`plt`来代替`pyplot`，利用`sns`来代替`seaborn`

# Figure

- `plt.figure(figsize=[6.4,4.8], dpi=100, facecolor='w', edgecolor='w')`
  - figsize 图像的尺寸，以英尺为单位
  - dpi 分辨率
  - facecolor。图像的背景颜色
  - edgecolor 边框颜色



# 关联图

- 展示一个事物随着另一个事物的变化如何变化
- 典型的关联图有：折线图，散点图，相关矩阵 ……



## 散点图

- `plt.scatter(x,y,s,c,marker,label,alpha,edgecolors,linewidths)`
  - **x,y:** scalar or array-like, shape (n, )
  - **s**: marker size.   **scalar or array-like**, shape (n, ), optional
    - 如果输入为array-like，但是长度不匹配，不等于n
      - 长度小于n，通过重复该序列来补齐长度到n
      - 长度大于n，截取前序列中的前n个数
  - **c**: marker  color, sequence, or sequence of colors, optional
    - A single color format string.
    - A sequence of colors of length n.
    - **A scalar or sequence of n numbers** to be mapped to colors using *cmap* and *norm*.
    - **A 2-D array** in which the rows are RGB or RGBA.If you want to specify the same RGB or RGBA value for all points, use a 2-D array with a single row. 
  - **Alpha**:透明度，scalar
  - **edgecolors**：点的边缘的颜色，{'face', 'none', *None*} or color or sequence of color,    
  - **linewidths**：点的外圈（边缘）的线条的宽度，线条的颜色为edgecolors指定的颜色，scalar or array-like
  - 总结一下，上述参数大部分都可以用scalar或者array来输入，用scalar表示所有的点都一样，用array表示每一个点的特点有array中对应元素指定，也就导致了如果用array需要和点的个数相同

### 气泡图

设置气泡图的关键在于设置`alpha` ，`marker size` ，透明度小于1，marker size 要变化（array like）



通过散点图（or 气泡图） 可以显示4个维度的信息

- 位置（x，y）
- 颜色
- 大小
- 在点上加上文字



### 凸包

- 包围一组散点的最小凸边形
- 凸边形：没有任何一个内角是**优角**（Reflexive Angle）
  - 优角：大于180 ，小于360

- 绘制凸包主要用到了`plt.polygon()`函数

- `ply.polygon(xy,alpha,color,facecolor,edgecolor,linewidth,linestyle)` 
  - xy 为多边形的点，为N*2的array
  - alpha 透明度
  - color 可以同时设置edgecolor和facecolor 
  - facecolor 多边形颜色(内部)
  - edgecolor 多边形边界线颜色
  - linewidth  多边形边框宽度
  - linestyle 多边形边框样式，{'-', '--', '-.', ':', '', (offset, on-off-seq), ...}



## 最佳拟合线(the line of the best fit)

- `seaboard.lmplot(x,y,data,hue,height,aspect,legend,palette,col,col_wrap,scatter_kws)`
  - Datas 是 dataframe对象
  - x,y,hue 为string，hue为scatter的label，也就是dataframe中对应列的名字
  - height 图像的高度
  - aspect 图像的纵横比，也就是长度/高度
  - legend 是否显示图例
  - palette colormap，matplotlib内建的colormap，通过string传入
  - Scatter_kws 对于scatter的设置，dict，比如`{s=12,linewidths=12,edgecolors='b'}`
  - col : string，按照dataframe中该string对应的列进行分类绘制图像，一个类别使用一张图，一张图绘制一条最佳拟合线
  - col_wrap 当分类(使用col)绘制时，限制每行绘制的图像数目



## 抖动图

- x,y位置相同的点，在绘图时，会被覆盖
- 抖动图可以让点产生一定的抖动，从而解决掉覆盖问题
- `seaboard.stripplot(x,y,jitter,size,ax,linewidth,palette)`
  - x,y 点的x,y坐标
  - Jitter 抖动幅度
  - size 点的尺寸
  - ax 在哪张图上画
  - linewidth 点的外围线宽
  - palette colormap



## 计数图

- 同样为了解决绘图时相同位置的点的覆盖问题
- 相同位置上点的数目越多，点越大
- 实际上，就是计数一下处于同一位置的点的数目，将size设置为数目
- `pat.scatter`





## 直方图

- **直方图和条形图的区别**

  - 条形图中的"条"一般是分开的，而直方图中的“条”一般是没有距离的
  - 条形图的横坐标一般**是分类型变量的不同类别**，纵坐标一般是**这一类别上的值之和或者计数**
  - 直方图的横坐标一般是**某个连续型变量上不同的取值空间**，纵坐标是**这一取值范围内样本的个数之和**
  - 条形图表示不同类别下的取值，核心是对比不同类别下的取值的差异；直方图表示不同取值区间内含有的样本个数，核心是查看某个变量的分布

- `plt.hist(x,bins,range,density,weights,cumulative,orientation,histtype,color)`
  - x 变量
  - bins 将变量分成多少段，也就是有多少个柱子的分布，根据变量的值将其进行分段
  - range： 直方图横坐标显示的范围
  - density ：True表示纵坐标为概率密度的值，False表示纵坐标为计数
  - cumulative： True表示直方图进行累积显示，也就是相当于累积分布图
  - orientation : 直方图的方向 'vertical' or 'horizontal'
  - histtype：直方图的类型
  - 'bar' 传统类型的直方图，如果给出多个数据，则条并排排列

  - 'barstacked' : 堆叠直方图，其中多个数据堆叠在一起
    - 'step'：生成一个默认未填充的线条轮廓
    - 'stepfilled'：生成一个默认填充的线条轮廓
  - color 柱子的颜色，如果是堆叠的，color可以是array-like
  - 返回n(shape = bins)，bins(shape=bins+1)
  - n 表示在每个bin内的计数
    - bins 表示每个bin的起止点
  - patches  a list of patch objects
      - 实际上直方图是有许多patch构成的，每一个柱子都是一个patch
  - orientation 直方图的方向 'vertical' 'horizontal'
  - stacked: 设置是否堆叠
  - align 'mid' 'left' 'right' 每个柱子与底部坐标的对齐方式

## 箱线图

- 用来表示变量分布
- 更着重于观察**重要分割点**
  - 异常值
  - 箱线图认可的最大值  min(上四分位数+1.5*四分位距，数据实际的最大值)
  - 上四分位数 Q3
  - 中位数 
  - 下四分位数 Q1 
  - 箱线图认可的最小值 max(下四分位数-1.5*四分位距，数据实际的最小值)
    - 四分位距：上四分位数 - 下四分位数
  - 异常值
- `sns.boxplot(x, ax, orient,meanline,color)`
  - x : 绘制的变量
  - ax ： 在哪张axes上绘制
  - orient 箱线图的方向 'v' or 'h'
  - meanline 是否显示均值线
  - color 箱线图的颜色





## 相关性矩阵图

- 将相关矩阵绘制出来

- 本质上是一个热力图
- `sns.heatmap(data,cmap,center,ax,annot)`
  - data 相关性矩阵
  - colormap 最好选择diverging Colomap
  - colormap 颜色中心对应的值
  - annot 设置为True，则在热力图的每个单元写入数据   

## 成对分析图

- 横坐标为不同特征时，显示两个特征之间的相关性图像
- 横坐标为相同特征时，显示这个特征的自身分布图
- `sns.pairplot(data,hue,kind)`
  - data: pd.dataframe
  - hue: 类别 category
  - Kind :reg or scatter，reg是带有回归线的，scatter不带回归线
- 当希望探索不同分类下的特征之间的相关性时，用成对分析图
- 当特征很多的时候，使用相关性矩阵图，当特征比较少或者数据较少的时候，使用成对分析图



# 偏差图

- 单个特征中的所有值与特定值之间的关系图，反映的是所有值偏离特定值的距离
- 什么时候需要
  - 探索某一特征的分布，探索该特征偏离某个特定值（均值，方差）的程度



## 发散型条形图

- `plt.hlines(y,xmin,xmax,colors='k',linestyles='solid',label='',*,data=None,**kwargs,)`
  - y : y轴的索引，指定每一个条的位置（这里的条实际上就是line）
  - xmin : 每行的开头
  - xmax：每行的结尾
  - colors: array like（独立指定每一个条的颜色） or scalar（指定所有条的颜色）
  - linestyle: 线条的类型 {'solid', 'dashed', 'dashdot', 'dotted'}
  - **kwargs：指定线条（line)的其他参数，比如alpha，linewidth等等
- 同样有`plt.vlines` 用法相同



## 发散型文本图

- 在发散型条形图上写上对应的num
- `plt.hlines` + `plt.text`



## 发散型包点图

- 本质上是scatter
- `plt.text` + `plt.scatter`



## 带标记的发散型棒棒糖图

-  `plt.hlines` +  `plt.scatter` + `ax.annotate` + `patches.Rectangle` + `plt.text`
-  只画棒棒糖图
   -  `plt.hlines` +`plt.scatter` + `plt.text`



## 面积图

- 对轴和线之间的区域进行着色

- `ax.fill_between(x,y1,y2,where,interpolate,**kwargs) ` 对两条曲线之间的区域进行着色

  - x 曲线的x坐标

  - y1,y2  两条曲线的y坐标

  - where：筛选要填充的区域

  - interpolate:交叉点位置的填充

  - **kwargs ：任何patches.polygon对象可以设置的属性都可以传进来


# 排序图

- 比较变量的大小



## 柱状图

- `ax.vlines(x,ymin,ymax,colors,linestyles,label,**kwargs)`
  - x 横坐标
  - ymin 条形图在y轴上的起点
  - ymax 条形图在y轴上的最上边
  - colors: array-like(length = len(x))  or scalar-like
  - linestyles: {'solid', 'dashed', 'dashdot', 'dotted'} 画柱状图一般用`solid`
  - **kwargs：本质上仍然画的是线，所以可以设置line2d的属性都可以传进来
    - 在画柱状图时常用linewidth



## 棒棒糖图

- 实质上和上面所说的发散型棒棒糖图是一个东西，只不过是移动一下

## 包点图

- 实际上和上面说的发散型包点图是一个东西，只不过是移动一下



## 坡度图

- 对比两种不同类型下取值，适合比较给定的人/项目/数据的“之前”和“之后”的位置和变化

- `matplotlib.lines.Line2D(x,y,marker, markestyle,.....)` 用于连接一连串的点

  - x 要连接的点的横坐标，array-like
  - y 要连接的点的纵坐标,，array-like
  - 其余的参数为为设置line2d的属性，比如color，linestyle，linewidth等，[更多的看这里](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.lines.Line2D.html?highlight=line2d#matplotlib.lines.Line2D)
  - 本质上和`plt.plot`没有区别

  - marker和markersize用来设置连接两点的线段的两个端点的marker style
    - 如果要连接多个点，那么连接每相邻两个点的线段都会有marker
    - 无论连接多少点，始终是一条线
  - **注意：想要连接两个点，必须先用scatter绘制出这两个点**
  - 返回一个`matplotlib.lines.Line2D`对象
  - 之后通过`ax.add_line(l)` 来显示该line

# 分布图

- 查看多组数据分布之间的不同



## 连续变量直方图

- 显示一个给定变量的频率分布
- 堆积变量直方图：显示多个变量的频率分布
  - `plt.hist  `设置 stacked=True，传入的data是一个二维list，其中的每一个元素代表一个变量的分布，color可以设置为array-like



## 分类变量直方图

- 显示每个变量的频率分布



# 密度图

- 对于连续变量，显示其概率密度分布
- 实际上和直方图很像，只不过密度图更光滑
- 大多数密度图使用的是核密度估计
- `sns.kdeplot(data,shade,vertical, bw, kernel,color,alpha,**kwargs)`
  - data 数据集 可以是一个也可以是两个
  - shade 在密度曲线下加上阴影
  - vertical 控制密度曲线的轴向，为true时为水平轴向
  - bw 类似于直方图中的binwidth，用于确定核的大小
  - kernel 核函数（双变量只能用高斯核）
    - gau 高斯核
    - cos cosine 余弦核
    - biw biweight 四次核
    - epa 抛物线
    - tri 三角
    - triw 三次
  - **kwargs 可以传入line2d的属性
  - 本质上画的还是一条线，只不过可以设置是否填充和轴之间的部分

## 直方密度曲线图

- `sns.displot(data, bins, hist, kde, hist_kws, kde_kws)`
  - data 绘制图形的数据
  - bins 直方图参数，把数据分成多少个bin
  - hist 控制直方图是否显示 True or False
  - kde 控制密度图是否显示 True or False
  - hist_kws 直方图的其他控制参数 dict
  - kde_kws 密度图的其他控制参数 dict
- 同时显示密度图和直方图



## Joyplot

- 允许不同组的密度曲线重叠，可视化大量分组数据的彼此关系分布的方法
- `pip install joypy`
- `joypy.joyplot(data, column=None, by=None, grid=False, xlabelsize=None, ylabelsize=None, xrot=None,yrot=None,hist=False, fade=False, ylim=max, fill=True, linecolor=None,title)`
  - data 绘图的数据集 pd.dataframe 或者 其他嵌套集合
  - column 使用data中的有限(某些)列进行绘图
  - by 分组列
  - grid 添加网格线
  - xlabelsize x轴标签大小
  - ylabelsize y轴标签大小
  - xrot x轴刻度标签旋转角度
  - yrot y轴刻度标签旋转角度
  - hist 是否显示直方图
  - fade True表示显示渐变色
  - ylim 共享y轴刻度
  - fill 曲线下的填充颜色
  - linecolor 曲线颜色
  - overlap 控制y轴刻度之间的重叠部分，值越小重叠越大
  - title 图形的标题

## 分布式包点图

- 可以显示按组划分的点的分布情况，点的颜色越暗说明该区域的点集中度越高
- `plt.scatter` + `plt.hlines`



# 组成图

## 华夫饼图

- `pip install pywaffle`

- pywaffle包： 配合matplotlib绘制华夫饼图

- ```python
  from pywaffle import Waffle
  data = {'Democratic': 50, 'Republican':30, "Libertarian":10}
  fig = plt.figure(
          figsize=(8,3),
          values=data, 
          FigureClass=Waffle, # 绘制华夫饼图
          rows = 5, # 华夫饼图有多少行
          colors=("#E22882", "#983D3D", "#DCB732"), # 每一类的颜色
          legend = {'loc':'upper left',  # 控制legend的位置
                   'bbox_to_anchor':(1,1)
                   }
  )
  ```

- *这里着重看一下ipynd文件里的用法示例*

- 二分类华夫饼图：KPI

  - ![](images/Waffle-Chart-in-Excel-Example.png)

- 什么时候不建议使用华夫饼图

  - 当对整体有贡献的类别太多的时候，华夫饼图能够展现的组成情况有限  
  - 测量的KPI或者总贡献可以超过100%时  
  - 华夫饼展现出“大概的比例”，当精确的占比（比如百分比数量）非常重要的时候，必须借助文字帮助

## 饼图

- `ax.pie(x,autopct,explode,colors,startangle)`
  - x 绘制饼图的数据，每个类别的计数
  - autopct 设定写在扇叶上的百分比，默认为None，可以输入字符串，函数或者None
  - explode  scalar or array-like ,表示扇叶之间的距离
  - colors  array-like 扇叶的颜色
  - startangle 第一瓣扇叶从什么角度开始，float or int
  - 返回
    - wedges ：list of `patches.wedge` 代表扇形图中的所有扇叶对象
    - texts 扇叶的位置
    - autotexts：当autopct不为None时，表示扇叶上的text对象

## 树形图

- `pip install squarify`
- `scarify.plot(sizes, color, label, ax, text_kwargs, bar_kwargs,**kwargs)`
  - sizes 也就是要绘图的数据
  - color ：color string or array-like 表示每一块的颜色
  - label  ：array-like 表示在每一块上加的text 
  - text_kwargs  设置text的属性
  - bar_kwargs 设置bar的属性
  - **kwagrs : Any additional kwargs are merged into `bar_kwargs`.



## 条形图

- 可以对比多类别下各种类别的数量关系

- 无法看到各个类别占总量的类别关系

- `plt.bar(x, height, width, bottom, align,color)`
  - x 横坐标
  - height 实际上也就是纵坐标（bar的高度
  - width scalar or array-like bar的宽度 , 0~1
  - align : {'center', 'edge'}
  - color : scalar or array-like 每个bar的颜色
  - 

