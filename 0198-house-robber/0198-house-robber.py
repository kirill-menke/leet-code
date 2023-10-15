class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [0] * (len(nums) + 2)

        for i in range(2, len(nums) + 2):
            mem[i] = max(mem[i - 1], mem[i - 2] + nums[i - 2])
        
        return mem[-1]

        