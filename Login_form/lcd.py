from tkinter import*
from tkinter import messagebox
import os
import sqlite3 as sql
import time
import datetime
from PIL import ImageTk,Image
from threading import*
import random
data_word = {}
data_translate = {}
app = Tk();

app.title("APP")

lbl_test = Label(app,text = "Hello world!",font = ("Times",34))
lbl_test.pack();
print("Khanh")
path  = "data_newword.db";
con = sql.connect(path);
with con:
	cur  = con.cursor();
	cur.execute("SELECT* FROM data_main");
	rows = cur.fetchall();
	for i in range(1,len(rows)+ 1):
		data_word[str(i)] = rows[i-1][1];
		data_translate[str(i)] = rows[i-1][2];
	print(data_word)
	print(data_translate)
con.close();
file_path = "access111_log.txt";
file_log = open(file_path,mode = 'a');
file_log.write("lut roi");
file_log.close();
app.mainloop();