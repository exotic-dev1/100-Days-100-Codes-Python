"""
Day53 :- Max Depth & Min Depth of Binary Tree
Difficulty :- Easy
Concepts :- recursion, trees
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepth(root):
    if not root:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    depth = 1 + max(left_depth, right_depth)
    print(f"Node {root.val} -> Max Depth: {depth}")
    
    return depth
    
def minDepth(root):
    if not root:
        return 0
    
    if not root.left:
        depth = 1 + minDepth(root.right)
        print(f"Node {root.val} -> Min Depth: {depth}")
        return depth
    
    if not root.right:
        depth = 1 + minDepth(root.left)
        print(f"Node {root.val} -> Min Depth: {depth}")
        return depth
    
    depth = 1 + min(minDepth(root.left), minDepth(root.right))
    print(f"Node {root.val} -> Min Depth: {depth}")
    
    return depth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print("Maximum Depth:", maxDepth(root))
print("Minimum Depth:", minDepth(root))