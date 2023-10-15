class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        neg = nums[0]
        pos = nums[0]

        for i in range(1, len(nums)):
            tmp_pos = max(pos * nums[i], neg * nums[i], nums[i])
            neg = min(pos * nums[i], neg * nums[i], nums[i])
            pos = tmp_pos
            max_prod = max(max_prod, pos)
        
        return max_prod
        


            

        

