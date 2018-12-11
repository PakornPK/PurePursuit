from turtle import * 
import numpy as np
import math
import time


#setup
Tr = Turtle()
wn = Screen()
wn.title('Pure Pursuit')
setup(500,500)
bgcolor('black')
mode("standard")
poly = ((18,0),(-18,0),(-18,32),(0,52),(18,32))
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
start_point = [50,50]
goto(start_point)
path = np.array([[-150,0],[150,0]])
stop_point = [-150,0]
seth(220)
speed(7)
showturtle()

for i in range(1):
#while True: 
        #step 1 
        pos_car = pos() #(x,y) current position 
        angle_H = heading()
        fc_x = math.cos(math.radians(angle_H))
        fc_y = math.sin(math.radians(angle_H)) 
        fc = 52 * np.array([fc_x,fc_y])
        frontCar = np.add(pos_car,fc)

        l1 = np.linalg.norm(pos_car-path[0])
        l2 = np.linalg.norm(pos_car-path[1])
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
        B = [pos_car[0]-nearPoint[0],pos_car[1]-nearPoint[1]]
        sizeA = np.linalg.norm(nearPoint-farPoint)
        powerSizeA = np.square(sizeA)
        vecA = np.array(A)
        vecB = np.array(B)
        AdotB = np.dot(vecA,vecB)
        P = AdotB/powerSizeA
        vecP = P*np.array(vecA)
        vertical_X = vecP[0]+nearPoint[0]
        vertical_Y = vecP[1]+nearPoint[1]
        verticalPoint = [vertical_X,vertical_Y]
        print('Vector A is ',vecA)
        print('Vector B is ',vecB)
        print('Vector P is ',vecP)
        print('Vertical Point is ({0:.3f},{1:.3f})'.format(vertical_X,vertical_Y))

        #step 4 
        #find shortate distance 
        shortate = np.linalg.norm(np.array(verticalPoint)-np.array(pos_car))
        np.array(shortate)
        print("Shortate distance = ",shortate)

        #fix V and Goal  
        Goal = [vertical_X - 50,verticalPoint[1]]
        print("Pos = ",pos())
        print("goal = ",Goal)

        #step 5 
        #find alpha 
        L = np.linalg.norm(np.array(Goal)-np.array(pos()))  
        eld = np.linalg.norm(np.array(Goal)-np.array(frontCar))
        alpha = np.arcsin(eld/L)
        #r = (L**2)/(2*shortate)
        K = (2*np.sin(alpha))/L
        V = 100
        angle_H = heading()
        print('heading before calculate = ',angle_H)
        defX = V*np.cos(math.radians(angle_H))
        defY = V*np.sin(math.radians(angle_H))
        Zixmar = np.arctan(K*52)
        defPhi = (V/52)*(np.tan(Zixmar))
        print("L =",L)
        #print("R =",r)
        print("DEF X = ",defX)
        print("DEF Y = ",defY)
        print("DEF PHI = ",defPhi)
        
        #step 6
        angle_H = angle_H + defPhi 
        posX = pos_car[0] + defX
        posY = pos_car[1] + defY
        seth(angle_H)
        goto(posX,posY)
        print("new Pos = ",pos())
        print('new Heading =',heading())
        print('-------------------',i,'------------------------------')

done()