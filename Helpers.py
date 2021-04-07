from Cells import *
import config
import random
import time
import math

def getCoordinates(event):
    x = event.x // config.SquareSize
    y = event.y // config.SquareSize
    
    return (x,y)

def clearWalls():
    if not config.MazeDrawn:
        for i in range(len(config.Grid)):
            for j in range(len(config.Grid[0])):
                if config.Grid[i][j] != config.StartCell and config.Grid[i][j] != config.EndCell: #Cant use IsWall, edges blead to other cells
                    ChangeColorTo(config.Grid[i][j], "White")
                    config.Grid[i][j].SearchVisited = False
                    config.Grid[i][j].isWall = False
                    config.Grid[i][j].WallUp = False
                    config.Grid[i][j].WallDown = False
                    config.Grid[i][j].WallRight = False
                    config.Grid[i][j].WallLeft = False
                    
        config.StartCell.SearchVisited = False
        config.EndCell.SearchVisited = False
        config.canvas.update()

def clearSearch():
    for i in range(len(config.Grid)):
        for j in range(len(config.Grid[0])):
            if config.Grid[i][j] != config.StartCell and config.Grid[i][j] != config.EndCell:
                if not config.Grid[i][j].isWall:
                    config.Grid[i][j].SearchVisited = False
                    config.Grid[i][j].RevertColor()

    config.StartCell.SearchVisited = False
    config.EndCell.SearchVisited = False



def replaceDrawCanvas():

    config.canvas.delete("all") #Need this to prevent memory leak. Bug where program runs slower after every "clear"
    for i in range(config.VCells):
        for j in range(config.HCells):
            config.Grid[i][j] = Cell(j ,i, config.canvas, config.SquareSize, config.root, "White", True) #The Cell class will automatically draw the squares

def bindDrawingMode():
    if not config.DrawingMode: 
        replaceDrawCanvas()
        config.DrawingMode = True
        config.StartCell = config.Grid[0][0]
        config.EndCell = config.Grid[config.VCells -1][config.HCells -1]
        config.canvas.bind('<B1-Motion>', DrawingMode)
    else:
        config.canvas.bind('<B1-Motion>', DrawingMode)

def DrawingMode(event):
    if (not config.AlgoWorking and not config.pausePlay) and config.DrawingMode:
        a = getCoordinates(event)
        (x, y) = a
        if x <= config.HCells - 1 and y <= config.VCells -1 and x >= 0 and y >= 0:
            if config.StartCell == None or a[0] != config.StartCell.x or a[1] != config.StartCell.y:
                if config.EndCell == None or a[0] != config.EndCell.x or a[1] != config.EndCell.y:
                    DrawCell = config.Grid[y][x]

                    tempChangeColorTo(DrawCell, "Black")
                    DrawCell.isWall = True
                    DrawCell.WallUp = True
                    DrawCell.WallDown = True
                    DrawCell.WallRight = True
                    DrawCell.WallLeft = True

                    if (x >= 0 and x < config.HCells - 1): #Restricts the horizontal bounds
                        config.Grid[y][x+1].WallLeft = True
                    if (x >= 1 and x <= config.HCells - 1): #Restricts the horizontal bounds
                        config.Grid[y][x-1].WallRight = True
                    if (y >= 0 and y < config.VCells - 1):
                        config.Grid[y+1][x].WallUp = True
                    if (y > 0 and y <= config.VCells - 1):
                        config.Grid[y-1][x].WallDown = True


def bindPlaceStart():
    config.canvas.unbind('<B1-Motion>')
    config.canvas.bind('<Button-1>', PlaceStart)

def PlaceStart(event):
    a = getCoordinates(event)

    if not config.Grid[a[1]][a[0]].isWall: #Fixes bug where start / cell was placed on a wall
        if (config.pausePlay or (not config.AlgoWorking and not config.pausePlay)): 
            if config.StartCell != None: 
                config.StartCell.RevertColor()

            config.StartCell = config.Grid[a[1]][a[0]]
            tempChangeColorTo(config.StartCell, "#4cdfff")
            config.canvas.unbind('<Button-1>')
        

def bindPlaceEnd():
    config.canvas.unbind('<B1-Motion>')
    config.canvas.bind('<Button-1>', PlaceEnd)

def PlaceEnd(event):
    a = getCoordinates(event)

    if not config.Grid[a[1]][a[0]].isWall:
        if (config.pausePlay or (not config.AlgoWorking and not config.pausePlay)):
            if config.EndCell != None: 
                config.EndCell.RevertColor()
            config.EndCell = config.Grid[a[1]][a[0]]
            tempChangeColorTo(config.EndCell, "#ffb763")
            config.canvas.unbind('<Button-1>')


def adjustSpeed(value):
    config.Speed = int(value)

