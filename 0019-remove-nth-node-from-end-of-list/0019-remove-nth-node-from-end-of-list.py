# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.count = 0

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(head, n):
            if not head:
                return None
            
            node = helper(head.next, n)
            self.count += 1

            if self.count == n + 1:
                head.next = node.next
            
            return head
        
        new_head = helper(head, n)
        return new_head if self.count > n else head.next
