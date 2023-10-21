# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        sentinel.next = head

        prev, current = sentinel, head

        while current and current.next:
            prev.next = current.next
            
            next_next = current.next.next
            current.next.next = current
            current.next = next_next

            prev = current
            current = next_next

        return sentinel.next