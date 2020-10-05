"""
Recursion check all nodes once
time: O(N), N = # of nodes in the tree
space: O(h), h = height of the tree
remarks: using recursion, i get the height of every single node and check if it's left and right subtree are balanced or not. if one is unbalanced, i return the fact that it is unbalanced to it's previous caller.

Recursion check height of every single node
time: O(N^2), could be 
space: O(h)
remarks: checking height of every single node is unneccesay 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            if root is None:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return check(root) != -1
    
    
class Solution:    
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if root is None:
                return 0
            else:
                return 1 + max(height(root.left), height(root.right))
        
        if root is not None:
            left = height(root.left) 
            right = height(root.right)
            if abs(left - right) > 1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return True 