def replaceGrid():
    config.canvas.delete("all") #Need this to prevent memory leak. Bug where program runs slower after every "clear"
    for i in range(config.VCells):
        for j in range(config.HCells):
            config.Grid[i][j] = Cell(j ,i, config.canvas, config.SquareSize, config.root, config.BackgroundColor, False) #The Cell class will automatically draw the squares


def clearCanvas(HCells, VCells, start, canvas, root, BackgroundColor):
    if config.pausePlay or (config.AlgoWorking == False and config.pausePlay == False):
        replaceGrid() ## This will be used in the findPossibleMoves Method
        config.Stack = [config.Grid[0][0]]
        config.AlgoWorking = False
        config.pausePlay = False
        config.DrawingMode = False
        config.MazeDrawn = False
        config.StartCell = config.Grid[0][0]
        config.EndCell = config.Grid[config.VCells -1][config.HCells-1]

def TrackPlacedColor(Cell):
    if config.Speed != 0 and config.AlgoWorking:
        config.canvas.itemconfig(Cell.SquareCell, fill = "Orange")
        config.root.after(config.Speed, config.canvas.update())
        config.canvas.itemconfig(Cell.SquareCell, fill = "White")
        Cell.color = "White"
    else:
        config.canvas.itemconfig(Cell.SquareCell, fill = "White")
        Cell.color = "White"

def ChangeColorTo(Cell, color):
    config.canvas.itemconfig(Cell.SquareCell, fill = color)
    Cell.color = color

def tempChangeColorTo(Cell, color):
    config.canvas.itemconfig(Cell.SquareCell, fill = color)

def TrackColor(Cell):
    if config.Speed != 0 and config.AlgoWorking:
        config.canvas.itemconfig(Cell.SquareCell, fill = "Blue")
        config.root.after(config.Speed, config.canvas.update())
        config.canvas.itemconfig(Cell.SquareCell, fill = "White")
        Cell.color = "White"

def ChangeColorBlue(Cell):
    if config.AlgoWorking or (config.AlgoWorking == False and config.pausePlay == False):
        config.canvas.itemconfig(Cell.SquareCell, fill = "Blue")
        Cell.color = "Blue"

def DebuggerColorChange(Cell):
    config.canvas.itemconfig(Cell.SquareCell, fill = "Blue")

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

    if config.AlgoWorking:
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
    return None

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

def BinaryTreeSortBotRight(possibilities):
    A = []
    for combo in possibilities:
        if combo[1] == "Right" or combo[1] == "Bot":
            A.append(combo)
    return A

def RecursiveBackTrack(Cell, Stack, canvas, root): #Recursive Back Track Algo
    pauseStall(config.root) #Checks if pause is active, ifso, will freeze program until otherwise
    if config.AlgoWorking: #Needs thsi to fix the pause / play glitch. Where pause then clear then resume starts at where it previously left off
        Cell.visited = True
        while len(config.Stack) != 0:
            ChangeColorTo(Cell, "Orange")
            config.root.after(config.Speed, config.canvas.update())
            GoodMoves = findGoodMoves(Cell, config.Grid, config.canvas)
            ChangeColorBlue(Cell)

            if (len(GoodMoves) > 0):
                ChosenCell = openPossibleWall(Cell, GoodMoves)
                config.Stack.append(ChosenCell)
            else:
                ChangeColorTo(config.Stack[-1], "White")
                config.Stack.pop()
            if len(config.Stack) > 0:
                return RecursiveBackTrack(config.Stack[-1], config.Stack, config.canvas, config.root)

def RecursiveBackTrackButton():

    '''Uses a stack. Keeps pushing to stack as it randomly travels the grid.
    Once it hits a dead end, keeps popping the stack until we land on a node where we can move
    in a different direction. Repeat this process'''

    if config.AlgoWorking == False and not config.DrawingMode and not config.MazeDrawn:
        config.AlgoWorking = True
        RecursiveBackTrack(config.Stack[0], config.Stack, config.canvas, config.root)
        config.AlgoWorking = False
        config.MazeDrawn = True

def HuntAndKill(row, Cell, canvas, root):

    Finished = False

    if config.AlgoWorking:
        while not Finished and config.AlgoWorking:
            Cell.visited = True
            TrackPlacedColor(Cell)
            pauseStall(config.root) #Pause / Play Mechanism
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

    '''Similar to recursive back track. Walks grid until finds a dead end.
    When it finds dead end, walk row then columns until an unvisited node is found.
    Connect that node first with an adjacent visited node, then repeat
    the process with the newly retrieved node'''

    if config.AlgoWorking == False and not config.DrawingMode and not config.MazeDrawn:
        config.AlgoWorking = True
        HuntAndKill(0, config.Stack[0], config.canvas, config.root)
        config.AlgoWorking = False
        config.MazeDrawn = True

