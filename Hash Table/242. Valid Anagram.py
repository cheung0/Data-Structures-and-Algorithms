"""
hash table
time: O(n)
space: O(n)
remarks: Build two hash tables with each string's frequency count. Check if the two hash tables are equal.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table1 = {}
        hash_table2 = {}
        
        for char in s:
            if char in hash_table1:
                hash_table1[char] += 1
            else:
                hash_table1[char] = 1
        
        for char in t:
            if char in hash_table2:
                hash_table2[char] += 1
            else:
                hash_table2[char] = 1
        
        return hash_table1 == hash_table2


"""
ascii character set
time: O(n)
space: O(n)
remarks: Make a ascii character set of 128 characters for both strings. Go to each character's ascii number place and increment. Check if the two sets are equal.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ascii_chars1 = [0] * 128
        ascii_chars2 = [0] * 128

        for char in s:
            ascii_chars1[ord(char)] += 1
        for char in t:
            ascii_chars2[ord(char)] += 1

        return ascii_chars1 == ascii_chars2
        
       
"""
sort
time: O(n log n)
space: O(1)
remarks: Sort both strings and check if they are equal.
"""
class Solution: 
    def isAnagram(self, s: str, t: str) -> bool: 
        return sorted(s) == sorted(t)
