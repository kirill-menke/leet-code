class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        for i in range(2**len(nums), 2**(len(nums) + 1)):
            bin_mask = bin(i)[3:]
            output.append([nums[i] for i in range(len(nums)) if bin_mask[i] == '1'])

        return output

