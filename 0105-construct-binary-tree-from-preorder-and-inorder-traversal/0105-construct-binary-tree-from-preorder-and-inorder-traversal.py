# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = 0

        def traverse(start, end):
            nonlocal pre_index
            if start >= end:
                return None
            
            root_idx = inorder.index(preorder[pre_index])
            pre_index += 1

            node = TreeNode(inorder[root_idx])
            node.left = traverse(start, root_idx)
            node.right = traverse(root_idx + 1, end)

            return node

        return traverse(0, len(preorder))