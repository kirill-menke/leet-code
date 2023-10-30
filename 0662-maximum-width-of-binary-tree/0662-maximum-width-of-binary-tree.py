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
            _, idx = queue[-1]
            
            for _ in range(len(queue)):
                node, left_idx = queue.pop()
            
                if node.left:
                    queue.appendleft((node.left, 2 * left_idx))
                if node.right:
                    queue.appendleft((node.right, 2 * left_idx + 1))

            max_width = max(max_width, left_idx - idx + 1)
        
        return max_width