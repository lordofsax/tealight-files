from tealight.logo import move, turn

def chessboard(size):
 for i in range(0,64):
    
  for i in range(0,4):   
   move(size)
   turn(90)    
  move(size)
  
turn(-90)  
chessboard(24)