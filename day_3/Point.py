class Point:
    x = 0
    y = 0

    def __init__(self, horizontal, vertical):
        self.x = horizontal
        self.y = vertical

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
