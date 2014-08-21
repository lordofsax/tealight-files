from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)


x = [2,5]
print x.index
value = x[1]
print value
x.remove(value)
print x.index

ans = "animals/Bear.png"

def animals():

  image(100,100, ans)
  image(200,100, "animals/Bear.png")

  image(100,200, "animals/Cat.png")
  image(200,200, "animals/Cat.png")

  image(100,300, "animals/Dog.png")
  image(200,300, "animals/Dog.png")

  image(100,400, "animals/Elephant.png")
  image(200,400, "animals/Elephant.png")

  image(100,500, "animals/Frog.png")
  image(200,500, "animals/Frog.png")

  image(100,600, "animals/Horse.png")
  image(200,600, "animals/Horse.png")

  image(100,700, "animals/Ladybird.png")
  image(200,700, "animals/Ladybird.png")

  image(100,800, "animals/Lion.png")
  image(200,800, "animals/Lion.png")

  image(300,100, "animals/Lobster.png")
  image(400,100, "animals/Lobster.png")

  image(300,200, "animals/Penguin.png")
  image(400,200, "animals/Penguin.png")

  image(300,300, "animals/Puffin.png")
  image(400,300, "animals/Puffin.png")

  image(300,400, "animals/Seagull.png")
  image(400,400, "animals/Seagull.png")

  image(300,500, "animals/Seal.png")
  image(400,500, "animals/Seal.png")

  image(300,600, "animals/Sheep.png")
  image(400,600, "animals/Sheep.png")

  image(300,700, "animals/Swan.png")
  image(400,700, "animals/Swan.png")

  image(300,800, "animals/Tiger.png")
  image(400,800, "animals/Tiger.png")

  image(500,100, "animals/Ant.png")
  image(600,100, "animals/Ant.png")

  image(500,200, "animals/Butterfly.png")
  image(600,200, "animals/Butterfly.png")

  image(500,300, "animals/Diplodocus.png")
  image(600,300, "animals/Diplodocus.png")

  image(500,400, "animals/Dolphin.png")
  image(600,400, "animals/Dolphin.png")

  image(500,500, "animals/Fish1.png")
  image(600,500, "animals/Fish1.png")

  image(500,600, "animals/Stegosaurus.png")
  image(600,600, "animals/Stegosaurus.png")

  image(500,700, "animals/Fish2.png")
  image(600,700, "animals/Fish2.png")

  image(500,800, "animals/Pterodactyl.png")
  image(600,800, "animals/Pterodactyl.png")

  
animals()