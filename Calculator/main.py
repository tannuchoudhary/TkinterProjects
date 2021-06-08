import tkinter
from tkinter import *
from tkinter import messagebox
# to show error in the messagebox

# setting up the tkinter window
root = tkinter.Tk()
# this is standard dimension for calculator
root.geometry("250x400+300+300")
# don't allow the calcualtor to be resizable, it will not look good
root.resizable(0, 0)
root.title("Calculator")

# val variable will be created globally so that it can be acessed everywhere
val = ""
A = 0
operator = ""

# function for numerical button clicked
# each time you have to write global val to tell compiler that we are trying to use same
# variable which we have defined above
# you have to implement these functions in the buttons using command


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)


def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)


def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)


def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)


def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)


def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)


def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)


def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)


def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


# functions for the operator button click
# you have to concatenate the operator buttons into operands to show them as string on screen
def btn_plus_clicked():
    global A
    global operator, val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn_minus_clicked():
    global A
    global operator, val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_mult_clicked():
    global A
    global operator, val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btn_div_clicked():
    global A
    global operator, val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


# button c is pressed to clear all data
# we will set value as empty string and will show it on the screen

def btn_c_pressed():
    global A, operator, val
    val = ""
    A = 0
    operator = ""
    data.set(val)


# function to find the result
# split the value through operators and store it in one variable i.e x
# now apply calculation between a and x
def result():
    global A, operator, val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        # a number can't be divided by zero
        # so display error message if user tries to divide anyhting with 0
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Allowed")
            # now you have to erase every data
            #as user has entered wrong value, so everything has to be cleared after showing error
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)


# the label that shows the result
# data will contain all elements in string variable and will convert it into no.s when needed
data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana", 20),
    textvariable=data,
    background="#ffffff",  # background is white
    fg="#000000",  # foreground is grey
)
lbl.pack(expand=True, fill="both")

# the frames section
# create 4 rows first(and each row will consist 4 buttons)
btnrow1 = Frame(root)
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")


# The buttons section
# now set 4 buttons in each row
#grrove sets the effect of button
btn1 = Button(
    btnrow1,
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2 = Button(
    btnrow1,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)

btn3 = Button(
    btnrow1,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btnplus = Button(
    btnrow1,
    text="+",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_plus_clicked,
)
btnplus.pack(side=LEFT, expand=True, fill="both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)

btn5 = Button(
    btnrow2,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,
)
btn5.pack(side=LEFT, expand=True, fill="both",)

btn6 = Button(
    btnrow2,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked,
)
btn6.pack(side=LEFT, expand=True, fill="both",)

btnminus = Button(
    btnrow2,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_minus_clicked,
)
btnminus.pack(side=LEFT, expand=True, fill="both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text="7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked,
)
btn7.pack(side=LEFT, expand=True, fill="both",)

btn8 = Button(
    btnrow3,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked,
)
btn8.pack(side=LEFT, expand=True, fill="both",)

btn9 = Button(
    btnrow3,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked,
)
btn9.pack(side=LEFT, expand=True, fill="both",)

btnmult = Button(
    btnrow3,
    text="*",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_mult_clicked,
)
btnmult.pack(side=LEFT, expand=True, fill="both",)

# button for frame4


btnc = Button(
    btnrow4,
    text="C",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_c_pressed,
)
btnc.pack(side=LEFT, expand=True, fill="both",)

btn0 = Button(
    btnrow4,
    text="0",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_0_isclicked,
)
btn0.pack(side=LEFT, expand=True, fill="both",)

btnequal = Button(
    btnrow4,
    text="=",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=result,
)
btnequal.pack(side=LEFT, expand=True, fill="both",)

btndiv = Button(
    btnrow4,
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_div_clicked,
)
btndiv.pack(side=LEFT, expand=True, fill="both",)

root.mainloop()
