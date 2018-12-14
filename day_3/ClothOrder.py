from day_3.Point import Point


class ClothOrder:
    from_left = 0
    from_top = 0
    height = 0
    width = 0
    all_points = set()

    # Example init_string
    # 12,548:19x10
    # 12 from left, 548 from right, 19 wide by 10 tall

    def __init__(self, init_string):
        comma = init_string.find(',')
        colon = init_string.find(':')
        ex = init_string.find('x')
        self.from_left = int(init_string[0:comma])
        self.from_top = int(init_string[comma + 1:colon])
        self.width = int(init_string[colon + 1:ex])
        self.height = int(init_string[ex + 1:])
        self.all_points = set()

    def get_all_points(self):
        if len(self.all_points) is 0:
            for x in range(self.from_left, self.from_left + self.width):
                for y in range(self.from_top, self.from_top + self.height):
                    self.all_points.add(Point(x, y))
        return self.all_points

    def overlaps_with(self, another_order):
        return self.column_overlaps(another_order) and self.row_overlaps(another_order)

    def contains_point(self, other_point):
        for point in self.get_all_points():
            if point.__eq__(other_point):
                return True
        return False

    def __eq__(self, other):
        return (self.from_left, self.from_top, self.width, self.height) == (other.from_left, other.from_top, other.width, other.height)

    def column_overlaps(self, another_order):
        my_start = self.from_left
        my_end = self.from_left + self.width
        another_start = another_order.from_left
        another_end = another_order.from_left + another_order.width
        return my_start <= another_start <= my_end or another_start <= my_start <= another_end

    def row_overlaps(self, another_order):
        my_start = self.from_top
        my_end = self.from_top + self.height
        another_start = another_order.from_top
        another_end = another_order.from_top + another_order.height
        return my_start <= another_start <= my_end or another_start <= my_start <= another_end

