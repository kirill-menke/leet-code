from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        
        for i, s in enumerate(strs):
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            group_dict[tuple(key)].append(s)
        
        return [val for val in group_dict.values()]

        