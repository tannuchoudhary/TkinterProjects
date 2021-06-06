from tkinter import *

# drawShape function will be called to draw a shape of cross and oval


def drawShape(x, y):
    global cross
    margin = 20
    # start with cross, and then cross will set to false andd oval will be drawn on next time
    if cross:
        # pass starting and ending cordinate of lines as parameter and color and width
        gameBoard.create_line(x+margin, y+margin,
                              x+(width/3)-margin, y+(height/3)-margin, fill="Blue", width=10)
        gameBoard.create_line(x+margin, y+(height/3)-margin,
                              x + (width/3)-margin, y+margin, fill="Blue", width=10)
        # set cross as false
        cross = False
        # now oval will be drawn by next player
    else:
        # pass starting and ending cordinate of oval
        gameBoard.create_oval(x+margin, y+margin,
                              x+(width/3)-margin, y+(height/3)-margin, width=10, outline="Red")
        # set cross as true so that next time cross will be drawn
        cross = True


def play(event):
    # set the variables position
    secondRow = height/3
    thirdRow = secondRow*2
    secondColumn = width/3
    thirdColumn = secondColumn*2

    # set offset as default
    offsetX = thirdColumn
    offsetY = thirdRow

    # put conditions so that you can tell the program that what section is being selected by players
    if event.y < secondRow:
        offsetY = 0
    elif event.y < thirdRow:
        offsetY = secondRow
    if event.x < secondColumn:
        offsetX = 0
    elif event.x < thirdColumn:
        offsetX = secondColumn

    # call drawshape to draw cross or oval
    drawShape(offsetX, offsetY)


window = Tk()
cross = True
# take the height and width of the window
width = 500
height = 500

# create canvas for drawing
gameBoard = Canvas(window, width=width, height=height)

# create 2 horizontal and two vertical lines for game

# two horizontal lines, i.e create 3 rows
gameBoard.create_line(0, height/3, width, height/3)
gameBoard.create_line(0, (height/3)*2, width, (height/3)*2)

# two vertical lines, i.e create 3 columns
gameBoard.create_line(width/3, 0, width/3, height)
gameBoard.create_line((width/3)*2, 0, (width/3)*2, height)

# show the result
gameBoard.pack()
gameBoard.bind("<Button-1>", play)
window.mainloop()
