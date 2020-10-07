"""
binary search
time: O(log N)
space: O(1)
remarks: Find the index of the smallest number with a modified binary search. With the smallest number, I know to use binary search on either the left of right of it.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        start = left
        left = 0
        right = len(nums) - 1
        
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
        
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1


'''
linear search
time: O(N)
space: O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1
