from operator import add

from day_13.Point import Point


class Intersection:

    def __init__(self, point):
        self.point = point
        self.connections = []
        self.connections_offset = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    def wire(self, points_to_type):
        for offset in self.connections_offset:
            connection_coordinate = list(map(add, self.point, offset))
            self.connections.append(points_to_type[Point(connection_coordinate)])

    def __eq__(self, other):
        return self.point == other.point

    def __hash__(self) -> int:
        return hash(self.point)
