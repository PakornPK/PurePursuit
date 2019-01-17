import tkinter 
import time 

root = tkinter.Tk()
time1 = ''

cv = tkinter.Canvas(root,width =500 ,height = 500, bg = 'red')
cv.pack
def tick():

    while 1 : 
        trigger = True 
        if trigger : 
            trigger = False
            cv.config(bg = 'green')
            cv.after(500,tick)
        elif not trigger: 
            trigger = True
            cv.config(bg = 'blue')
            cv.after(500,tick)

tick()

root.mainloop()