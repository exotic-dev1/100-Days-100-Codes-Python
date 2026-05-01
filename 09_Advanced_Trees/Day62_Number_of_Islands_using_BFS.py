"""
Day62 :- Number of Islands using BFS
Difficulty :- Medium
Concepts :- graphs, BFS, queue
"""
from collections import deque

def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        grid[r][c] = '0'

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    grid[nr][nc] == '1'):
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                bfs(r, c)

    return islands

grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','1'],
    ['0','0','1','0','1'],
    ['0','0','0','1','1']
]

result = numIslands(grid)
print("Number of Islands:", result)