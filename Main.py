## Initially building the Recursive Backtracking Algorithm for maze generation
from tkinter import *
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

MazeMenu.add_command(label = "Recursive Back Tracking", command = lambda: RecursiveBackTrackButton(config.Stack[0], config.Stack, config.canvas, config.root)) # Prevents Command from auto running
MazeMenu.add_command(label = "Hunt and Kill", command = lambda: HuntAndKillButton())


config.root.option_add('*tearOff',FALSE)
config.root.mainloop()

