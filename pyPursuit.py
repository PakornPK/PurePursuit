import tkinter
from tkinter import ttk 
import numpy as np 
import time 
import math

class pyPursuit(tkinter.Frame):
    def __init__(self, master): 
        super(pyPursuit, self).__init__(master)
        self.poly = [[190,370],[210,370],[210,400],[190,400]]
        self.angle = 0 
        self.center = self.find_center(self.poly)
        self.shortate = np.linalg.norm(self.center[0]-250) # path fig 
        self.grid()
        self.create_widgets()

    def create_widgets(self): 
        self.CV = tkinter.Canvas(width=500, height=500, bg = 'pink')
        self.CV.grid()

        path_Line = self.CV.create_line(250,0,250,500)
        textPathTop = self.CV.create_text(270,10,text='(250,0)')
        textPathBottom = self.CV.create_text(275,490,text='(250,500)')
        textSh = self.CV.create_text(50,20,text = 'Shortate = ' + str(self.shortate))
        textLH = self.CV.create_text(55,35,text = 'Look ahead = 80.0')
        textL = self.CV.create_text(30,50,text = 'L = '+ str(np.linalg.norm(np.array(self.center)-np.array([250,self.center[1]]))))
        
        self.poly = self.rotate(self.poly,self.angle,tuple(self.center))
        self.carBot = self.CV.create_polygon(self.poly, fill = 'yellow' ,outline = 'black')
        textCenter = "({0},{1})".format(str(self.center[0]),str(self.center[1]))
        textcar = self.CV.create_text(self.center[0],self.center[1],text= textCenter)
        lineSh = self.CV.create_line(self.center[0],self.center[1],250,self.center[1], fill = 'green')
        lineLH = self.CV.create_line(250,self.center[1],250,self.center[1]-80, fill = 'green')
        lineL =self.CV.create_line(self.center[0],self.center[1],250,self.center[1]-80, fill = 'green')
        



        
    def rotate(self, points, angle, center): 
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center
        new_points = []
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        return new_points

    def find_center(self,old_point):
        point = np.array(old_point)
        X = np.linalg.norm(point[0][0]-point[1][0])/2 
        Y = np.linalg.norm(point[0][1]-point[1][1])/2  
        center = [point[3][0]+X,point[3][1]+Y]     
        return center 




if __name__ == "__main__":

    gui = tkinter.Tk()
    gui.title('PyPursuit Simmulation Pure Pursuit Path tracking')
    gui.geometry('500x500')
    sim = pyPursuit(gui)
    gui.mainloop()