class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(s_iter):
            result = []
            num = []

            for char in s_iter:
                if char.isalpha():
                    result.append(char)
                elif char.isdigit():
                    num.append(char)
                elif char == '[':
                    ret = helper(s_iter)
                    c_num = int(''.join(num))
                    
                    for _ in range(c_num):
                        result.extend(ret)
                    num = []
                elif char == ']':
                    return result
            
            return ''.join(result)
            
        return helper(iter(s))
            
