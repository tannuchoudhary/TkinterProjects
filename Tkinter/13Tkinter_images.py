from tkinter import *
window = Tk()

# tkinter doesn't support adding images, you hav to put it in any other widget
# i.e you have to put images in button, or label or anything else
# bcz only images can't be implemented in tkinter

# create an img variable and call PhotoImage function adn pass the path of image in it
img = PhotoImage(file="sqr-blue.png")

# you can resize image using zoom() : for maximizing or subsample() : for minimizing
img = img.subsample(2)

# put image inside label or button or anything else
temp = Label(window, image=img)

temp.pack()
window.mainloop()
