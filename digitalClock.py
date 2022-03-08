from cgitb import text
from tkinter import *
import time
from tkinter import font 
# 
root = Tk ()
root.title("DIGITAL CLOCK (@MondalCodeHub)")
root.iconbitmap('clock.ico')
root.geometry('1080x333')
root.maxsize(1080,301)
root.minsize(1080,299)
# 
clock = Label(root, font='comicsansms 200 bold', bg='black', foreground='red')
clock.grid(row=0, column=1)
# textVar = Label(root,text="MondalCodeHUb", font='comicsansms 10 bold',bg='black', foreground='red')
# textVar.grid(row=1,column=1)
# 
def digitalClockFunc():
    currentTime = time.strftime("%H:%M:%S")
    clock.config(text=currentTime)
    clock.after(200,digitalClockFunc)
digitalClockFunc()
# 
root.mainloop()