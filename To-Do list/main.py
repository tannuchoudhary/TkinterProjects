from tkinter import *

window = Tk()

# you can change the title of the window
window.title("TODO-list")

# define the listbox
content = Listbox(window, font="Ariel 24 bold")

# write a new variable to keep track of task that the user wrote into the entry
# when user write something into the entry, store it into the task variable and add it to the
# list variable to add it to the content when user clicks the add button
# task will be an instance of a string variable
task = StringVar()

# variable for new entry
e = Entry(window, textvariable=task, font="Ariel 24")

# create button for add and delete
# the functionality of add button is implemented through command
# Python lambda function can be used in GUI programming with Tkinter. It allows to create
# small, inline functions for the command parameter. We have three buttons that share one
# callback. The lambda function allows us to send specific data to the callback function.
add = Button(window, text="Add", font="Ariel 20", padx=26,
             command=lambda content=content, task=task: content.insert(END, task.get()))

# here if you type anchor, computer will know that it has to delete the selected content
delete = Button(window, text="Delete", font="Ariel 20",
                command=lambda content=content: content.delete(ANCHOR))

# now place these elements, somewhere in your window
# both add and delete will be in same line just little bit apart
# columnspan = 2 bcz we want two cells, one for add and one for delete
content.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

# now place the entry button
e.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
add.grid(row=2, column=0, padx=5, pady=20)
delete.grid(row=2, column=1, padx=5, pady=20)

window.mainloop()
