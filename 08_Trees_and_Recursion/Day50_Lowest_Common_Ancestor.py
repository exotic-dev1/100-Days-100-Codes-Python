"""
Day50 :- Lowest Common Ancestor (Binary Tree)
Difficulty :- Medium
Concepts :- recursion, trees

Approach:-
1.Define the function
2.Use logic:-
left = search left subtree  
right = search right subtree  

if both exist → current node is LCA  
else → return whichever is not None
3. Create a sample tree
4. Display the result
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    
    if root is None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
        
    return left if left else right
    
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)


p = root.left  
q = root.right 

lca = lowestCommonAncestor(root, p, q)

print(lca.val)