# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder = []
        stack = []
        curr = root
        
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif(stack):
                curr = stack.pop()
                if inorder and inorder[-1] == p:
                    return curr
                inorder.append(curr)
                curr = curr.right
            else:
                break
        