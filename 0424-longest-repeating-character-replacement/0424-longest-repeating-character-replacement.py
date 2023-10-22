
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        char_count = [0] * 26

        while right < len(s):
            char_count[ord(s[right]) - ord('A')] += 1
            window_size = right - left + 1
            most_frequent_char = max(char_count) 

            if window_size - most_frequent_char - k > 0:
                char_count[ord(s[left]) - ord('A')] -= 1
                left += 1
        
            right += 1

        return right - left

