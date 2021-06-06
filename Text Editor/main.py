from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import ttk


def closeWindow():
    window.destroy()


def changeFont():
    content["font"] = fontVar + " " + str(sizeVar) + " " + typeVar


def fontChanged(event):
    global fontVar
    fontVar = event.widget.get(ANCHOR)
    changeFont()


def sizeChanged(event):
    global sizeVar
    sizeVar = event.widget.get(ANCHOR)
    changeFont()


def typeChanged(event):
    global typeVar
    typeVar = event.widget.get()
    changeFont()

    # Ariel 20 bold
# function definition to save the file


def saveFile():
    f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    # if user cancels the file i.e does not want to save the file then return from the function
    # this is exactly like the break statement
    if f is None:
        return
    try:
        # take the whole text written by user, typecast it into string and write it into file
        textUserWrote = str(content.get(1.0, END))
        f.write(textUserWrote)
    # in case if file can't be opened
    except:
        print("Cannot save the file")
    finally:
        f.close()

# this is the function definition to open the file in the read mode only
# *.* this does mean that it will open files of all extension,
# if you will write .txt in that place then it will open only text file


def openFile():
    try:
        t = filedialog.askopenfile(mode='r', title="Select File",
                                   filetypes=[("All Files", "*.*")])
        # now read everything from the file which you have just opened and copy it at the end of the content
        content.insert(END, t.read())

    except:
        print("Cannot load the file")
    finally:
        if t:
            t.close()


def optionsClick():
    optionWindow = Tk()
    lblFont = Label(optionWindow, text="Font:")
    lblSize = Label(optionWindow, text="Size:")
    lblType = Label(optionWindow, text="Type:")
    fontBox = Listbox(optionWindow)
    for f in font.families():
        fontBox.insert(END, f)

 # let us create another list box for size
    sizeBox = Listbox(optionWindow)
    for i in range(8, 88, 4):
        sizeBox.insert(END, i)
    typeOptions = ("normal", "bold", "normal italic", "bold italic")
    cbxType = ttk.Combobox(optionWindow, values=typeOptions)
    cbxType.set("normal")

    # i want my changes to occur without clicking any button, just by selecting
    # any button, the changes should be made, for that i have to add some functionalities
    # add some events
    fontBox.bind("<<ListboxSelect>>", fontChanged)
    sizeBox.bind("<<ListboxSelect>>", sizeChanged)
    cbxType.bind("<<ComboboxSelected>>", typeChanged)
    # place all the labels

    lblFont.grid(row=0, column=0, padx=10, pady=5)
    lblSize.grid(row=0, column=1, padx=10, pady=5)
    lblType.grid(row=0, column=2, padx=10, pady=5)
    fontBox.grid(row=1, column=0, padx=10, pady=5)
    sizeBox.grid(row=1, column=1, padx=10, pady=5)
    cbxType.grid(row=1, column=2, padx=10, pady=5)
    optionWindow.mainloop()


window = Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)
window.geometry("500x400")
fontVar = "Ariel"
sizeVar = 11
typeVar = "normal"
fileMenu = Menu(mainMenu)
# create a dropdown menu using cascade
# and add elements in that dropdown using add_command
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=closeWindow)
fileMenu.add_command(label="Help")
mainMenu.add_cascade(label="Help")

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")
editMenu.add_command(label="Options", command=optionsClick)


content = Text(window)
content.place(width=500, height=400)
window.mainloop()
