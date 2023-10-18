class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_end = len(strs[0])

        for i, s in enumerate(strs):
            j = 0
            while j < min(prefix_end, len(s)) and strs[0][j] == s[j]:
                j += 1
            prefix_end = min(prefix_end, j)
        
        return strs[0][:prefix_end]

