


"""
time: O(N)
space: O(N)
remarks: Get the left and right part of the nums. Reset the input array.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = []
        right = []
        
        for i in range(len(nums) - k, len(nums)):
            left.append(nums[i])
        for j in range(len(nums) - k):
            right.append(nums[j])
            
        left_right = left + right
        index = 0
        
        for k in range(len(nums)):
            nums[k] = left_right[index]
            index += 1
d
            
        
