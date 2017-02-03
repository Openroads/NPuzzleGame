import math
import copy
from NPuzzleGame import Board
from NPuzzleGame import State

inputList =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
size = math.sqrt(len(inputList))
board = Board(3)

board.setTiles([6,8,0,7,5,4,3,2,1])
boardCop = copy.deepcopy(board)
boardCop.swappLeft()
board.showBoard()
boardCop.showBoard()

print (board.checkState())
board.setTiles([1,2,3,4,5,6,7,8,0])
#board.showBoard()
print (board.checkState())
if size.is_integer():
    board2 = Board(int(size))
    board2.setTiles(inputList)
    #board2.showBoard()


def bfs(inputList):

    size = math.sqrt(len(inputList))

    if size.is_integer():
        board = Board(int(size))
        initialState = State(board)
        frontier = [initialState]
        explored = []

        while len(frontier)>0:
            state = frontier.pop(0)
            explored.append(state)

            if state.goalTest():
                return True
            #else:
                #tutaj dodac sasiadow do frontierow

    else:
        print("Incorrect data")

