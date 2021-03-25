## Initially building the Recursive Backtracking Algorithm for maze generation
from tkinter import *
from Cells import *
import random
import config
import time
import sys

sys.setrecursionlimit(10**6)

def generateGrid(HCells, VCells, stack, canvas, root, BackgroundColor):
    temp = [[0]*config.HCells for pos in range(config.VCells)] #Has to be 2D Array to allow for the finding of left, right, top, bot to be very efficient

    for i in range(config.VCells):
        for j in range(config.HCells):
            temp[i][j] = Cell(j ,i, canvas, config.SquareSize, root, config.BackgroundColor) #The Cell class will automatically draw the squares
    
    return temp


def findGoodMoves(Cell, Grid, canvas):#Must keep track of Borders to ensure I dont go out of bounds
    PossibleCells = []
    Relation = []

    CurrX = Cell.x
    CurrY = Cell.y
    HCells = len(Grid[0]) - 1 #Works with Index rather than length
    VCells = len(Grid) - 1

    if (CurrX >= 0 and CurrX < HCells): #Restricts the horizontal bounds
        if not Grid[CurrY][CurrX+1].visited: #Checks Right Cell
            PossibleCells.append(Grid[CurrY][CurrX+1])
            Relation.append("Right") #Indicates the Right Cell was a free cell

    if (CurrX >= 1 and CurrX <= HCells): #Restricts the horizontal bounds
        if not Grid[CurrY][CurrX-1].visited:#Checks Left Value
            PossibleCells.append(Grid[CurrY][CurrX-1]) 
            Relation.append("Left") #Indicates the Left Cell was a free cell

    if (CurrY >= 0 and CurrY < VCells):
        if not Grid[CurrY+1][CurrX].visited:
            PossibleCells.append(Grid[CurrY+1][CurrX]) #Checks Buttom Cell
            Relation.append("Bot") #Indicates the Bottom Cell was a free cell

    if (CurrY > 0 and CurrY <= VCells):
        if not Grid[CurrY-1][CurrX].visited:
            PossibleCells.append(Grid[CurrY-1][CurrX]) #Checks Top Value
            Relation.append("Top") #Indicates the Top Cell was a free Cell

    #for thing in PossibleCells: # Changes Color of available Cells, for debugging purposes
       # thing.ChangeColor()

    return tuple(zip(PossibleCells, Relation)) #Combines 2 lists to a list of tuples

def FindNext(Cell, Stack, canvas, root):
    pauseStall(root) #Checks if pause is active, ifso, will freeze program until otherwise
    if config.AlgoWorking: #Needs thsi to fix the pause / play glitch. Where pause then clear then resume starts at where it previously left off
        Cell.visited = True

        while len(Stack) != 0:

            Cell.ChangeColor()
            GoodMoves = findGoodMoves(Cell, Grid, canvas)
            

            if (len(GoodMoves) > 0):
                RandoCell = random.randint(0,len(GoodMoves) - 1)
                ChosenCombo = GoodMoves[RandoCell] # Will be in form (Cell, Location relative to original)

            if (len(GoodMoves) > 0):
                ChosenCell = ChosenCombo[0]

                if ChosenCombo[1] == "Top":
                    Cell.deleteTopWall()
                    ChosenCell.deleteBotWall()

                if ChosenCombo[1] == "Bot":
                    Cell.deleteBotWall()
                    ChosenCell.deleteTopWall()

                if ChosenCombo[1] == "Left":
                    Cell.deleteLeftWall()
                    ChosenCell.deleteRightWall()

                if ChosenCombo[1] == "Right":
                    Cell.deleteRightWall()
                    ChosenCell.deleteLeftWall()

                Stack.append(ChosenCell)
                root.after(1, canvas.update())
            else:
                Stack[-1].TrackColor()
                Stack.pop()
            if len(Stack) > 0:
                return FindNext(Stack[-1], Stack, canvas, root)

def clearCanvas(HCells, VCells, start, canvas, root, BackgroundColor):
    global Grid
    global Stack

    if config.pausePlay or (config.AlgoWorking == False and config.pausePlay == False):
        Grid = generateGrid(HCells, VCells, [], canvas, root, BackgroundColor) ## This will be used in the findPossibleMoves Method
        Stack = [Grid[0][0]]
        config.AlgoWorking = False
        config.pausePlay = False

def RecursiveBackTrackButton(First, Stack, canvas, root):
    config.AlgoWorking = True
    FindNext(First, Stack, canvas, root)
    config.AlgoWorking = False

def pausePlay():
    if config.AlgoWorking == True:
        config.pausePlay = not config.pausePlay
    else:
        config.pausePlay = False

def pauseStall(root):
    while config.pausePlay:
        root.after(50, canvas.update()) #Every 50 milisecond will check of PausePlay has changed

root = Tk()
root.title('Pathfinding Visualizer developed by Christopher Abboud')
root.geometry('{}x{}'.format(config.CanvasWidth, config.CanvasHeight + config.BottomButtonSpace)) #Mega canvas size - the mini canvas is within this
root.resizable(width=False, height=False) #Prevents window from being resized

Selection = Menu(root)

canvas = Canvas(root, height = config.CanvasHeight + 1, width = config.CanvasWidth, highlightthickness=0, bg = config.BackgroundColor) # +1 to canvas height for bottom pixel
canvas.pack()

Grid = generateGrid(config.HCells, config.VCells, [], canvas, root, config.BackgroundColor) ## This will be used in the findPossibleMoves Method
Stack = [Grid[0][0]]

root.config(menu = Selection)


subMenu = Menu(Selection)
Selection.add_cascade(label = "Maze Generation Algorithms", menu = subMenu)
Selection.add_cascade(label = "Clear Canvas", command = lambda: clearCanvas(config.HCells, config.VCells, [], canvas, root, config.BackgroundColor))
Selection.add_cascade(label = "Pause / Play", command = pausePlay)
subMenu.add_command(label = "Recursive Back Tracking", command = lambda: RecursiveBackTrackButton(Stack[0], Stack, canvas, root)) # Prevents Command from auto running

root.mainloop()

