class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = values[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            if values[s[i]] < values[s[i + 1]]:
                number -= values[s[i]]
            else:
                number += values[s[i]]
        
        return number

