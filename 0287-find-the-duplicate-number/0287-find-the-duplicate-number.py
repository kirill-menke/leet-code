class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = 0
        n = len(nums) - 1
        n_bit_length = len(bin(n)[2:])

        for bit in range(n_bit_length):
            nums_count = 0
            base_count = 0

            for i in range(n + 1):
                if nums[i] & (1 << bit):
                    nums_count += 1
                if i & (1 << bit):
                    base_count += 1
            
            if nums_count > base_count:
                duplicate |= (1 << bit)
        
        return duplicate

                
