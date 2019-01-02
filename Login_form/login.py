from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3 as sql
import time
import datetime
from PIL import ImageTk,Image
from threading import*
import random
from playsound import playsound
from gtts import gTTS

check_status = True
data_pwd = {}
data_age = {}
data_sex = {}
data_img = {}
data_word = {}
data_translate = {}
global stt,qus,max_stt;
max_stt = 125
stt = 0
img = [0]
'''
	init form origant
'''
def login_init():
	global app;
	app = Tk();
	app.title("Login");
	app.geometry("400x150+420+270");
	app.resizable(height= False,width = False);
	app.iconbitmap("photos/k.ico");
	app.protocol("WM_DELETE_WINDOW",quit)
def quit():
	 x = messagebox.askokcancel("Quit","Do you want to quit?");
	 if(x == True):
	 	t.cancel();
	 	t1.cancel();
	 	check_status = False
	 	try:
	 		ui.destroy();
	 	except:
	 		print("khong co");
	 	try:
	 		app.destroy();
	 	except:
	 		print("khong co");
	 	exit();
def login_susscues():
	global user_name,times1; 
	user_name = user.get().lower();
	pwd = password.get().lower();
	if user_name in data_pwd and data_pwd[user_name]==pwd:
		file_path = "log\\access_log.txt";
		file_log = open(file_path,mode = 'a');
		file_log.write(user_name.title() + " login at " +  time.ctime() + "\n");
		file_log.close();
		app.destroy();
		ui_init();
		ui_setup();
		t.start();
		ui.mainloop();
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
def load_data():
	path  = "database\\data_newword.db";
	con = sql.connect(path);
	with con:
		cur  = con.cursor();
		cur.execute("SELECT* FROM data123");
		rows = cur.fetchall();
		for i in range(1,len(rows)+ 1):
			data_word[str(i)] = rows[i-1][1];
			data_translate[str(i)] = rows[i-1][2];
			if (os.path.isfile("speak\\" + str(data_word[str(i)]) + ".mp3")==False):
				speak = gTTS(text = data_word[str(i)], lang='en', slow=False)
				speak.save("speak\\" + str(data_word[str(i)]) + ".mp3")
		print(data_word)
		print(data_translate)
	con.close();	
def start_question():
	global stt,qus,question,ans,btn_next,sel,y,ck,progressbar;
	stt = stt + 1;
	load_data();
	score.set("0/" + str(max_stt));
	ans = [0,0,0,0];
	ck = [-1,-1,-1,-1]
	qus = '';
	sel = IntVar();
	sel.set(-1);
	question = StringVar();
	ans[0] = StringVar();
	ans[1] = StringVar();
	ans[2] = StringVar();
	ans[3] = StringVar();
	rnd = [0,0,0,0]
	# random fisrt questtion
	x = random.randint(1,len(data_word))
	qus = data_word[str(x)];
	question.set("			Question" + " " + str(stt) + ": " + qus + " ?");
	path_sp = "speak\\" + str(qus) + ".mp3"
	playsound(path_sp)
	# random location anwser correct!
	y = random.randint(0,3);
	rnd[0] = x;
	for i in range(0,4):
		#  anwser correct
		if i == y:
			ans[i].set(str(data_translate[str(x)]));
		else:
		#incorrect
			x1 = random.randint(1,len(data_word))
			while x1 in rnd:
				x1 = random.randint(1,len(data_word))
			rnd.append(x1)
			ans[i].set(str(data_translate[str(x1)]))
	#frame 3 set up
	btn_dicrect.config(state = DISABLED);
	frame_3  = Frame(ui);
	frame_3.place(x = 0 ,y = 400);
	lbl_question = Label(frame_3,textvariable = question,font=("Times",16,'bold'),justify = RIGHT);
	ck[0] = Radiobutton(frame_3,value=0,variable = sel,textvariable = ans[0],font=("Times",16,'bold'),justify = LEFT,anchor = NW,height = 1,width = 20);
	ck[1] = Radiobutton(frame_3,value=1,variable = sel,textvariable = ans[1],font=("Times",16,'bold'),justify = LEFT,anchor = W,height = 1,width = 20);
	ck[2] = Radiobutton(frame_3,value=2,variable = sel,textvariable = ans[2] ,font=("Times",16,'bold'),justify = LEFT,anchor = W,height = 1,width = 20);
	ck[3] = Radiobutton(frame_3,value=3,variable = sel,textvariable = ans[3],font=("Times",16,'bold'),justify = LEFT,anchor = NW,height = 2,width = 20);

	lbl_question.grid(row = 0,column = 0);
	frame_3.grid_columnconfigure(0,minsize = 400)
	frame_3.grid_columnconfigure(1,minsize = 400)
	frame_3.grid_rowconfigure(1,minsize = 100)
	frame_3.grid_rowconfigure(1,minsize = 50)
	frame_3.grid_rowconfigure(2,minsize = 50)

	ck[0].grid(row = 1 ,column = 0);
	ck[1].grid(row = 1,column = 1);
	ck[2].grid(row = 2,column = 0);
	ck[3].grid(row = 2,column = 1);

	btn_next = Button(ui,state = NORMAL,bg = 'white',text = "Next",activebackground = "green",font=("Times",16,'bold'),bd = 5,height = 1,width = 10,command = next_question);
	btn_next.place(x = 650, y =520)
	progressbar = ttk.Progressbar(ui,mode='determinate',orient="horizontal", length= max_stt*4 + 5,value = 0,maximum = 125)
	progressbar.place(x = 125 ,y = 535);
	progressbar.step(1);
	lbl_direct.config(fg = "green");
	t1.start();
