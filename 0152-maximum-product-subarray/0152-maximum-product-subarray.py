class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest_pos = [nums[0]] * len(nums)
        largest_neg = [nums[0]] * len(nums)

        for i in range(1, len(nums)):
            largest_pos[i] = max(largest_pos[i - 1] * nums[i], largest_neg[i - 1] * nums[i], nums[i])
            largest_neg[i] = min(largest_pos[i - 1] * nums[i], largest_neg[i - 1] * nums[i], nums[i])

        return max(largest_pos)

            
