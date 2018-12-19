from tkinter import*

master = Tk()

frame = Frame(height = "400",width = "400")
frame.pack()
frame.config(bg="green")
btn_1 = Button(frame,text = "Test")
btn_1.pack()
master.mainloop()