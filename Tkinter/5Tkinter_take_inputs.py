# in this we will learn how to write texts in frame
# and take the text that user writes and put that in a variable
from tkinter import *

# this is a function definition


def PrintValue():
    print(userWrote.get())


window = Tk()

userWrote = StringVar()

# step 2 - as we don't have any command which will warn us when user start writting something
# so we define a trace, which means we will wait for some event to happen, i.e user wrote
# and if that event happens, i.e if anything changes in text then we will call some function
# mode= writting, callback is lambda expression
# lambda expression includes free value i.e name, index, mode
# now write the function which you want to call i.e PrintValue()
userWrote.trace("w", lambda name, index, mode: PrintValue())

# step 1- Display entry in a window, which will take input from the user
# accpet the text that user write and put it in a variable userWrote
e = Entry(window, fg="Yellow", bd=5, bg="Black", textvariable=userWrote)

# display using pack
e.pack()

window.mainloop()
