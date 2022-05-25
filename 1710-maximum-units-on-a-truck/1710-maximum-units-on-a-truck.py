from collections import defaultdict

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # Runtime:  O(n) + O(1000) = O(n) where n is the length of boxTypes array
        # Space:    O(1000) = O(1)
        
        buckets = defaultdict(int)
        total_weight = 0
        
        for num, weight in boxTypes:
            buckets[weight] += num
        
        for w in range(1000, 0, -1):
            num = min(truckSize, buckets[w])
            total_weight += num * w
            truckSize -= num
            if truckSize == 0:
                return total_weight
            
        return total_weight
            
        