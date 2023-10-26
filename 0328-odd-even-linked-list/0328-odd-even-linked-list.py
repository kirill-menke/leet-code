# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_sentinel = even_curr = ListNode(-1)
        odd_sentinel = odd_curr = ListNode(-1)

        count = 1
        while head:
            if count % 2 == 0:
                even_curr.next = head
                even_curr = even_curr.next
            else:
                odd_curr.next = head
                odd_curr = odd_curr.next
            
            next_tmp = head.next
            head.next = None
            head = next_tmp
            count += 1

        odd_curr.next = even_sentinel.next

        return odd_sentinel.next