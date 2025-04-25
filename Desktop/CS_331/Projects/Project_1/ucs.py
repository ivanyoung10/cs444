import heapq

def ucs(start, goal, map):
    # priority queue and visited node path length from start
    # check neighbors and add them to queue
    # check if any other path to a node is better than another
    # if goal node is curr node break
    # #make sure to add nodes explored, expanded, and maintained

    priority_queue = [(start, 0)]
    visited = {start: (0, None)}
    nodes_explored = 0
    nodes_expanded = 0
    nodes_maintained = len(priority_queue)

    while priority_queue:
        curr_node, curr_cost = heapq.heappop(priority_queue)
        nodes_explored += 1
        if curr_node == goal:
            return reconstruct_path(visited, start, goal), curr_cost, nodes_explored, nodes_expanded, nodes_maintained

        neighbors = (map[curr_node])

        for neighbor in neighbors:
            total_cost = curr_cost + int(map[curr_node][neighbor])
            if neighbor not in visited or total_cost < visited[neighbor][0]:
                nodes_expanded += 1
                visited[neighbor] = (total_cost, curr_node)
                heapq.heappush(priority_queue, (neighbor, total_cost))

    return None

def reconstruct_path(visited, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1]
    path.reverse()
    return path


#used this for help with the path reconstruction
#https://www.geeksforgeeks.org/uniform-cost-search-ucs-in-ai/
