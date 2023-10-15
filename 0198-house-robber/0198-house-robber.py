class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def rob_helper(current_idx):
            if current_idx >= len(nums):
                return 0
            if current_idx == len(nums) - 1:
                return nums[current_idx]
            
            return max(nums[current_idx] + rob_helper(current_idx + 2), nums[current_idx + 1] + rob_helper(current_idx + 3))
    
        return rob_helper(0)