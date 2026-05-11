"""
Day72 :- Shortest Path in Unweighted Graph
Difficulty :- Medium
Concepts :- BFS, graphs, shortest path
"""
from collections import deque

def shortest_path(graph, start, end):

    queue = deque([(start, [start])])

    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None 

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
end = 'F'

path = shortest_path(graph, start, end)

print("Shortest Path:", path)