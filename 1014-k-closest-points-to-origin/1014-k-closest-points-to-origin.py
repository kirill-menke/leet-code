from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heapq.heappush(heap, (distance, [x, y]))
        
        return list(zip(*[heapq.heappop(heap) for _ in range(k)]))[1]