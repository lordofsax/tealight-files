from tealight.logo import move, turn


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

def waterwheel(edges, size):  #side = sidelength
  angle = 360 / edges      #finds angle between each edge
  decoration = size / 2  #makes square side length half size
  for i in range(0, edges):
    move(size)
    square(decoration)
    turn(angle)

turn(-90)      #affects starting pitch of "turtle"
waterwheel(12,75)
