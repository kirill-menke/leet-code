class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2

        n = len(nums)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, subset_sum + 1):
                num = nums[i - 1]
                if num <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]
