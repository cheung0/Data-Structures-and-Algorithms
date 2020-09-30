'''
stack
time: O(N)
space: O(N)
remarks: For each char in the input string, check to see if it is equal to the top of the stack and remove the top of the stack if they are. Else, put it in the stack.
'''
class Solution:
    def removeDuplicates(self, S: str) -> str:  
        stack = []
        
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
