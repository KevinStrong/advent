from day_13.Point import Point
from day_13.intersection import Intersection
from day_13.straight import Straight

points_to_types = {}

# Hello Linda!

def create_track(param, point):
    if param in ['+']:
        return Intersection(point)
    if param in ['-', '|', '\\', '/']:
        return Straight(param, point)


with open('day_13/input.txt') as f:
    for y, line in enumerate([l.rstrip() for l in f]):
        for x, symbol in enumerate(line):
            if symbol != ' ':
                point = Point([x, y])
                points_to_types[point] = create_track(symbol, point)
for track in points_to_types.values():
    track.wire(points_to_types)
