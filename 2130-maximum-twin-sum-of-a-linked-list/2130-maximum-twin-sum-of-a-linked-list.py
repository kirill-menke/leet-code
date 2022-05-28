# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head):
        prev = None
        while head:
            _next = head.next
            head.next = prev
            prev, head = head, _next
            
        return prev
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_head = self.reverseList(slow)
        _max = 0
        
        while second_head:
            _max = max(_max, head.val + second_head.val)
            head, second_head = head.next, second_head.next
            
        return _max
            