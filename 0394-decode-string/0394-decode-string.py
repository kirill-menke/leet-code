class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                repeat = []
                while stack[-1] != '[':
                    repeat.append(stack.pop())
                
                stack.pop()

                num = 0
                exp = 0
                while stack and stack[-1].isdigit():
                    num += 10**exp * int(stack.pop())
                    exp += 1 
                
                for _ in range(num):
                    stack.extend(repeat[::-1])

        return ''.join(stack)
