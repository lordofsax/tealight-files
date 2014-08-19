from tealight.logo import move, turn

def chessboard(size):
 for i in range(0,4):
  move(size)
  turn(90)
 size = size * 7/8
 for i in range(0,2): 
  move(size)
  turn(90)
  
turn(-90)  
chessboard(240)