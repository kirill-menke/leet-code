class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for b in s:
            if b in opening_brackets:
                if not stack or opening_brackets[b] != stack.pop():
                    return False
            else:
                stack.append(b)

        return not stack
        
