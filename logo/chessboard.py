from tealight.logo import move, turn

def chessboard(sizeT):
 for i in range(0,4):
  move(sizeT)
  turn(90)
 
   
  
turn(-90)  
chessboard(240)