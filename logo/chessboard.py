from tealight.logo import move, turn

def chessboard(size):
 for i in range(0,10):  
  for i in range(0,5):
   move(size)
   turn(90)
 
   
  
turn(-90)  
chessboard(24)