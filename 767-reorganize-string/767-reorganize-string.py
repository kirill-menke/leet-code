from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)
        
        result = []
        prev_count = 0
        prev_char = ""
        
        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            
            count += 1
            prev_count = count
            prev_char = char
            
        return "".join(result) if len(result) == len(s) else ""
            
            