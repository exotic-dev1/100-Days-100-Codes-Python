"""
Day55 :- Symmetric Tree
Difficulty :- Easy
Concepts :- recursion, trees
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isMirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val and
            isMirror(left.left, right.right) and
            isMirror(left.right, right.left))

def isSymmetric(root):
    return isMirror(root, root)


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

# Print result
if isSymmetric(root):
    print("Tree is symmetric")
else:
    print("Tree is not symmetric")