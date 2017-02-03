import math
import copy
from NPuzzleGame import Board
from NPuzzleGame import State
firstinList = [1,2,5,3,4,0,6,7,8]
#inputList =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
inputList =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
'''size = math.sqrt(len(inputList))
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

'''

def bfs(inputList):
    nodeList =[]
    size = math.sqrt(len(inputList))

    if size.is_integer():
        board = Board(int(size))
        board.setTiles(inputList)
        initialState = State(board)
        frontier = [initialState]
        explored = []

        while len(frontier) > 0:
            state = frontier.pop(0)
            print("node:")
            state.board.showBoard()
            explored.append(state)

            if state.goalTest():
                print("Out put :")

                while state != None:
                    print("Node:")
                    nodeList.append(state)
                    state = state.parent
                return nodeList

            directions = state.board.checkDirectionsMovement()
            if directions['Up']:
                newState = State(state, 'Up')
                if newState not in frontier and newState not in explored:
                    frontier.append(newState)
            if directions['Down']:
                newState = State(state, 'Down')
                if newState not in frontier and newState not in explored:
                    frontier.append(newState)
            if directions['Left']:
                newState = State(state, 'Left')
                if newState not in frontier and newState not in explored:
                    frontier.append(newState)
            if directions['Right']:
                newState = State(state, 'Right')
                if newState not in frontier and newState not in explored:
                    frontier.append(newState)

        return False
    else:
        print("Incorrect data")

path = bfs(firstinList)
for node in path:
    node.board.showBoard()
    print(node.movement)