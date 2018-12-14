# Find the fuel cell's rack ID, which is its X coordinate plus 10.
# Begin with a power level of the rack ID times the Y coordinate.
# Increase the power level by the value of the grid serial number (your puzzle input).
# Set the power level to itself multiplied by the rack ID.
# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
# Subtract 5 from the power level.

grid_serial_number = 3999
grid_size = 300  # Top left is 1,1, top right is grid_size,1

max_power = -10e10
point_power_lookup = {}
grid_power_lookup = {}
max_location = [-1, -1, -1]
max_power = 0


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Grid:

    def __init__(self, point, size):
        self.point = point
        self.size = size

    def __eq__(self, other):
        return (self.point.x, self.point.y, self.size) == (other.point.x, other.point.y, other.size)

    def __hash__(self) -> int:
        return hash((self.point.x, self.point.y, self.size))


def find_power(x, y):
    this_point = Point(x, y)
    if this_point in point_power_lookup:
        return point_power_lookup[this_point]
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = int((power_level / 100) % 10)
    power_level -= 5
    point_power_lookup[this_point] = power_level
    return power_level


# def find_grid_power(x, y, grid_size):
#     total_power = 0
#     for local_x in range(x, x + grid_size):
#         for local_y in range(y, y + grid_size):
#             total_power += find_power(local_x, local_y)
#     return total_power

def find_power_L(x, y, length):
    total_power = find_power(x, y)
    for i in range(1, length):
        total_power += find_power(x, y + i)
        total_power += find_power(x + i, y)
    return total_power


def find_grid_power(x, y, grid_size):
    if grid_size == 1:
        return find_power(x, y)
    this_grid = Grid(Point(x, y), grid_size)
    if this_grid in grid_power_lookup:
        return grid_power_lookup[this_grid]

    total_power = find_power_L(x, y, grid_size)
    total_power += find_grid_power(x + 1, y + 1, grid_size - 1)
    grid_power_lookup[this_grid] = total_power
    return total_power


for local_size in range(1, grid_size + 1):
    for x in range(1, grid_size - local_size + 2):
        for y in range(1, grid_size - local_size + 2):
            power = find_grid_power(x, y, local_size)
            if power > max_power:
                max_power = power
                max_location = [x, y, local_size]
    print("grid size: " + str(local_size))
    print("best location:" + ','.join(map(str, max_location)))
    print("best power:" + str(max_power))

print(','.join(map(str, max_location)))

with open('file_to_write', 'w') as f:
    f.write('max_power: ' + str(max_power))
    f.write('top left corner: ' + ','.join(map(str, max_location)))
