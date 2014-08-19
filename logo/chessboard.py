from tealight.logo import move, turn

def chessboard(sizeT):
 for i in range(0,4):
  move(sizeT)
  turn(90)
  
 size = sizeT * 7/8 
 for i in range(0,3): 
  move(size)
  turn(90)
  
 size = sizeT * 6/8 
 for i in range(0,3): 
  move(size)
  turn(90) 
  
 size = sizeT * 5/8 
 for i in range(0,3): 
  move(size)
  turn(90) 
   
  
turn(-90)  
chessboard(240)