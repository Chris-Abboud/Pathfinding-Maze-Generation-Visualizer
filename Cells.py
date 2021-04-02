class Cell():
    def __init__(self, x, y, canvas, SquareSize, root, color):
        self.visited = False 
        self.x = x #X cordinate
        self.y = y #Y cordinate
        self.color = color
        self.canvas = canvas
        self.root = root

        #Had to create properties for each  wall so that removing a wall is an easy operation
        self.SquareCell = canvas.create_rectangle(x * SquareSize, y * SquareSize, (x+1) * SquareSize, (y+1) * SquareSize, fill = color, outline = "") 
        self.topWall = canvas.create_line(x * SquareSize, y * SquareSize, (x + 1) * SquareSize, y * SquareSize, fill = "Black")
        self.botWall = canvas.create_line(x * SquareSize, (y + 1) * SquareSize, (x + 1) * SquareSize, (y + 1) * SquareSize, fill = "Black")
        self.leftWall = canvas.create_line(x * SquareSize, y * SquareSize, x * SquareSize, (y + 1) * SquareSize, fill = "Black")
        self.rightWall = canvas.create_line((x + 1) * SquareSize, y  * SquareSize, (x + 1) * SquareSize, (y + 1) * SquareSize, fill = "Black")
        #root.after(1, canvas.update()) #Adds a delay of 1 between each run through, this is just for debugging

        self.WallUp = True
        self.WallDown = True
        self.WallLeft = True
        self.WallRight = True
    
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