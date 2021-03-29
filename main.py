import tkinter
from tkinter import *
from tkinter import messagebox
 
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

X = ""
A = 0
operator = ""


def button_1_isckd():
    global X
    X = X + "1"
    data.set(X)

def button_2_isckd():
    global X
    X = X + "2"
    data.set(X)

def button_3_isckd():
    global X
    X = X + "3"
    data.set(X)

def button_4_isckd():
    global X
    X = X + "4"
    data.set(X)

def button_5_isckd():
    global X
    X = X + "5"
    data.set(X)

def button_6_isckd():
    global X
    X = X + "6"
    data.set(X)

def button_7_isckd():
    global X
    X = X + "7"
    data.set(X)

def button_8_isckd():
    global X
    X = X + "8"
    data.set(X)

def button_9_isckd():
    global X
    X = X + "9"
    data.set(X)

def button_0_isckd():
    global X
    X = X + "0"
    data.set(X)


def button_plus_ckd():
    global A
    global operator,X
    A = int(X)
    operator = "+"
    X = X + "+"
    data.set(X)

def button_minus_ckd():
    global A
    global operator,X
    A = int(X)
    operator = "-"
    X = X + "-"
    data.set(X)

def button_mult_ckd():
    global A
    global operator,X
    A = int(X)
    operator = "*"
    X = X + "*"
    data.set(X)

def button_div_ckd():
    global A
    global operator,X
    A = int(X)
    operator = "/"
    X = X + "/"
    data.set(X)

def button_c_pressed():
    global A,operator,X
    X = ""
    A = 0
    operator = ""
    data.set(X)


# function to find the result
def result():
    global A,operator,X
    X2 = X
    if operator == "+":
        x = int((X2.split("+")[1]))
        C = A + x
        X = str(C)
        data.set(X)
    if operator == "-":
        x = int((X2.split("-")[1]))
        C = A - x
        X = str(C)
        data.set(X)
    if operator == "*":
        x = int((X2.split("*")[1]))
        C = A * x
        X = str(C)
        data.set(X)
    if operator == "/":
        x = int((X2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            X = ""
            data.set(X)
        else:
            C = int(A / x)
            data.set(C)


# the label that shows the result
data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

# the frames section
buttonrow1 = Frame(root)
buttonrow1.pack(expand = True, fill = "both")

buttonrow2 = Frame(root)
buttonrow2.pack(expand = True, fill = "both")

buttonrow3 = Frame(root)
buttonrow3.pack(expand = True, fill = "both")

buttonrow4 = Frame(root)
buttonrow4.pack(expand = True, fill = "both")


# The buttons section
button1 = Button(
    buttonrow1,
    text = "1",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_1_isckd,
)
button1.pack(side = LEFT, expand = True, fill = "both",)

button2 = Button(
    buttonrow1,
    text = "2",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_2_isckd,
)
button2.pack(side = LEFT, expand = True, fill = "both",)

button3 = Button(
    buttonrow1,
    text = "3",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_3_isckd,
)
button3.pack(side = LEFT, expand = True, fill = "both",)

buttonplus = Button(
    buttonrow1,
    text = "+",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_plus_ckd,
)
buttonplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

button4 = Button(
    buttonrow2,
    text = "4",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_4_isckd,
)
button4.pack(side = LEFT, expand = True, fill = "both",)

button5 = Button(
    buttonrow2,
    text = "5",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_5_isckd,
)
button5.pack(side = LEFT, expand = True, fill = "both",)

button6 = Button(
    buttonrow2,
    text = "6",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_6_isckd,
)
button6.pack(side = LEFT, expand = True, fill = "both",)

buttonminus = Button(
    buttonrow2,
    text = "-",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_minus_ckd,
)
buttonminus.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

button7 = Button(
    buttonrow3,
    text = "7",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_7_isckd,
)
button7.pack(side = LEFT, expand = True, fill = "both",)

button8 = Button(
    buttonrow3,
    text = "8",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_8_isckd,
)
button8.pack(side = LEFT, expand = True, fill = "both",)

button9 = Button(
    buttonrow3,
    text = "9",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_9_isckd,
)
button9.pack(side = LEFT, expand = True, fill = "both",)

buttonmult = Button(
    buttonrow3,
    text = "*",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_mult_ckd,
)
buttonmult.pack(side = LEFT, expand = True, fill = "both",)

# button for frame4


buttonc = Button(
    buttonrow4,
    text = "C",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_c_pressed,
)
buttonc.pack(side = LEFT, expand = True, fill = "both",)

button0 = Button(
    buttonrow4,
    text = "0",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_0_isckd,
)
button0.pack(side = LEFT, expand = True, fill = "both",)

buttonequal = Button(
    buttonrow4,
    text = "=",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = result,
)
buttonequal.pack(side = LEFT, expand = True, fill = "both",)

buttondiv = Button(
    buttonrow4,
    text = "/",
    font = ("Verdana", 10),
    relief = GROOVE,
    border = 0,
    command = button_div_ckd,
)
buttondiv.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()
