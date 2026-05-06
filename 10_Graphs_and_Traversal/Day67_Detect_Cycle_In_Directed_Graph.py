"""
Day67 :- Detect Cycle in Directed Graph
Difficulty :- Medium
Concepts :- DFS, graphs, recursion stack
"""
def hasCycle(V, edges):
    from collections import defaultdict
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
    
    visited = [False] * V
    recStack = [False] * V
    
    def dfs(node):
        visited[node] = True
        recStack[node] = True
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recStack[neighbor]:
                return True
        
        recStack[node] = False
        return False
    
    for i in range(V):
        if not visited[i]:
            if dfs(i):
                return True
    
    return False

V1 = 4
edges1 = [(0, 1), (1, 2), (2, 3), (3, 1)] 

print("Graph 1 has cycle:", hasCycle(V1, edges1))

V2 = 4
edges2 = [(0, 1), (1, 2), (2, 3)]

print("Graph 2 has cycle:", hasCycle(V2, edges2))