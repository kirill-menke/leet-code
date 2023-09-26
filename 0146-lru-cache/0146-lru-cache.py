from collections import deque

class ListNode:
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def appendleft(self, node):
        node.next = self.head.next
        node.next.prev = node

        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.appendleft(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.appendleft(node)
        elif self.capacity > 0:
            self.capacity -= 1
            node = ListNode(value, key)
            self.appendleft(node)
            self.cache[key] = node
        else:
            node_to_delete = self.tail.prev
            self.remove(node_to_delete)
            del self.cache[node_to_delete.key]

            node = ListNode(value, key)
            self.appendleft(node)
            self.cache[key] = node
        

            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)