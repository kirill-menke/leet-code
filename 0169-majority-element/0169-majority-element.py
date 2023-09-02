from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        
        for num in nums:
            num_count[num] += 1
        
        return max(num_count, key=lambda x: num_count[x])

