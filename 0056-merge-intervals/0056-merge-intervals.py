class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = set()
        start = 0
        end = 1
        
        for curr in intervals:
            remove = set()
            for prev in res:
                # If current interval overlaps with one of the previous
                if curr[end] >= prev[start] and curr[start] <= prev[end]:
                    curr[start] = min(curr[start], prev[start])
                    curr[end] = max(curr[end], prev[end])
                    remove.add(tuple(prev))
            res -= remove
            res.add(tuple(curr))

        return res
            