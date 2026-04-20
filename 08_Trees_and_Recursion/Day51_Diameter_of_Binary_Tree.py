"""
Day51 :- Diameter of Binary Tree
Difficulty :- Medium
Concepts :- recursion, trees
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0
        
        left = height(node.left)
        right = height(node.right)
        
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    height(root)
    return diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)

print("Diameter of the tree:", diameterOfBinaryTree(root))