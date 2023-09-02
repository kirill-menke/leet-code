class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev = set()

        for num in nums:
            if num in prev:
                return True
            else:
                prev.add(num)

        return False
