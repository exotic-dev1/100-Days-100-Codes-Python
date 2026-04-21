"""
Day52 :- Path Sum (Root to Leaf)
Difficulty :- Easy
Concepts :- recursion, trees
"""
def hasPathSum(node, targetSum):
    if not node:
        return False
    
    targetSum -= node.val
    
    if not node.left and not node.right:
        return targetSum == 0
    
    return hasPathSum(node.left, targetSum) or \
           hasPathSum(node.right, targetSum)
           
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(5)
root.left = Node(4)
root.right = Node(8)

targetSum = 9

print(hasPathSum(root, targetSum))  # True (5 → 4)