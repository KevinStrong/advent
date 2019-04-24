from day_13.Point import Point
from operator import add


def build_connections(symbol):
    connections = 0
    if symbol == '|':
        connections = [[0, 1], [0, -1]]
    if symbol == '\\':
        connections = [[1, 1], [-1, -1]]
    if symbol == '/':
        connections = [[1, -1], [-1, 1]]
    if symbol == '-':
        connections = [[1, 0], [1, 0]]
    return connections


class Straight:

    def __init__(self, type, point):
        self.point = point
        self.connections = []
        self.connections_offset = build_connections(type)

    def wire(self, points_to_type):
        for offset in self.connections_offset:
            connection_coordinate = list(map(add, self.point, offset))
            self.connections.append(points_to_type[Point(connection_coordinate)])

    def __eq__(self, other):
        return self.point == other.point

    def __hash__(self) -> int:
        return hash(self.point)
