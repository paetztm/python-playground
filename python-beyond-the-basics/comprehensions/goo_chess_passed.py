import math

GRID_SIZE = 8


class Point(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column

    @staticmethod
    def is_valid_point(row, column):
        return 0 <= row < GRID_SIZE and 0 <= column < GRID_SIZE

    def append_valid_point(self, neighbors, row, column):
        if self.is_valid_point(row, column):
            neighbors.append(Point(row, column))

    def get_neighbor_points(self):
        neighbors = []
        row = self.row
        column = self.column
        self.append_valid_point(neighbors, row + 1, column + 2)
        self.append_valid_point(neighbors, row + 1, column - 2)
        self.append_valid_point(neighbors, row - 1, column + 2)
        self.append_valid_point(neighbors, row - 1, column - 2)
        self.append_valid_point(neighbors, row + 2, column + 1)
        self.append_valid_point(neighbors, row + 2, column - 1)
        self.append_valid_point(neighbors, row - 2, column + 1)
        self.append_valid_point(neighbors, row - 2, column - 1)
        return neighbors


def get_row(point):
    return int(point / GRID_SIZE)


def get_column(point):
    return point % GRID_SIZE


def is_corner(point):
    return (point.column == 0 and point.row == 0) or (point.column == 0 and point.row == GRID_SIZE - 1) or (point.column == GRID_SIZE - 1 and point.row == 0) or (point.column == GRID_SIZE - 1 and point.row == GRID_SIZE - 1)


def memoize(func):
    cache = {}

    def wrapper(src, dest):
        source = Point(get_row(src), get_column(src))
        destination = Point(get_row(dest), get_column(dest))
        distance = math.sqrt((destination.column - source.column)**2 + (destination.row - source.row)**2)
        # corners with diagonal of 1 aren't equal to every where else
        if distance == 1.4142135623730951 and (is_corner(source) or is_corner(destination)):
            count = func(source, destination)
        elif distance not in cache:
            count = func(source, destination)
            cache[distance] = count
        else:
            count = cache[distance]
        return count

    return wrapper

@memoize
def answer(source, destination):
    # your code here
    check_points = [[False for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

    count = 0
    neighbors = source.get_neighbor_points()
    check_points[source.row][source.column] = True
    while not check_points[destination.row][destination.column]:
        count += 1
        temp_neighbors = []
        for point in neighbors:
            if not check_points[point.row][point.column]:
                check_points[point.row][point.column] = True
                temp_neighbors.extend(point.get_neighbor_points())
            if check_points[destination.row][destination.column]:
                break
        neighbors = temp_neighbors
    return count
