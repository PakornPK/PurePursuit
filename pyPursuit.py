import tkinter
from tkinter import ttk 
from threading import Thread
from random import randint
import numpy as np 
import time 
import math
	
        
            

class pyPursuit(tkinter.Frame):
    def __init__(self, master): 
        super(pyPursuit, self).__init__(master)
        self.angle = 0
        self.center = [100,430]
        self.loop = True
        self.LH = 60
        self.grid()
        self.CV = tkinter.Canvas(width=1000, height=500, bg = 'pink')
        self.CV.grid()
        self._run()
        #self.right_run()
        #self.lelf_run()
        #self.down_run()
        #self.top_run()

    def _run(self): 
        for f in range(23):
            self.down_run()
            time.sleep(0.1)
            self.CV.update()
        for s in range(10):
            self.d2r()
            time.sleep(0.1)
            self.CV.update()
        for t in range(15):
            self.right_run()
            time.sleep(0.1)
            self.CV.update()

        for fo in range(13):
            self.d2r()
            time.sleep(0.1)
            self.CV.update()

        for fi in range(20):
            self.top_run()
            time.sleep(0.1)
            self.CV.update()

        for si in range(13):
            self.d2r()
            time.sleep(0.1)
            self.CV.update()

        for se in range(13):
            self.lelf_run()
            time.sleep(0.1)
            self.CV.update()

        for si in range(10):
            self.d2r()
            time.sleep(0.1)
            self.CV.update()

        """
        if self.loop :  
            self.CV.after(1000,self._run)"""

    def right_run(self): 
        self.CV.delete('all')
        self.poly = self.createCarBot(self.center[0],self.center[1],self.angle)
        self.shortate = np.linalg.norm(self.center[0]-400) # constance x

        path_Line1 = self.CV.create_line(100,100,100,400)
        path_Line2 = self.CV.create_line(400,100,400,400)
        path_Line3 = self.CV.create_line(100,100,400,100)
        path_Line4 = self.CV.create_line(100,400,400,400)
        textPath1 = self.CV.create_text(100,90,text='(100,100)',fill ='blue')
        textPath2 = self.CV.create_text(400,90,text='(400,100)',fill ='blue')
        textPath3 = self.CV.create_text(400,410,text='(400,400)',fill ='blue')
        textPath4 = self.CV.create_text(100,410,text='(100,400)',fill ='blue')
        textSh = self.CV.create_text(45,20,text = 'Shortate = {:.3f}' .format(self.shortate))
        textLH = self.CV.create_text(50,35,text = 'Look ahead = {}'.format(self.LH))

        try : 
            L = 0 
            R = 0 
            ct =0 
            lh = 0
            d =0
            ct = np.array(self.center)
            lh = np.array([400.0,self.center[1]-self.LH])
            L = np.linalg.norm(ct-lh)
            textL = self.CV.create_text(35,50,text = 'L = {0:.3f}'.format(L))
            R = np.square(L)/(2*self.shortate)
            D = R-self.shortate 
            textR = self.CV.create_text(35,65,text = 'R = {0:.3f}'.format(R))
            textSpeed = self.CV.create_text(44,80, text = 'Speed = 2 m/s')

            
            textCenter = "({0:.3f},{1:.3f},Φ={2:.3f})".format(self.center[0],self.center[1],self.angle)
            textcar = self.CV.create_text(self.center[0],self.center[1]+5,text= textCenter)
            lineLH = self.CV.create_line(400,self.center[1],400,self.center[1]-self.LH, fill = 'green')
            lineL = self.CV.create_line(self.center[0],self.center[1],400,self.center[1]-self.LH, fill = 'green')

            fc_x = math.cos(math.radians(self.angle))
            fc_y = math.sin(math.radians(self.angle)) 
            fc = 30 * np.array([fc_x,fc_y])
            frontCar = np.add(self.center,fc)
            lineFront = self.CV.create_line(frontCar[0],frontCar[1],lh[0],lh[1],fill = 'red')
            ld = L 
            eld = np.linalg.norm(frontCar-lh)
            
            alpha = math.degrees(np.arcsin(eld/ld))
            K = (2*np.sin(math.radians(alpha)))/ld
            zixmar = math.degrees(np.arctan(K*30))
            textZixmar = self.CV.create_text(30,125, text = 'δ = {:.3f}'.format(zixmar))
            textELD = self.CV.create_text(35,95, text= 'eld = {:.3f}'.format(eld))
            textAlpha = self.CV.create_text(30,110, text= 'α = {:.3f}'.format(alpha))

            
                

            deff_x = math.degrees(0.2*np.cos(math.radians(self.angle)))
            deff_y = math.degrees(0.2*np.sin(math.radians(self.angle)))
            deff_phi = math.degrees((0.2/3)*np.tan(math.radians(zixmar)))
            
            if self.center[0] < 400 : 
                lineR = self.CV.create_line(self.center[0],self.center[1],self.center[0]+R,self.center[1], fill = 'green')
                textCenterR = self.CV.create_text(self.center[0]+R,self.center[1],text = '({0:.3f},{1:.3f})'.format(400+D,self.center[1]))
                circle = self.create_circle(self.center[0]+R,self.center[1],R,self.CV)
            else:
                lineR = self.CV.create_line(self.center[0],self.center[1],self.center[0]-R,self.center[1], fill = 'green')
                textCenterR = self.CV.create_text(self.center[0]-R,self.center[1],text = '({0:.3f},{1:.3f})'.format(400-D,self.center[1]))
                circle = self.create_circle(self.center[0]-R,self.center[1],R,self.CV)

            self.poly = self.rotate(self.poly,self.angle,tuple(self.center))
            self.carBot = self.CV.create_polygon(self.poly, fill = 'yellow' ,outline = 'black')
            
            if  self.center[0] < 400 :

                self.center[0] = self.center[0]+deff_x
                self.center[1] = self.center[1]+deff_y
                self.angle = self.angle + deff_phi
                #print('X = {0:.3f}, Y = {1:.3f}, Φ = {2:.3f}'.format(self.center[0]-deff_x,self.center[1]+deff_y,self.angle+deff_phi))
                
            else:
                self.center[0] = self.center[0]+deff_x
                self.center[1] = self.center[1]+deff_y
                self.angle = self.angle - deff_phi
                #print('X = {0:.3f}, Y = {1:.3f}, Φ = {2:.3f}'.format(self.center[0]+deff_x,self.center[1]+deff_y,self.angle-deff_phi))
        

            
        except: 
            raise
        
    def lelf_run(self): 
        self.CV.delete('all')
        self.poly = self.createCarBot(self.center[0],self.center[1],self.angle)
        self.shortate = np.linalg.norm(self.center[0]-100) # constance x

        path_Line1 = self.CV.create_line(100,100,100,400)
        path_Line2 = self.CV.create_line(400,100,400,400)
        path_Line3 = self.CV.create_line(100,100,400,100)
        path_Line4 = self.CV.create_line(100,400,400,400)
        textPath1 = self.CV.create_text(100,90,text='(100,100)',fill ='blue')
        textPath2 = self.CV.create_text(400,90,text='(400,100)',fill ='blue')
        textPath3 = self.CV.create_text(400,410,text='(400,400)',fill ='blue')
        textPath4 = self.CV.create_text(100,410,text='(100,400)',fill ='blue')
        textSh = self.CV.create_text(45,20,text = 'Shortate = {:.3f}' .format(self.shortate))
        textLH = self.CV.create_text(50,35,text = 'Look ahead = {}'.format(self.LH))

        try : 
            L = 0 
            R = 0 
            ct =0 
            lh = 0
            d = 0
            ct = np.array(self.center)
            lh = np.array([100.0,self.center[1]+self.LH])
            L = np.linalg.norm(ct-lh)
            textL = self.CV.create_text(35,50,text = 'L = {0:.3f}'.format(L))
            R = np.square(L)/(2*self.shortate)
            D = R-self.shortate 
            textR = self.CV.create_text(35,65,text = 'R = {0:.3f}'.format(R))
            textSpeed = self.CV.create_text(44,80, text = 'Speed = 2 m/s')

            
            textCenter = "({0:.3f},{1:.3f},Φ={2:.3f})".format(self.center[0],self.center[1],self.angle)
            textcar = self.CV.create_text(self.center[0],self.center[1]+5,text= textCenter)
            lineLH = self.CV.create_line(100,self.center[1],100,self.center[1]+self.LH, fill = 'green')
            lineL = self.CV.create_line(self.center[0],self.center[1],100,self.center[1]+self.LH, fill = 'green')

            fc_x = math.cos(math.radians(self.angle))
            fc_y = math.sin(math.radians(self.angle)) 
            fc = 30 * np.array([fc_x,fc_y])
            frontCar = np.add(self.center,fc)
            lineFront = self.CV.create_line(frontCar[0],frontCar[1],lh[0],lh[1],fill = 'red')
            ld = L 
            eld = np.linalg.norm(frontCar-lh)
            alpha = math.degrees(np.arcsin(eld/ld))
            K = (2*np.sin(math.radians(alpha)))/ld
            zixmar = math.degrees(np.arctan(K*30))
            textZixmar = self.CV.create_text(30,125, text = 'δ = {:.3f}'.format(zixmar))
            textELD = self.CV.create_text(35,95, text= 'eld = {:.3f}'.format(eld))
            textAlpha = self.CV.create_text(30,110, text= 'α = {:.3f}'.format(alpha))

            deff_x = math.degrees(0.2*np.cos(math.radians(self.angle)))
            deff_y = math.degrees(0.2*np.sin(math.radians(self.angle)))
            deff_phi = math.degrees((0.2/3)*np.tan(math.radians(zixmar)))
            
            if self.center[0] < 100 : 
                lineR = self.CV.create_line(self.center[0],self.center[1],self.center[0]+R,self.center[1], fill = 'green')
                textCenterR = self.CV.create_text(self.center[0]+R,self.center[1],text = '({0:.3f},{1:.3f})'.format(100+D,self.center[1]))
                circle = self.create_circle(self.center[0]+R,self.center[1],R,self.CV)
            else:
                lineR = self.CV.create_line(self.center[0],self.center[1],self.center[0]-R,self.center[1], fill = 'green')
                textCenterR = self.CV.create_text(self.center[0]-R,self.center[1],text = '({0:.3f},{1:.3f})'.format(100-D,self.center[1]))
                circle = self.create_circle(self.center[0]-R,self.center[1],R,self.CV)

            self.poly = self.rotate(self.poly,self.angle,tuple(self.center))
            self.carBot = self.CV.create_polygon(self.poly, fill = 'yellow' ,outline = 'black')
            if  self.center[0] > 100 :

                self.center[0] = self.center[0]+deff_x
                self.center[1] = self.center[1]+deff_y
                self.angle = self.angle + deff_phi
                #print('X = {0:.3f}, Y = {1:.3f}, Φ = {2:.3f}'.format(self.center[0]-deff_x,self.center[1]+deff_y,self.angle+deff_phi))
                
            else:
                self.center[0] = self.center[0]+deff_x
                self.center[1] = self.center[1]+deff_y
                self.angle = self.angle - deff_phi
                #print('X = {0:.3f}, Y = {1:.3f}, Φ = {2:.3f}'.format(self.center[0]+deff_x,self.center[1]+deff_y,self.angle-deff_phi))
            
            
        except: 
            raise
      
    def down_run(self): 
        self.CV.delete('all')
        self.poly = self.createCarBot(self.center[0],self.center[1],self.angle)
        self.shortate = np.linalg.norm(self.center[1]-400) # constance x

        path_Line1 = self.CV.create_line(100,100,100,400)
        path_Line2 = self.CV.create_line(400,100,400,400)
        path_Line3 = self.CV.create_line(100,100,400,100)
        path_Line4 = self.CV.create_line(100,400,400,400)
        textPath1 = self.CV.create_text(100,90,text='(100,100)',fill ='blue')
        textPath2 = self.CV.create_text(400,90,text='(400,100)',fill ='blue')
        textPath3 = self.CV.create_text(400,410,text='(400,400)',fill ='blue')
        textPath4 = self.CV.create_text(100,410,text='(100,400)',fill ='blue')
        textSh = self.CV.create_text(45,20,text = 'Shortate = {:.3f}' .format(self.shortate))
        textLH = self.CV.create_text(50,35,text = 'Look ahead = {}'.format(self.LH))

        try : 
            L = 0 
            R = 0 
            ct =0 
            lh = 0
            d = 0
            ct = np.array(self.center)
            lh = np.array([self.center[0]+self.LH,400.0]) ### 
            L = np.linalg.norm(ct-lh)
            textL = self.CV.create_text(35,50,text = 'L = {0:.3f}'.format(L))
            R = np.square(L)/(2*self.shortate)
            D = R-self.shortate 
            textR = self.CV.create_text(35,65,text = 'R = {0:.3f}'.format(R))
            textSpeed = self.CV.create_text(44,80, text = 'Speed = 2 m/s')

            
            textCenter = "({0:.3f},{1:.3f},Φ={2:.3f})".format(self.center[0],self.center[1],self.angle)
            textcar = self.CV.create_text(self.center[0],self.center[1]+5,text= textCenter)
            lineLH = self.CV.create_line(self.center[0],400,self.center[0]+self.LH,400, fill = 'green')
            lineL = self.CV.create_line(self.center[0],self.center[1],self.center[0]+self.LH,400, fill = 'green')

            fc_x = math.cos(math.radians(self.angle))
            fc_y = math.sin(math.radians(self.angle)) 
            fc = 30 * np.array([fc_x,fc_y])
            frontCar = np.add(self.center,fc)
            lineFront = self.CV.create_line(frontCar[0],frontCar[1],lh[0],lh[1],fill = 'red')
            ld = L 
            eld = np.linalg.norm(frontCar-lh)
            alpha = math.degrees(np.arcsin(eld/ld))
            K = (2*np.sin(math.radians(alpha)))/ld
            zixmar = math.degrees(np.arctan(K*30))
            textZixmar = self.CV.create_text(30,125, text = 'δ = {:.3f}'.format(zixmar))
            textELD = self.CV.create_text(35,95, text= 'eld = {:.3f}'.format(eld))
            textAlpha = self.CV.create_text(30,110, text= 'α = {:.3f}'.format(alpha))

            deff_x = math.degrees(0.2*np.cos(math.radians(self.angle)))
            deff_y = math.degrees(0.2*np.sin(math.radians(self.angle)))
            deff_phi = math.degrees((0.2/3)*np.tan(math.radians(zixmar)))
            
            if self.center[1] < 400 : 
                lineR = self.CV.create_line(self.center[0],self.center[1],self.center[0],self.center[1]+R, fill = 'green')
                textCenterR = self.CV.create_text(self.center[0],self.center[1]+R,text = '({0:.3f},{1:.3f})'.format(400+D,self.center[1]))
                circle = self.create_circle(self.center[0],self.center[1]+R,R,self.CV)
            else:
                lineR = self.CV.create_line(self.center[0],self.center[1],self.center[0],self.center[1]-R, fill = 'green')
                textCenterR = self.CV.create_text(self.center[0],self.center[1]-R,text = '({0:.3f},{1:.3f})'.format(400+D,self.center[1]))
                circle = self.create_circle(self.center[0],self.center[1]-R,R,self.CV)

            self.poly = self.rotate(self.poly,self.angle,tuple(self.center))
            self.carBot = self.CV.create_polygon(self.poly, fill = 'yellow' ,outline = 'black')
            if  self.center[1] < 400 :

                self.center[0] = self.center[0]+deff_x
                self.center[1] = self.center[1]+deff_y
                self.angle = self.angle + deff_phi
                #print('X = {0:.3f}, Y = {1:.3f}, Φ = {2:.3f}'.format(self.center[0]-deff_x,self.center[1]+deff_y,self.angle+deff_phi))
                
            else:
                self.center[0] = self.center[0]+deff_x
                self.center[1] = self.center[1]+deff_y
                self.angle = self.angle - deff_phi
                #print('X = {0:.3f}, Y = {1:.3f}, Φ = {2:.3f}'.format(self.center[0]+deff_x,self.center[1]+deff_y,self.angle-deff_phi))
            
            
        except: 
            raise
               
    def top_run(self): 
        self.CV.delete('all')
        self.poly = self.createCarBot(self.center[0],self.center[1],self.angle)
        self.shortate = np.linalg.norm(self.center[1]-100) # constance x

        path_Line1 = self.CV.create_line(100,100,100,400)
        path_Line2 = self.CV.create_line(400,100,400,400)
        path_Line3 = self.CV.create_line(100,100,400,100)
        path_Line4 = self.CV.create_line(100,400,400,400)
        textPath1 = self.CV.create_text(100,90,text='(100,100)',fill ='blue')
        textPath2 = self.CV.create_text(400,90,text='(400,100)',fill ='blue')
        textPath3 = self.CV.create_text(400,410,text='(400,400)',fill ='blue')
        textPath4 = self.CV.create_text(100,410,text='(100,400)',fill ='blue')
        textSh = self.CV.create_text(45,20,text = 'Shortate = {:.3f}' .format(self.shortate))
        textLH = self.CV.create_text(50,35,text = 'Look ahead = {}'.format(self.LH))

        try : 
            L = 0 
            R = 0 
            ct =0 
            lh = 0
            d = 0
            ct = np.array(self.center)
            lh = np.array([self.center[0]-self.LH,100.0]) ### 
            L = np.linalg.norm(ct-lh)
            textL = self.CV.create_text(35,50,text = 'L = {0:.3f}'.format(L))
            R = np.square(L)/(2*self.shortate)
            D = R-self.shortate 
            textR = self.CV.create_text(35,65,text = 'R = {0:.3f}'.format(R))
            textSpeed = self.CV.create_text(44,80, text = 'Speed = 2 m/s')

            
            textCenter = "({0:.3f},{1:.3f},Φ={2:.3f})".format(self.center[0],self.center[1],self.angle)
            textcar = self.CV.create_text(self.center[0],self.center[1]+5,text= textCenter)
            lineLH = self.CV.create_line(self.center[0],100,self.center[0]-self.LH,100, fill = 'green')
            lineL = self.CV.create_line(self.center[0],self.center[1],self.center[0]-self.LH,100, fill = 'green')

            fc_x = math.cos(math.radians(self.angle))
            fc_y = math.sin(math.radians(self.angle)) 
            fc = 30 * np.array([fc_x,fc_y])
            frontCar = np.add(self.center,fc)
            lineFront = self.CV.create_line(frontCar[0],frontCar[1],lh[0],lh[1],fill = 'red')
            ld = L 
            eld = np.linalg.norm(frontCar-lh)
            alpha = math.degrees(np.arcsin(eld/ld))
            K = (2*np.sin(math.radians(alpha)))/ld
            zixmar = math.degrees(np.arctan(K*30))
            textZixmar = self.CV.create_text(30,125, text = 'δ = {:.3f}'.format(zixmar))
            textELD = self.CV.create_text(35,95, text= 'eld = {:.3f}'.format(eld))
            textAlpha = self.CV.create_text(30,110, text= 'α = {:.3f}'.format(alpha))

            deff_x = math.degrees(0.2*np.cos(math.radians(self.angle)))
            deff_y = math.degrees(0.2*np.sin(math.radians(self.angle)))
            deff_phi = math.degrees((0.2/3)*np.tan(math.radians(zixmar)))
            
            if self.center[1] < 100 : 
                lineR = self.CV.create_line(self.center[0],self.center[1],self.center[0],self.center[1]+R, fill = 'green')
                textCenterR = self.CV.create_text(self.center[0],self.center[1]+R,text = '({0:.3f},{1:.3f})'.format(100+D,self.center[1]))
                circle = self.create_circle(self.center[0],self.center[1]+R,R,self.CV)
            else:
                lineR = self.CV.create_line(self.center[0],self.center[1],self.center[0],self.center[1]-R, fill = 'green')
                textCenterR = self.CV.create_text(self.center[0],self.center[1]-R,text = '({0:.3f},{1:.3f})'.format(100+D,self.center[1]))
                circle = self.create_circle(self.center[0],self.center[1]-R,R,self.CV)

            self.poly = self.rotate(self.poly,self.angle,tuple(self.center))
            self.carBot = self.CV.create_polygon(self.poly, fill = 'yellow' ,outline = 'black')
            if  self.center[1] > 100 :

                self.center[0] = self.center[0]+deff_x
                self.center[1] = self.center[1]+deff_y
                self.angle = self.angle + deff_phi
                #print('X = {0:.3f}, Y = {1:.3f}, Φ = {2:.3f}'.format(self.center[0]-deff_x,self.center[1]+deff_y,self.angle+deff_phi))
                
            else:
                self.center[0] = self.center[0]+deff_x
                self.center[1] = self.center[1]+deff_y
                self.angle = self.angle - deff_phi
                #print('X = {0:.3f}, Y = {1:.3f}, Φ = {2:.3f}'.format(self.center[0]+deff_x,self.center[1]+deff_y,self.angle-deff_phi))
            
            
        except: 
            raise
                
    def d2r(self): 
        self.CV.delete('all')
        self.poly = self.createCarBot(self.center[0],self.center[1],self.angle)
        

        path_Line1 = self.CV.create_line(100,100,100,400)
        path_Line2 = self.CV.create_line(400,100,400,400)
        path_Line3 = self.CV.create_line(100,100,400,100)
        path_Line4 = self.CV.create_line(100,400,400,400)
        textPath1 = self.CV.create_text(100,90,text='(100,100)',fill ='blue')
        textPath2 = self.CV.create_text(400,90,text='(400,100)',fill ='blue')
        textPath3 = self.CV.create_text(400,410,text='(400,400)',fill ='blue')
        textPath4 = self.CV.create_text(100,410,text='(100,400)',fill ='blue')
        textSh = self.CV.create_text(45,20,text = 'Shortate = {:.3f}' .format(self.shortate))
        textLH = self.CV.create_text(50,35,text = 'Look ahead = {}'.format(self.LH))

        try : 
           
            deff_x = math.degrees(0.2*np.cos(math.radians(self.angle)))
            deff_y = math.degrees(0.2*np.sin(math.radians(self.angle)))
            deff_phi = math.degrees((0.2/3)*np.tan(math.radians(60)))

            self.poly = self.rotate(self.poly,self.angle,tuple(self.center))
            self.carBot = self.CV.create_polygon(self.poly, fill = 'yellow' ,outline = 'black')
           
            self.center[0] = self.center[0]+deff_x
            self.center[1] = self.center[1]+deff_y
            self.angle = self.angle - deff_phi
            
            
        except: 
            raise



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
    gui.geometry('1000x500')
    sim = pyPursuit(gui)
gui.mainloop()