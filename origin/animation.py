
import math


class Coordinates():
    def __init__(self, x, y, width, height):
        '''
        x, y = Center or shape 
        if circle, width=height=radius 
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def rectangle(self):
        Ox = self.x - 1/2*self.width
        Oy = self.y - 1/2*self.height
        output = [[Ox+w, Oy] for w in range(self.width)] +\
                 [[Ox+self.width, Oy+h] for h in range(self.height)] +\
                 [[Ox+self.width-w, Oy+self.height] for w in range(self.width)] +\
                 [[Ox, Oy+self.height-h] for h in range(self.height)]
        return output

    def circle(self) -> list:
        output = []
        for i in [k*0.1 for k in range(3600)]:
            Ox = self.x + self.width * math.sin(math.radians(i))
            Oy = self.y + self.height * math.cos(math.radians(i))
            output.append([Ox, Oy])
        return output


def animation_path(list, width):
    output = []
    if len(list) < width:
        width = len(list)
    for i in range(len(list) + width - 1):
        if i+1 < width:
            output.append(list[0:i+1])
        elif i+1 >= width:
            output.append(list[i+1-width: i+1])
        elif i+1 > len(list):
            output.append(list[i+1-width-len(list)::])
    return output
