# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        def helper(node, current_list, targetSum):
            if not node:
                return
            
            current_list.append(node.val)
            helper(node.left, current_list, targetSum - node.val)
            helper(node.right, current_list, targetSum - node.val)

            if targetSum - node.val == 0 and not (node.left or node.right):
                output.append(current_list[:])

            current_list.pop()
        
        helper(root, [], targetSum)
        return output