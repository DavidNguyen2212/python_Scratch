from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("Digital Clock")

def clock():
    string = strftime('%H:%M:%S:%p')    # %I là 24h , %H là 12h
    label.config(text=string)
    label.after(1000, clock)
label = Label(root, font=("Arial", 100), background='black', foreground='green')
label.pack(anchor='center')
clock()



root.mainloop()