from tkinter import *


def callback():
    print(checkVar.get())


window = Tk()

checkVar = StringVar()

# Checkbutton is instance for checkbox
# command is for functionality
# callback function
chb = Checkbutton(window, text="option 1", width=50, height=10, variable=checkVar,
                  command=callback, onvalue="RGB", offvalue="OFF")
chb.pack()
window.mainloop()
