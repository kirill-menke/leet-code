# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, 0)])
        max_width = 1

        while queue:
            current_len = len(queue)
            right_idx = left_idx = None

            for i in range(current_len):
                node, idx = queue.pop()
                if right_idx is None:
                    right_idx = idx
                left_idx = idx

                max_width = max(max_width, left_idx - right_idx + 1)

                if node.left:
                    queue.appendleft((node.left, 2 * idx))
                if node.right:
                    queue.appendleft((node.right, 2 * idx + 1))
        
        return max_width