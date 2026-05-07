"""
Day68 :- Topological Sort (DFS)
Difficulty :- Medium
Concepts :- graphs, DFS, stack
"""
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited, stack):
        visited[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)

        stack.append(node)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for node in range(self.V):
            if not visited[node]:
                self.dfs(node, visited, stack)

        return stack[::-1]


g = Graph(6)

g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

result = g.topological_sort()

print("Topological Sort:")
print(result)