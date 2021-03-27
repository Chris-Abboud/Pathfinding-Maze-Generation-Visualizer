from Cells import *
import config
import random
import time

def clearCanvas(HCells, VCells, start, canvas, root, BackgroundColor):
    if config.pausePlay or (config.AlgoWorking == False and config.pausePlay == False):
        config.Grid = config.generateGrid(config.HCells, config.VCells, [], config.canvas, config.root, config.BackgroundColor) ## This will be used in the findPossibleMoves Method
        config.Stack = [config.Grid[0][0]]

        config.AlgoWorking = False
        config.pausePlay = False

def findGoodMoves(Cell, Grid, canvas):#Must keep track of Borders to ensure I dont go out of bounds
    PossibleCells = []
    Relation = []

    CurrX = Cell.x
    CurrY = Cell.y
    HCells = len(config.Grid[0]) - 1 #Works with Index rather than length
    VCells = len(config.Grid) - 1

    if (CurrX >= 0 and CurrX < HCells): #Restricts the horizontal bounds
        if not config.Grid[CurrY][CurrX+1].visited: #Checks Right Cell
            PossibleCells.append(config.Grid[CurrY][CurrX+1])
            Relation.append("Right") #Indicates the Right Cell was a free cell

    if (CurrX >= 1 and CurrX <= HCells): #Restricts the horizontal bounds
        if not config.Grid[CurrY][CurrX-1].visited:#Checks Left Value
            PossibleCells.append(config.Grid[CurrY][CurrX-1]) 
            Relation.append("Left") #Indicates the Left Cell was a free cell

    if (CurrY >= 0 and CurrY < VCells):
        if not config.Grid[CurrY+1][CurrX].visited:
            PossibleCells.append(config.Grid[CurrY+1][CurrX]) #Checks Buttom Cell
            Relation.append("Bot") #Indicates the Bottom Cell was a free cell

    if (CurrY > 0 and CurrY <= VCells):
        if not config.Grid[CurrY-1][CurrX].visited:
            PossibleCells.append(config.Grid[CurrY-1][CurrX]) #Checks Top Value
            Relation.append("Top") #Indicates the Top Cell was a free Cell

    return tuple(zip(PossibleCells, Relation)) #Combines 2 lists to a list of tuples

def FindNext(Cell, Stack, canvas, root):
    pauseStall(config.root) #Checks if pause is active, ifso, will freeze program until otherwise
    if config.AlgoWorking: #Needs thsi to fix the pause / play glitch. Where pause then clear then resume starts at where it previously left off
        Cell.visited = True

        while len(config.Stack) != 0:

            Cell.ChangeColor()
            GoodMoves = findGoodMoves(Cell, config.Grid, config.canvas)
            

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

                config.Stack.append(ChosenCell)
                config.root.after(1, config.canvas.update())
            else:
                config.Stack[-1].TrackColor()
                config.Stack.pop()
            if len(config.Stack) > 0:
                return FindNext(config.Stack[-1], config.Stack, config.canvas, config.root)

def RecursiveBackTrackButton(First, Stack, canvas, root):
    config.AlgoWorking = True
    FindNext(First, config.Stack, config.canvas, config.root)
    config.AlgoWorking = False

def pausePlay():
    if config.AlgoWorking == True:
        config.pausePlay = not config.pausePlay
    else:
        config.pausePlay = False

    print("pausePlay: ", config.pausePlay)
    print("AlgoWorking: ", config.AlgoWorking)

def pauseStall(root):
    while config.pausePlay:
        config.root.after(50, config.canvas.update()) #Every 50 milisecond will check of PausePlay has changed

def HuntAndKillButton(Grid, canvas, root):
    print("LOL")