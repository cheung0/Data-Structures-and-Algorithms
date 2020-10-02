'''
linked list
time: O(N)
space: O(1)
remarks: Traverse linked list. If the current node's value is the same as the next node's value, skip the next node.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = head
        
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        
        return head
