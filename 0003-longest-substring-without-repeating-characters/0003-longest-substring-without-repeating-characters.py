class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        max_count = 0

        visited = set()
        curr_count = 0

        while fast < len(s):
            if s[fast] in visited:
                max_count = max(max_count, curr_count)
                while s[slow] != s[fast]:
                    visited.remove(s[slow])
                    slow += 1
                    curr_count -= 1
                slow += 1
            else:
                visited.add(s[fast])
                curr_count += 1

            fast += 1

        return max(max_count, curr_count)