def BinaryTreeAlgorithm():
    for i in range(len(config.Grid)):
        for j in range(len(config.Grid[0])):
            if config.AlgoWorking:
                config.Grid[i][j].visited = True
                ChangeColorTo(config.Grid[i][j], "Orange")
                config.root.after(config.Speed, config.canvas.update())
                ChangeColorTo(config.Grid[i][j], "White")

                pauseStall(config.root)
                PossibleMoves = BinaryTreeSortBotRight(findGoodMoves(config.Grid[i][j], config.Grid, config.canvas) + findBadMoves(config.Grid[i][j], config.Grid, config.canvas))
                
                if len(PossibleMoves) > 0 and config.AlgoWorking: #config.AlgoWOrking is temporary fix to clear error
                    ChosenCell = openPossibleWall(config.Grid[i][j], PossibleMoves)
                    ChosenCell.visited = True
                    TrackColor(ChosenCell)
            else:
                return #Shuts off if clear was performed

def BinaryTreeButton():

    '''Very Simple Algorithm. Has a bias, in this case South East
    Will walk across all nodes and will open either an east wall or south wall
    Creates very simple solved maze'''

    if config.AlgoWorking == False and not config.DrawingMode and not config.MazeDrawn:
        config.AlgoWorking = True
        BinaryTreeAlgorithm()
        config.AlgoWorking = False
        config.MazeDrawn = True


def PrimsAlgorithm():

    Cell = config.Grid[int(config.VCells / 2)][int(config.HCells / 2)]
    FrontiereSet = [Cell]
    

    while len(FrontiereSet) > 0:
        pauseStall(config.root)
        if config.AlgoWorking:
            Cell.ChangeColor()
            Cell.visited = True
            FrontiereSet.remove(Cell)

            FrontiereAdjacents = findGoodMoves(Cell, config.Grid, config.canvas)
            
            for Combo in FrontiereAdjacents:
                if not Combo[0] in FrontiereSet: #Prevents double duplicates
                    FrontiereSet.append(Combo[0])
                    ChangeColorBlue(Combo[0])

            if len(FrontiereSet) > 0:
                config.root.after(config.Speed, config.canvas.update())
                ChosenFrontiere = random.choice(FrontiereSet)
                VisitedPossibles = findBadMoves(ChosenFrontiere, config.Grid, config.canvas)
                openPossibleWall(ChosenFrontiere, VisitedPossibles)
                
                Cell = ChosenFrontiere
        else:
            return
            
def PrimsAlgorithmButton():

    if config.AlgoWorking == False and not config.DrawingMode and not config.MazeDrawn:
        config.AlgoWorking = True
        PrimsAlgorithm()
        config.AlgoWorking = False
        config.MazeDrawn = True


def SidewinderAlgorithm():
    for i in range(len(config.Grid[0])): #Takes care of first row
        pauseStall(config.root)
        if config.AlgoWorking:
            config.Grid[0][i].visited = True
            if i < len(config.Grid[0]) - 1:
                openPossibleWall(config.Grid[0][i], [[config.Grid[0][i+1], "Right"]])
            TrackPlacedColor(config.Grid[0][i])
        else:
            return 

    for i in range(1, len(config.Grid)):
        TempSet = [config.Grid[i][0]] #Need 2d List as open possible wall takes 2d list
        config.Grid[i][0].visited = True
        TrackPlacedColor(config.Grid[i][0])
        for j in range(1, len(config.Grid[0])):
            pauseStall(config.root)
            if config.AlgoWorking:
                config.Grid[i][j].visited = True
                MoveForward = random.choice([True, False])
                if MoveForward:
                    TempSet.append(config.Grid[i][j]) 
                    ChangeColorTo(config.Grid[i][j], "Blue")
                    openPossibleWall(config.Grid[i][j-1], [[config.Grid[i][j], "Right"]])
                else:
                    for thing in TempSet:
                        ChangeColorTo(thing, "White")
                    ChosenOpening = random.choice(TempSet)
                    openPossibleWall(ChosenOpening, [[config.Grid[ChosenOpening.y - 1][ChosenOpening.x], "Top"]])
                    TempSet = [config.Grid[i][j]]
                    ChangeColorTo(config.Grid[i][j], "Blue")

                config.root.after(config.Speed, config.canvas.update())
            else:
                return

        if len(TempSet) > 0: #This means it stopped on last node
            ChosenOpening = random.choice(TempSet)
            openPossibleWall(ChosenOpening, [[config.Grid[ChosenOpening.y-1][ChosenOpening.x], "Top"]])
            for thing in TempSet:
                    ChangeColorTo(thing, "White")
        