def ui_init():
	global ui;
	ui = Tk();
	ui.title("English");
	ui.resizable(height = False,width = False);
	ui.geometry("800x600");
	ui.protocol("WM_DELETE_WINDOW",quit)
	ui.iconbitmap("photos/k.ico");
def ui_setup():
	global score_var,male_var,female_var,age,img_path,score,sel,btn_dicrect,btn_time,xxx,dir_rect,lbl_direct;
	score_var = 0;
	sel = IntVar();
	sel.set(0)
	xxx = StringVar();
	score = StringVar();
	score.set("None");
	age = StringVar();
	dir_rect = StringVar();
	male_var = BooleanVar();
	female_var = BooleanVar();
	age = data_age[user_name];
	img[0] = ImageTk.PhotoImage(Image.open(data_img[user_name]));
	img_path = img[0];
	dir_rect.set("Please press next button to run!")
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

	lbl_user = Label(frame_2,text = "Name:",fg= "black",font=("Times",16,'bold'),anchor = NW,padx = 15,pady = 15);
	lbl_age = Label(frame_2,text = "Age:",fg = "black",font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW);
	lbl_sex = Label(frame_2,text = "Sex:",fg = "black",font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW);
	lbl_score = Label(frame_2,text = "Score:",fg = "black",font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW);
	lbl_time = Label(frame_2,text = "Clock:",fg = "black",font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW);
	lbl_direct = Label(ui,justify = LEFT,textvariable = dir_rect,fg = "black",font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW);
	
	btn_user = Label(frame_2,text =user_name.title(),font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW,height = 1,width = 20);
	btn_age = Label(frame_2,text = age,font=("Times",16,'bold'),padx = 15,pady = 15,anchor = NW,height = 1,width = 20);
	btn_score = Label(frame_2,textvariable = score,font=("Times",16,'bold','italic'),height = 1,width = 20,fg = "blue");
	btn_time = Label(frame_2,textvariable = xxx,font=("Times",16,'bold'),height = 1,width = 20,fg = "#EC870E");
	btn_dicrect = Button(ui,text = "Start",bg = 'white',activebackground = "pink",font=("Times",16,'bold'),bd = 5,height = 1,width = 10,command = start_question)
	ckmale = Checkbutton(frame_2, text='Male',font=("Times",16,'bold'),state =DISABLED,onvalue=True,variable = male_var);
	ckfemale = Checkbutton(frame_2,text = 'Female',font=("Times",16,'bold'),state = DISABLED,onvalue=True,variable = female_var);
	

	lbl_user.grid(row = 0,column = 0);
	lbl_age.grid(row = 1,column = 0);
	lbl_sex.grid(row = 2,column = 0);
	lbl_time.grid(row = 3,column  = 0);
	lbl_direct.place(x = 402, y = 290)

	btn_user.grid(row = 0,column = 1,columnspan = 2);
	btn_age.grid(row = 1,column = 1,columnspan = 2);

	ckmale.grid(row = 2,column = 1);
	ckfemale.grid(row = 2,column = 2);

	btn_time.grid(row = 3,column = 1,columnspan = 2);
	lbl_score.grid(row = 4,column = 0);
	btn_score.grid(row = 4,column = 2);
	btn_dicrect.place(x = 520,y = 350);
	lbl_name = Label(ui,text = "Code and design by Pham Duc Khanh",fg = "#00CC00",font=("Times",12,'italic','bold'));
	lbl_name.place(x= 300 ,y = 570)
