"""
Day56 :- Maximum Path Sum in Binary Tree
Difficulty :- Hard
Concepts :- recursion, trees, optimization
"""
def maxPathSum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        current_path = node.val + left + right
        max_sum = max(max_sum, current_path)

        return node.val + max(left, right)

    dfs(root)
    return max_sum
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1, TreeNode(2), TreeNode(3))

print(maxPathSum(root))