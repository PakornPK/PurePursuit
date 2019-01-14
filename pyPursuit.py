import tkinter
from tkinter import ttk 
import numpy as np 
import time 
import math

class pyPursuit(tkinter.Frame):
    def __init__(self, master): 
        super(pyPursuit, self).__init__(master)
        self.angle = -90 
        self.center = [200,450]
        self.poly = self.createCarBot(self.center[0],self.center[1],self.angle)
        self.shortate = np.linalg.norm(self.center[0]-250) # path fig 
        self.LH = 100
        self.grid()
        self.create_widgets()

    def create_widgets(self): 
        self.CV = tkinter.Canvas(width=500, height=500, bg = 'pink')
        self.CV.grid()
        

        path_Line = self.CV.create_line(250,0,250,500)
        textPathTop = self.CV.create_text(270,10,text='(250,0)')
        textPathBottom = self.CV.create_text(275,490,text='(250,500)')
        textSh = self.CV.create_text(50,20,text = 'Shortate = ' + str(self.shortate))
        textLH = self.CV.create_text(55,35,text = 'Look ahead = {}'.format(self.LH))

        ct = np.array(self.center)
        lh = np.array([250.0,self.center[1]-self.LH])
        L = np.linalg.norm(ct-lh)
        textL = self.CV.create_text(35,50,text = 'L = {0:.3f}'.format(L))
        R = np.square(L)/(2*self.shortate)
        D = R-self.shortate 
        textR = self.CV.create_text(35,65,text = 'R = {0:.3f}'.format(R))
        textSpeed = self.CV.create_text(44,80, text = 'Speed = 2 m/s')

        self.poly = self.rotate(self.poly,self.angle,tuple(self.center))
        self.carBot = self.CV.create_polygon(self.poly, fill = 'yellow' ,outline = 'black')
        textCenter = "({0},{1},Φ={2})".format(self.center[0],self.center[1],self.angle)
        textcar = self.CV.create_text(self.center[0],self.center[1]+5,text= textCenter)
        lineR = self.CV.create_line(self.center[0],self.center[1],250+D,self.center[1], fill = 'green')
        lineLH = self.CV.create_line(250,self.center[1],250,self.center[1]-self.LH, fill = 'green')
        lineL = self.CV.create_line(self.center[0],self.center[1],250,self.center[1]-self.LH, fill = 'green')
        textCenterR = self.CV.create_text(250+D,self.center[1],text = '({0},{1})'.format(250+D,self.center[1]))
        circle = self.create_circle(250+D,self.center[1],R,self.CV)

        fc_x = math.cos(math.radians(self.angle))
        fc_y = math.sin(math.radians(self.angle)) 
        fc = 30 * np.array([fc_x,fc_y])
        frontCar = np.add(self.center,fc)
        print(frontCar)
        lineFront = self.CV.create_line(frontCar[0],frontCar[1],lh[0],lh[1],fill = 'red')
        ld = L 
        eld = np.linalg.norm(frontCar-lh)
        alpha = math.degrees(np.arcsin(eld/ld))
        textELD = self.CV.create_text(35,95, text= 'eld = {:.3f}'.format(eld))
        textAlpha = self.CV.create_text(30,110, text= 'α = {:.3f}'.format(alpha))
        """
        for i in range(10):
            self.CV.tag_raise(self.carBot) 
            self.CV.move(self.carBot,10,-10)
            time.sleep(1)
            self.CV.update()
        """

    def create_circle(self,x, y, r, canvasName): 
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, outline = 'green')

    def createCarBot(self,x,y,angle):  
        Carbot = [[x,y-10],[x+30,y-10],[x+30,y+10],[x,y+10]]
        return Carbot
        
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




if __name__ == "__main__":

    gui = tkinter.Tk()
    gui.title('PyPursuit Simmulation Pure Pursuit Path tracking')
    gui.geometry('500x500')
    sim = pyPursuit(gui)
    gui.mainloop()