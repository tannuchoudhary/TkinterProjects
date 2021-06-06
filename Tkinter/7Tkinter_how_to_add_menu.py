# in this, we will lern how to create menu and  make them functionable
# we can see that in any app, there are so many drop down menus, like here there is
# file, edit, view, selection and each menu contains other elements inside it which have their
# own work and they do some job, i.e they are functionable


#from tkinter import everything
from tkinter import *

window = Tk()

# create a menu and assign instance Menu and pass window as parameter i.e master
mainMenu = Menu(window)

# configure the menu i.e set it to the main menu
# we are connecting menu to the window
window.config(menu=mainMenu)


def test():
    print("hhhh")


fileMenu = Menu(mainMenu)

# add_cascade adds new dropdown menu to the window
mainMenu.add_cascade(label="File", menu=fileMenu)
# add_command adds elements in the menu
# command is used to add functionality, here it will run test function
fileMenu.add_command(label="Open", command=test)
fileMenu.add_command(label="Save", command=test)

# add_separator to seperate elements in the menu from other
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=test)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

# if you want to add a menu which will redirect you to other site or anything else
# i.e if you don't want a dropdown menu, you want just a menu
mainMenu.add_command(label="Help")

window.mainloop()
