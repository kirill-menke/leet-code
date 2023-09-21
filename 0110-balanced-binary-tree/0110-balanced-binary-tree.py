# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[0]
    
    def isBalancedHelper(self, root):
        if not root:
            return (True, -1)

        balanced, height_left = self.isBalancedHelper(root.left)
        if not balanced:
            return (False, 0)

        balanced, height_right = self.isBalancedHelper(root.right)
        if not balanced:
            return (False, 0)

        return abs(height_left - height_right) < 2, 1 + max(height_left, height_right)

    
    