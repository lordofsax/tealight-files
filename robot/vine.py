from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def Movement():

 FruitPresence = touch()
  
 while (FruitPresence == 'fruit'):
  move()
  FruitPresence = touch()
  NewSource = look()
 if NewSource == 'fruit':
  Movement()  
 if FruitPresence != 'fruit':
  turn(-1)
  Movement()
  
Movement()