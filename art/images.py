from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 0
y = 150

width = 20
height = 8

for i in range(0,width):
  for j in range(0,height):
    if j % 4 == 0:
      image(x + i * 30, y + j * 30, "misc/YellowFlower.png")
    else:
      image(x + i * 30, y + j * 30, "misc/Clover.png")
     
