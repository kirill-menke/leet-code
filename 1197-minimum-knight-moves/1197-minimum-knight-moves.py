class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        @cache
        def dfs(x, y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            
            return min(
                dfs(abs(x - 2), abs(y - 1)), 
                dfs(abs(x - 1), abs(y - 2))
            ) + 1
                       
        return dfs(abs(x), abs(y))