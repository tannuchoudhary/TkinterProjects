# we don't have to write tkinter again and again
from tkinter import *

# now you just need to write Tk in the place of tkinter
window = Tk()

# define few elements
# we want to divide these windows into some elements/parts
# as we can see that all the applications are divided into some parts
# for e.g this console is divided into many parts like, one part is containing the name of
# the program, one part is containing the content of the program  and one part is containing
# output of the program
# these invisible rectangles are called frames

#fTop is frame in top and fBot is frame in bottom
# in paranthesis, pass the master i.e window
fTop = Frame(window)

# and when we create an element, we need to show it
fTop.pack()

fBot = Frame(window)
fBot.pack(side=BOTTOM)

# define few labels and also mention that where are you going to define these labels
# Both the labels in the frame will be in different line by default
# you can change this by passing parameter in pack
lbl1 = Label(fTop, text="Hello Tannu,")
lbl2 = Label(fTop, text="U r great")
lbl3 = Label(fBot, text="Bye")

# by default in different lines
# lbl1.pack()
# lbl2.pack()
# lbl3.pack()

lbl1.pack(side=LEFT)
lbl2.pack(side=RIGHT)
lbl3.pack()


# we need window to be seen
window.mainloop()
