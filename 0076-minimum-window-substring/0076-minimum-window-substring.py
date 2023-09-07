from collections import Counter

class Solution:
    def is_subset(self, s1, s2):
        for k, v in s1.items():
            if k not in s2 or v > s2[k]:
                return False
        
        return True


    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        left, right = 0, 0
        count_t = Counter(t)
        min_window = float("inf")
        ans = [-1, -1]
        count_window = Counter()

        while right < len(s):
            count_window[s[right]] += 1
            
            while left <= right and self.is_subset(count_t, count_window):
                if right - left + 1 < min_window:
                    min_window = right - left + 1
                    ans = [left, right]

                count_window[s[left]] -= 1
                left += 1

            right += 1
        
        i, j = ans
        return s[i : j + 1]
            
            
            

            
        



                
                