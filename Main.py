## Initially building the Recursive Backtracking Algorithm for maze generation
from tkinter import *
from Cells import *
import random
import sys


sys.setrecursionlimit(10**6)

def generateGrid(HCells, VCells, stack, canvas, root, BackgroundColor):
    temp = [[0]*HCells for pos in range(VCells)] #Has to be 2D Array to allow for the finding of left, right, top, bot to be very efficient

    for i in range(VCells):
        for j in range(HCells):
            temp[i][j] = Cell(j ,i, canvas, SquareSize, root, BackgroundColor) #The Cell class will automatically draw the squares
    
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
    Cell.visited = True

    while len(Stack) != 0:

        if Stop:
            scanning()

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

CanvasWidth = 1500 #Width of the Interactive Canvas
CanvasHeight = 850 #Height of the Interactive Canvas

Stop = False
HCells = 50
VCells = 25
SquareSize = 30
BackgroundColor = "pink"

root = Tk()
root.title('Pathfinding Visualizer developed by Christopher Abboud')
root.geometry('{}x{}'.format(CanvasWidth, CanvasHeight)) #Mega canvas size - the mini canvas is within this
root.resizable(width=False, height=False) #Prevents window from being resized

Selection = Menu(root)

canvas = Canvas(root, height = CanvasHeight, width = CanvasWidth, highlightthickness=0, bg = BackgroundColor) #
canvas.pack()

Grid = generateGrid(HCells, VCells, [], canvas, root, BackgroundColor) ## This will be used in the findPossibleMoves Method
Stack = [Grid[0][0]]

root.config(menu = Selection)


subMenu = Menu(Selection)
Selection.add_cascade(label = "Maze Generation Algorithms", menu = subMenu)
subMenu.add_command(label = "Recursive Back Tracking", command = lambda: FindNext(Stack[0], Stack, canvas, root)) # Prevents Command from auto running

#FindNext(Stack[0], Stack, canvas, root)
print("DONE BABY!!!!")

root.mainloop()

