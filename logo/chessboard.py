from tealight.logo import move, turn

def chessboard(size):
 for i in range(0,4):
  move(size)
  turn(90)
  
  for i in range(0,3): 
   move(size)
   turn(90)
  
turn(-90)  
chessboard(240)