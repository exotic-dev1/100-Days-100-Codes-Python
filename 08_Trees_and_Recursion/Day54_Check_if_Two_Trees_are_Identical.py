"""
Day54 :- Check if Two Trees are Identical
Difficulty :- Easy
Concepts :- recursion, trees
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    
    return (root1.val == root2.val and
            are_identical(root1.left, root2.left) and
            are_identical(root1.right, root2.right))

a = Node(1)
a.left = Node(2)
a.right = Node(3)

b = Node(1)
b.left = Node(2)
b.right = Node(3)

print(are_identical(a, b))