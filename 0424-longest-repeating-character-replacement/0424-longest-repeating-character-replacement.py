class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_size = 0

        char_count = [0] * 26
        while right < len(s):
            char_count[ord(s[right]) - ord('A')] += 1

            while left < len(s) and (right - left + 1) - max(char_count) > k:
                char_count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            max_size = max(max_size, (right - left + 1))
            right += 1
        
        return max_size