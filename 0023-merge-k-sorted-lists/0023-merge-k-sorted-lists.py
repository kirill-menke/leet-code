# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        running = ListNode(-1)
        sentinel = ListNode(-1, running)

        while True:
            min_val, min_idx = float("inf"), None
            for i, node in enumerate(lists):
                if node and node.val < min_val:
                    min_val = node.val
                    min_idx = i
            
            if min_idx is None:
                break
            
            lists[min_idx] = lists[min_idx].next

            next_node = ListNode(min_val)
            running.next = next_node
            running = next_node

        return sentinel.next.next
        


