from tkinter import *

root = Tk()

root.geometry("300x300")

text = "Hello World"

l = Label(root, text="Nästa Hello World!")
l.pack(side=TOP)

b = Button(root, text="klicka här")
b.pack()

def test():
	print("test output")

b2 = Button(root, text="2", command=test)
b2.pack()

root.mainloop()
