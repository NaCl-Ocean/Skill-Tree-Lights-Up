from PIL import ImageFilter
from PIL import Image
from PIL import ImageDraw
from collections.abc import Iterable
print(Image.NEAREST)
print(hasattr(filter,'filter'))
img  =  Image.open('../coding.png')
draw = ImageDraw.Draw(img)
draw.line((0,0,500,100),fill='black',width=5)





img.show()

