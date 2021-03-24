## Initially building the Recursive Backtracking Algorithm for maze generation
from tkinter import *

class Cell():
    def __init__(self, x, y, canvas, SquareSize, root):
        self.visited = False
        self.x = x
        self.y = y

        self.SquareCell = canvas.create_rectangle(x * SquareSize, y * SquareSize, (x+1) * SquareSize, (y+1) * SquareSize, outline = "")
        self.topWall = canvas.create_line(x * SquareSize, y * SquareSize, (x + 1) * SquareSize, y * SquareSize, fill = "Black")
        self.botWall = canvas.create_line(x * SquareSize, (y + 1) * SquareSize, (x + 1) * SquareSize, (y + 1) * SquareSize, fill = "Black")
        self.leftWall = canvas.create_line(x * SquareSize, y * SquareSize, x * SquareSize, (y + 1) * SquareSize, fill = "Black")
        self.rightWall = canvas.create_line((x + 1) * SquareSize, (y + 1) * SquareSize, (x + 1) * SquareSize, (y + 1) * SquareSize, fill = "Black")
        root.after(1, canvas.update())

        self.WallUp = False
        self.WallDown = False
        self.WallLeft = False
        self.WallRight = False
    
    def deleteTopWall(self):
        canvas.itemconfig(self.topWall, fill = "Blue")
    
    def deleteBopWall(self):
        canvas.itemconfig(self.botWall, fill = "Blue")
    
    def deleteRightWall(self):
        canvas.itemconfig(self.rightWall, fill = "Blue")
    
    def deleteLeftWall(self):
        canvas.itemconfig(self.leftWall, fill = "Blue")

def generateGrid(HCells, VCells, stack, canvas, root):
    for i in range(VCells):
        for j in range(HCells):
            TempCell = Cell(j ,i, canvas, SquareSize, root)
            stack.append(TempCell)
    return stack

CanvasWidth = 1500
CanvasHeight = 750

HCells = 50
VCells = 25
SquareSize = 30

root = Tk()
root.geometry('{}x{}'.format(CanvasWidth, CanvasHeight))
root.resizable(width=False, height=False)


canvas = Canvas(root, height = CanvasHeight, width = CanvasWidth, highlightthickness=0, bg = "blue")
canvas.pack()

stack = generateGrid(HCells, VCells, [], canvas, root) # Generates Grid 10x20
stack[55].deleteTopWall()

root.mainloop()

