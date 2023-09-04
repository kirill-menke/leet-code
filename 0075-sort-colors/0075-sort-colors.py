class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bottom, mid, top = 0, 0, len(nums) - 1
        
        while mid <= top:
            if nums[mid] == 0:
                nums[bottom], nums[mid] = nums[mid], nums[bottom]
                mid += 1
                bottom += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[top], nums[mid] = nums[mid], nums[top]
                top -= 1


            