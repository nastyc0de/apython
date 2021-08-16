from PIL import Image
import numpy as np
class Canvas:
    def __init__(self, color, a, b):
        self.color = color
        self.a = a
        self.b = b

        self.data = np.zeros((self.a, self.b, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

class Rectangle:
    def __init__(self, x, y, a, b, color):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.color = color
    
    def draw(self, canvas):
        canvas.data[self.x: self.x + self.a, self.y: self.y + self.b] = self.color

class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
        canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color
