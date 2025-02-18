# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.next, self.prev = None , None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.cap = capacity
#         self.head = Node(0,0)
#         self.tail = Node(0,0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             node =self.cache[key]
#             self._remove(node)
#             self._insert(node)
#             return node.val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self._remove(self.cache[key])
#         node = Node(key,value)
#         self.cache[key] = node
#         self._insert(node)
#         if len(self.cache)>self.cap:
#             lru = self.tail.prev
#             self._remove(lru)
#             del self.cache[lru.key]

#     def _insert(self,node):
#         next = self.head.next
#         self.head.next = node
#         node.prev = self.head
#         node.next = next
#         next.prev = node
    
#     def _remove(self, node):
#         prev = node.prev
#         next = node.next
#         prev.next = next
#         next.prev = prev



# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)


from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # Move the key to the end to show that it was recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move the key to the end because it was recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item from the OrderedDict, which is the least recently used
            self.cache.popitem(last=False)
            