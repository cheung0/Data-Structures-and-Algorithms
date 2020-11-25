"""
trivial
time: O(n)
space: O(n)
reason: Add all the even integers, then the odd integers.
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []

        for char in A:
            if char % 2 == 0:
                ans.append(char)
        for char in A:
            if char % 2 == 1:
                ans.append(char)

        return ans
