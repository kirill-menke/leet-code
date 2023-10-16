class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pivot_idx = None

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot_idx = i - 1
                break
        
        if pivot_idx is None:
            nums.sort()
            return
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[pivot_idx]:
                nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
                break
        
        left, right = pivot_idx + 1, len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1
        
        
