"""
Day60 :- Vertical Order Traversal
Difficulty :- Medium
Concepts :- BFS, hashmap, trees
"""
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def verticalTraversal(root):
    col_table = defaultdict(list)
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()
        if node:
            col_table[col].append((row, node.val))
            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))

    result = []
    for col in sorted(col_table.keys()):
        col_table[col].sort()
        result.append([val for row, val in col_table[col]])

    return result
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(verticalTraversal(root))