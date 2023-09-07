from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        count_s = Counter(s[:len(p)])

        output = []
        left, right = 0, len(p) - 1

        while right < len(s):
            if count_p == count_s:
                output.append(left)
            
            if count_s[s[left]] > 1:
                count_s[s[left]] -= 1
            else:
                del count_s[s[left]]
            
            left += 1

            right += 1
            if right < len(s):
                count_s[s[right]] += 1
            
        return output
            

                