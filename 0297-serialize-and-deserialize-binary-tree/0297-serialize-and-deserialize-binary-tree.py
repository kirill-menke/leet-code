# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        queue = deque([root])
        output = []
       
        while queue:
            node = queue.pop()
            if not node:
                output.append("None,")
            else:
                output.append(f"{node.val},")
                queue.appendleft(node.left)
                queue.appendleft(node.right)
        
        return "".join(output)[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        next_neighbor = 1
        
        while queue:
            node = queue.pop()
            if nodes[next_neighbor] != 'None':
                node.left = TreeNode(int(nodes[next_neighbor]))
                queue.appendleft(node.left)
            next_neighbor += 1
            if nodes[next_neighbor] != 'None':
                node.right = TreeNode(int(nodes[next_neighbor]))
                queue.appendleft(node.right)
            next_neighbor += 1
                
        return root



        
        
        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))