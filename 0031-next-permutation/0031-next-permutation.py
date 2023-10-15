class Solution:
    def reverse(self, nums, start):
        for i, elem in enumerate(reversed(nums[start:]), start):
            nums[i] = elem

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_idx = -1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                swap_idx = i - 1
                break
        
        if swap_idx == -1:
            self.reverse(nums, 0)
            return

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[swap_idx]:
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
                break

        self.reverse(nums, swap_idx + 1)