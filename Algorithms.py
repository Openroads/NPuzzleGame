import math

from NPuzzleGame import State
from heapq import heappush, heappop

def bfs(board):
        initialState = State(board)
        frontier = [initialState]
        explored = set(str(initialState.board.array))

######  data to return for the program output

        nodeList = []
        nodes_expanded = 0
        max_fringe = 0
        max_search_depth = 0
        length = len(frontier)

        while length > 0:
            if length > max_fringe:
                max_fringe = length
            state = frontier.pop(0)

            if max_search_depth < state.depth:
                max_search_depth = state.depth

            #CHECKING GOAL TEST###########################################
            if state.goalTest():
                fringe_size = len(frontier)
                search_depth = state.depth
                while state != None:
                    #print(state)
                    nodeList.append(state)
                    state = state.parent
                nodeList.reverse()
                return nodeList, nodes_expanded, fringe_size, max_fringe,search_depth,max_search_depth
            ##############################################################
            nodes_expanded += 1
            directions = state.board.checkDirectionsMovement()
            if directions['Up']:
                newState = State(state, 'Up')
                strState = str(newState.board.array)
                if strState not in explored:
                    frontier.append(newState)
                    explored.add(strState)
            if directions['Down']:
                newState = State(state, 'Down')
                strState = str(newState.board.array)
                if strState not in explored:
                    frontier.append(newState)
                    explored.add(strState)
            if directions['Left']:
                newState = State(state, 'Left')
                strState = str(newState.board.array)
                if strState not in explored:
                    frontier.append(newState)
                    explored.add(strState)
            if directions['Right']:
                newState = State(state, 'Right')
                strState = str(newState.board.array)
                if strState not in explored:
                    frontier.append(newState)
                    explored.add(strState)
            length = len(frontier)
        return []


def dfs(board):
        initialState = State(board)
        frontier = [initialState]
        explored = set(str(initialState.board.array))
        nodes_expanded = 0
        nodeList = []
        max_fringe = 0
        max_search_depth = 0

        length = len(frontier)
        while length > 0:

            if length > max_fringe:
                max_fringe = length

            state = frontier.pop()

            if max_search_depth < state.depth:
                max_search_depth = state.depth

            if state.goalTest():
                fringe_size = len(frontier)
                search_depth = state.depth
                while state != None:
                    nodeList.append(state)
                    state = state.parent
                nodeList.reverse()
                return nodeList, nodes_expanded, fringe_size, max_fringe,search_depth,max_search_depth

            nodes_expanded += 1
            directions = state.board.checkDirectionsMovement()
            if directions['Right']:
                newState = State(state, 'Right')
                strState = str(newState.board.array)
                if strState not in explored:
                    frontier.append(newState)
                    explored.add(strState)
            if directions['Left']:
                newState = State(state, 'Left')
                strState = str(newState.board.array)
                if strState not in explored:
                    frontier.append(newState)
                    explored.add(strState)
            if directions['Down']:
                newState = State(state, 'Down')
                strState = str(newState.board.array)
                if strState not in explored:
                    frontier.append(newState)
                    explored.add(strState)
            if directions['Up']:
                newState = State(state, 'Up')
                strState = str(newState.board.array)
                if strState not in explored:
                    frontier.append(newState)
                    explored.add(strState)
            length = len(frontier)
        return []


def astar(board):
    initialState = State(board)
    frontier = []
    heappush(frontier,(0,initialState))
    explored = set(str(initialState.board.array))

    ######  data to return for the program output

    nodeList = []
    nodes_expanded = 0
    max_fringe = 0
    max_search_depth = 0
    length = len(frontier)

    while length > 0:
        if length > max_fringe:
            max_fringe = length

        state = heappop(frontier)

        if max_search_depth < state.depth:
            max_search_depth = state.depth

        # CHECKING GOAL TEST###########################################
        if state.goalTest():
            fringe_size = len(frontier)
            search_depth = state.depth
            while state != None:
                # print(state)
                nodeList.append(state)
                state = state.parent
            nodeList.reverse()
            return nodeList, nodes_expanded, fringe_size, max_fringe, search_depth, max_search_depth
        ##############################################################
        nodes_expanded += 1

        directions = state.board.checkDirectionsMovement()

        for direction,flag in directions.items():
            if flag:
                newState = State(state, direction)
                strState = str(newState.board.array)
                if strState not in explored:
                    explored.add(strState)
                    heurist_val = astar_heuristic(state.board)
                    heappush(frontier,(heurist_val,newState))


        length=len(frontier)
    return []


def astar_heuristic(board):
    value = 0
    for x in range(0,board.boardSize):
        value = value + math.fabs(x - board.array[x])
    return value