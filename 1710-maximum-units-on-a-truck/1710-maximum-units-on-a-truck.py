class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # Runtime:  O(n * log(k)) since our heap has size k and we need to pop n times in worst case
        # Space:    O(k) since out heap has size k
        
        n = len(boxTypes)
        heap = []
        
        for i in range(n):
            for j in range(boxTypes[i][0]):
                weight = boxTypes[i][1]
                if len(heap) < truckSize:
                    heapq.heappush(heap, weight)
                elif heap[0] < weight:
                    heapq.heappushpop(heap, weight)
        
        return sum(heap)
        
        