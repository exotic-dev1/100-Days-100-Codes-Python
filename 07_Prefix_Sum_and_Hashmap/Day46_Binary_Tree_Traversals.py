"""
Day46 :- Binary Tree Traversals
Difficulty :- Medium
Concepts :- recursion, trees, DFS

Approach:
1. create class code
2. initialize self, root
3. define inorder
4. define pre-order
5. define post-order
6. create sample tree
7. print the traversals
"""
class node:
    def __init__(self,root):
        self.root = root
        self.left = None
        self.right = None
        
def inorder(node):
    if node:
        inorder(node.left)
        print(node.root, end=" ");
        inorder(node.right)

def preorder(node):
    if node:
        print(node.root, end = " ");
        preorder(node.left)
        preorder(node.right)
        
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.root, end = " ");
        
root = node(1)
root.left = node(2)
root.right = node(3)

root.left.left = node(4)
root.left.right = node(5)

print("Inorder:",inorder(root))
print("Pre-Order:",preorder(root))
print("Post-Order:",postorder(root))
