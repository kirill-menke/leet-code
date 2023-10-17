# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum_sum = -float("inf")

        def helper(root):
            if not root:
                return 0
            
            left_sum = helper(root.left)
            right_sum = helper(root.right)
            self.maximum_sum = max(self.maximum_sum, root.val + left_sum + right_sum, root.val + left_sum, root.val + right_sum, root.val)

            return max(left_sum + root.val, right_sum + root.val, root.val)
        
        helper(root)
        return self.maximum_sum