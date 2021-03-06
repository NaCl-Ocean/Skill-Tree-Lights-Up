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
  
- 输入最好为`numpy.array`
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
    - ![render list](images/matplotlib_render.png)
    - **vector graphics**   矢量图
    - **raster graphics**  栅格图，以像素进行渲染
  - **interactive backends**
    - 如何显示图形到屏幕
    - ![backend list](images/matplotlib_backend.png)

- **rcparams**

  - Matplotlib.pyplot 显示图形的默认属性

  - 通过`pyplot.rcparams` 可以进行查看

  - 修改

    - `pyplot.rcParams['lines.linewidth'] = 2`

    - ```
      params = {'axes.titlesize':12}
      pyplot.rcParams.update(params)
      ```

    - 也可以使用预设的风格

      - ```python
        pyplot.style.use('seaborn-whitegrid')
        pyplot.style.available # 查看所有风格
        ```

        

# Artist基本对象

上述Artist对象是我们绘图时所重点关注的，分为两种

- **Primitives** ：也就是**line2D**，**AxesImage**，**patch**等

  - 通过Axes对象建立，例`axes.plot()`创建一个Line2D对象

  - 相同类型的Primitives对象以列表的形式存放在axes对象的对应属性中，如`axes.lines`也就包含着axes绘制的所有Line

    - 那么相应地，既然是个列表，那么其中的元素是否可以删去，答案是可以的，删去后自然该axes不显示对应的line了

  - 所有的Primitives对象都有以下属性

    - ![](images/matplotlib_artist_pro.png)

    - 这些属性一般是私有属性，不建议直接`object.__property`来修改，一般通过getter来查看，通过setter来设置

    - ```python
      label = line.get_label()
      line.set_label('line')
      line.set(label='line',visible=False)  # 同时设置多个属性
      ```

      

- **Containers**：也就是**Axis**，**Axes**，**Figure**

- **总体来说matplotlib中基本对象存在着层级关系。**

  ![ ](images/matplotlib_container.png)

## Figure

- **Top level container**
- **更加focus的是用来存放Axes，通过Figure的help function来建立Axes或者删除Axes**
  - 一个Figure可以有多个Axes
- ![Figure attribute](images/matplotlib_figure_pro.png)
- 背景是Rectangle对象

- `pat.gcf()` 获取当前figure

## Axes

- 创建的Axes对象以列表的形式存放在`figure.axes`中

- 背景是Rentangle对象或者Circle对象

- 通常更关注的是通过helper function来创建Artist对象，之后通过该Artist对象来具体设置该对象的一些性质

- `plt.gca()`   获取当前axes

- `ax.grid(which,axis,**kwargs)`  划分grid，根据x轴和y轴的tick将axes划分为网格

  - which : {'major', 'minor', 'both'} 根据x轴和y轴上的哪种tick去划分网格
  - Axis: {'both', 'x', 'y'}  
    - 如果是‘x'，只根据x轴上的tick去划分网格
    - 如果是'y'，只根据y轴的tick去划分网格
    - 如果是`both`，那么根据x轴和y轴上的tick去划分网格
  - **kwargs：设置 line2d 的属性，比如linestyle，alpha，color等

- | Helper method                    | Artist               | Container                 |
  | -------------------------------- | -------------------- | ------------------------- |
  | ax\.annotate \- text annotations | Annotate             | ax\.texts                 |
  | ax\.bar \- bar charts            | Rectangle            | ax\.patches               |
  | ax\.errorbar\-error bar plots    | Line2D and Rectangle | ax\.lines and ax\.patches |
  | ax\.fill \- shared area          | Polygon              | ax\.patches               |
  | ax\.hist \- histograms           | Rectangle            | ax\.patches               |
  | ax\.imshow \- image data         | Axesimage            | ax\.images                |
  | ax\.legend \- axes legends       | Legend               | ax\.legends               |
  | ax\.plot \- xy plots             | Line2D               | ax\.lines                 |
  | ax\.scatter \- scatter charts    | PolygonCollection    | ax\.collections           |
  | ax\.text \- text                 | Text                 | ax\.texts                 |

- | Axes attribute | Description                            |
  | -------------- | -------------------------------------- |
  | artists        | A list of Artist instances             |
  | patch          | Rectangle instance for Axes background |
  | collections    | A list of Collection instances         |
  | images         | A list of Axesimage                    |
  | legends        | A list of Legend instances             |
  | lines          | A list of Line2D instances             |
  | patches        | A list of Patch instances              |
  | texts          | A list of Text instances               |
  | xaxis          | matplotlib\.axis\. XAxis instance      |
  | yaxis          | matplotilib\.axis\. YAxis instance     |
  | spines         | axes的四条轴                           |

