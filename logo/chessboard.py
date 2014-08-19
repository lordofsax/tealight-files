from tealight.logo import move, turn

def chessboard(size):
 for i in range(1,4):
  move(size)
  turn(90)
  
turn(-90)  
chessboard(240)