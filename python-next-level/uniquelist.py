
class UniqueList:
    def __init__(self, items):
        self.items = []
        for item in items:
            self.append(item)

    def append(self, item):
        if item not in self.items:
            self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

u = UniqueList([3, 7, 2, 9, 3, 4, 2])
print u[2: 4]
