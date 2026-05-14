"""
Day75 :- Cheapest Flights Within K Stops
Difficulty :- Medium
Concepts :- graphs, heap, modified Dijkstra
"""
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        heap = [(0, src, 0)]
        
        dist = {}

        while heap:

            cost, city, stops = heapq.heappop(heap)
            
            if city == dst:
                return cost

            if stops > k:
                continue

            for nei, price in graph[city]:

                new_cost = cost + price

                if (nei, stops + 1) not in dist or new_cost < dist[(nei, stops + 1)]:

                    dist[(nei, stops + 1)] = new_cost

                    heapq.heappush(
                        heap,
                        (new_cost, nei, stops + 1)
                    )

        return -1
        
n = 4

flights = [
    [0,1,5],
    [1,2,5],
    [0,3,2],
    [3,1,2],
    [1,4,1],
    [4,2,1]
]

src = 0
dst = 2
k = 2

sol = Solution()

answer = sol.findCheapestPrice(
    n,
    flights,
    src,
    dst,
    k
)

print("Cheapest Price:", answer)