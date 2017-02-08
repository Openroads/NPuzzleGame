import math
import resource
import time
from Algorithms import bfs
from Algorithms import dfs
from NPuzzleGame import Board
import sys

if len(sys.argv) == 1:
    #alg = sys.argv[1]
    #inputList = sys.argv[2].split(',')
    #inputList = [int(x) for x in inputList]
    inputList =[3,1,2,4,0,5,6,7,8]
    size = math.sqrt(len(inputList))
    if size.is_integer():
        alg = 'dfs'
        board = Board(inputList)
        Board.initializeStaticVariables(inputList)
        board.designateBorders()
        if alg == 'bfs':
            start = time.time()
            path = bfs(board)
            end = time.time()
            time_measure = end - start
            print(time_measure)

            movements = path[0]
            movement_name = [move.movement for move in path[0]]
            for x in range(0, len(movements)):
                print(movements[x].movement)
                movements[x].board.showBoard()
            print("Nodes expanded %d" % path[1])
            print("Fringe_size: %d" % path[2])
            print("max_fringe_size: %d" % path[3])
            print("search_depth: %d" % path[4])
            print("Max_search_depth: %d" % path[5])
            print("Resource:")
            print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

            with open("Output.txt", "w") as text_file:
                print("path_to_goal: {}".format(movement_name[1:]), file=text_file)
                print("cost_of_path: {}".format(len(movement_name)-1), file=text_file)
                print("nodes_expanded: {}".format(path[1]), file=text_file)
                print("fringe_size: {}".format(path[2]), file=text_file)
                print("max_fringe_size: {}".format(path[3]), file=text_file)
                print("search_depth: {}".format(path[4]), file=text_file)
                print("max_search_depth: {}".format(path[5]), file=text_file)
                print("running_time: {}".format(time_measure), file=text_file)
                print("max_ram_usage: {}".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024), file=text_file)

        elif alg == 'dfs':
            start = time.time()
            path = dfs(board)

            end = time.time()
            time_measure = end - start
            print(time_measure)

            movements = path[0]
            movement_name = [move.movement for move in path[0]]

            with open("Output.txt", "w") as text_file:
                print("path_to_goal: {}".format(movement_name[1:]), file=text_file)
                print("cost_of_path: {}".format(len(movement_name)-1), file=text_file)
                print("nodes_expanded: {}".format(path[1]), file=text_file)
                print("fringe_size: {}".format(path[2]), file=text_file)
                print("max_fringe_size: {}".format(path[3]), file=text_file)
                print("search_depth: {}".format(path[4]), file=text_file)
                print("max_search_depth: {}".format(path[5]), file=text_file)
                print("running_time: {}".format(time_measure), file=text_file)
                print("max_ram_usage: {}".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024), file=text_file)

            for node in path[0]:
                print(node.movement)
                node.board.showBoard()
            print("Nodes expanded %d" % path[1])
            print("Cost of path: %d" % (len(movement_name)-1))
            print("Fringe_size: %d" % path[2])
            print("max_fringe_size: %d" % path[3])
            print("search_depth: %d" % path[4])
            print("Max_search_depth: %d" % path[5])
            print("Resource:")
            print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024)
        elif alg == 'astar':
            path = astar(board)


    else:
        print("Incorrect data")