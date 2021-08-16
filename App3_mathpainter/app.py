

from classes import Canvas, Rectangle, Square

canvas = Canvas(a=20, b=30, color=(255,255,255))
r1 = Rectangle(x=1,y=4,a=15,b=10,color=(100,40, 110))
r1.draw(canvas)
s1 = Square(x=4,y=6,side=4, color=(0,110,3))
s1.draw(canvas)
canvas.make('canvas.png')