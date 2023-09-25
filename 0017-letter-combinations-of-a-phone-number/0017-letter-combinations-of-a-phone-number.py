class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        output = []

        def backtrack(idx, curr):
            if len(curr) == len(digits):
                output.append(''.join(curr))
                return
            
            letters = char_map[int(digits[idx])]
            for letter in letters:
                curr.append(letter)
                backtrack(idx + 1, curr)
                curr.pop()
        
        if not digits:
            return []
            
        backtrack(0, [])
        return output
                

