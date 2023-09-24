# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        def traverse_postorder(node):
            if not node:
                return True, -1

            left_balanced, left_height = traverse_postorder(node.left)
            right_balanced, right_height = traverse_postorder(node.right)

            balanced = abs(left_height - right_height) < 2 and left_balanced and right_balanced
            return balanced, 1 + max(left_height, right_height)
            

        return traverse_postorder(root)[0]