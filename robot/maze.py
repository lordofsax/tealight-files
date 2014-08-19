from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

def Movement():
 SpaceFound = 0

 while (SpaceFound == 0):
  move()
  if right_side() != 'wall':
   SpaceFound = 1
   turn(1)
   Movement()
  else if left_side != 'wall':
   SpaceFound = 1
   turn(-1)
   Movement()
Movement()