"""
Day47 :- Level Order Traversal (BFS)
Difficulty :- Medium
Concepts :- queue, BFS, trees

Approach:-
1. Import deque from collections
2. create queue
3. Push root into queue
4. While queue not empty
5. Pop first element
6. Print it Add left & right children
7. Create a sample tree for execution
8. Display the result
"""
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return

    queue = deque()
    queue.append(root) 

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order:", end=" ")
level_order_traversal(root)