import tkinter as tk 
from tkinter  import * 
tks = tk.Tk() 
tks.geometry('200x300+300+300') 
tks.title('Calculator') 
tks.resizable(0,0)

btn1 = Frame(tks, bg="#000000")
btn1.pack(expand=True, fill="both")


btn2 = Frame(tks, bg="#FFFFFF")
btn2.pack(expand=True, fill="both")

btn3 = Frame(tks, bg="#000000")
btn3.pack(expand=True, fill="both")

btn4 = Frame(tks, bg="#FFFFFF")
btn4.pack(expand=True, fill="both")

tks.mainloop() 
