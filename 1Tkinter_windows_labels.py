import tkinter
# this is a class that stands for new window
window = tkinter.Tk()

# create a new label that will be shown in the window that we just cretaed
lblHello = tkinter.Label(window, text="Hello world!")

# show label
lblHello.pack()

# when we create a new instance of window, it dissapears immediately
# this stops the window on screen so that user can see it
# loop through the window till the application is closed by user
window.mainloop()
