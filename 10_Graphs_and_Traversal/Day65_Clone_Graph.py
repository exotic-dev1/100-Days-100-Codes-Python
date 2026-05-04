"""
Day65 :- Clone Graph
Difficulty :- Medium
Concepts :- graph, DFS, hashmap
"""
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None

    visited = {}

    def dfs(curr):

        if curr in visited:
            return visited[curr]

        clone = Node(curr.val)

        visited[curr] = clone

        for neighbor in curr.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)

node1 = Node(1)
node2 = Node(2)

node1.neighbors.append(node2)
node2.neighbors.append(node1)

result = cloneGraph(node1)

print(result.val)