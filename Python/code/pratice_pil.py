from PIL import ImageFilter
from PIL import Image
from PIL import ImageDraw
print(Image.NEAREST)
print(hasattr(filter,'filter'))
img  =  Image.open('../coding.png')
draw = ImageDraw.Draw(img)
draw.line((0,0,500,100),fill='rgb(255,0,0)',width=5)


img = Image.new('L',(300,300),color=128)
img.show()
