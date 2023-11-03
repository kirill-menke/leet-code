class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            bin_num = bin(num)[2:]
            ans.append(sum(1 for char in bin_num if char == '1'))
        return ans

    