"""
Day48 :- Height of Binary Tree
Difficulty :- Easy
Concepts :- recursion, trees
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    
    if root is None:
      return 0

    left_height = height(root.left)

    right_height = height(root.right)

    return max(left_height, right_height) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(height(root))