def final_question():
	global y,sel,score_var,progressbar;
	progressbar.step(1);
	btn_next.config(state = DISABLED,activebackground = "white" )
	btn_next.update();
	print(sel.get())
	ck[y].config(fg = "green")
	ck[y].update()
	if sel.get() == y:
		print("correct");
		t3 = Timer(0,correct);
		t3.start();
		score_var = score_var + 1;
		score.set(str(score_var) + "/" + str(max_stt));
	else:
		print("incorrect");
		t4 = Timer(0,incorrect);
		t4.start();
		ck[sel.get()].config(fg ="red");
		ck[sel.get()].update();
	result();
	file_path = "progress\\" + str(user_name) + str(".txt");
	file_progress = open(file_path,mode = 'a');
	now = datetime.datetime.now();
	file_progress.write(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "--" + str(now.day) + ":" + str(now.month) + ":" + str(now.year) +": "+ str(score.get()) + "\n");
	file_progress.close();
# intit database
def next_question():
	global stt,question,y,sel,score_var,progressbar;
	stt = stt + 1;
	progressbar.step(1);
	if stt <= max_stt:
		btn_next.config(state = NORMAL)
		btn_next.config(state = DISABLED,activebackground = "white" )
		btn_next.update();
		print(sel.get())
		ck[y].config(fg = "green")
		ck[y].update()
		if sel.get() == y:
			print("correct");
			t3 = Timer(0,correct);
			t3.start();			
			score_var = score_var + 1;
			score.set(str(score_var) + "/" + str(max_stt));
		else:
			print("incorrect");
			t4 = Timer(0,incorrect);
			t4.start();			
			ck[sel.get()].config(fg ="red");
			ck[sel.get()].update();
		t2 = Timer(0,delay)
		t2.start();	
	else:
		final_question();
def data_init():
	path  = "database\\data_user.db";
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
	con.close();
def hello():
	try:
		while check_status == True:
			now = datetime.datetime.now()
			xxx.set(str(now.hour) + " : " + str(now.minute) + " : " + str(now.second));
			time.sleep(1)
	except:
		print("Finish!!!")
def limit_time():
	global stt;
	try:
		second = 59;
		minute = 9;
		while minute >= 0:
			x = "Times:         " + str(minute) + " : " + str(second)
			dir_rect.set(x);
			print(x);
			second = second - 1;
			if second == -1:
				second = 59;
				minute = minute - 1;
			time.sleep(1);
		lbl_direct.config(fg = "red");
		dir_rect.set("Times:          Timeout!!!");
		# timeout 
		btn_next.config(state = DISABLED,activebackground = "white" )
		btn_next.update();
		for i in range(0,4):
			ck[i].config(state = DISABLED);
			ck[i].update();
		# result
		score.set(str(stt) + "/" + str(max_stt)  +"--"+ str(score_var) + "/" + str(stt));
		file_path = "progress\\" + str(user_name) + str(".txt");
		file_progress = open(file_path,mode = 'a');
		now = datetime.datetime.now();
		file_progress.write("Timeout " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "--" + str(now.day) + ":" + str(now.month) + ":" + str(now.year) +": "+ str(score.get()) + "\n");
		file_progress.close();
	except:
		print("Bye Bye!!!")
		exit();
def delay():
	global question,y,sel,score_var;
	time.sleep(1.5);
	sel.set(-1)
	for i in range(0,4):
		ck[i].config(fg = "black");
		ck[i].update();
	btn_next.config(state = NORMAL,activebackground = "white")
	btn_next.update();
	rnd = [0,0,0,0]
	x = random.randint(1,len(data_word))
	qus = data_word[str(x)]
	question.set("			Question" + " " + str(stt) + ": " + qus  + " ?");
	path_sp = "speak\\" + str(qus) + ".mp3"
	playsound(path_sp)
	# random location anwser correct!
	y = random.randint(0,3);
	rnd[0] = x;
	for i in range(0,4):
			#  anwser correct
		if i == y:
			ans[i].set(str(data_translate[str(x)]));
		else:
			#incorrect
			x1 = random.randint(1,len(data_word))
			while x1 in rnd:
				x1 = random.randint(1,len(data_word))
			rnd.append(x1)
			ans[i].set(str(data_translate[str(x1)]))
def result():
	global score_var,score;
	if score_var == max_stt:
		score.set("Excellent! " + str(score_var) + "/" + str(max_stt));
	elif(score_var > (4*max_stt)/5):
		score.set("Good " + str(score_var) + "/" + str(max_stt));
	elif(score_var > max_stt/2):
		score.set("Medium " + str(score_var) + "/" + str(max_stt));
	else:
		score.set("Very Bad!" + str(score_var) + "/" + str(max_stt));
def correct():
	playsound("audio\\ting_correct.wav");
def incorrect():
	playsound("audio\\incorrect.wav")
if __name__ == '__main__':
	t = Timer(0, hello);
	t1 = Timer(0,limit_time);
	t2 = Timer(0,delay)
	data_init();
	login_init();
	login_setup();
	mainloop();