"""
recursive
remarks: Start from root of tree and touch all the children downwards, checking the mirror condition.
time: O(N), N = # of nodes
space: O(h), h = height of the tree

iterative with stack
remarks: Same idea as recursive sol.
time: O(N), N = # of nodes
space: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return check(root1.left, root2.right) and check(root1.right, root2.left)
        
        if root is None:
            return True
        
        return check(root.left, root.right)
    
    
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: 
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop(0)
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
            
        return True
