from tkinter import *

def creat_resgister():
	global frame;
	frame.destroy();
	print("Da pha huy frame")
win = Tk();
win.title("Windows");
win.geometry("300x100");
win.resizable(height = False,width = False)
frame = Frame(win);
frame.pack();
lbl_fistname = Label(frame,text = "Fist Name:");
lbl_middlename = Label(frame,text = "Middle Name:")
lbl_surname = Label(frame,text = "Surname: ")

btn_login = Button(frame,text = "Login",command = creat_resgister);

ety_fisrtname = Entry(frame);
ety_midldletname = Entry(frame);
ety_surname = Entry(frame);

lbl_fistname.grid(row = 0,column = 0)
lbl_middlename.grid(row = 1, column = 0)
lbl_surname.grid(row = 2, column = 0)


ety_fisrtname.grid(row = 0,column = 1)
ety_midldletname.grid(row = 1,column = 1)
ety_surname.grid(row = 2,column = 1)

btn_login.grid(row = 3,column = 1)

win.mainloop()