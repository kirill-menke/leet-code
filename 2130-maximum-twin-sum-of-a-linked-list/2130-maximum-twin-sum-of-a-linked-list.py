# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Find mid of list
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse second half of list
        curr, prev = slow, None
        
        while curr:
            _next = curr.next
            curr.next = prev
            curr, prev = _next, curr
            
        _max = 0
        first, second = head, prev
        
        while second:
            _max = max(_max, first.val + second.val)
            first = first.next
            second = second.next
        
        return _max
            
            
            
            
            
        
        
        
        
        