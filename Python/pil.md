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

- **四种采样滤波器**

  - `NEAREST`
  - `BILINEAR`
  - `BICUBIC`
  - `ANTIALIAS`



# ImageColor

- **指定RGB格式的color**
- pillow支持以下几种格式的color**字符串样式**
  - 十六进制 `#ff0000`
  - RGB functions   `rgb(255,0,0)` 或者`rgb(100%,0%,0%)`
  - Hue-Saturation-Lightness (HSL)  `hsl(hue, saturation%, lightness%)`
  - 预定义的string，'black'等等 [pillow中的预定义color](https://pillow-cn.readthedocs.io/zh_CN/latest/_modules/PIL/ImageColor.html#getrgb)
- `ImageColor.getrgb(string)`  将color字符串转换为元组(red, green, blue)



# ImageFilter

- 有一些预定义的filter，如BLUR，SHARPNESS等
- 具体查阅[官方文档](https://pillow-cn.readthedocs.io/zh_CN/latest/reference/ImageFilter.html)



# Image模块

- 核心是**Image对象**

- **创建Image对象**
  - `Image.open(file_path,mode='r')`  通过图像文件创建一个Image对象，返回Image_obj
  - `Image.new(mode,size,color)`   创建一个空白的Image对象，color的格式需和mode匹配，返回Image_obj，**size为2-tuple(width,height)**
    - mode为rgb时，可以通过上述的color字符串指定
    - mode为1时，指定为0或者1
    - mode为L时，指定为0-255之间的一个整数
    - model为F时，指定为浮点数
    - 其他同理
  - `Image.fromarray(obj,mode=None)` 通常用于从其他格式的矩阵对象转换为PIL.Image对象，如numpy.array
  
- 图像显示
  
  - `image_obj.show(title)`   
  
- 图像保存
  
- `image_obj.save(file_path,format)`    format为'jpg'，'png'等
  
- **图像处理**

  - **函数的特点是返回一个新的image对象，不会对原image对象产生影响**

  - 图像旋转   `Image_obj.rotate(angle, resample=0, expand=True/False)`   

    - resample使用哪种采样滤波器，`PIL.Image.NEAREST`  或者`PIL.Image.BILINEAR`

      或者`PIL.Image.BICUBIC`或者`PIL.Image.ANTIALIAS`

    - expand为True进行填充，为False不进行填充，返回原图相同大小的Image_obj

  - 图像缩放  `Image_obj.resize(size, resample=0)` 

    - `size` 2-tuple:(width,height)
    - `resample`同上

  - 滤波 `Image_obj.filter(filter)`  

    - `filter`需为通过`Imagefilter`定义的filter对象
    - 例：`im.filter(ImageFilter.BLUR)`

  - 分离通道 `Image_obj.spilt()`  

    - 返回一个tuple，包含`Image_obj`的各个通道，每个通道都是一个Image对象

- **图像合成**

  - `Image.alpha_composite(im1, im2)`   im1与im2需要有 $\alpha$ 通道， $\alpha$ 通道用来表征图像的透明程度
  - `Image.blend(im1, im2, alpha)`   $out = image1 * (1.0 - alpha) + image2 * alpha$   

- **查看图像的属性**
  
  - `Image_obj.size`  返回2-tuple 的size
  - `Image.format`   查看原图像文件的格式 'jpg',....
  - `Image_obj.mode`   查看图像的mode
  
- **获得像素点的像素值**
  
  - `Image_obj.getdata(band=None)` 以sequence的形式返回每个像素点的像素值，默认返回所有的通道。
  - `Image_obj.getpixel(xy)` 返回坐标为(x,y)出像素点的像素值



# ImageDraw 模块

- 画图流程
  - 通过`Image`对象创建`ImageDraw`对象
  - 画图
  - 删除`ImageDraw`对象
- 画图所需要的元素
  - 颜色：颜色指定需要与image的mode相对应，同上`Image.new`
  - 字体(text)：需要用到`Imagefont`模块
  - 粗细：利用整数来指定，数字越大，越粗
- 创建`ImageDraw`对象
  - `draw = ImageDraw.Draw(im, mode=None)`    
- [可以绘制的形状](https://pillow-cn.readthedocs.io/zh_CN/latest/reference/ImageDraw.html#example-draw-a-gray-cross-over-an-image)
- 注意：draw对象调用绘制形状的方法会对image对象立即生效



# ImageFont模块

- 主要功能是加载字体文件，生成一个ImageFont对象，用于上面绘制text
- 加载的字体文件有两种
  - 位图字体  `ImageFont.load(filename)`
  - TrueType or OpenType 字体   `ImageFont.truetype(file_path,size)`