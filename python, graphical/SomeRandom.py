# coding=utf-8
from tkinter import *

root = Tk()

def myClick():
	l = Label(root, text="Hejsan svejsan")
	l.pack()

myButton = Button(root, text="klicka på mig",command=myClick, bg="yellow", fg="blue")
myButton.pack()

root.mainloop()
