

config.root.config(menu = Selection)

PlaceStartButton = Button(config.root, text = "Place/ Replace Start Cell", background = "#4cdfff", command = bindPlaceStart)
PlaceStartButton.place(x = 50, y = config.CanvasHeight + 15)

PlaceEndButton = Button(config.root, text = "Place/Replace End Cell", background = "#ffb763", command = bindPlaceEnd)
PlaceEndButton.place(x = 225, y = config.CanvasHeight + 15)

MazeMenu = Menu(Selection, tearoff=False) #Menu for Maze Generation Algorithms
PathFindingMenu = Menu(Selection, tearoff = False) #PathFinding Algos
