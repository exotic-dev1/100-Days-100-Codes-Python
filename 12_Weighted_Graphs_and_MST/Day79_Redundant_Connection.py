"""
Day79 :- Redundant Connection
Difficulty :- Medium
Concepts :- graphs, union find, cycle detection
"""
class Solution:
    def findRedundantConnection(self, edges):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX == rootY:
                return False

            parent[rootY] = rootX
            return True
            
        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
                
            if not union(u, v):
                return [u, v]
                
edges = [
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 4],
    [1, 5]
]

sol = Solution()

result = sol.findRedundantConnection(edges)

print("Redundant Edge:", result)