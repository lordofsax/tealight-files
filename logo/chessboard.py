from tealight.logo import move, turn

def chessboard(size):
 for i in range(0,64):   
  move(size)
  turn(90)    

turn(-90)  
chessboard(24)