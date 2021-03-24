class Cell():
    def __init__(self, x, y, canvas, SquareSize, root, color):
        self.visited = False 
        self.x = x #X cordinate
        self.y = y #Y cordinate
        self.color = color
        self.canvas = canvas

        #Had to create properties for each  wall so that removing a wall is an easy operation
        self.SquareCell = canvas.create_rectangle(x * SquareSize, y * SquareSize, (x+1) * SquareSize, (y+1) * SquareSize, outline = "") 
        self.topWall = canvas.create_line(x * SquareSize, y * SquareSize, (x + 1) * SquareSize, y * SquareSize, fill = "Black")
        self.botWall = canvas.create_line(x * SquareSize, (y + 1) * SquareSize, (x + 1) * SquareSize, (y + 1) * SquareSize, fill = "Black")
        self.leftWall = canvas.create_line(x * SquareSize, y * SquareSize, x * SquareSize, (y + 1) * SquareSize, fill = "Black")
        self.rightWall = canvas.create_line((x + 1) * SquareSize, (y + 1) * SquareSize, (x + 1) * SquareSize, (y + 1) * SquareSize, fill = "Black")
        #root.after(1, canvas.update()) #Adds a delay of 1 between each run through, this is just for debugging

        self.WallUp = False
        self.WallDown = False
        self.WallLeft = False
        self.WallRight = False
    
    def deleteTopWall(self):
        self.canvas.itemconfig(self.topWall, fill = self.color)
    
    def deleteBopWall(self):
        self.canvas.itemconfig(self.botWall, fill = self.color)
    
    def deleteRightWall(self):
        self.canvas.itemconfig(self.rightWall, fill = self.color)
    
    def deleteLeftWall(self):
        self.canvas.itemconfig(self.leftWall, fill = self.color)