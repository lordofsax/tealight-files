from tealight.logo import move, turn

def polygon(edges, size):  #function with 2 vars, edges and size
  angle = 360.0 / edges    #angle of rotation = degrees in circle/number of edges
  for i in range(0, edges):#while i is less than number edges
    move(size)             #move size
    turn(angle)            #turn value of angle
    
polygon(360,1)             #call function