## Axis

- 用来设置axis label，tick line，tick label，grid lines

- | Accessor method       | Description                                                |
  | --------------------- | ---------------------------------------------------------- |
  | get\_scale            | The scale of the axis, e\.g\., "log' or "linear'           |
  | get\_view\_interval   | The interval instance of the axis view limits              |
  | get\_data interval    | The interval instance of the axis data limits              |
  | get\_gridlines        | A list of grid lines for the Axis                          |
  | get\_label            | The axis label \- a Text instance                          |
  | get\_ticklabels       | A list of Text instances \- keyword minor=True\|False      |
  | get\_ticklines        | A list of Line2D instances \- keyword minor=True\|False    |
  | get\_ticklocs         | A list of Tick locations \- keyword minor=True\|False      |
  | get\_major\_locator   | The matplotlib\.ticker\.Locator instance for major ticks   |
  | get\_major\_formatter | The matplotlib\.ticker\.Formatter instance for major ticks |
  | get\_minor\_locator   | The matplotlib\.ticker\.Locator instance for minor ticks   |
  | get\_minor\_formatter | The matplotlib\.ticker\.Formatter instance for minor ticks |
  | get\_major\_ticks     | A list of Tick instances for major ticks                   |
  | get\_minor\_ticks     | A list of Tick instances for minor ticks                   |
  | grid                  | Turn the grid on or off for the major or minor ticks       |

- 从上面看，可以看到一个层级关系，每一层都相当于为一层提供一个接口，用来返回相应的对象。

- `ax.invert_yaxis()` 反转y轴，上下反转，也就是说如果原来y轴是在下面的话，反转以后，y轴在上面

- `ax.invert_xaxis()` 反转x轴，左右反转，x轴同理

- `ax.set_ylim(bottom.top)` 设置y轴显示范围

- `ax.set_xlim(bottom,top)`设置x轴显示范围

## Tick

- 注意：axis只有xaxis和yaxis，但是tick是四条边都算在内的

- | Tick attribute | Description     |
  | -------------- | --------------- |
  | tick1line      | Line2D instance |
  | tick2line      | Line2D instance |
  | gridline       | Line2D instance |
  | label1         | Text instance   |
  | label2         | Text instance   |

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
# 在这里x轴显示1，2，3，因此得到了3个tick，
# 这样设计的好处其实就是tick之间相互独立，可以分别去设置，互不影响 
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



# Spines

- 实质上也就是xaxis和yaxis，但是可以用spines去设置xaxis和yaxis的alpha，color等等

- `ax.spines`

  - 是一个orderdict对象

  - ```python
    OrderedDict([('left', <matplotlib.spines.Spine at 0x7fbadb3d6160>),
                 ('right', <matplotlib.spines.Spine at 0x7fbadd348ba8>),
                 ('bottom', <matplotlib.spines.Spine at 0x7fbadd348ef0>),
                 ('top', <matplotlib.spines.Spine at 0x7fbadd348860>)])
    ```

  - 可以很明显看出，分别代表四条边，分别对4个Spine对象进行独立设置，即可以改变图像轴的特点

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

  - <img src="images\legend_object.png" width="400px" />

- **创建Legend对象的方法**

  - `axes.legend()` 不传参数，会寻找axes中可以生成legend entry的所有handler（需要有label），并转为legend entry进行显示

  - `axes.legend(['label1','label2',...]) ` label需要与ax.artist中的对象相对应

  - 指定要显示的handler，如上所示

  - 自定义artist对象，可以不在axes中

  - 通过handler map

    - 根据handler创建legend entry实际上是将handler映射为对应的handlerbase对象。

    - 那么也就引申出了handler map，可以将某个handler map 为某个handlerbase对象，也可以将某一类handler map 为某个handlerbase对象，映射为的handlerbase对象继承到handler的属性

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

    - 当输入为2-tuple时，表示legend的bbox的loc的坐标等于该tuple，比如loc='upper left' ，Bbox_to_anchor=(0.5,0.5)，表示legend的bbox的左上角位于axes的(0.5，0.5)这个位置
    - ![](images/bbox_to_anchor用法2.png)
    - 当输入为4-tuple时，可以通过该tuple在axes中绘制出一个rectangle，此时legend的bbox的loc的坐标等于该rectangle的loc的坐标，比如'upper left'，表示legend的左上角的坐标等于rectangle的左上角的坐标
    - ![](images/bbox_to_anchor用法1.png)

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

- ![Transform](images/matplotlib_transform.png)

