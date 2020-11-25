# Patch

- 顾名思义，也就是补丁，我们可以利用该模块来创造更多的图形，让这些图形可以处于图像中的任意位置，比如rectangle(矩形)，Polygon(多边形)，Arrow(箭头)

- 需要导入 `Matplotlib.patches` 

- 使用流程

  - ```python
    import matplotlib.patches as patches
    
    # for example
    p = pathces.rectangle(...)
    # for axes
    ax.add_patch(p) or ax.add_artist(p1)
    # for figure
    fig.add_artist(p)
    ```

- 以下用`patches`来简称`matplotlib.patches`

- 可以创造的所有patch都基于（继承自）`Matplotlib.patches.patch`该对象

- 一个patch对象具备基本的如下属性

  - alpha 透明度
  - color 颜色
  - facecolor 填充色
  - edgecolor 边缘线的颜色
  - fill 是否进行填充
  - label 
  - linestyle 边缘线的样式
  - linewidth 边缘线的宽度
  - transform
  - 其余还有很多，[看这里](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch)

## Rectangle

- `patches.Rectangle(xy, width, height, angle, **kwargs)`
  - xy （float, float)  表示矩形左边的坐标和下边的坐标
  - width, height 宽度 高度
  - angle 矩形旋转角度
  - **kwagrs 上面patch对象可以设置的属性，都可以传进来