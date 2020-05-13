# 前引

- PIL全称Python Image Libary，pillow是PIL引出的一个分支
- 主要包含以下功能
  - 图像简单处理（旋转，缩放，滤波等）
  - 图像绘制
- 主要用到了如下几个模块：
  - Image
    - 图像的操作
      - 打开图像，保存图像，显示图像
    - 图像的属性
    - 图像的简单处理
      - filter、resize、rotate、crop等
  - ImageDraw
    - 在图像上绘制简单的形状（line，rectangle，polygon，text，point，ellipse）
  - ImageColor
    - 为Image模块和ImageDraw模块服务
  - ImageFilter
    - 有一些预定义的滤波器，为Image模块服务

# 基本概念

- 通道（band) 

- 模式（mode)：像素以什么格式进行存储

  - | mode | mean                              |
    | ---- | --------------------------------- |
    | 1    | 1bit，单通道，黑白                |
    | L    | 8bit，单通道，黑白                |
    | P    | 8bit，调色板，                    |
    | RGB  | 8bit，三通道，                    |
    | RGBA | 8bit，四通道，A表示透明度$\alpha$ |
    | I    | 32bit，整数，单通道               |
    | F    | 32bit，浮点，单通道               |

- 大小(size)



# ImageColor

- **指定RGB格式的color**
- pillow支持以下几种格式的color**字符串样式**
  - 十六进制 `#ff0000`
  - RGB functions   `rgb(255,0,0)` 或者`rgb(100%,0%,0%)`
  - Hue-Saturation-Lightness (HSL)  `hsl(hue, saturation%, lightness%)`
- `ImageColor.getrgb(string)`  将color字符串转换为元组(red, green, blue)

# Image模块

- 核心是**Image对象**
- **创建Image对象**
  - `Image.open(file_path,mode='r')`  通过图像文件创建一个Image对象，返回Image_obj
  - `Image.new(mode,size,color)`   创建一个空白的Image对象，color的格式需和mode匹配，返回Image_obj
    - mode为rgb时，可以通过上述的color字符串指定
    - mode为1时，指定为0或者1
    - mode为L时，指定为0-255之间的一个整数
    - 其他同理
- 图像显示
  - `image_obj.show(title)`   
- 图像保存
  - `image_obj.save(file_path,format)`    format为'jpg'，'png'等

- 图像处理（函数的特点是返回一个新的image对象，不会对原image对象产生影响）
  - 

