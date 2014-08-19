from tealight.logo import move, turn

def chessboard(size):
 for i in range(0,4):  
  for i in range(0,5):
   turn(90)
   move(size)
   
  move(size)
   
  
turn(-180)  
chessboard(24)