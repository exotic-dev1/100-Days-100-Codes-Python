"""
Day76 :- Minimum Spanning Tree (Prim's Algorithm)
Difficulty :- Medium
Concepts :- graphs, MST, heap, greedy
"""
import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]

    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        total_cost += weight

        if weight != 0:
            mst_edges.append((prev_node, node, weight))

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
                prev_node = node

    return total_cost, mst_edges

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

cost, mst = prim(graph, 'A')

print("Minimum Cost:", cost)
print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")