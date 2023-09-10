from bisect import bisect_left

class Solution:
    def find_best_sequence(self, pos):
        if pos == len(self.jobs):
            return 0
        if self.mem[pos]:
            return self.mem[pos]

        next_idx = bisect_left(self.jobs, self.jobs[pos][1], key=lambda x: x[0])
        max_profit = max(self.find_best_sequence(pos + 1), self.jobs[pos][2] + self.find_best_sequence(next_idx))
        self.mem[pos] = max_profit

        return max_profit
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.mem = [None] * len(profit)
        self.jobs = sorted(zip(startTime, endTime, profit))

        return self.find_best_sequence(0)
        