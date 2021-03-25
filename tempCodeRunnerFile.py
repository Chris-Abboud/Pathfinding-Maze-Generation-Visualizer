Cell.visited = True

    while len(Stack) != 0:

        Cell.ChangeColor()
        GoodMoves = findGoodMoves(Cell, Grid, canvas)
        

        if (len(GoodMoves) > 0):
            RandoCell = random.randint(0,len(GoodMoves) - 1)
            ChosenCombo = GoodMoves[RandoCell] # Will be in form (Cell, Location relative to original)

        if (len(GoodMoves) > 0):
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

            Stack.append(ChosenCell)
            root.after(1, canvas.update())
        else:
            Stack[-1].TrackColor()
            Stack.pop()
        if len(Stack) > 0:
            return FindNext(Stack[-1], Stack, canvas, root)
