# grid is the imaginary table inside your window
# you can use these to basically define where you want to put those elements

from tkinter import *
window = Tk()

labelUser = Label(window, text="Username:")
labelPass = Label(window, text="Password:")

# create entry for user to enter elements
eUser = Entry(window)
ePass = Entry(window)

# default allignment
# labelUser.grid(row=0)
# labelPass.grid(row=1)

#north-up, south-down, east-right, west-left
# you can change allignmentt from here
labelUser.grid(row=0, sticky=E)
labelPass.grid(row=1, sticky=E)

# default column
# eUser.grid(row=0)
# ePass.grid(row=1)

# if you will not set the column, it will be default as 0
eUser.grid(row=0, column=1)
ePass.grid(row=1, column=1)

window.mainloop()
