class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def helper(current, opened=0, closed=0):
            if len(current) == 2 * n:
                result.append(''.join(current))
            else:
                if opened < n:
                    current.append('(')
                    helper(current, opened + 1, closed)
                    current.pop()
                
                if closed < opened:
                    current.append(')')
                    helper(current, opened, closed + 1)
                    current.pop()
                    
        helper([])
        return result