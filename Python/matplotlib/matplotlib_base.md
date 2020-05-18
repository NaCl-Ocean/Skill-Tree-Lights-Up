# 前引

- figure
  - 用来展示图的窗口
  - 一个figure中可以有多个axes，但是axes只能在一个figure中
- Axes
  - 空间（坐标系），二维坐标系，三维坐标系
  - 所有的绘图都是在对Axes对象进行操作
- axis
  - 坐标轴
  - 设置边界，并生成tick(刻度)和ticklabe(标记刻度的字符串)
- Artist
  - 所有可以在axes上画的都是Artist，比如line，point，text等，实际上figure，axes也是Artist对象，但是比较特殊，单列出来

- 输入最好的`numpy.array`
- 画图有两种方式
  - 创建figure对象和axes对象，进行面向对象的操作(prefer)
  - 直接使用`pyplot.plot`
- ![matplotlib基本概念图示](https://matplotlib.org/3.2.1/_images/anatomy.png)
- **matplotlib的两种模式**
  - 交互模式
    - `plt.ion()`  打开交互模式
    - 在交互终端运行时，可以实时显示图像，画图的操作会实时显示到图像窗口
    - IDE以及Ipython  默认模式为交互模式
    - `plt.plot(x)`或`plt.imshow(x)`直接出图像，不需要`plt.show()`，之后绘图的操作实时显示到图像窗口，也可以`plt.draw()`
  - 非交互模式
    - `plt.ioff()` 关闭交互模式，打开非交互模式
    - 当使用`plt.show()`时，才打开一个图像窗口，呈现绘图，`plt.show()`之后的代码只有在关闭该图像窗口之后才可以运行
    - 在终端运行py文件时，默认为非交互模式
  - pycharm比较特殊，当以非交互模式运行时，绘图会在view窗口中显示，不会影响`plt.show()`之后的代码运行
- **后端(backend)**
  - 前端就是我们写的代码，后端就是负责显示图形的底层代码
  - **non-interactive backends**
    - 负责如何存储绘图文件，如png，pdf
    - ![render list](http://image.haiyang1218.cn/images/matplotlib_render.png)
    - **vector graphics**   矢量图
    - **raster graphics**  栅格图，以像素进行渲染
  - **interactive backends**
    - 如何显示图形到屏幕
    - ![backend list](http://image.haiyang1218.cn/images/matplotlib_backend.png)



# Artist基本对象

上述Artist对象是我们绘图时所重点关注的，分为两种

- **Primitives** ：也就是**line2D**，**AxesImage**，**patch**等

  - 通过Axes对象建立，例`axes.plot()`创建一个Line2D对象

  - 相同类型的Primitives对象以列表的形式存放在axes对象的对应属性中，如`axes.lines`也就包含着axes绘制的所有Line

    - 那么相应地，既然是个列表，那么其中的元素是否可以删去，答案是可以的，删去后自然该axes不显示对应的line了

  - 所有的Primitives对象都有以下属性

    - ![](http://image.haiyang1218.cn/images/matplotlib_artist_pro.png)

    - 这些属性一般是私有属性，不建议直接`object.__property`来修改，一般通过getter来查看，通过setter来设置

    - ```python
      label = line.get_label()
      line.set_label('line')
      line.set(label='line',visible=False)  # 同时设置多个属性
      ```

      

- **Containers**：也就是**Axis**，**Axes**，**Figure**

- **总体来说matplotlib中基本对象存在着层级关系。**

  ![container object](http://image.haiyang1218.cn/images/matplotlib_container.png)

## Figure

- **Top level container**
- **更加focus的是用来存放Axes，通过Figure的help function来建立Axes或者删除Axes**
  - 一个Figure可以有多个Axes
- ![Figure attribute](http://image.haiyang1218.cn/images/matplotlib_figure_pro.png)
- 背景是Rectangle对象

## Axes

- 创建的Axes对象以列表的形式存放在`figure.axes`中

- 背景是Rentangle对象或者Circle对象

- 通常更关注的是通过helper function来创建Artist对象，之后通过该Artist对象来具体设置该对象的一些性质

- $$\begin{array}{lll}
  \hline
   \text { Helper method } & \text { Artist } & \text { Container } \\
    \hline \text { ax.annotate - text annotations } & \text { Annotate } & \text { ax.texts } \\
    \hline \text { ax.bar - bar charts } & \text { Rectangle } & \text { ax.patches } \\
    \hline \text { ax.errorbar - error bar plots } & \text { Line2D and } & \text { ax.lines and ax.patches } \\
    & \text { Rectangle } & \\
    \hline \text { ax.fill - shared area } & \text { Polygon } & \text { ax.patches } \\
    \hline \text { ax.hist - histograms } & \text { Rectangle } & \text { ax.patches } \\
    \hline \text { ax.imshow - image data } & \text { Axesimage } & \text { ax.images } \\
    \hline \text { ax.legend - axes legends } & \text { Legend } & \text { ax.legends } \\
    \hline \text { ax.plot - xy plots } & \text { Line2D } & \text { ax.lines } \\
    \text { ax.scatter - scatter charts } & \text { PolygonCollection } & \text { ax.collections } \\
    \hline \text { ax.text - text } & \text { Text } & \text { ax.texts } \\
    \hline
    \end{array}$$

  

- $$\begin{array}{ll}
\hline
  \text { Axes attribute } & \text { Description } \\
  \hline \text { artists } & \text { A list of Artist instances } \\
  \hline \text { patch } & \text { Rectangle instance for Axes background } \\
  \hline \text { collections } & \text { A list of Collection instances } \\
  \hline \text { images } & \text { A list of Axesimage } \\
  \hline \text { legends } & \text { A list of Legend instances } \\
  \hline \text { lines } & \text { A list of Line2D instances } \\
  \hline \text { patches } & \text { A list of Patch instances } \\
  \hline \text { texts } & \text { A list of Text instances } \\
  \hline \text { xaxis } & \text { matplotlib.axis. XAxis instance } \\
  \hline \text { yaxis } & \text { matplotilib.axis. YAxis instance } \\
  \hline
  \end{array}$$
  
  

## Axis

- 用来设置axis label，tick line，tick label，grid lines

- $$\begin{array}{ll}
  \hline
  \text { Accessor method } & \text { Description } \\
  \hline \text { get_scale } & \text { The scale of the axis, e.g., "log' or "linear' } \\
  \hline \text { get_view_interval } & \text { The interval instance of the axis view limits } \\
  \hline \text { get_data_interval } & \text { The interval instance of the axis data limits } \\
  \hline \text { get_gridlines } & \text { A list of grid lines for the Axis } \\
  \hline \text { get_label } & \text { The axis label - a Text instance } \\
  \hline \text { get_ticklabels } & \text { A list of Text instances - keyword minor=True|False } \\
  \hline \text { get_ticklines } & \text { A list of Line2D instances - keyword minor=True|False } \\
  \hline \text { get_ticklocs } & \text { A list of Tick locations - keyword minor=True|False } \\
  \hline \text { get_major_locator } & \text { The matplotlib.ticker.Locator instance for major ticks } \\
  \hline \text { get_major_formatter } & \text { The matplotlib.ticker.Formatter instance for major ticks } \\
  \hline \text { get_minor_locator } & \text { The matplotlib.ticker.Locator instance for minor ticks } \\
  \hline \text { get_minor_formatter } & \text { The matplotlib.ticker.Formatter instance for minor ticks } \\
  \hline \text { get_major_ticks } & \text { A list of Tick instances for major ticks } \\
  \hline \text { get_minor_ticks } & \text { A list of Tick instances for minor ticks } \\
  \hline \text { grid } & \text { Turn the grid on or off for the major or minor ticks }\\
  \hline
  \end{array}$$

  

- 从上面看，可以看到一个层级关系，每一层都相当于为一层提供一个接口，用来返回相应的对象。

## Tick

- 注意：axis只有xaxis和yaxis，但是tick是四条边都算在内的
- $$\begin{array}{ll}
  \hline \text { Tick attribute } & \text { Description } \\
  \hline \text { tick1line } & \text { Line2D instance } \\
  \hline \text { tick2line } & \text { Line2D instance } \\
  \hline \text { gridline } & \text { Line2D instance } \\
  \hline \text { label1 } & \text { Text instance } \\
  \hline \text { label2 } & \text { Text instance } \\
  \hline
  \end{array}$$
- 
- 这里的tick1line，tick2line以及label1，label2也就是每个axis对应的两条边

```python
fig = plt.figure()
# figure->axes
ax = fig.add_axes([0.2,0.2,0.5,0.5])
# axes->line
line_1, = ax.plot([1,2,3],[4,5,6],linestyle = '-',visible = 'False',marker='.',
                    markeredgecolor = 'g',markeredgewidth = 4)
line_1.set_label('test')
# axes->axis
yaxis = ax.yaxis
xaxis = ax.xaxis
# axis->tick
for tick in yaxis.get_major_ticks():
    tick.label1.set_visible(True)
    tick.label2.set_visible(True)
    tick.tick1line.set_visible(True)
    tick.tick2line.set_visible(True)

for tick in xaxis.get_major_ticks():
    tick.label1.set_visible(True)
    tick.label2.set_visible(True)
    tick.tick1line.set_visible(True)
    tick.tick2line.set_visible(True)
plt.show()
```



# Legend

- 基本概念

  - **legend entry**  ：也就是图例条目，一个图例中可以包含多个图例条目，每个图例条目由**legend key**和**legend label**组成

  - **legend handle**：可以用来生成legend entry的artist对象，也就是说会自动根据legend handle的属性生成对应的lengend entry

  - ```python
    line_1, = ax.plot([1,2,3],[4,5,6],linestyle = '-',visible = 'False',marker='.',
                        markeredgecolor = 'g',markeredgewidth = 4)
    line_2, = ax.plot([1,2,3],[6,5,4],linestyle='--')
    # line_1,line_2即为legend handle
    ax.legend([line_1,line_2],['test_1','test_2'])
    ```

  - <img src="F:\about study\07其他\Skill-Tree-Lights-Up\Python\legend_object.png" width="400px" />

- **创建Legend对象的方法**

  - `axes.legend()` 不传参数，会寻找axes中可以生成legend entry的所有handler（需要有label），并转为legend entry进行显示

  - 指定要显示的handler，如上所示

  - 自定义artist对象，可以不在axes中

  - 通过handler map

    - 根据handler创建legend entry实际上是将handler映射为对应的handlerbase对象。

    - 那么也就引申出了handler map，可以将某个handler映射为某个handlerbase对象，也可以将某一类handler映射为某个handlerbase对象，映射为的handlerbase对象继承到handler的属性

    - ```python
      from matplotlib.legend_handler import HandlerLine2D
      # 将某一个handler映射为Handlerbase
      ax.legend(handler_map={line_1:Handlerline2D(numpoints=4)})
      # 将某一类handler映射为Handlerbase
      ax.legend(handler_map={type(line_1):Handlerline2D(numpoints=4)})
      ```

  - 通过handler tuple

    - 将多个handler合并为一个handler，lable需指定，这些handler的key一层层地绘制，成为新的handler的key。

    - ```python
      legend = ax.legend([(line_1,line_2)],['test'],loc='upper right',bbox_to_anchor=(0.6,1))
      ```

    - <img src="C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200516124811048.png" alt="image-20200516124811048" style="zoom:70%;" />

- Legend的位置

  - loc：在bbox中的位置，有'upper right'，'lower left'，'best'（选择legend不被axes中artist对象遮挡的最佳位置，也就是IOU最小的位置）等等

  - bbox_to_anchor：默认为axes.bbox，也就是整个axes的背景，2-tuple为(x,y)，4-tuple为(x,y,width,height)

  - ```python
    legend = ax.legend([line_1,line_2],['test_1','test_2'],
                       loc='upperright',bbox_to_anchor=(0.6,1))
    ```

- 创建多个Legend

  - ```python
    legend_1 = ax.legend([(line_1,line_2)],['test'],loc='upper right',bbox_to_anchor=(0.6,1))
    legend_1.set_label('legend_1')
    # 手动将legend添加到axes的artist中
    ax.add_artist(legend_1)
    legend_2 = ax.legend([line_2],['test_2'])
    ```

  - **需要将legend手动添加到axes中**，否则只会显示最后的legend



# Figure layout

- 布局Figure中的axes

- 在这里focus到**gridspec**

- **创建跨越行和列的子图**

  - **先通过`add_gridspec`创建gridspec对象**

  - **之后通过`add_subplot`传入gridspec切片，创建subplot**

  - ```python
    gs = fig3.add_gridspec(3, 3)
    f3_ax1 = fig3.add_subplot(gs[0, :]) # 切片操作
    f3_ax1.set_title('gs[0, :]')
    f3_ax2 = fig3.add_subplot(gs[1, :-1])
    f3_ax2.set_title('gs[1, :-1]')
    f3_ax3 = fig3.add_subplot(gs[1:, -1])
    f3_ax3.set_title('gs[1:, -1]')
    f3_ax4 = fig3.add_subplot(gs[-1, 0])
    f3_ax4.set_title('gs[-1, 0]')
    f3_ax5 = fig3.add_subplot(gs[-1, -2])
    f3_ax5.set_title('gs[-1, -2]')
    ```

  - <img src="https://matplotlib.org/3.2.1/_images/sphx_glr_gridspec_003.png" style="zoom:67%;" />

- **创建定制宽高比的子图**

  - 这里主要讲的是比例，因此成比例扩大widths与heights中的值是不会影响布局的

  - ```python
    widths = [2, 3, 1.5]
    heights = [1, 3, 2]
    spec5 = fig5.add_gridspec(ncols=3, nrows=3, width_ratios=widths,
                            height_ratios=heights)
    ```

  - <img src="https://matplotlib.org/3.2.1/_images/sphx_glr_gridspec_005.png" style="zoom: 67%;" />



- 结合subplots

  - ```python
    fig7, f7_axs = plt.subplots(ncols=3, nrows=3)
    # 获取当前figure中的gridspec对象
    # 通过任何一个子图获取到的gridspec对象都是相同的
    gs = f7_axs[1, 2].get_gridspec()
    # remove the underlying axes
    for ax in f7_axs[1:, -1]:
        ax.remove()
    axbig = fig7.add_subplot(gs[1:, -1])
    ```

- **subgridspec**

  - ```python
    fig10 = plt.figure(constrained_layout=True)
    gs0 = fig10.add_gridspec(1, 2)
    
    gs00 = gs0[0].subgridspec(2, 3)
    gs01 = gs0[1].subgridspec(3, 2)
    ```

    

# Transform

- ![Transform](http://image.haiyang1218.cn/images/matplotlib_transform.png)

- Transform实际上是一种坐标系的映射，将一个坐标系上的点映射到另一个坐标系（display)上。不论怎样，画图我们是要显示在屏幕上的，如何决定一个元素在屏幕上(display)的位置也就是transform要做的事。我们也可以把transform当作一个函数（实际上它们都是对象），比如`fig,transAxes`  ，`ax.transAxes.transform((0.5,0.5))->[328.  237.6]`，也就是输入本坐标系下点的坐标，返回其在'display'坐标系下的坐标，也就是最根本的坐标系（屏幕显示）是'display'坐标系，但是该坐标系我们通常不需要关注。

- `xaxis`  我们都知道在二维坐标系下，表示一个点的位置用(x,y)来表示。对于`ax.get_xaxis_transform()`来说，x对应着`ax.transData`，而y对应着`ax.transAxes`。`yaxis`相反。

  - ```python
    from matplotlib import transforms
    fig,ax = plt.subplots(1,1)
    x = np.random.randn(1000)
    ax.hist(x, 30)
    # x=1,width=1，y=0.height=1
    rect = mpatches.Rectangle((1, 0), width=1, height=1,
                             transform=ax.get_xaxis_transform(), color='yellow',
                             alpha=0.5)
    
    ax.add_patch(rect)
    ```

  - ![image-20200518152331916](https://matplotlib.org/3.2.1/_images/sphx_glr_transforms_tutorial_005.png)

- 一种transform pipeline

  - `transofrm_a+transform.ScaledTranslation(x_offset,y_offfset,transoform_b)` 

  - 首先在transform_a中绘制相应元素，之后根据x_offset 与 y_offset在transoform_b中进行偏移

  - ```python
    xdata, ydata = (0.2, 0.7), (0.5, 0.5)
    ax.plot(xdata, ydata, "o")
    ax.set_xlim((0, 1))
    
    trans = (fig.dpi_scale_trans +
             transforms.ScaledTranslation(0.2, 0.5, ax.transData))
    
    # 首先在dpi_scale_trans中绘制一个圆心位于(0,0)，150*130 points大小的圆，之后将该圆平移到ax.transData下(0.2,0.5)圆心的位置  --》(0+0.2,0+0.5)=(0.2,0.5)
    circle = mpatches.Ellipse((0, 0), 150/72, 130/72, angle=40,
                              fill=None, transform=trans)
    ax.add_patch(circle)
    plt.show()
    ```

    



# Color

##  颜色格式

- an RGB or RGBA (red, green, blue, alpha) **tuple** of **float** values in closed interval `[0, 1]`，eg:`(0.5,0.5,0.5)`
- a hex RGB or RGBA **string** ，eg：'0f0f0f'
- one of {'b'(blue), 'g'(gray), 'r'(red), 'c'(cyan), 'm'(magenta), 'y'(yellow), 'k'(black), 'w'(white)}
- css4/x11 color name（**string**)
- xkcd color name（**string**)  eg：'xkcd:gold'
  - 上述两种实际上是对于颜色的一个命名
  - [颜色差异对比or查表](https://matplotlib.org/3.2.1/_images/sphx_glr_colors_003.png)



## colormap

- colormap实际上是一个table（or array），大小为N*4（or N\*3)，也就是通过索引将数值映射为颜色

- colormap要做的事是输入一个[0,1]的值，然后插值为索引，找到对应的颜色

- **Listedcolormap对象**

  - 创建listedcolormap

    - `ListedColormap(list,name)`  name为colormap的名字，list中的元素为matolotlib中的颜色格式，自定义listcolormap，这样的colormap有`len(list)`种颜色

    - `cm.get_cmap(name,len)`   matplotlib中内置的colormap，name为colormap的名字，将原colormap压缩为len长，比如原colormap的len为512，传入256，下采样为256长。

    - 从已有的colormap中创建 

      - ```python
        cmap = cm.get_cmap('viridis',512)
        # 实际上可以看作缩小了色彩的动态范围
        new_cmap = ListedColormap(cmap(np.linspace(0.25,0.75,256)))
        ```

  - 操作listedcolormap

    - 推荐通过numpy.array来操作

    - ```python
      (new_cmap(np.linspace(0,0.5,128)))   -->输出为list
      ```

- **linear segmented colormap对象**

  - listedcolormap均匀地将一个[0,1]的数映射为index，linear segmented colormaps 非均匀映射

  - 格式：

    - ```
                          x     y0   y1
      cdict = {'red':   [(0.0,  0.0, 0.0),
                         (0.5,  1.0, 0.5),
                         (1.0,  1.0, 1.0)],
      
               'green': [(0.0,  0.0, 0.0),
                         (0.25, 0.0, 0.5),
                         (0.75, 1.0, 1.0),
                         (1.0,  1.0, 1.0)],
      
               'blue':  [(0.0,  0.0, 0.0),
                         (0.5,  0.0, 0.3),
                         (1.0,  1.0, 1.0)]}
      'red','green','blue'以及'alpha'(optional),也就对应着RGB or RGBA                   每一列的格式为(x,y0,y1),其中每个分量的x必须布满[0,1]，每个分量的值单独进行寻找
      算法步骤：
      	input z
      	for channel in ['red','green','blue']:
      		if x[i] < z < x[i+1]:
      			channel = linearly interpolated between y1[i] and y0[i+1]
      eg: if z = 0.4,则'red'分量映射到[0.0,1.0],'green'分量映射到[0.5,1.0],'blue'分量映射到[0.0,0.0]
      ```

  - 创建linear segmented colormap

    - `LinearSegmentedColormap(name, segmentdata)` ，segmentdata也就是上述的cdict，必须要'red'，'green'，'blue'字段，可选'alpha'字段。

    - `LinearSegmentedColormap.from_list(name,colors,N=256)` Make a linear segmented colormap with *name* from a sequence of *colors* which evenly transitions from colors[0] at val=0 to colors[-1] at val=1. *N* is the number of rgb quantization levels.

    - ```python
      LinearSegmentedColormap.from_list(['black','cyan','ivory'])
      ```

##  Normalize

  - 从上面可以知道，colormap只接收[0,1]的值，小于0取0，大于1取1，那么如何取到更大的范围？  Normalize
  - Normalize将[vmin,vmax]的值映射到[0,1]（归一化），之后colormap用这个[0,1]的值取得相应的颜色
  - **LinearNormalize对象**
    - $x^* = \frac{x-x_{min}}{x_{max}-x_{min}}$ 
    - `colors.Normalize(vmin,vmax,clip=False)` ，若clip为True，则超出范围的取0或者1，取决于哪个距离更近
  - **LogNormalize对象**
    - $x^* = \frac{log(x)-log{x_{min}}}{log(x_{max})-log(x_{min})}$
    - `colors.LogNorm(vmin,vmax,clip)`，默认采用$log_{10}$
  - **BoundayNorm对象**
    - `colors.BoundaryNorm(boundaris,ncolors)`  映射到[0，ncolors-1]
  - **symmetric log对象**

# Text

![Text 总览](http://image.haiyang1218.cn/images/matplotlib_text.png)

 

## Text的属性

- | font 属性   | 可用参数                                                     |
  | ----------- | ------------------------------------------------------------ |
  | fontsize    | { 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' }或者数字（整数大于0） |
  | fontstyle   | {'normal', 'italic' , 'oblique'} 正常or斜体                  |
  | fontfamily  | ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']，一个列表，[参考释义](https://baike.baidu.com/item/font-family/7529050?fr=aladdin) |
  | fontweight  | {'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}或者大于的整数 |
  | fontvariant | {'normal','small-caps'}，'small-caps'所有字母为大写字母，'normal'设置首字母大写 |

  - **注意：设置字体的familt或者name时，需要先将字体添加到rcParams中**

  - ![Font](http://image.haiyang1218.cn/images/matplotlib_font.png)

  - ```python
    matplotlib.rcParams['font.family'].append('serif')
    ```

  - 上述字体属性同样可以通过 **FontProperties** 来完成，[fontproperites](https://matplotlib.org/3.2.1/api/font_manager_api.html#matplotlib.font_manager.FontProperties)

- | location 属性       | 含义                                                         |
  | ------------------- | ------------------------------------------------------------ |
  | x，y                | float 标记boundingbox的位置（在axes中的位置）                |
  | verticalalignment   | {'center','top','bottom','baeline'}，标记text与boundingbox竖直对齐方式 |
  | horizontalalignment | {'center','right','left'}，标记text与boundingbox水平对齐方式 |
  | multialignment      | {'left','right','center'}，标记text各行的对齐方式            |
  | rotation            | {'vertical','horizontal'}或者旋转角度                        |

- | 其他  | 含义                                   |
  | ----- | -------------------------------------- |
  | text  | string                                 |
  | color | 符合color格式要求的任意string 或者其他 |

- `text(x,y,str,*kwargs)`可以在axes的任何地方加上text，kwargs接收任意text的属性

## xlabel/ylabel

- `axes.set_xlabel(string,**kwargs)`   `axes.set_ylabel(string,**kwargs)`

- 可以接收上述text中的任何属性（以关键字参数的形式传入）,但是注意一些属性不会按照你想要的方式奏效

- `labelpad`  label特有的关键字参数，改变label到axis的距离

- ```
  axes.set_xlabel('time',color='b',)
  ```

## Titles

- `axes.set_title(string,**kwargs)`  
- 可选的关键字参数
  - `loc`  ['center','left','right']，[loc参考](https://matplotlib.org/3.2.1/_images/sphx_glr_text_intro_008.png)
  - `pad` 大于0的整数，改变title到axis的距离

## Tick

-  一些基本概念：
  - Tick locator：tick label的内容
  - Tick formatter：tick label(str)的格式
  - 也就是说formatter 将locator的内容按照定义的格式进行显示
  - Tick  有major tick和 minor tick
  - nbins ：axes显示多少个间隔，相邻两Tick间为一个bin
-  **Tick locator**
   -  FixedLocator  `FixedLocator(locs,nbins=None) `  ，locs为array格式/list格式	
      - axis上的major tick是一个list，每个元素也就是一个tick，但是不一定会将这些tick都显示出来，若nbins为None，则会选择适合的tick进行显示，比如前6个tick已经包含了要显示的内容，那么就只会显示前6个tick
   -  MaxNLocator   `MaxNLocator(nbins='auto',steps=[1,2,2.5,5,10])`  
      - nbins='auto'，会根据axis的长度与绘图的元素自动选择合适步长，nbins指定时，通过steps选择步长，步长的值为steps中元素的$10^n$倍
   -  设置Locator
      -    `axis.set_major_locator(locator)` 
      -  `axis.set_ticks(array/list)` array中所有的元素（tick）都强制显示
-  **Tick formatter**
   - `matplotlib.ticker.StrMethodFormatter({x:...})`  str.format的格式化用法相似，注意必须有**x**
   - `matplotlib.ticker.FormatStrFormatter(str)`  与`%`格式化用法相似
   -  设置Formatter
      - `axis.set_major_formatter(formatter)`

## annotations

- annotations与text方法不同，会多一个箭头，用以指向要标记的地方

# 参考

[backend参考](http://vra.github.io/2017/06/13/mpl-backend/)

[Artist参考](https://matplotlib.org/tutorials/intermediate/artists.html#sphx-glr-tutorials-intermediate-artists-py)

