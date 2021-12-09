from tkinter import *
import tkinter as tk


root=Tk()

root.geometry("666x911")

v=tk.IntVar()

mb=MenuButton(root, text="Det är en meny")
mb.meny=Menu(mb)
mb["Menu"]=mb.menu


root.mainloop()
