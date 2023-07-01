class DisjointSet:
    def __init__(self, V: int):
        self.parent = [x for x in range(V)]
        self.rank = [0 for x in range(V)]

    def union(self, x: int, y: int) -> bool:
        x_parent = self.find_parent(x)
        y_parent = self.find_parent(y)
        # print(x, x_parent, y, y_parent)
        if x_parent == y_parent:
            return False
        if self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.parent[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] == self.rank[y_parent]:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1
        return True

    def find_parent(self, x: int):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]