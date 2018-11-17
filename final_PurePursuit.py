from turtle import * 
import numpy as np
import math


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
path = np.array([[-150,0],[150,0]])
stop_point = [-150,0]
seth(225)
speed(3)
showturtle()

#step 1 
pos = pos() #(x,y) current position 

l1 = np.linalg.norm(pos-path[0])
l2 = np.linalg.norm(pos-path[1])
print('Line 1st = {0:.3f}'.format(l1))
print('Line 2st = {0:.3f}'.format(l2))

#step 2 
if l1 > l2 :
        nearPoint = path[1]
        farPoint = path[0]
        print('Near Point is ',nearPoint)
        print('Far Point is ',farPoint)
else :
        nearPoint = path[0]
        farPoint = path[1]
        print('Near Point is ',nearPoint)
        print('Far Point is ',farPoint)

#step 3 
#vector A is Path 
#vector B is Current position 
A = [farPoint[0]-nearPoint[0],farPoint[1]-nearPoint[1]]
B = [pos[0]-nearPoint[0],pos[1]-nearPoint[1]]
sizeA = np.linalg.norm(nearPoint-farPoint)
powerSizeA = np.square(sizeA)
vecA = np.array(A)
vecB = np.array(B)
AdotB = np.dot(vecA,vecB)
P = AdotB/powerSizeA
vecP = P*np.array(vecA)
vertical_X = vecP[0]+nearPoint[0]
vertical_Y = vecP[1]+nearPoint[1]
print('Vector A is ',vecA)
print('Vector B is ',vecB)
print('Vector B is ',vecP)
print('Vertical Point is ({0:.3f},{1:.3f})'.format(vertical_X,vertical_Y))

#step 4 
#find the cut point with circle cut line 
y = 0 #equation of path 
x1 = -1*np.sqrt(-y**2 +2704) + start_point[0] 
x2 = np.sqrt(-y**2 + 2704) + start_point[0]  
print('Cut Point is ({0:.3f},{1:.3f})'.format(x1,x2))

#step 5
if np.linalg.norm(np.array([x1,0])-stop_point) < np.linalg.norm(np.array([x2,0])-stop_point) :
        goalPoint = [x1,y] 
else:
        goalPoint = [x2,y] 
print('Select Goal Point = ',goalPoint)

#step 6 
angle_H = heading()
fc_x = math.cos(math.radians(angle_H))
fc_y = math.sin(math.radians(angle_H)) 
fc = 52 * np.array([fc_x,fc_y])
fronCar = np.add(pos,fc) 
ld = np.linalg.norm(pos-goalPoint)
eld = np.linalg.norm(fronCar-goalPoint)
Alpha = np.arcsin(eld/ld)
Zixmar = math.degrees((2*52)*np.sin(Alpha)/ld)
Theta = (20/52)*np.tan(Zixmar)

seth(180+Zixmar)
print(heading())
fd(20)

done()