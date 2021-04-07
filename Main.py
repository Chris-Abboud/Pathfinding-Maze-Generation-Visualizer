## Initially building the Recursive Backtracking Algorithm for maze generation
from  tkinter import *
from Cells import *
from Helpers import *

import random
import config
import time
import sys

sys.setrecursionlimit(10**6)

Selection = Menu(config.root)

config.root.config(menu = Selection)

PlaceStartButton = Button(config.root, text = "Place Start Cell", background = "#4cdfff", command = bindPlaceStart)
PlaceStartButton.place(x = 20, y = config.CanvasHeight + 15)

PlaceEndButton = Button(config.root, text = "Place End Cell", background = "#ffb763", command = bindPlaceEnd)
PlaceEndButton.place(x = 125, y = config.CanvasHeight + 15)

speedSlider = Scale(config.root, label = "Adjust Speed Here", from_= 0, to = 150, showvalue = 0, resolution = 1, length = 350, orient = HORIZONTAL, command = lambda val: adjustSpeed((val)))
speedSlider.set(1)

speedSlider.place(x = 230, y = config.CanvasHeight + 1)

PlaceDrawButton = Button(config.root, text = "Custom Draw Walls", background = "#5a5a5a", fg = "White", command = bindDrawingMode,)
PlaceDrawButton.place(x = 605, y = config.CanvasHeight + 15)

PlaceClearWall = Button(config.root, text = "Clear Search", background = "#5a5a5a", fg = "White", command = clearSearch)
PlaceClearWall.place(x = 730, y = config.CanvasHeight + 15)

PlaceEraseWall = Button(config.root, text = "Clear Walls", background = "#5a5a5a", fg = "White", command = clearWalls)
PlaceEraseWall.place(x = 820, y = config.CanvasHeight + 15)


MazeMenu = Menu(Selection, tearoff=False) #Menu for Maze Generation Algorithms
PathFindingMenu = Menu(Selection, tearoff = False) #PathFinding Algos

Selection.add_cascade(label = "Maze Generation Algorithms", menu = MazeMenu)
Selection.add_cascade(label = "Pathfinding Algorithms", menu =  PathFindingMenu)

Selection.add_cascade(label = "Clear Canvas", command = lambda: clearCanvas(config.HCells, config.VCells, [], config.canvas, config.root, config.BackgroundColor))
Selection.add_cascade(label = "Start / Stop", command = pausePlay)
Selection.add_cascade(label = "Enter Wall Debugger Mode", command = lambda: WallDebuggerButton())

MazeMenu.add_command(label = "Recursive Back Tracking", command = lambda: RecursiveBackTrackButton()) # Prevents Command from auto running
MazeMenu.add_command(label = "Hunt and Kill", command = lambda: HuntAndKillButton())
MazeMenu.add_command(label = "Binary Tree", command = lambda: BinaryTreeButton())
MazeMenu.add_command(label = "Prims Algorithm", command = lambda: PrimsAlgorithmButton())
MazeMenu.add_command(label = "Sidewinder Algorithm", command = lambda: SidewinderButton())

PathFindingMenu.add_command(label = "Dijkstras", command = lambda: DijkstrasAlgorithmButton())
PathFindingMenu.add_command(label = "A*")
PathFindingMenu.add_command(label = "D*")
PathFindingMenu.add_command(label = "Breadth First Search")





config.root.option_add('*tearOff',False)
config.root.mainloop()