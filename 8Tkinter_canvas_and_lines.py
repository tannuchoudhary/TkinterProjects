from tkinter import *
window = Tk()

c = Canvas(window, width=300, height=200)
c.pack()

# pass the cordinates for, from where to where you want to create line
# you can also draw circle, triangle, pentagon or anything else
c.create_line(0, 0, 300, 200, fill="Red")
c.create_line(0, 200, 300, 0, fill="Green")
window.mainloop()
