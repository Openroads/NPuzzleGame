import math
import copy
from NPuzzleGame import Board
from NPuzzleGame import State
firstinList = [1,2,5,3,4,0,6,7,8]
firstinList = [1,2,5,3,7,4,0,7,8]
gameList = [1,2,5,3,4,0,6,7,8]
#inputList =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
inputList =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


def bfs(inputList):
    size = math.sqrt(len(inputList))
    if size.is_integer():
        nodeList = []
        board = Board(int(size))
        board.setTiles(inputList)
        initialState = State(board)
        frontier = [initialState]
        explored = []

        while len(frontier) > 0:
            state = frontier.pop(0)
            explored.append(state)

            if state.goalTest():

                while state != None:
                    nodeList.append(state)
                    state = state.parent
                nodeList.reverse()
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

        return nodeList
    else:
        print("Incorrect data")

path = bfs(gameList)
for node in path:
    print(node.movement)
    node.board.showBoard()
