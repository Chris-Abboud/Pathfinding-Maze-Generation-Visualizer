class Cell():
    def __init__(self, x, y, canvas, SquareSize, root, color, DrawMode):
        self.visited = False 
        self.SearchVisited = False
        self.isWall = False
        
        self.x = x #X cordinate
        self.y = y #Y cordinate
        self.color = color
        self.canvas = canvas
        self.root = root
        self.distance = 10 ** 6 #Use for dijkstras
        self.parentCell = 0 #Use For dijkstras, sort of a linked list


        DrawModeBool = True
        borderColor = "Black"

        #Had to create properties for each  wall so that removing a wall is an easy operation
        self.SquareCell = canvas.create_rectangle(x * SquareSize, y * SquareSize, (x+1) * SquareSize, (y+1) * SquareSize, fill = color, outline = "") 

        if DrawMode:
            borderColor = "White"

        self.topWall = canvas.create_line(x * SquareSize, y * SquareSize, (x + 1) * SquareSize, y * SquareSize, fill = borderColor)
        self.botWall = canvas.create_line(x * SquareSize, (y + 1) * SquareSize, (x + 1) * SquareSize, (y + 1) * SquareSize, fill = borderColor)
        self.leftWall = canvas.create_line(x * SquareSize, y * SquareSize, x * SquareSize, (y + 1) * SquareSize, fill = borderColor)
        self.rightWall = canvas.create_line((x + 1) * SquareSize, y  * SquareSize, (x + 1) * SquareSize, (y + 1) * SquareSize, fill = borderColor)
        #root.after(1, canvas.update()) #Adds a delay of 1 between each run through, this is just for debugging


       
        if DrawMode:
            DrawModeBool = False #Meaning if its in draw mode, then there is no walls to start
            self.canvas.delete(self.topWall)
            self.canvas.delete(self.botWall)
            self.canvas.delete(self.leftWall)
            self.canvas.delete(self.rightWall)

        self.WallUp = DrawModeBool
        self.WallDown = DrawModeBool
        self.WallLeft = DrawModeBool
        self.WallRight = DrawModeBool

    
    def ChangeColor(self):
        self.color = "White"
        self.canvas.itemconfig(self.SquareCell, fill = self.color)
    
    def RevertColor(self):
        self.canvas.itemconfig(self.SquareCell, fill = self.color)

    def deleteTopWall(self):
        self.canvas.delete(self.topWall)
        self.WallUp = False
    
    def deleteBotWall(self):
        self.canvas.delete(self.botWall)
        self.WallDown = False
    
    def deleteRightWall(self):
        self.canvas.delete(self.rightWall)
        self.WallRight = False
    
    def deleteLeftWall(self):
        self.canvas.delete(self.leftWall)
        self.WallLeft = False