"""
greedy
time: O(n), n = length of s
space: O(1)
remarks: Iterate through s. Increase balance for a 'L' and decrease balance of a 'R'. When the number of 'L' and 'R' is the same, that means we have a balanced string.
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced = 0
        ans = 0
        
        for char in s:
            if char == 'L':
                balanced += 1
            else:
                balanced -= 1
            if balanced == 0:
                ans += 1
        
        return ans
