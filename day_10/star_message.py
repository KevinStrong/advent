import re

import matplotlib.pyplot

stars_input = open("day_10/input.txt").readlines()

stars = []


class Star:

    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def __hash__(self):
        return hash(
            (self.x, self.vel_x, self.y, self.vel_y))  # Hash based off location so I can fetch from display grid.

    def __eq__(self, other):
        return (self.x, self.y, self.vel_x, self.vel_y) == (other.x, other.y, other.vel_x, other.vel_y)

    def wait(self, duration):
        self.y += self.vel_y * duration
        self.x += self.vel_x * duration


for star_input in stars_input:
    matcher = re.match("position=< ?(-?\d*), {1,2}(-?\d*)> velocity=< ?(-?\d*), {1,2}(-?\d*)>", star_input)
    x = int(matcher.group(1))
    y = int(matcher.group(2))
    vel_x = int(matcher.group(3))
    vel_y = int(matcher.group(4))
    stars.append(Star(x, y, vel_x, vel_y))


def print_stars():
    x = []
    y = []
    for star in stars:
        x.append(star.x)
        y.append(star.y)
    matplotlib.pyplot.scatter(x, y)
    matplotlib.pyplot.show()


def wait_for_stars(param):
    for star in stars:
        star.wait(param)

#10100
#10236
#10180
#10227 - ding ding ding

wait_for_stars(10227)
print_stars()
# for _ in range(1, 5):
#     wait_for_stars(1)
#     print_stars()
