## Initially building the Recursive Backtracking Algorithm for maze generation
from tkinter import *
from Cells import *

def generateGrid(HCells, VCells, stack, canvas, root, BackgroundColor):
    temp = [[0]*HCells for pos in range(VCells)] #Has to be 2D Array to allow for the finding of left, right, top, bot to be very efficient

    for i in range(VCells):
        for j in range(HCells):
            temp[i][j] = Cell(j ,i, canvas, SquareSize, root, BackgroundColor) #The Cell class will automatically draw the squares
    
    return temp

CanvasWidth = 1500 #Width of the Interactive Canvas
CanvasHeight = 750 #Height of the Interactive Canvas

HCells = 50
VCells = 25
SquareSize = 30
BackgroundColor = "pink"
root = Tk()
root.geometry('{}x{}'.format(CanvasWidth, CanvasHeight)) #Mega canvas size - the mini canvas is within this
root.resizable(width=False, height=False) #Prevents window from being resized


canvas = Canvas(root, height = CanvasHeight, width = CanvasWidth, highlightthickness=0, bg = BackgroundColor) #
canvas.pack()

Grid = generateGrid(HCells, VCells, [], canvas, root, BackgroundColor) ## This will be used in the findPossibleMoves Method


root.mainloop()


### SUDO CODE FOR ALGORITHM

"""
def FindNext(Cell, Stack)
    if len(Stack) == 1:
        return Done
    else:
        Cell.visted = True

        GoodMoves = findPossCellMoves(Cell) Choose random good move
        Remove Wall Between

        if len(GoodMoves) == 0:
            Stack.pop

        FindNext(Stack[-1], Stack)

"""