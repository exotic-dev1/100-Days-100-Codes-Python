"""
Day61 :- Number of Islands
Difficulty :- Medium
Concepts :- graphs, DFS/BFS
"""
def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):

        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        print(f"Visiting cell ({r}, {c})")

        grid[r][c] = '0'

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                print(f"\nNew island found at ({r}, {c})")
                count += 1
                dfs(r, c)

    return count

grid = [
    ['1','1','0','0'],
    ['1','0','0','1'],
    ['0','0','1','1'],
    ['0','0','0','0']
]

print("Number of islands:", numIslands(grid))