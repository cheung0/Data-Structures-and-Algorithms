class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# two pointers
# time: O(N)
# space: O(1)
class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# Set
# time: O(N)
# space: O(N)
class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        seen = set()

        while temp:
            if temp in seen:
                return True
            seen.add(temp)
            temp = temp.next

        return False

a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
a.next = b
b.next = c
c.next = a

test = Solution2()
print(test.hasCycle(a))
