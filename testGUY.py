from cProfile import label
from tkinter import *
win = Tk()
win.title("Pogoda Program")
win.geometry("500x300")
win.resizable(False,False) #Заборона зміни розміру вікна
nap = label(win, text="текст для напису")
nap.place(relx=0.1, relx=0.4)
win.mainloop()