
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for s in strs:
            letter_count = [0] * 26
            for char in s:
                letter_count[ord(char) - ord('a')] += 1
            
            letter_count = tuple(letter_count)
            if letter_count in anagram_dict:
                anagram_dict[letter_count].append(s)
            else:
                anagram_dict[letter_count] = [s]
        
        return anagram_dict.values()
