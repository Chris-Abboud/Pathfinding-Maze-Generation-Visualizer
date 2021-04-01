from Cells import *
import config
import random
import time

def adjustSpeed(value):
    config.Speed = int(value) #By default slider value is a string

def clearCanvas(HCells, VCells, start, canvas, root, BackgroundColor):
    if config.pausePlay or (config.AlgoWorking == False and config.pausePlay == False):
        config.Grid = config.generateGrid(config.HCells, config.VCells, [], config.canvas, config.root, config.BackgroundColor) ## This will be used in the findPossibleMoves Method
        config.Stack = [config.Grid[0][0]]

        config.AlgoWorking = False
        config.pausePlay = False

def TrackColor(Cell):
    if config.Speed > 0:
        config.canvas.itemconfig(Cell.SquareCell, fill = "Blue")
        config.root.after(config.Speed, config.canvas.update())
        config.canvas.itemconfig(Cell.SquareCell, fill = "White")

def findBadMoves(Cell, Grid, canvas):#Must keep track of Borders to ensure I dont go out of bounds
    PossibleCells = []
    Relation = []

    CurrX = Cell.x
    CurrY = Cell.y
    HCells = len(config.Grid[0]) - 1 #Works with Index rather than length
    VCells = len(config.Grid) - 1

    if (CurrX >= 0 and CurrX < HCells): #Restricts the horizontal bounds
        if config.Grid[CurrY][CurrX+1].visited: #Checks Right Cell
            PossibleCells.append(config.Grid[CurrY][CurrX+1])
            Relation.append("Right") #Indicates the Right Cell was a free cell

    if (CurrX >= 1 and CurrX <= HCells): #Restricts the horizontal bounds
        if config.Grid[CurrY][CurrX-1].visited:#Checks Left Value
            PossibleCells.append(config.Grid[CurrY][CurrX-1]) 
            Relation.append("Left") #Indicates the Left Cell was a free cell

    if (CurrY >= 0 and CurrY < VCells):
        if config.Grid[CurrY+1][CurrX].visited:
            PossibleCells.append(config.Grid[CurrY+1][CurrX]) #Checks Buttom Cell
            Relation.append("Bot") #Indicates the Bottom Cell was a free cell

    if (CurrY > 0 and CurrY <= VCells):
        if config.Grid[CurrY-1][CurrX].visited:
            PossibleCells.append(config.Grid[CurrY-1][CurrX]) #Checks Top Value
            Relation.append("Top") #Indicates the Top Cell was a free Cell

    return tuple(zip(PossibleCells, Relation)) #Combines 2 lists to a list of tuples

def openPossibleWall(Cell, Possibilities): #Opens random wall and returns the cell that was shifted to
    RandoCell = random.randint(0,len(Possibilities) - 1)
    ChosenCombo = Possibilities[RandoCell]

    if (len(Possibilities) > 0):
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
    
    return ChosenCell

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

def FindNext(Cell, Stack, canvas, root): #Recursive Back Track Algo
    pauseStall(config.root) #Checks if pause is active, ifso, will freeze program until otherwise
    if config.AlgoWorking: #Needs thsi to fix the pause / play glitch. Where pause then clear then resume starts at where it previously left off
        Cell.visited = True

        while len(config.Stack) != 0:

            Cell.ChangeColor()
            GoodMoves = findGoodMoves(Cell, config.Grid, config.canvas)
            

            if (len(GoodMoves) > 0):
                ChosenCell = openPossibleWall(Cell, GoodMoves)
                config.Stack.append(ChosenCell)
                config.root.after(config.Speed, config.canvas.update())
            else:
                TrackColor(config.Stack[-1])
                config.Stack.pop()
            if len(config.Stack) > 0:
                return FindNext(config.Stack[-1], config.Stack, config.canvas, config.root)

def RecursiveBackTrackButton():
    if config.AlgoWorking == False:
        config.AlgoWorking = True
        FindNext(config.Stack[0], config.Stack, config.canvas, config.root)
        config.AlgoWorking = False

def HuntAndKill(row, Cell, canvas, root):

    Finished = False
    while not Finished:
        pauseStall(config.root) #Pause / Play Mechanism
        Cell.visited = True
        Cell.ChangeColor()
        GoodMoves = findGoodMoves(Cell, config.Grid, config.canvas)

        if (len(GoodMoves) > 0): #If It can keep finding new move
                ChosenCell = openPossibleWall(Cell, GoodMoves) #Will open possible wall and return the wall it opened
                config.root.after(config.Speed, config.canvas.update()) #Slows down the visual
                Cell = ChosenCell #Reassigns new cell, will keep looping until it hits dead end
        else: #Else we hunt for a new cell
            for i in range (row, len(config.Grid)): #Added row so it does not have to start from the 0'th row everytime
                for j in range(len(config.Grid[0])):
                    pauseStall(config.root)
                    TrackColor(config.Grid[i][j]) #Shows Left to Right scanning
                    if config.Grid[i][j].visited == False: #Stops when it hits new Node
                        BadMoves = findBadMoves(config.Grid[i][j], config.Grid, config.canvas)
                        openPossibleWall(config.Grid[i][j], BadMoves) #Opens a visited wall, calls hunt kill again on the cell just created
                        return HuntAndKill(i, config.Grid[i][j], config.canvas, config.root) #Feed in I which is the row we left off at
                    else:
                        Finished = True

def HuntAndKillButton():
    if config.AlgoWorking == False:
        config.AlgoWorking = True
        HuntAndKill(0, config.Stack[0], config.canvas, config.root)
        config.AlgoWorking = False

def pausePlay():
    if config.AlgoWorking == True:
        config.pausePlay = not config.pausePlay
    else:
        config.pausePlay = False

    #print("pausePlay: ", config.pausePlay) #For debugging 
    #print("AlgoWorking: ", config.AlgoWorking) #For debugging

def pauseStall(root):
    while config.pausePlay:
        config.root.after(50, config.canvas.update()) #Every 50 milisecond will check of PausePlay has changed

