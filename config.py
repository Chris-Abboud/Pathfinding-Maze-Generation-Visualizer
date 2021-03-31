from tkinter import *
from Cells import *

def generateGrid(HCells, VCells, Stack, canvas, root, BackgroundColor):
    temp = [[0]*HCells for pos in range(VCells)] #Has to be 2D Array to allow for the finding of left, right, top, bot to be very efficient

    for i in range(VCells):
        for j in range(HCells):
            temp[i][j] = Cell(j ,i, canvas, SquareSize, root, BackgroundColor) #The Cell class will automatically draw the squares
    
    return temp
    
CanvasWidth = 900 #Width of the Interactive Canvas # Must be multiplte of SquareSize AND CanvasWidth / 2 must also be multiple of SquareSize
CanvasHeight = int(CanvasWidth / 2) #Height of the Interactive Canvas
BottomButtonSpace = 100
SquareSize = 30

AlgoWorking = False
pausePlay = False

Stop = False
HCells = int(CanvasWidth / SquareSize)
VCells = int(CanvasHeight / SquareSize)

BackgroundColor = "pink"

root = Tk()
root.title('Pathfinding Visualizer developed by Christopher Abboud')
root.geometry('{}x{}'.format(CanvasWidth, CanvasHeight + BottomButtonSpace)) #Mega canvas size - the mini canvas is within this
root.resizable(width=False, height=False) #Prevents window from being resized

canvas = Canvas(root, height = CanvasHeight + 1, width = CanvasWidth, highlightthickness=0, bg = BackgroundColor) # +1 to canvas height for bottom pixel
canvas.pack()

Grid = generateGrid(HCells, VCells, [], canvas, root, BackgroundColor) ## This will be used in the findPossibleMoves Method
Stack = [Grid[0][0]]

