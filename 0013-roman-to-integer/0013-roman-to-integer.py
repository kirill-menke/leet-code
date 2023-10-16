class Solution:
    def romanToInt(self, s: str) -> int:
        number_map = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        i = 0
        
        while i < len(s) - 1:
            if number_map[s[i + 1]] > number_map[s[i]]:
                number += number_map[s[i + 1]] - number_map[s[i]]
                i += 1
            else:
                number += number_map[s[i]]
            i += 1
            
        if i != len(s):
            number += number_map[s[i]]

        return number
                