- Transform实际上是一种坐标系的映射，将一个坐标系上的点映射到另一个坐标系（display)上。不论怎样，画图我们是要显示在屏幕上的，如何决定一个元素在屏幕上(display)的位置也就是transform要做的事。我们也可以把transform当作一个函数（实际上它们都是对象），比如`fig,transAxes`  ，`ax.transAxes.transform((0.5,0.5))->[328.  237.6]`，也就是输入本坐标系下点的坐标，返回其在'display'坐标系下的坐标，也就是最根本的坐标系。（屏幕显示）是'display'坐标系，但是该坐标系我们通常不需要关注。

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
  - `plt.cm.colors.cname.keys()` 预定义的所有颜色名称
- css4/x11 color name（**string**)
- xkcd color name（**string**)  eg：'xkcd:gold'
  - 上述两种实际上是对于颜色的一个命名
  - [颜色差异对比or查表](https://matplotlib.org/3.2.1/_images/sphx_glr_colors_003.png)



## colormap

- colormap实际上是一个table（or array），大小为N*4（or N\*3)，也就是通过索引将数值映射为颜色

- **Listedcolormap对象**

  - 将color存储在`.colors` 属性中，可以通过该属性查看其包含的所有颜色

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

    - 查找某一个颜色

    - 推荐通过numpy.array来操作

    - ```python
      (new_cmap(np.linspace(0,0.5,128)))   -->输出为list
      ```

  - ```
  cm = plt.cm.tab10  --> 一种built in的colormap，包含了10种颜色
    cm(range(10))--> 获得包含的所有颜色
  cm(5.2)  --> 本质上通过nearest-neighbor interpolation 得到的是cm(5)对应的颜色
    cm(0.5)  --> 如果输入是一个0-1之间的浮点数，则将其映射到1-10之间，之后通过nearest-neighbor interpolation得到其对应的颜色，也就是cm(5)
    ```
  ```
    
    
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
      'red','green','blue'以及'alpha'(optional),也就对应着RGB or RGBA                   
      每一列的格式为(x,y0,y1),其中每个分量的x必须布满[0,1]，每个分量的值单独进行寻找
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
  
      - ```
        LinearSegmentedColormap.from_list(['black','cyan','ivory'])
        ```

- matplotlib中built in了许多colormap，可以通过`Matplotlib.cm.get_cmap` 去查看
  - matplotlib将colormap分成了4种（可以来这里看不同colormap的效果   [colormap效果](https://matplotlib.org/3.2.1/tutorials/colors/colormaps.html#sphx-glr-tutorials-colors-colormaps-py)）:
    - **sequential colormap** :在某种单一颜色的基础上，通过改变色彩的饱和度而形成的渐变色（通常是饱和度递增），适用于数值fenbu线性
    - **diverging Colomap**: 由两种颜色构成，从一种颜色过渡到另一种颜色，先是饱和度减小，之后饱和度增大，适用于数据有中zhi和左右边界的情况
    - **cyclic colormap**:起点和终点是相同的颜色，用于围绕中心对称的数据
    - **qualitative colormap**: 由多个独立颜色组合而成的渐变色，适用于离散分布的情况
- 如何使用colormap

##  Normalize

  - 从上面可以知道，colormap只接收[0,1]的值，小于0取0，大于1取1，那么如何取到更大的范围？----》  **Normalize**
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

![Text 总览](images/matplotlib_text.png)

 

## Text的属性

- | font 属性   | 可用参数                                                     |
  | ----------- | ------------------------------------------------------------ |
  | fontsize    | { 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' }或者数字（整数大于0） |
  | fontstyle   | {'normal', 'italic' , 'oblique'} 正常or斜体                  |
  | fontfamily  | ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']，一个列表，[参考释义](https://baike.baidu.com/item/font-family/7529050?fr=aladdin) |
  | fontweight  | {'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}或者大于的整数 字体的粗细 |
  | fontvariant | {'normal','small-caps'}，'small-caps'所有字母为大写字母，'normal'设置首字母大写 |

  - **注意：设置字体的familt或者name时，需要先将字体添加到rcParams中**

  - ![Font](images/matplotlib_font.png)

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
| alpha | 透明度                                 |
  | bbox  | 在text外包一个框                       |
  
- `text(x,y,str,fontdict,*kwargs)`可以在axes的任何地方加上text，kwargs接收任意text的属性，也可以通过fontdict传入属性

  - `text(0,0,'test',fontdict={'fontsize':10,'horizontalalignment':'center'})`

## xlabel/ylabel

- `axes.set_xlabel(string,**kwargs)`   `axes.set_ylabel(string,**kwargs)`

- 可以接收上述text中的任何属性（以关键字参数的形式传入）,但是注意一些属性可能不会按照你想要的方式奏效

- `labelpad`  label特有的关键字参数，改变label到axis的距离，整数，以1/72为单位（72ppi）

- ```
  axes.set_xlabel('time',color='b',labelpad=0.1)
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
  - nbins ：axis显示多少个间隔，相邻两Tick间为一个bin
  - 每个tick有4个重要的属性：tick1line，tick2line，label1，label2。
    - 如果是xaxis上的tick，那么tick1line和label1表示top的tick，tick2line和label2表示bottom的tick
    - 如果是yaxis上的tick，那么tick1line和label1表示left的tick，tick2line和label2表示right的tick
    - tick1line和tick2line是line object，label1和label2是text object，可以用来设置fontsize等
    - 
