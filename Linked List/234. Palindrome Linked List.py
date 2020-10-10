"""
two pointer
time: O(N)
space: O(N)
remarks: Iterate through the linked list and put all the values in an array. Use a two pointer approach to check for palindromeness. 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        tmp = head
        
        while tmp:
            vals.append(tmp.val)
            tmp = tmp.next
        
        left = 0
        right = len(vals) - 1
        
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        
        return True