def SidewinderButton():
    if config.AlgoWorking == False and not config.DrawingMode and not config.MazeDrawn:
        config.AlgoWorking = True
        SidewinderAlgorithm()
        config.AlgoWorking = False
        config.MazeDrawn = True


def DjikstrasAlgorithm():
    Curr = config.StartCell
    Curr.distance = 0

    Unvisited = [Curr]
    End = config.EndCell

    while (Curr != End):
        X = Curr.x
        Y = Curr.y
        pauseStall(config.root)

        if not Curr.WallUp and Y != 0:
            if not config.Grid[Y-1][X].SearchVisited:
                config.Grid[Y-1][X].distance = Curr.distance + 1
                if config.Grid[Y-1][X] not in Unvisited:
                    Unvisited.append(config.Grid[Y-1][X])
                    if config.Grid[Y-1][X] != config.EndCell:
                        tempChangeColorTo(config.Grid[Y-1][X], "Blue") #Doesnt alter root color. For clear search

        if not Curr.WallRight and X != config.HCells - 1:
            if not config.Grid[Y][X+1].SearchVisited:
                config.Grid[Y][X+1].distance = Curr.distance + 1
                if config.Grid[Y][X+1] not in Unvisited:
                    Unvisited.append(config.Grid[Y][X+1])

                    if config.Grid[Y][X+1] != config.EndCell:
                        tempChangeColorTo(config.Grid[Y][X+1], "Blue")

        if not Curr.WallLeft and X != 0:
            if not config.Grid[Y][X-1].SearchVisited:
                config.Grid[Y][X-1].distance = Curr.distance + 1
                if config.Grid[Y][X-1] not in Unvisited:
                    Unvisited.append(config.Grid[Y][X-1])
                    if config.Grid[Y][X-1] != config.EndCell:
                        tempChangeColorTo(config.Grid[Y][X-1], "Blue")

        if not Curr.WallDown and Y != config.VCells -1:
            if not config.Grid[Y+1][X].SearchVisited: #Ensures Unvisited Node
                config.Grid[Y+1][X].distance = Curr.distance + 1
                if config.Grid[Y+1][X] not in Unvisited:
                    Unvisited.append(config.Grid[Y+1][X])
                    if config.Grid[Y+1][X] != config.EndCell:
                        tempChangeColorTo(config.Grid[Y+1][X], "Blue")

        Curr.SearchVisited = True
        Unvisited.remove(Curr)

        config.root.after(config.Speed, config.canvas.update())

        Curr = Unvisited[0]
        for Cell in Unvisited:
            if Cell.distance < Curr.distance:
                Curr = Cell
def DijkstrasAlgorithmButton():
    if config.AlgoWorking == False:
        config.AlgoWorking = True
        DjikstrasAlgorithm()
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

####################################################################################################

                                #    Debugger - Helps find valid walls

####################################################################################################
def moveUp(event):
    if config.CurrentCellDebug.WallUp == False and config.CurrentCellDebug.y > 0:
        config.CurrentCellDebug.RevertColor()
        config.CurrentCellDebug = config.Grid[config.CurrentCellDebug.y - 1][config.CurrentCellDebug.x]
        DebuggerColorChange(config.CurrentCellDebug)
        config.root.after(config.Speed, config.canvas.update())

def moveLeft(event):
    if config.CurrentCellDebug.WallLeft == False and config.CurrentCellDebug.x > 0:
        config.CurrentCellDebug.RevertColor()
        config.CurrentCellDebug = config.Grid[config.CurrentCellDebug.y][config.CurrentCellDebug.x - 1]
        DebuggerColorChange(config.CurrentCellDebug)
        config.root.after(config.Speed, config.canvas.update())

def moveDown(event):
    if config.CurrentCellDebug.WallDown == False and config.CurrentCellDebug.y < config.VCells:
        config.CurrentCellDebug.RevertColor()
        config.CurrentCellDebug = config.Grid[config.CurrentCellDebug.y + 1][config.CurrentCellDebug.x]
        DebuggerColorChange(config.CurrentCellDebug)
        config.root.after(config.Speed, config.canvas.update())

def moveRight(event):
    if config.CurrentCellDebug.WallRight == False and config.CurrentCellDebug.x < config.HCells:
        config.CurrentCellDebug.RevertColor()
        config.CurrentCellDebug = config.Grid[config.CurrentCellDebug.y][config.CurrentCellDebug.x + 1]
        DebuggerColorChange(config.CurrentCellDebug)
        config.root.after(config.Speed, config.canvas.update())

def WallDebugger():
    config.root.bind('<Left>', moveLeft)
    config.root.bind('<Right>', moveRight)
    config.root.bind('<Down>', moveDown)
    config.root.bind('<Up>', moveUp)


def WallDebuggerButton():
    config.CurrentCellDebug = config.Grid[0][0]
    WallDebugger()
####################################################################################################