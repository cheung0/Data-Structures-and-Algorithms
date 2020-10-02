'''
stack and string
time: O(N)
space: O(N)
remarks: For each character in the string if it is a opening bracket, put it in the stack. Else the charcter is a closing bracket. If the stack is empty, that means no opening bracket closed the closing bracket, and I return False. Or if the top of the stack does not match, I return False.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif stack == [] or mapping[char] != stack.pop():
                    return False
                
        return stack == []
