from tealight.logo import move, turn

def spiral(size):
  
  if size > 300:
    return
  
  move(size)
  turn(95)
  spiral(size + 5)
  
spiral(0)