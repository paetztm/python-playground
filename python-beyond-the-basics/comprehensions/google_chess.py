GRID_SIZE = 8

class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    @staticmethod
    def is_valid_point(row, column):
        return 0 <= row < 8 and 0 <= column < 8

    def append_valid_point(self, neighbors, row, column):
        if self.is_valid_point(row, column):
            neighbors.append(Point(row, column))

    def get_neighbor_points(self):
        neighbors = []
        src_row = self.row
        src_column = self.column
        self.append_valid_point(neighbors, src_row+1, src_column+2)
        self.append_valid_point(neighbors, src_row+1, src_column-2)
        self.append_valid_point(neighbors, src_row-1, src_column+2)
        self.append_valid_point(neighbors, src_row-1, src_column-2)
        self.append_valid_point(neighbors, src_row+2, src_column+1)
        self.append_valid_point(neighbors, src_row+2, src_column-1)
        self.append_valid_point(neighbors, src_row-2, src_column+1)
        self.append_valid_point(neighbors, src_row-2, src_column-1)
        return neighbors


def get_row(point):
    return int(point / 8)


def get_column(point):
    return point % 8


def answer(src, dest):
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



for x in range(64):
    for y in range(64):
        print(answer(x, y))
print(answer(19, 36)) # = 1
print(answer(0, 60)) # = 3