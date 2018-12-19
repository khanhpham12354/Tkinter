from tkinter import*

class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill = BOTH,expand = 1)
        quitButton = Button(self, text = "Quit",width = "8",height = "4",fg= "green",bg= "black")
        quitButton.place(x=0,y=0)
        enterButton = Button(self,text = "Enter")
        enterButton.place(x=160,y=0)
root = Tk()
root.geometry("200x200")
app = Window(root)
root.mainloop()
