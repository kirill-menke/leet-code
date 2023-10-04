class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        mem = [0] * (n + 2)
        mem[1] = 1

        for i in range(2, n + 2):
            mem[i] = mem[i - 1] + mem[i - 2]

        return mem[-1]