

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

- `plt.scatter(x,y,s,c,marker,label)`
  - **x,y:** scalar or array-like, shape (n, )
  - **s**: marker size.   **scalar or array-like**, shape (n, ), optional
  - **c**: marker  color, sequence, or sequence of colors, optional
    - A single color format string.
    - A sequence of colors of length n.
    - **A scalar or sequence of n numbers** to be mapped to colors using *cmap* and *norm*.
    - **A 2-D array** in which the rows are RGB or RGBA.If you want to specify the same RGB or RGBA value for all points, use a 2-D array with a single row. 
  - 总结一下，上述参数大部分都可以用scalar或者array来输入，用scalar表示所有的点都一样，用array表示每一个点的特点有array中对应元素指定，也就导致了如果用array需要和点的个数相同

