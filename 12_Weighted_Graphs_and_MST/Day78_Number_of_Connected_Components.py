"""
Day78 :- Number of Connected Components
Difficulty :- Medium
Concepts :- graphs, union find
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.components -= 1


def count_components(n, edges):
    uf = UnionFind(n)

    for u, v in edges:
        uf.union(u, v)

    return uf.components

n = 5
edges = [[0,1], [1,2], [3,4]]

print(count_components(n, edges))