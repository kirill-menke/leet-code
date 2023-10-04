# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop, heapify

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i) for i, node in enumerate(lists) if node]
        heapify(heap)

        sentinel = current = ListNode(-1)

        while heap:
            node_val, idx = heappop(heap)
            current.next = lists[idx]
            current = current.next

            if current.next:
                heappush(heap, (current.next.val, idx))
                lists[idx] = lists[idx].next
            
        return sentinel.next



