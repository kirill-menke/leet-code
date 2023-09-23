# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def traverse_inorder(root):
            if not root:
                return []
            
            return traverse_inorder(root.left) + [root.val] + traverse_inorder(root.right)

        return traverse_inorder(root)[k - 1]