"""
counting sort
time: O(N)
space: O(1)
remarks: Count number of 0s, 1s, and 2s. Fill them back in input array.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = ones = twos = 0
        res = []
        index = 0
        
        for n in nums:
            if n == 0:
                zeros += 1
            elif n == 1:
                ones += 1
            else:
                twos += 1
        
        for i in range(zeros):
            nums[index] = 0
            index += 1
        for j in range(ones):
            nums[index] = 1
            index += 1
        for k in range(twos):
            nums[index] = 2
            index += 1

"""
three pointers
time: O(N)
space: O(1)
remarks: Keep modifying while white pointer is less than or equal to blue pointer. 
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            
