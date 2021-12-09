from tkinter import *

root = Tk()

root.title("TITle")
root.geometry("420x69")

e1=Entry(root)
e2=Entry(root)

l1 =Label(root, text="Email:")
l2 =Label(root, text="Password:")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1.grid(row=1, column=1)
e2.grid(row=0, column=1)

root.title("Login")
b=Button(text="Skicka", fg="#ffffff", bg="#000000")
b.grid(row=2, column=1)


root.mainloop()
