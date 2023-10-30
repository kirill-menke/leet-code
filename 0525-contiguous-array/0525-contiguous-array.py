class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_to_index = {0: -1}
        count = 0
        max_window = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_to_index:
                max_window = max(max_window, i - count_to_index[count])
            else:
                count_to_index[count] = i
        
        return max_window