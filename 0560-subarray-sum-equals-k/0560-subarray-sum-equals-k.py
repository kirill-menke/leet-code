from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = defaultdict(int)
        sum_count[0] += 1
        
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - k in sum_count:
                count += sum_count[curr_sum - k]
            sum_count[curr_sum] += 1
                
        return count