# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd_sentinel, even_sentinel = ListNode(-1), ListNode(-1)
        odd_head, even_head = odd_sentinel, even_sentinel
        even = False

        while head:
            if even:
                even_head.next = head
                even_head = even_head.next
            else:
                odd_head.next = head
                odd_head = odd_head.next

            even = not even
            head = head.next
        
        odd_head.next = even_sentinel.next
        even_head.next = None
        
        return odd_sentinel.next