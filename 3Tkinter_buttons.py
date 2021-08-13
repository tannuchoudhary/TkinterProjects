from tkinter import*

window = Tk()

#bd = border
#bg = background
#fg = foreground
# padx = horizontal padding
# pady = vertical padding
btn = Button(window, bd=20, bg="Red", fg="white", text="Click Me",
             padx=50,  pady=80)

# we can use place instead of pack
# with place, we can pass the parameters in the form of coedinates where we can define where we wan to place the button
btn.place(x=50, y=50)

window.mainloop()
