from tkinter import*

window = Tk()

# we have to define the function foro button clicked


def handleClick():
    print("Button clicked")


#bd = boundary
#bg = background
#fg = foreground
# padx = horizontal padding
# pady = vertical padding
btn = Button(window, bd=20, bg="Red", fg="white", text="Click Me",
             padx=50,  pady=80, command=handleClick)

# we can use place instead of pack
btn.place(x=50, y=50)

window.mainloop()


# you can see that each time you click a button, you see an output printing button clicked on
# output console, just pass command = handleClick as parameter and define the function in the top
