# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.sentinel = ListNode(-1)
        
        def helper(node):
            if not node or not node.next:
                self.sentinel.next = node
                return
            
            helper(node.next)
            node.next.next = node
            node.next = None
        
        helper(head)
        return self.sentinel.next

