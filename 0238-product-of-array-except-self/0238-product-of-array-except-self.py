class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod, postfix_prod = [], []
        
        for i, num in enumerate(nums):
            prev = prefix_prod[-1] if prefix_prod else 1
            prefix_prod.append(num * prev)

        for i, num in enumerate(reversed(nums)):
            prev = postfix_prod[-1] if postfix_prod else 1
            postfix_prod.append(num * prev)
        
        postfix_prod = list(reversed(postfix_prod))

        output = []
        
        for i, num in enumerate(nums):
            prefix = prefix_prod[i - 1] if i != 0 else 1
            postfix = postfix_prod[i + 1] if i < len(nums) - 1 else 1
            output.append(prefix * postfix)

        return output


        

