from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
SpaceFound = 0

while (SpaceFound == 0):
 move()
 if right_side() != 'wall':
  SpaceFound = 1