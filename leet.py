from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert box","Stop")

but=Button(root,text="Ok",command=msg())
but.place(x=100,y=100)
root.mainloop()