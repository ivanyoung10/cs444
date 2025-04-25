from bfs import bfs
from ucs import ucs
from dls import dls
from a_star import a_star


class Agent:
    def __init__(self, start, goal, map, coordinates=None):
        self.start = start
        self.goal = goal
        self.map = map
        self.coordinates = coordinates

    def run(self, algorithm):
        if algorithm == 'bfs':
            return bfs(self.start, self.goal, self.map)
        elif algorithm == 'ucs':
            return ucs(self.start, self.goal, self.map)
        elif algorithm == 'dls':
            return dls(self.start, self.goal, self.map)
        elif algorithm == 'astar':
            return a_star(self.start, self.goal, self.map, self.coordinates)
        else:
            raise ValueError('Invalid algorithm')
