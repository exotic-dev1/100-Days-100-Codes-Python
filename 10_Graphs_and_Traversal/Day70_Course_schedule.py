"""
Day70 :- Course Schedule
Difficulty :- Medium
Concepts :- graphs, BFS, topological sort
"""
from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    
    graph = defaultdict(list)
    
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
        
    queue = deque()

    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)
            
    completed = 0

    while queue:
        node = queue.popleft()
        completed += 1

        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed == numCourses

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print(canFinish(numCourses, prerequisites))