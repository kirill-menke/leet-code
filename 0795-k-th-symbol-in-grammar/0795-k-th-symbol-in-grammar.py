class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def dfs(curr, n, k):
            if n == 1:
                return curr
            
            nodes_count = 2**(n - 1)
            if k > nodes_count / 2:
                return dfs(not curr, n - 1, k - nodes_count / 2)
            else:
                return dfs(curr, n - 1, k)
            
        return int(dfs(False, n, k))