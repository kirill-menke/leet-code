class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []

        for inter in intervals:
            if newInterval[0] > inter[1]:
                left.append(inter)
            elif newInterval[1] < inter[0]:
                right.append(inter)
            else:
                newInterval[0] = min(newInterval[0], inter[0])
                newInterval[1] = max(newInterval[1], inter[1])
        
        return left + [newInterval] + right