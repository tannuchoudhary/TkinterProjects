from tkinter import *
window = Tk()

c = Canvas(window, width=300, height=200)
c.pack()
c.create_line(0, 0, 300, 200, fill="Red")
c.create_line(0, 200, 300, 0, fill="Green")

c.create_rectangle(0, 0, 300, 200, fill="Red")
c.create_rectangle(0, 200, 300, 0, fill="Green")

c.create_rectangle(80, 60, 220, 130, fill="Red")
c.create_rectangle(100, 80, 200, 120, fill="Green")

# you can create oval or circle by just changing the data values
# you can also create a point i.e dot by changing the data values

c.create_oval(100, 80, 200, 120, fill="White")
c.create_oval(140, 90, 160, 110, fill="Blue")
c.create_oval(149, 99, 151, 101, fill="White")


window.mainloop()
