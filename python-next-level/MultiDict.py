
class MultiDict:
    def __init__(self):
        self.data = {}

    def insert(self, key, value):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(value)

    def get(self, key):
        return self.data[key]

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.insert(key, value)


m = MultiDict()
m.insert("x", 3)
print(m["x"])

m["y"] = 5

print(m["y"])
