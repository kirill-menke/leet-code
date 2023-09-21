# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([-1, root])
        result = []

        tmp = []
        while len(queue) > 1:
            node = queue.pop()
            
            if not node:
                continue
            if node == -1:
                result.append(tmp)
                tmp = []
                queue.appendleft(-1)
                continue
            else:
                tmp.append(node.val)
                queue.appendleft(node.left)
                queue.appendleft(node.right)

        if tmp:
            result.append(tmp)

        return result
