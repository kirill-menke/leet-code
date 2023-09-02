class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_b = {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket in open_b.values():
                stack.append(bracket)
            elif stack and stack[-1] == open_b[bracket]:
                stack.pop()
            else:
                return False

        return not stack