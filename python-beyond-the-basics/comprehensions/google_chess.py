import math

GRID_SIZE = 8
class Point:
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


def memoize(func):
    cache = {}

    def wrapper(src, dest):
        source = Point(get_row(src), get_column(src))
        destination = Point(get_row(dest), get_column(dest))
        distance = math.sqrt((destination.column - source.column)**2 + (destination.row - source.row)**2)

        if not distance in cache:
            cache[distance] = func(source, destination)
        return cache[distance]

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

def answer2(src, dest):
    # your code here
    if src == dest:
        return 0
    check_points = [[False for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
    source = Point(get_row(src), get_column(src))
    destination = Point(get_row(dest), get_column(dest))

    count = 0
    neighbors = source.get_neighbor_points()
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

import time
total_time = 0
start_time = time.time()
left_answers = []
right_answers = []
for x in range(GRID_SIZE**2):
    for y in range(GRID_SIZE**2):
        answer1 = answer(x, y)
        answer3 = answer2(x, y)
        if not answer1 == answer3:
            print("{} answer1 {} answer2 {} x {} y".format(answer1, answer3, x, y))
            a = "a" + a

        # left_answers.append(answer(x, y))
        # right_answers.append(answer2(x, y))
print(time.time() - start_time)
print(left_answers == right_answers)
#print(answer(19, 36)) # = 1
#print(answer(1, 9)) # = 3