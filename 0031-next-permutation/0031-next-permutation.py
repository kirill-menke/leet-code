class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start_idx = None

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                start_idx = i - 1
                break
        
        if start_idx is None:
            nums.sort()
            return

        for j in range(len(nums) - 1, start_idx, -1):
            if nums[j] > nums[start_idx]:
                nums[j], nums[start_idx] = nums[start_idx], nums[j]
                break
        
        for i, num in enumerate(reversed(nums[start_idx + 1:]), start_idx + 1):
            nums[i] = num
        

            


        