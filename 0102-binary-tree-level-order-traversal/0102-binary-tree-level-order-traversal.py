# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        output = []

        while queue:
            output.append([])
            for _ in range(len(queue)):
                node = queue.pop()
                if node:
                    output[-1].append(node.val)
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
        
        output.pop()
        return output
