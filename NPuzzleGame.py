import copy


class State:

    def __init__(self, prevBoard,move="Initial"):
        if move == "Initial":
            self.board = prevBoard
        else:
            self.board = copy.deepcopy(prevBoard)
            if move == "Up":
                self.board.swappUp()
            elif move == "Down":
                self.board.swappDown()
            elif move == "Left":
                self.board.swappLeft()
            elif move == "Right":
                self.board.swappRight()
            else:
                print("It's problem with new state - swapping")

    def goalTest(self):
        return self.board.checkState()

    def __eq__(self, other):
        return self.board == other.board

class Board:
    def __init__(self, n):
        self.n_dim = n
        self.boardSize = n * n
        self.array = [None] * n
        self.blankPosition = self.boardSize
        for i in range(0, n):
            self.array[i] = [-1] * n

    def __eq__(self, other):
        if self.n_dim != other.n_dim:
            return False
        for i in range(0, self.n_dim):
            for j in range(0, self.n_dim):
                if self.array[i][j] != other[i][j]:
                    return False
        return True

    def setTiles(self, tilesList):
        self.blankPosition = [i for i, x in enumerate(tilesList) if x == 0][0]
        print(self.blankPosition)
        if len(tilesList) != self.boardSize:
            print("Incorrect number of tiles")
            return False
        else:
            it = 0
            for i in range(0, self.n_dim):
                self.array[i] = tilesList[it:it + self.n_dim]
                it += self.n_dim

            '''
            x = 0
            for i in range(0,self.n_dim):
                for j in range(0,self.n_dim):
                    self.array[i][j] = tilesList[x]
                    x+=1
            '''

    def showBoard(self):
        for x in self.array:
            print(x)

    def checkState(self):
        checkCount = 1
        for row in self.array:
            for x in row:
                if checkCount != x:
                    if checkCount == self.boardSize and x == 0:
                        return True
                    else:
                        return False
                checkCount += 1
        return True

    def checkDirectionsMovement(self):
        moveDirections = {"Up": False, "Down": False, "Left": False, "Right": False}


    def swappUp(self):
        if self.blankPosition < self.n_dim:
            print("You can't go up")
            return False
        else:
            position = 0
            value = 0
            prevBlankPosition = self.blankPosition
            self.blankPosition -= self.n_dim
            for i in range(0, self.n_dim):
                for j in range(0, self.n_dim):
                    if position == self.blankPosition:
                        value = self.array[i][j]
                        self.array[i][j] = 0
                    position += 1
            position = 0

            for i in range(0, self.n_dim):
                for j in range(0, self.n_dim):
                    if position == prevBlankPosition:
                        self.array[i][j] = value
                    position += 1
            return True

    def swappDown(self):
        if self.blankPosition >= self.boardSize - self.n_dim:
            print("You can't go down")
            return False
        else:
            position = 0
            value = 0
            prevBlankPosition = self.blankPosition
            self.blankPosition += self.n_dim
            for i in range(0, self.n_dim):
                for j in range(0, self.n_dim):
                    if position == self.blankPosition:
                        value = self.array[i][j]
                        self.array[i][j] = 0
                    position += 1
            position = 0

            for i in range(0, self.n_dim):
                for j in range(0, self.n_dim):
                    if position == prevBlankPosition:
                        self.array[i][j] = value
                    position += 1
            return True

    def __checkIfLeftBorder(self):
        position = 0
        for i in range(0, self.n_dim):
            for j in range(0, self.n_dim):
                if position == self.blankPosition:
                    if self.array[i][0] == 0:
                        return True
                position += 1
        return False

    def __checkIfRightBorder(self):
        position = 0
        for i in range(0, self.n_dim):
            for j in range(0, self.n_dim):
                if position == self.blankPosition:
                    print(self.array[i][self.n_dim-1])
                    if self.array[i][self.n_dim-1] == 0:
                        return True
                position += 1
        return False

    def swappLeft(self):
        if self.__checkIfLeftBorder():
            print("You can't go Left")
            return False
        else:
            position=0
            value = 0
            prevBlankPosition = self.blankPosition
            self.blankPosition -= 1
            for i in range(0, self.n_dim):
                for j in range(0, self.n_dim):
                    if position == self.blankPosition:
                        value = self.array[i][j]
                        self.array[i][j] = 0
                    position += 1
            position = 0

            for i in range(0, self.n_dim):
                for j in range(0, self.n_dim):
                    if position == prevBlankPosition:
                        self.array[i][j] = value
                    position += 1
            return True

    def swappRight(self):
        if self.__checkIfRightBorder():
            print("You can't go Right")
            return False
        else:
            position = 0
            value = 0
            prevBlankPosition = self.blankPosition
            self.blankPosition += 1
            for i in range(0, self.n_dim):
                for j in range(0, self.n_dim):
                    if position == self.blankPosition:
                        value = self.array[i][j]
                        self.array[i][j] = 0
                    position += 1
            position = 0

            for i in range(0, self.n_dim):
                for j in range(0, self.n_dim):
                    if position == prevBlankPosition:
                        self.array[i][j] = value
                    position += 1
            return True
