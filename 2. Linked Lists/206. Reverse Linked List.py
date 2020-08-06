"""
iterative
remarks: Must set a pointer ahead before reversing.
time: O(N)
space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = next = head
        prev = None
        
        while next:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
