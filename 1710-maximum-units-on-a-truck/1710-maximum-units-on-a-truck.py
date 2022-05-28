class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = []
        
        for box in boxTypes:
            for i in range(box[0]):
                heapq.heappush(heap, box[1])
                if len(heap) > truckSize:
                    heapq.heappop(heap)
        
        return sum(heap)