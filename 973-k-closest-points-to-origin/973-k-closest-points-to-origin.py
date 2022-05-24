class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        dist = lambda e: e[0]**2 + e[1]**2
        
        for p in points:
            if len(heap) < k:
                heapq.heappush(heap, (-dist(p), p))
            elif heap[0][0] < -dist(p):
                heapq.heappushpop(heap, (-dist(p), p))
                
        return map(lambda l: l[1], heap)
        
            
                
            
                
                