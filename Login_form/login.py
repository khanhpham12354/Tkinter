from tkinter import*
from tkinter import messagebox
import os
import sqlite3 as sql
import time
from PIL import ImageTk,Image
data_pwd = {}
data_age = {}
data_sex = {}
data_img = {}
img = [0]
def login_init():
	global app;
	app = Tk();
	app.title("Login");
	app.geometry("400x150+420+270");
	app.resizable(height= False,width = False);
	app.iconbitmap("photos/lcd.ico");
def quit():
	 x = messagebox.askokcancel("Quit","Do you want to quit?");
	 if(x==True):
	 	exit();
def login_susscues():
	global user_name; 
	user_name = user.get().lower();
	pwd = password.get().lower();
	if user_name in data_pwd and data_pwd[user_name]==pwd:
		messagebox.showinfo("Success","Successfully!!!")
		file_path = "access_log.txt";
		file_log = open(file_path,mode = 'a');
		file_log.write(user_name.title() + " login at " +  time.ctime() + "\n");
		file_log.close();
		app.destroy();
		ui_init();
		ui_setup();
	else:
		if user_name not in data_pwd:
			messagebox.showerror("Error","Incorrect Username!");
		else:
			messagebox.showerror("Error","Incorrect Password!");
def login_setup():
	global user,password;
	user = StringVar();
	password = StringVar();
	frame_1 = Frame(app);
	frame_1.pack();
	lbl_user = Label(frame_1,text = "User:",bg = "white",fg= "black",font=("Times",16,'bold'));
	lbl_pass = Label(frame_1,text = "Password:",bg="white",fg = "black",font=("Times",16,'bold'));

	etn_user = Entry(frame_1,font=("Times",16,'bold'),justify= RIGHT,textvariable = user);
	etn_pass = Entry(frame_1,font=("Times",16,'bold'),justify = RIGHT,show ='*',textvariable = password);

	lbl_user.grid(row = 0,column = 0);
	lbl_pass.grid(row = 1,column = 0);

	etn_user.grid(row = 0,column = 1);
	etn_pass.grid(row = 1,column = 1);

	frame_2 = Frame(app);
	frame_2.place(x=110,y=70);
	frame_3 = Frame(frame_2,height = 10,width = 40)
	btn_login = Button(frame_2,text = "Login",font=("Times",16,'bold'),bd = 5,padx =20,activebackground = "green",command = login_susscues)
	btn_quit = Button(frame_2,text = "Quit",font=("Times",16,'bold'),bg = "black",fg = "white",activebackground = "red",bd = 5,padx =20,command = quit);


	btn_login.grid(row = 0,column = 0);
	frame_3.grid(row = 0,column = 1);
	btn_quit.grid(row = 0,column = 2);

def ui_init():
	global ui;
	ui = Tk();
	ui.title("Resum");
	ui.resizable(height = False,width = False);
	ui.geometry("800x600+420+270");
	#ui.iconbitmap();
def ui_setup():
	global male_var,female_var,age,img_path;
	age = StringVar();
	age = data_age[user_name];
	male_var = BooleanVar();
	female_var = BooleanVar();
	img[0] = ImageTk.PhotoImage(Image.open(data_img[user_name]));
	img_path = img[0];
	if data_sex[user_name] == '1':
		female_var.set(False);
		male_var.set(True);
	else:
		female_var.set(True);
		male_var.set(False);
	# frame 1 set up
	frame_1 = Frame(ui);
	frame_1.place(x = 0,y = 0);
	canvas_1 = Canvas(frame_1,height = 400,width = 400,bg = "white")
	picture = canvas_1.create_image(0,0,anchor = NW,image = img_path);
	canvas_1.pack();

	#frame 2 set up
	frame_2 = Frame(ui);
	frame_2.place(x = 400,y = 0);

	lbl_user = Label(frame_2,text = "Name:",bg = "white",fg= "black",font=("Times",16,'bold'),anchor = NW,padx = 15,pady = 15);
	lbl_age = Label(frame_2,text = "Age:",bg="white",fg = "black",font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW);
	lbl_sex = Label(frame_2,text = "Sex:",bg="white",fg = "black",font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW);
	
	btn_user = Label(frame_2,text =user_name.title(),font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW,height = 1,width = 20);
	btn_age = Label(frame_2,text = age,font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW,height = 1,width = 20);
	ckmale = Checkbutton(frame_2, text='Male',font=("Times",16,'bold'),state =DISABLED,onvalue=True,variable = male_var);
	ckfemale = Checkbutton(frame_2,text = 'Female',font=("Times",16,'bold'),state = DISABLED,onvalue=True,variable = female_var);
	

	lbl_user.grid(row = 0,column = 0);
	lbl_age.grid(row = 1,column = 0);
	lbl_sex.grid(row = 2,column = 0);

	btn_user.grid(row = 0,column = 1,columnspan = 2);
	btn_age.grid(row = 1,column = 1,columnspan = 2);

	ckmale.grid(row = 2,column = 1);
	ckfemale.grid(row = 2,column = 2);
	
	#frame 3 set up
	frame_3  = Frame(ui);
	frame_3.place(x = 0 ,y = 400);
	image3 = Canvas(frame_3,height = 200,width = 800,bg = "blue")
	image3.pack();
# intit database
def data_init():
	global data;
	path  = os.path.dirname(__file__) + "\\data_user.db";
	con = sql.connect(path);
	with con:
		cur  = con.cursor();
		cur.execute("SELECT* FROM customer");
		rows = cur.fetchall();
		for i in range(0,len(rows)):
			data_pwd[rows[i][1]] = rows[i][2];
			data_age[rows[i][1]] = rows[i][3];
			data_sex[rows[i][1]] = rows[i][4];
			data_img[rows[i][1]] = rows[i][5];
		# print(data_pwd)
		# print(data_age)
		# print(data_sex)
		# print(data_img)
	con.close();

if __name__ == '__main__':
	data_init();
	login_init();
	login_setup();
	mainloop();