from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)


x = ["dog",7,5]
#print x.index
#print x[0]
#value = x[0]
#print value
#x.remove(value)
#print x.index
#print x[0]

for i in x[::-1]:
  print i
  
animal_array = ["animals/Bear.png", "animals/Bear.png", "animals/Cat.png", "animals/Cat.png", "animals/Dog.png", "animals/Dog.png", "animals/Elephant.png", "animals/Elephant.png", "animals/Frog.png", "animals/Frog.png", "animals/Horse.png", "animals/Horse.png", "animals/Ladybird.png", "animals/Ladybird.png", "animals/Lion.png", "animals/Lion.png", "animals/Lobster.png", "animals/Lobster.png", "animals/Penguin.png", "animals/Penguin.png", "animals/Puffin.png", "animals/Puffin.png", "animals/Seagull.png", "animals/Seagull.png", "animals/Seal.png", "animals/Seal.png", "animals/Sheep.png", "animals/Sheep.png", "animals/Swan.png", "animals/Swan.png", "animals/Tiger.png", "animals/Tiger.png", "animals/Ant.png", "animals/Ant.png", "animals/Butterfly.png", "animals/Butterfly.png", ] 
  
def place_animals():
  
  global animal_array 
  
  x = 100
  y = 100
  
  for i in animal_array[::-1]:
    
    
    
    image(x, y, i)
    
    if x < 600:
    
      x = x + 100
    
    else:
    
      x = 100
    
      y = y + 100
  
  

def animals():

  image(100,100, "animals/Bear.png")
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

  
#animals()

place_animals()