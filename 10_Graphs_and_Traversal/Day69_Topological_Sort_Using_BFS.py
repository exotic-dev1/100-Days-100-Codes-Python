"""
Day69 :- Topological Sort using BFS (Kahn's Algorithm)
Difficulty :- Medium
Concepts :- graphs, BFS, indegree
"""
from collections import deque

def topological_sort(vertices, edges):

    graph = {i: [] for i in range(vertices)}
    indegree = [0] * vertices

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()

    for i in range(vertices):
        if indegree[i] == 0:
            queue.append(i)

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != vertices:
        return "Graph contains a cycle!"

    return topo_order

vertices = 6
edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

result = topological_sort(vertices, edges)
print("Topological Sort:", result)