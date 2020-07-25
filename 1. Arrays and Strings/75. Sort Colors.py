"""
one pass three pointers
remarks: Iterate through array, checking each element. If it is red, I swap it with a pointer at the front, incrementing the red and white pointers. If it is white, I just increment white pointer. Else it must be blue, so I swap at the end, decrementing the blue pointer. Notice white pointer could get another blue object.
time: O(N)
space: O(1)

counting sort
remarks: Get number of red, white, blue objects by iterating through array. Iterate through array again, overwriting with numbers of these objects.
time: O(2N) = O(N)
space: O(1) or O(N)? 
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
            
            # nums[white] == 2
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                
                
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        
        for n in nums:
            if n == 0:
                zeros += 1
            elif n == 1:
                ones += 1
            else:
                twos += 1
        
        for i in range(len(nums)):
            if zeros > 0:
                nums[i] = 0
                zeros -= 1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
                twos -= 1
