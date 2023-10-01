from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        sorted_frequencies = sorted(task_count.values(), reverse=True)
        idle_slots = (sorted_frequencies[0] - 1) * n

        for i in range(1, len(sorted_frequencies)):
            avail_gaps = sorted_frequencies[0] - 1
            idle_slots -= min(avail_gaps, sorted_frequencies[i])
            
        idle_slots = max(0, idle_slots)
        
        return idle_slots + len(tasks)
