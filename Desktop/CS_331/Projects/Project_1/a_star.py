import heapq
import math

def a_star(start, goal, map, coordinates):
    # find for distance on globe algorithm
    # Uses a priority Queue
    # first import start
    # check all local nodes, take euclidian distance first
    # move current node to one with shortest euclidian distance
    # if node has been explored, remove it from the list
    # make sure to add nodes explored, expanded, and maintained


    priority_queue = [(float(0), 0, start)]
    visited = {start: (0, None)}
    nodes_explored = 0
    nodes_expanded = 0
    nodes_maintained = len(priority_queue)

    while priority_queue:
        curr_cost, curr_dist, curr_node = heapq.heappop(priority_queue)
        nodes_explored += 1
        if curr_node == goal:
            return reconstruct_path(visited, start, goal), curr_dist, nodes_explored, nodes_expanded, nodes_maintained

        neighbors = (map[curr_node])

        for neighbor in neighbors:
            travel_cost = int(map[curr_node][neighbor])
            ucs_cost = curr_dist + travel_cost
            heuristic_cost = haversine(coordinates[neighbor][0], coordinates[neighbor][1], coordinates[goal][0], coordinates[goal][1])
            total_cost = ucs_cost + heuristic_cost
            if neighbor not in visited or ucs_cost < visited[neighbor][0]:
                nodes_expanded += 1
                visited[neighbor] = (ucs_cost, curr_node)
                heapq.heappush(priority_queue,(total_cost, ucs_cost, neighbor))

    return None

def reconstruct_path(visited, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1]
    path.reverse()
    return path
    pass

#from this link https://www.geeksforgeeks.org/haversine-formula-to-find-distance-between-two-points-on-a-sphere/
def haversine(lat1, lon1, lat2, lon2):
       dLat = (lat2 - lat1) * math.pi / 180.0
       dLon = (lon2 - lon1) * math.pi / 180.0

       # convert to radians
       lat1 = (lat1) * math.pi / 180.0
       lat2 = (lat2) * math.pi / 180.0

       # apply formulae
       a = (pow(math.sin(dLat / 2), 2) +
            pow(math.sin(dLon / 2), 2) *
                math.cos(lat1) * math.cos(lat2));
       rad = 6371
       c = 2 * math.asin(math.sqrt(a))
       return rad * c
