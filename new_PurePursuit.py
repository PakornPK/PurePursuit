from turtle import * 
import numpy as np
import math 
import time 
import _thread

def normDistance(x1,x2,y1,y2):
        x = (x2 - x1)**2 
        y = (y2 - y1)**2 
        xy = x+y 
        l = math.sqrt(xy)
        return l 

def frontCar():
    global car,result
    car = np.array(pos())
    angle_H = heading()
    fc_x = math.cos(math.radians(angle_H))
    fc_y = math.sin(math.radians(angle_H)) 
    fc = 52 * np.array([fc_x,fc_y])
    result = np.add(car,fc) 
    return result

def shortPath():
    global path_select,path
    path = np.array([[-150.0,0.0],[150.0,0.0]])  
    current_pos = np.array(pos()) 
    try:
        short_zero =  np.subtract(path[0],current_pos)
        short_one =  np.subtract(path[1],current_pos)
        
        if abs(short_zero[0]) >= abs(short_one[0]) and abs(short_zero[1]) >= abs(short_one[1]):
            path_select = True 
        else:
            path_select = False 

    except ValueError :
        print('Value Error')
        raise 


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
seth(0)
speed(3)
showturtle()


#run
global path_select ,car,shortPoint,path,result
frontCar()
shortPath()




while not(np.array_equal(car,path)):
    shortPoint = np.array([car[0],0]) #point be vertical 
    cutPoint = [shortPoint[0]+52,shortPoint[0]-52]     
    if path_select == True : 
        stop_point = path[0]
    else : 
        stop_point = path[1]
    print(stop_point)

 
    if stop_point[0] < 0 :
        ld = normDistance(car[0],cutPoint[1],car[1],0) 
    else:
        ld = normDistance(car[0],cutPoint[0],car[1],0) 
    print(ld)
    eld = normDistance(result[0],cutPoint[1],result[1],0)
    print(eld)  

    if eld >= ld : 
        h = heading()
        seth(h+1)
        print(h)
    else: 
        fd(100)

"""
l = eld/ld
print(l)
alpha = math.asin(l)
print(math.degrees(alpha))
seth(math.degrees(alpha))
"""
done()
