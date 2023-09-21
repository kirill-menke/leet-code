# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth_val = None
        self.k = k
        self.traverse_inorder(root, k)
        return self.kth_val

    def traverse_inorder(self, node, k): 
        if not node or self.kth_val:
            return
        
        self.traverse_inorder(node.left, k)

        self.k -= 1
        if self.k == 0:
            self.kth_val = node.val
        
        self.traverse_inorder(node.right, k)
