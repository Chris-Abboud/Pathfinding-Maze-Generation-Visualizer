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

PlaceStartButton = Button(config.root, text = "Place/ Replace Start Cell", background = "#4cdfff", command = bindPlaceStart)
PlaceStartButton.place(x = 140, y = config.CanvasHeight + 15)

PlaceEndButton = Button(config.root, text = "Place/Replace End Cell", background = "#ffb763", command = bindPlaceEnd)
PlaceEndButton.place(x = 625, y = config.CanvasHeight + 15)

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

PathFindingMenu.add_command(label = "Dijkstras")
PathFindingMenu.add_command(label = "A*")
PathFindingMenu.add_command(label = "D*")
PathFindingMenu.add_command(label = "Breadth First Search")


speedSlider = Scale(config.root, label = "Adjust Speed Here", from_= 0, to = 100, showvalue = 0, resolution = 1, length = 300, orient = HORIZONTAL, command = lambda val: adjustSpeed((val)))
speedSlider.set(1)

speedSlider.pack()


config.root.option_add('*tearOff',False)
config.root.mainloop()