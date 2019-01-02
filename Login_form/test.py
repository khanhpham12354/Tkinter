from tkinter import ttk
from tkinter import *
import time
root = Tk()
def next():
	global pb;
	pb.step(4)

x = IntVar(0);
x.set(0)
pb = ttk.Progressbar(root, orient="horizontal", length=125, mode="determinate",variable = x)
pb.pack()
btn = Button(root,text = "press me",command = next);
btn.pack();

root.mainloop()