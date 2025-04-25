def dls(start, goal, map):
    #TRACK NUMBER OF NODES EXPLORED, NUMBER OF SUCCESSORS, NUMBER OF NODES STORED
    #Stack based data structure
    # Explore neighbors, add them to stack
    # Once the depth limit has been reached, recurse
    # End once goal state is reached
    # #make sure to add nodes explored, expanded, and maintained

    stack = [(start, 0)]
    nodes_explored = 0
    nodes_expanded = 0
    nodes_maintained = 0
    depth = 0

    while True:
        if simple_dls(start, goal, map, depth) == None:
            depth += 1
            simple_dls(start, goal, map, depth)
        else:
            return simple_dls(start, goal, map, depth)







def simple_dls(start, goal, map, depth):
    stack = [(start, 0)]
    nodes_explored = 0
    nodes_expanded = 0
    nodes_maintained = 0
    cost = 0
    visited = []

    while stack:
        curr_node = stack.pop()
        nodes_explored += 1

        if curr_node[0] == goal:
            visited.append(goal)
            return visited, cost, nodes_explored, nodes_expanded, nodes_maintained

        if curr_node not in visited:
            visited.append(curr_node)
            neighbors = list(map[curr_node[0]].keys())

            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in stack:
                    full_neighbor = (neighbor, int(curr_node[1]+1))
                    if full_neighbor[1] < depth:
                        stack.append(full_neighbor)
                        nodes_expanded += 1


    return None
