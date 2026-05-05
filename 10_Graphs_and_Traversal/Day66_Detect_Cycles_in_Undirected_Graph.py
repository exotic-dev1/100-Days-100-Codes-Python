"""
Day66 :- Detect Cycle in Undirected Graph
Difficulty :- Medium
Concepts :- DFS, graphs
"""
def has_cycle(n, edges):
    
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True

        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False

n = 3
edges = [(0, 1), (1, 2), (2, 0)]
print(has_cycle(n, edges))

n = 3
edges = [(0, 1), (1, 2)]
print(has_cycle(n, edges))