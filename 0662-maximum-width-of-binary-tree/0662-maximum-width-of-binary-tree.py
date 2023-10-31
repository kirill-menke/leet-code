# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        most_right_idx = []
        max_width = 0

        def dfs(node, level, idx):
            if not node:
                return
            if level == len(most_right_idx):
                most_right_idx.append(idx)

            nonlocal max_width
            max_width = max(max_width, most_right_idx[level] - idx + 1)

            dfs(node.right, level + 1, 2 * idx + 1)
            dfs(node.left, level + 1, 2 * idx)

        dfs(root, 0, 0)
        return max_width