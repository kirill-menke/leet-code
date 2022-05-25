class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
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
        
        