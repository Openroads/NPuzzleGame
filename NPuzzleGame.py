import math


class State:
    def __init__(self, prevState,move="Initial"):
        self.parent = prevState
        if move == "Initial":
            self.board = prevState
            self.depth = 0
            self.parent = None
            self.movement = None
        else:
            self.board = Board(prevState.board.array[:])
            self.movement = move
            self.depth = self.parent.depth + 1
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
        return self.board.checkState1() or self.board.checkState2()

    def __eq__(self, other):
        if type(other) is State:
            return self.board == other.board
        else:
            return False


class Board:
    leftBorder = []
    rightBorder = []

    def __init__(self, tilesList):
        self.__moveDirections = {'Up': True, 'Down': True, 'Left': True, 'Right': True}
        self.boardSize = len(tilesList)
        self.n_dim = int(math.sqrt(self.boardSize))
        self.array = tilesList
        self.blankPosition = self.array.index(0)

    def __eq__(self, other):
        return self.array == other.array

    def showBoard(self):
        for x in range(0,self.boardSize):
            print(self.array[x], end=" ")
            if x in self.rightBorder:
                print()

    def checkState1(self):
        checkCount = 0
        for x in self.array:
                if checkCount != x:
                    return False
                checkCount += 1
        return True

    def checkState2(self):
        checkCount = 1

        for x in range(0, self.boardSize-1):
            if x != checkCount:
                return False
        if self.array[self.boardSize-1] == 0:
            return True

    def checkDirectionsMovement(self):

        if self.blankPosition < self.n_dim:
            self.__moveDirections['Up'] = False
        else:
            self.__moveDirections['Up'] = True
        if self.blankPosition >= self.boardSize - self.n_dim:
            self.__moveDirections['Down'] = False
        else:
            self.__moveDirections['Down'] = True
        if self.__checkIfRightBorder():
            self.__moveDirections['Right'] = False
        else:
            self.__moveDirections['Right'] = True
        if self.__checkIfLeftBorder():
            self.__moveDirections['Left'] = False
        else:
            self.__moveDirections['Left'] = True
        return self.__moveDirections

    def swappUp(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition -= self.n_dim
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[self.blankPosition]

    def swappDown(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition += self.n_dim
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[self.blankPosition]

    def designateBorders(self):
        left = 0
        while left < self.boardSize:
            Board.leftBorder.append(left)
            left += self.n_dim

        right = self.n_dim-1
        while right <= self.boardSize:
            Board.rightBorder.append(right)
            right += self.n_dim

    def __checkIfLeftBorder(self):
        return self.blankPosition in Board.leftBorder

    def __checkIfRightBorder(self):
        return self.blankPosition in Board.rightBorder

    def swappLeft(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition -= 1
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[self.blankPosition]

    def swappRight(self):
        prevBlankPosition = self.blankPosition
        self.blankPosition += 1
        self.array[self.blankPosition], self.array[prevBlankPosition] = self.array[prevBlankPosition], self.array[self.blankPosition]
