"""
hash table
time: O(n + m), n = length of nums1, m = length of nums2
space: O(n + m)
remarks: 
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = {}
        ans = []
        
        for n in nums1:
            if n in freq1:
                freq1[n] += 1
            else:
                freq1[n] = 1
        
        for n in nums2:
            if n in freq1 and freq1[n] > 0:
                freq1[n] -= 1
                ans.append(n)
        
        return ans


"""
two pointer
time: O(max(n, m)), n = length of nums1, m = length = nums2
space: O(max(n, m))
remarks: Assume that the input arrays are already sorted. 
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        i = 0
        j = 0
        ans = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
                
        return ans
