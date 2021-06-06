from tkinter import *
from tkinter import ttk


def callback(event):
    print(event.widget.get())


window = Tk()
tValues = ("A", "B", "C")
# combobox will be new instance of ttk
cbx = ttk.Combobox(window, values=tValues)

# now  you can change the default value
cbx.set("Name of my Combobox")

# if you want to bind an event, i.e you want an event to occur if user selects any option
cbx.bind("<<ComboboxSelected>>", callback)

cbx.pack()

window.mainloop()
