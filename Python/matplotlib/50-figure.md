

以下都用`plt`来代替`pyplot`

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



- ​	

