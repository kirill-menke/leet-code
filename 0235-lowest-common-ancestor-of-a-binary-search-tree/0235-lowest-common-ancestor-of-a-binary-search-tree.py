# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(N)
# O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)
        
    def helper(self, node, p, q):
        if p.val < node.val and q.val < node.val:
            return self.helper(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return self.helper(node.right, p, q)
        else:
            return node