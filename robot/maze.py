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
  
 WallPresence = touch() 

 while (SpaceFound == 0):

  if right_side() != 'wall':
   SpaceFound = 1
   turn(1)
   Movement()
    
  elif left_side != 'wall' and WallPresence == 'wall' :
   SpaceFound = 1
   turn(-1)
   Movement()
    
  move()  
   
Movement()