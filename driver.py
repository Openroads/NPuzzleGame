import math
import resource
import time
from Algorithms import bfs
from Algorithms import dfs
from NPuzzleGame import Board
import sys

if len(sys.argv) == 1:
    print(sys.argv)
    inputList = [1,2,5,3,4,0,6,7,8]
    size = math.sqrt(len(inputList))
    if size.is_integer():
        print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000)
        start = time.time()

        board = Board(inputList)
        path = dfs(board)

        end = time.time()
        print(end - start)

        for node in path[0]:
            print(node.movement)
            node.board.showBoard()
        print("Nodes expanded %d" % path[1])
    else:
        print("Incorrect data")