from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, Xsize, Ysize, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (Xsize * cos(angle))
    y0 = y + (Ysize * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)
    x = x0
    y = y0

star(100, 300, "blue", 10, 12, 50)
star(400, 400, "purple", 20, 15, 100)
star(250, 200, "orange", 12, 30, 30)