from tkinter import *   # hiện thực giao diện người dùng GUI
from PIL import Image, ImageTk  # giúp chèn ảnh
from googletrans import Translator
import os

os.chdir(r"C:\Users\DELL\Documents\Python3\Six_Project\ggTranslate")
# Tạo tk window
root = Tk()
root.title("Google galaxy")
root.geometry("500x630")    #size
root.iconbitmap('logo.ico') #chuyển ảnh png, jpg về ico

load = Image.open('background.png') # mở hình
render = ImageTk.PhotoImage(load)   # xuất hình ra
img = Label(root, image=render)
img.place(x=0, y=0)

name = Label(root, text="Translator", fg="#ffffff", bd=0, bg="#011425")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)

box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady=20)


button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0, END)    # trong tkinter bắt đầu từ 1.0
    box1.delete(1.0, END)
def translate():
    INPUT = box.get(1.0, END)
    print(INPUT)
    t = Translator()
    a = t.translate(INPUT, dest="en", src="vi")
    b = a.text
    box1.insert(END, b)
clear_Button = Button(button_frame, text="Clear text", font = (("Arial"), 10, 'bold'), bg="#303030", fg="#ffffff", command=clear)
clear_Button.place(x=150, y=310)
trans_Button = Button(button_frame, text="Translate text", font = (("Arial"), 10, 'bold'), bg="#303030", fg="#ffffff", command=translate)
trans_Button.place(x=290, y=310)

box1 = Text(root, width=28, height=8, font=("ROBOTO", 16))
box1.pack(pady=50)


root.mainloop() #main chính của Tk

