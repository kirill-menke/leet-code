class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        start_idx = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_gain += gain
            curr_gain += gain

            if curr_gain < 0:
                start_idx = i + 1
                curr_gain = 0
        
        return start_idx if total_gain >= 0 else -1

        