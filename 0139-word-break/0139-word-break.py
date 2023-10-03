class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table = [False] * (len(s) + 1)
        table[0] = True

        for i, char in enumerate(s, 1):
            for prev in range(i - 1, -1, -1):
                if s[prev: i] in wordDict and table[prev]:
                    table[i] = True
                    break

        return table[-1]