-  **Tick locator**
   -  FixedLocator  `FixedLocator(locs,nbins=None) `  ，locs为array格式/list格式	
      - axis上的major tick是一个list，每个元素也就是一个tick，但是不一定会将这些tick都显示出来，若nbins为None，则会选择适合的tick进行显示，比如前6个tick已经包含了要显示的内容，那么就只会显示前6个tick
   -  MaxNLocator   `MaxNLocator(nbins='auto',steps=[1,2,2.5,5,10])`  
      - nbins='auto'，会根据axis的长度与绘图的元素自动选择合适步长，nbins指定时，通过steps选择步长，步长的值为steps中元素的$10^n$倍
   -  设置Locator
      -    `axis.set_major_locator(locator)` 
      -  `axis.set_ticks(array or list)` array中所有的元素（tick）都强制显示
-  **Tick formatter**
   - `matplotlib.ticker.StrMethodFormatter('{x:...}')`  str.format的格式化用法相似，注意必须有**x**
     - [format格式化](toi)
   - `matplotlib.ticker.FormatStrFormatter(str)`  与`%`格式化用法相似
   -  设置Formatter
      - `axis.set_major_formatter(formatter)`
   - 设置label
     - `axis.set_ticklabels(list)`
       - list其中的元素为string

## annotations

- annotations与text方法不同，会多一个箭头，用以指向要标记的地方

- `ax.annotate(s, xy, xytext,xycoords,arrowprops,annotation_clip,**kwargs)`

  - s 要注释的文本内容 string

  - xy  : tuple (float, float) 注释点的x坐标和y坐标（也就是要标记的地方）

  - xytext : tuple (float, float) 文本内容的x坐标和y坐标

  - xycoords :  对于注释点的transform的方式

    - 输入为str：`figure points` `figure piexls `  `figure fraction` `axes points` `axes pixels` `axes fraction`  `data` `polar`
    - 输入为transform对象

  - arrowpops 箭头的样式

    - 可以通过dict的方式来设置（这里着重看这种方式，还有其他方式）

      - `{width:_, head width:_,headlength:_,shrink:_ ,？}`
      - width 箭身的宽度
      - headwidth 箭头的宽度
      - headlength 箭头的长度
      - shrink :text 离箭头的距离
      - ？:实质上箭头是`matplotlib.patches.FancyArrowPatch` class，因此FancyArrowPatch可以设置的属性都可以传进来

    - 也可以通过arrowstyle来设置，如果arrowpops的dict中有`arrowstyle`这个key，那么上面的key（除了**？**）设置的内容被forbidden。arrowstyle支持的str类型有这些：

      - | Name       | Attrs                                         |
        | ---------- | --------------------------------------------- |
        | `'-'`      | None                                          |
        | `'->'`     | head_length=0.4,head_width=0.2                |
        | `'-['`     | widthB=1.0,lengthB=0.2,angleB=None            |
        | `'|-|'`    | widthA=1.0,widthB=1.0                         |
        | `'-|>'`    | head_length=0.4,head_width=0.2                |
        | `'<-'`     | head_length=0.4,head_width=0.2                |
        | `'<->'`    | head_length=0.4,head_width=0.2                |
        | `'<|-'`    | head_length=0.4,head_width=0.2                |
        | `'<|-|>'`  | head_length=0.4,head_width=0.2                |
        | `'fancy'`  | head_length=0.4,head_width=0.4,tail_width=0.4 |
        | `'simple'` | head_length=0.5,head_width=0.5,tail_width=0.2 |
        | `'wedge'`  | tail_width=0.3,shrink_factor=0.5              |

  - **kwargs 用来设置注释的文本内容的属性，任何text可以设置的属性都可以传进去

  - [更多的看这里](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.axes.Axes.annotate.html?highlight=annotate#matplotlib.axes.Axes.annotate)

# 参考

[backend参考](http://vra.github.io/2017/06/13/mpl-backend/)

[Artist参考](https://matplotlib.org/tutorials/intermediate/artists.html#sphx-glr-tutorials-intermediate-artists-py)

