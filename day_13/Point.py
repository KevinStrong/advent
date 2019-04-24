class Point:

    def __init__(self, coordinate):
        self.x = coordinate[0]
        self.y = coordinate[1]

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))
