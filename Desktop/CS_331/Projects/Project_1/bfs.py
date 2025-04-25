def bfs(start, goal, map):
    #Queue data structure and list for visited
    #store all neighbors in queue
    #move to next item in queue once all neighbors are explored
    #end when goal state is current node
    #make sure to add nodes explored, expanded, and maintained
    #

    queue = [start]
    visited = []
    cost = 0
    nodes_explored = 0
    nodes_expanded = 0
    nodes_maintained = len(queue)

    while queue:
        curr_node = queue.pop(0)
        nodes_explored += 1
        if curr_node == goal:
            visited.append(goal)
            return visited, cost, nodes_explored, nodes_expanded, nodes_maintained
        if curr_node not in visited:
            visited.append(curr_node)
            neighbors = list(map[curr_node].keys())
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    nodes_expanded += 1

    return None
