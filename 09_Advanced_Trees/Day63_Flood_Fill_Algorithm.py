"""
Day63 :- Flood Fill Algorithm
Difficulty :- Easy
Concepts :- DFS/BFS, graphs, grid traversal
"""
def flood_fill_dfs(image, sr, sc, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == new_color:
        return image

    def dfs(r, c):

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original_color:
            return
        
        image[r][c] = new_color
        
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(sr, sc)
    return image
    
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

print(flood_fill_dfs(image, 1, 1, 2))