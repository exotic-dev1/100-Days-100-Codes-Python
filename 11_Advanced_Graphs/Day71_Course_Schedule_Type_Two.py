"""
Day71 :- Course Schedule II
Difficulty :- Medium
Concepts :- graphs, BFS, topological sort
"""
from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):

    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque()

    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == numCourses:
        return order
    else:
        return []

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print("Course Order:", findOrder(numCourses, prerequisites))