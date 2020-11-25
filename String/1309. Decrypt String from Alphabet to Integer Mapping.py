"""
hash table, string
time: O(n)
space: O(1)
reason: Build the hashtable that maps numbers to alphabets. Iterate through the input, converting each input digit to an ouput digit and adding each output digit to the answer. Lesson learned: be careful of conversions between string and int.
"""
class Solution:
    def freqAlphabets(self, s: str) -> str:
        # ord('a') = 97
        ans = ''
        mapping = {}
        for i in range(0, 26):
            output_digit = chr(97 + i)
            mapping[str(i + 1)] = output_digit
            
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#': 
                input_digit = s[i: i + 2]  
                ans += mapping[input_digit] 
                i += 3
            else:
                input_digit = s[i]
                ans += mapping[input_digit]
                i += 1
        
        return ans
