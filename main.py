import tkinter as tk 
from tkinter  import * 
tks = tk.Tk() 
tks.geometry("250x400+300+300") 
tks.resizable(0,0)
tks.title('Calculator') 


dt = StringVar()
lb = Label(
    tks,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    textvariable = dt,
    background = "#ffffff",
    fg = "#000000",

    

)

lb.pack(expand = True, fill = "both")



btn1 = Frame(tks, bg="#000000")
btn1.pack(expand=True, fill="both")


btn2 = Frame(tks, bg="#000000")
btn2.pack(expand=True, fill="both")

btn3 = Frame(tks, bg="#000000")
btn3.pack(expand=True, fill="both")

btn4 = Frame(tks, bg="#000000")
btn4.pack(expand=True, fill="both")






b1 = Button(btn1, text = "1", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b1.pack(side = LEFT, expand = True, fill = "both",)

b2 = Button(btn1, text = "2", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b2.pack(side = LEFT, expand = True, fill = "both",)

b3 = Button(btn1, text = "3", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b3.pack(side = LEFT, expand = True, fill = "both",)

b4 = Button(btn1, text = "+", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b4.pack(side = LEFT, expand = True, fill = "both",)

b5 = Button(btn2, text = "4", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b5.pack(side = LEFT, expand = True, fill = "both",)

b6 = Button(btn2, text = "5", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b6.pack(side = LEFT, expand = True, fill = "both",)

b7 = Button(btn2, text = "6", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b7.pack(side = LEFT, expand = True, fill = "both",)

b8 = Button(btn2, text = "-", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b8.pack(side = LEFT, expand = True, fill = "both",)



b9 = Button(btn3, text = "7", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b9.pack(side = LEFT, expand = True, fill = "both",)

b10 = Button(btn3, text = "8", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b10.pack(side = LEFT, expand = True, fill = "both",)

b11 = Button(btn3, text = "9", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b11.pack(side = LEFT, expand = True, fill = "both",)

b12 = Button(btn3, text = "*", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b12.pack(side = LEFT, expand = True, fill = "both",)

b13 = Button(btn4, text = "0", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b13.pack(side = LEFT, expand = True, fill = "both",)

b14 = Button(btn4, text = "/", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b14.pack(side = LEFT, expand = True, fill = "both",)

b15 = Button(btn4, text = "%", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b15.pack(side = LEFT, expand = True, fill = "both",)

b16 = Button(btn4, text = "=", font = ("Verdana", 10),
    relief = GROOVE,
    border = 0
)
b16.pack(side = LEFT, expand = True, fill = "both",)


tks.mainloop() 
