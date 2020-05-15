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
- ![](https://matplotlib.org/3.2.1/_images/anatomy.png)
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
    - ![image-20200515151620251](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200515151620251.png)
    - **vector graphics**   矢量图
    - **raster graphics**  栅格图，以像素进行渲染
  - **interactive backends**
    - 如何显示图形到屏幕
    - ![image-20200515151633250](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200515151633250.png)



# Artist对象总览

上述Artist对象是我们绘图时所重点关注的，分为两种

- **Primitives** ：也就是**line2D**，**AxesImage**，**patch**等

  - 通过Axes对象建立，例`axes.plot()`创建一个Line2D对象

  - 相同类型的Primitives对象以列表的形式存放在axes对象的对应属性中，如`axes.lines`也就包含着axes绘制的所有Line

    - 那么相应地，既然是个列表，那么其中的元素是否可以删去，答案是可以的，删去后自然该axes不显示对应的line了

  - 所有的Primitives对象都有以下属性

    - ![image-20200515184835931](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200515184835931.png)

    - 这些属性一般是私有属性，不建议直接`object.__property`来修改，一般通过getter来查看，通过setter来设置

    - ```python
      label = line.get_label()
      line.set_label('line')
      line.set(label='line',visible=False)  # 同时设置多个属性
      ```

      

- **Containers**：也就是**Axis**，**Axes**，**Figure**

- **总体来说matplotlib中基本对象存在着层级关系。**

  ![matplotlib_object](F:\about study\07其他\Skill-Tree-Lights-Up\Python\matplotlib_object.png)

## Figure

- **Top level container**
- **更加focus的是用来存放Axes，通过Figure的help function来建立Axes或者删除Axes**
  - 一个Figure可以有多个Axes
- ![image-20200515193504043](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200515193504043.png)
- 背景是Rectangle对象

## Axes

- 创建的Axes对象以列表的形式存放在`figure.axes`中

- 背景是Rentangle对象或者Circle对象

- 通常更关注的是通过helper function来创建Artist对象，之后通过该Artist对象来具体设置该对象的一些性质

- ![image-20200515195056408](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200515195056408.png)

- ![image-20200515195115410](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200515195115410.png)

  

## Axis

- 用来设置axis label，tick line，tick label，grid lines
- ![image-20200515200953759](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200515200953759.png)

- 从上面看，可以看到一个层级关系，每一层都相当于为一层提供一个接口，用来返回相应的对象。

## Tick

- 注意：axis只有xaxis和yaxis，但是tick是四条边都算在内的
- ![image-20200515202014508](C:\Users\26401\AppData\Roaming\Typora\typora-user-images\image-20200515202014508.png)
- 这里的tick1line，tick2line以及label1，label2也就是每个axis对应的两条边



# Legend对象



# 参考

[backend参考](http://vra.github.io/2017/06/13/mpl-backend/)

[Artist参考](https://matplotlib.org/tutorials/intermediate/artists.html#sphx-glr-tutorials-intermediate-artists-py)

