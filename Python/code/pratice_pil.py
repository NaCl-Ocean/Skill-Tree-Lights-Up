from PIL import ImageFilter
from PIL import Image,ImageDraw,ImageColor,ImageFont
import string
import random

class VerifyCode:
    def __init__(self,line_num,char_num,size):
        self.line_num = line_num
        self.char_num = char_num
        self.width = size[0]
        self.height = size[1]
        self.img = Image.new(mode='RGB',size=size,color='rgb(255,255,255)')
        self.draw = ImageDraw.Draw(self.img)
        self.len_line_max = 30
        self.generate_noise()
        self.generate_lines()
        self.generate_chars()

        del self.draw
        self.img.filter(ImageFilter.BLUR)
        self.img.show()

    def generate_coordinate(self):
        x_left = random.randint(0,self.width-self.len_line_max)
        x_right = random.randint(x_left,self.width)
        y_upper = random.randint(0,self.height-self.len_line_max)
        y_lower = random.randint(y_upper,self.height)
        return (x_left,y_upper,x_right,y_lower)

    def generate_lines(self):
        for i in range(self.line_num):
            color = random.choice(list(ImageColor.colormap))
            coordinate = self.generate_coordinate()
            width = random.randint(1,5)
            self.draw.line(coordinate,color,width)

    def generate_chars(self):
        for i in range(self.char_num):
            char = random.choice(string.ascii_letters + string.digits)
            color = random.choice(list(ImageColor.colormap))
            x = random.randint(0,self.width-50)
            y = random.randint(0,self.height-50)
            font = ImageFont.truetype('arialuni.ttf',size=int(self.height*0.3))
            self.draw.text((x,y),char,fill=color,font=font)

    def generate_noise(self):
        for i in range(0,self.width):
            for j in range(0,self.height):
                color = random.choice(list(ImageColor.colormap))
                self.draw.point((i,j),fill=color)


test = VerifyCode(5,4,(500,200))








