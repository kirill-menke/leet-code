class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        subset_sum = total_sum / 2

        @cache
        def helper(subset_sum, current_idx):
            if subset_sum == 0:
                return True
            if current_idx < 0 or subset_sum < 0:
                return False

            ret = helper(subset_sum - nums[current_idx], current_idx - 1) or helper(subset_sum, current_idx - 1)

            return ret

        return helper(subset_sum, len(nums) - 1)


