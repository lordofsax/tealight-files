from tealight.logo import move, turn

def spiral(size):  #function with var size
  
  if size > 300:   #end function once var size > 
    return
  
  move(size)       #move  size pixels
  turn(0.1)         #rotate
  spiral(size + 5) #increase size by 5
  
spiral(5)          #call spiral with size = 0