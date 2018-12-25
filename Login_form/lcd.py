from tkinter import*
from tkinter.ttk import *

mGui = Tk()

mGui.geometry('450x450')
mGui.title('Hanix Downloader')
style = Style()
style.configure("BW.TLabel", foreground="green", background="white",font =("Time",16,'bold'))

l1 = Label(text="Test", style="BW.TLabel").pack()
l2 = Label(text="Test", style="BW.TLabel").pack()

# mpb = Progressbar(mGui,orient ="horizontal",length = 200, mode ="determinate")
# mpb.pack()
# mpb["maximum"] = 100

mGui.mainloop()