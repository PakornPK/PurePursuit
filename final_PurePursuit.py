from turtle import * 
import numpy as np
import math 

def normDistance(x1,x2,y1,y2):
        x = (x2 - x1)**2 
        y = (y2 - y1)**2 
        xy = x+y 
        l = math.sqrt(xy)
        return l 


#setup
Tr = Turtle()
wn = Screen()
wn.title('Pure Pursuit')
setup(500,500)
bgcolor('black')
mode("standard")
poly = ((18,0),(-18,0),(-18,52),(18,52))
s = Shape("compound")
s.addcomponent(poly,"yellow","red")
register_shape("car", s)
hideturtle()
shape("car")
pen(fillcolor="black", pencolor="blue", pensize=5)
pensize(3)
penup()
goto(-150,0)
pendown()
goto(150,0)
penup()

#start 
start_point = [100,100]
goto(start_point)
path = [-150,0],[150,0]
stop_point = [-150,0]
seth(0)
speed(3)
showturtle()

#step 1 
pos = pos()
l1 = normDistance(pos[0],-150,pos[1],0)
l2 = normDistance(pos[0],150,pos[1],0)
print(l2)



done()