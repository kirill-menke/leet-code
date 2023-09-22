# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, node):
        if not node:
            return -1
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        diameter = 2 + self.get_height(root.left) + self.get_height(root.right)
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(diameter, left_diameter, right_diameter)
