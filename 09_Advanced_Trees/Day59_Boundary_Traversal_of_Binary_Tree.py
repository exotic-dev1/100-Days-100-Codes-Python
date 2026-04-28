"""
Day59 :- Boundary Traversal of Binary Tree
Difficulty :- Medium
Concepts :- trees, DFS
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def is_leaf(node):
    return node.left is None and node.right is None

def add_left_boundary(root, res):
    curr = root.left
    while curr:
        if not is_leaf(curr):
            res.append(curr.data)
        
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
            
def add_leaves(root, res):
    if is_leaf(root):
        res.append(root.data)
        return
    
    if root.left:
        add_leaves(root.left, res)
    if root.right:
        add_leaves(root.right, res)

def add_right_boundary(root, res):
    curr = root.right
    temp = []
    
    while curr:
        if not is_leaf(curr):
            temp.append(curr.data)
        
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    
    while temp:
        res.append(temp.pop())


def boundary_traversal(root):
    if not root:
        return []
    
    res = []
    
    if not is_leaf(root):
        res.append(root.data)
    
    add_left_boundary(root, res)
    add_leaves(root, res)
    add_right_boundary(root, res)
    
    return res
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(7)
root.left.right.right = Node(8)
root.right.right = Node(6)
root.right.right.left = Node(9)

print(boundary_traversal(root))