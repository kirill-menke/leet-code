class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        writes = 0
        start = 0

        while writes < len(nums):
            current_idx = start
            current_num = nums[current_idx]

            while True:
                next_idx = (current_idx + k) % len(nums)
                current_num, nums[next_idx] = nums[next_idx], current_num
                current_idx = next_idx
                writes += 1
                
                if current_idx == start:
                    break
            
            start += 1






        
