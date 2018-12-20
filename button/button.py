from tkinter import *
import os
from PIL import ImageTk, Image

form = Tk();
form.title("Button")
img = [0]
x = 0
img[0] = ImageTk.PhotoImage(Image.open("Photos/ON.jpg"))
def callback():
	# global x 
	# x = x + 1;
	# print("click ",x);
	# button.config(text = str(x))# cấu hinh lai nut nhan
	form.destroy()
	os.system("python test.py");
button = Button(form,
	text = "Click me", #chữ hiển thị lên bututon
	command = callback,#tên hàm được gọi khi npress
	bg= "red",# màu nền của nút
	fg = "green",# màu chữ của nút nhấn
	activebackground = "pink",#màu nền khi nuutshaojt động
	activeforeground = "orange",# màu chữ khi nút hoạt động
	state = NORMAL,# trạng thái của nút
 #    width = "4",#chiều rộng nút nhấn
	# height = "5",#chiều cao nút nhấn
    # image = img[0],
    font = ("Times")
	)
button.place(x = 200,y=400)# đặt ví trị của nút nhấn
button.pack()
form.mainloop()