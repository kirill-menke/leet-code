class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def check(start):
            if start >= len(s):
                return True
            
            for i in range(start + 1, len(s) + 1):
                if s[start: i] in wordDict and check(i):
                    return True
            
            return False

        return check(0)