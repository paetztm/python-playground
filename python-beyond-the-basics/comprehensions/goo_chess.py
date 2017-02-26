
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

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    def __hash__(self):
        result = self.row
        result = 31 * result + self.column
        return result


def get_row(point):
    return int(point / GRID_SIZE)


def get_column(point):
    return point % GRID_SIZE

def memoize(func):
    cache = {}
    def wrapper(src, dest):
        key = src
        if key not in cache:
            cache[key] = func(src, dest)
        return cache[key]
    return wrapper


def answer_with_checkpoints(src, dest):
    # your code here
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


def answer(src, dest):
    # your code here
    if src == dest:
        return 0
    cache = set()
    # check_points = [[False for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
    source = Point(get_row(src), get_column(src))
    destination = Point(get_row(dest), get_column(dest))
    count = 0
    neighbors = source.get_neighbor_points()
    while destination not in cache:
        count += 1
        temp_neighbors = []
        for point in neighbors:
            if point not in cache:
                cache.add(point)
                temp_neighbors.extend(point.get_neighbor_points())
            if destination in cache:
                break
        neighbors = temp_neighbors

    return count



import time
total_time = 0
start_time = time.time()

left_answers = []
right_answers = []
# for x in range(GRID_SIZE**2):
#     for y in range(GRID_SIZE**2):
#         answer(x, y)
#         #right_answers.append(answer_with_checkpoints(x, y))
# print(time.time() - start_time)
#print(left_answers == right_answers)
print(answer(0, 0)) # = 2 should it be 0?
#print(answer_with_checkpoints(0, 1))
