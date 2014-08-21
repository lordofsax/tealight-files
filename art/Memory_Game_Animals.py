from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import (screen_width, screen_height)

from random import shuffle



animal_array = ["animals/Bear.png", "animals/Bear.png", "animals/Cat.png", "animals/Cat.png", "animals/Dog.png", "animals/Dog.png", "animals/Elephant.png", "animals/Elephant.png", "animals/Frog.png", "animals/Frog.png", "animals/Horse.png", "animals/Horse.png", "animals/Ladybird.png", "animals/Ladybird.png", "animals/Lion.png", "animals/Lion.png", "animals/Lobster.png", "animals/Lobster.png", "animals/Penguin.png", "animals/Penguin.png", "animals/Puffin.png", "animals/Puffin.png", "animals/Seagull.png", "animals/Seagull.png", "animals/Seal.png", "animals/Seal.png", "animals/Sheep.png", "animals/Sheep.png", "animals/Swan.png", "animals/Swan.png", "animals/Tiger.png", "animals/Tiger.png", "animals/Ant.png", "animals/Ant.png", "animals/Butterfly.png", "animals/Butterfly.png", "animals/Diplodocus.png", "animals/Diplodocus.png", "animals/Dolphin.png", "animals/Dolphin.png", "animals/Fish1.png", "animals/Fish1.png", "animals/Stegosaurus.png", "animals/Stegosaurus.png", "animals/Fish2.png", "animals/Fish2.png", "animals/Pterodactyl.png", "animals/Pterodactyl.png"] 

shuffle(animal_array)

def placeAnimals():
  
  animal_array = ["animals/Bear.png", "animals/Bear.png", "animals/Cat.png", "animals/Cat.png", "animals/Dog.png", "animals/Dog.png", "animals/Elephant.png", "animals/Elephant.png", "animals/Frog.png", "animals/Frog.png", "animals/Horse.png", "animals/Horse.png", "animals/Ladybird.png", "animals/Ladybird.png", "animals/Lion.png", "animals/Lion.png", "animals/Lobster.png", "animals/Lobster.png", "animals/Penguin.png", "animals/Penguin.png", "animals/Puffin.png", "animals/Puffin.png", "animals/Seagull.png", "animals/Seagull.png", "animals/Seal.png", "animals/Seal.png", "animals/Sheep.png", "animals/Sheep.png", "animals/Swan.png", "animals/Swan.png", "animals/Tiger.png", "animals/Tiger.png", "animals/Ant.png", "animals/Ant.png", "animals/Butterfly.png", "animals/Butterfly.png", "animals/Diplodocus.png", "animals/Diplodocus.png", "animals/Dolphin.png", "animals/Dolphin.png", "animals/Fish1.png", "animals/Fish1.png", "animals/Stegosaurus.png", "animals/Stegosaurus.png", "animals/Fish2.png", "animals/Fish2.png", "animals/Pterodactyl.png", "animals/Pterodactyl.png"] 

  shuffle(animal_array)
  
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
    
place_animals()