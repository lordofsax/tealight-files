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

  if left_side() != 'wall':
   SpaceFound = 1
   turn(1)
   move()
   Movement()    
    
  elif right_side != 'wall':
   WallPresence = touch()
   if WallPresence == 'wall': 
    SpaceFound = 1
    turn(-1)
    move()
    Movement()
    
  move()  
   
Movement()