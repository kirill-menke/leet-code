# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush, heapify

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i) for i, node in enumerate(lists) if node]
        heapify(heap)
        sentinel = running = ListNode(-1)

        while heap:
            min_val, idx = heappop(heap)
            
            next_node = ListNode(min_val)
            running.next = next_node
            running = next_node

            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(heap, (lists[idx].val, idx))

        return sentinel.next
        


