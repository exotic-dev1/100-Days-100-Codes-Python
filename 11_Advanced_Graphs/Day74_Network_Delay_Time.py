"""
Day74 :- Network Delay Time
Difficulty :- Medium
Concepts :- graphs, Dijkstra, heap
"""
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
            
        min_heap = [(0, k)]
        
        dist = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if node in dist:
                continue
            
            dist[node] = time
            
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(
                        min_heap,
                        (time + weight, neighbor)
                    )
                    
        if len(dist) == n:
            return max(dist.values())

        return -1
        
times = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]

n = 4
k = 2

sol = Solution()

answer = sol.networkDelayTime(times, n, k)

print("Minimum time needed:", answer)