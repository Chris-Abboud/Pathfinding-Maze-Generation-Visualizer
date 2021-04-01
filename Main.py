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

MazeMenu = Menu(Selection, tearoff=False) #Menu for Maze Generation Algorithms
Selection.add_cascade(label = "Maze Generation Algorithms", menu = MazeMenu)
Selection.add_cascade(label = "Clear Canvas", command = lambda: clearCanvas(config.HCells, config.VCells, [], config.canvas, config.root, config.BackgroundColor))
Selection.add_cascade(label = "Pause / Play", command = pausePlay)


MazeMenu.add_command(label = "Recursive Back Tracking", command = lambda: RecursiveBackTrackButton()) # Prevents Command from auto running
MazeMenu.add_command(label = "Hunt and Kill", command = lambda: HuntAndKillButton())

speedSlider = Scale(config.root, label = "Adjust Speed Here", from_= 0, to = 100, showvalue = 0, resolution = 1, length = 300, orient = HORIZONTAL, command = lambda val: adjustSpeed(val))
speedSlider.set(10)

speedSlider.pack()

config.root.option_add('*tearOff',False)
config.root.mainloop()

