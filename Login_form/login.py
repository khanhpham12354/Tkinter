from tkinter import*
from tkinter import messagebox
import os
data = {'pham duc khanh':'123456','dinh duy nam':'123321'}

# intit login form
def login_init():
	global app;
	app = Tk();
	app.title("Login");
	app.geometry("400x150");
	app.resizable(height= False,width = False);
	app.iconbitmap("photos/lcd.ico");
def quit():
	exit();
def login_susscues():
	user_name = user.get().lower();
	pwd = password.get().lower();
	if user_name in data and data[user_name]==pwd:
		messagebox.showinfo("Success","Successfully!!!")
		app.destroy();
		os.system("python lcd.py");
	else:
		if user_name not in data:
			messagebox.showerror("Error","Incorrect Username!");
		else:
			messagebox.showerror("Error","Incorrect Password!");
def login_setup():
	global user,password;
	user = StringVar();
	password = StringVar();
	frame_1 = Frame(app);
	frame_1.pack();
	lbl_user = Label(frame_1,text = "User:",bg = "white",fg= "black",font=("Times",16,'bold'),);
	lbl_pass = Label(frame_1,text = "Password:",bg="white",fg = "black",font=("Times",16,'bold'));

	etn_user = Entry(frame_1,font=("Times",16,'bold'),justify= RIGHT,textvariable = user);
	etn_pass = Entry(frame_1,font=("Times",16,'bold'),justify = RIGHT,show ='*',textvariable = password);

	lbl_user.grid(row = 0,column = 0);
	lbl_pass.grid(row = 1,column = 0);

	etn_user.grid(row = 0,column = 1);
	etn_pass.grid(row = 1,column = 1);

	frame_2 = Frame(app);
	frame_2.place(x=110,y=70);
	frame_3 = Frame(frame_2,height = 10,width = 30)
	btn_login = Button(frame_2,text = "Login",font=("Times",16,'bold'),bd = 5,padx =20,activebackground = "green",command = login_susscues)
	btn_quit = Button(frame_2,text = "Quit",font=("Times",16,'bold'),bg = "black",fg = "white",activebackground = "red",bd = 5,padx =20,command = quit);


	btn_login.grid(row = 0,column = 0);
	frame_3.grid(row = 0,column = 1)
	btn_quit.grid(row = 0,column = 2);

if __name__ == '__main__':
	login_init();
	login_setup();
	app.mainloop();