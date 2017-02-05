from NPuzzleGame import State
firstinList = [1,2,5,3,4,0,6,7,8]
#firstinList = [1,2,5,3,7,4,0,7,8]
gameList = [1,0,5,3,4,2,6,7,8]
#inputList =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
inputList =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def bfs(board):

        initialState = State(board)
        frontier = [initialState]
        explored = []

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
            #state.board.showBoard()
            #print('-----------------')


            if (nodes_expanded > 10880):
                print(nodes_expanded)
            explored.append(state)
            #CHECKING GOAL TEST###########################################
            if state.goalTest():
                fringe_size = length
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
            length = len(frontier)
        return nodeList, nodes_expanded


def dfs(board):
    initialState = State(board)
    frontier = [initialState]
    explored = []
    nodes_expanded = 0
    nodeList = []

    length = len(frontier)
    while length > 0:
        nodes_expanded += 1
        #print(nodes_expanded)
        state = frontier.pop()

        explored.append(state)

        if state.goalTest():
            while state != None:
                #print(state)
                nodeList.append(state)
                state = state.parent
            nodeList.reverse()
            return nodeList,nodes_expanded

        directions = state.board.checkDirectionsMovement()
        if directions['Right']:
            newState = State(state, 'Right')
            if newState not in frontier and newState not in explored:
                frontier.append(newState)
        if directions['Left']:
            newState = State(state, 'Left')
            if newState not in frontier and newState not in explored:
                frontier.append(newState)
        if directions['Down']:
            newState = State(state, 'Down')
            if newState not in frontier and newState not in explored:
                frontier.append(newState)
        if directions['Up']:
            newState = State(state, 'Up')
            if newState not in frontier and newState not in explored:
                frontier.append(newState)

        length = len(frontier)
    return nodeList, nodes_expanded



