# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0:
#             return None
#         for i in range(1,len(lists)):
#             lists[i] = self.merge(lists[i-1], lists[i])
#         return lists[-1]

#     def merge(self,l1,l2):
#         dummy = ListNode()
#         tail = dummy
#         while l1 and l2:
#             if l1.val<l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
            
            
#             tail = tail.next
        
        
#         tail.next = l1 or l2
        
#         return dummy.next

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()  # A dummy node to ease operations
        current = dummy

        # Initialize the heap with the head of each list
        for i, node in enumerate(lists):
            if node:
                # Push tuple (node value, list index, node) into the heap
                # The list index ensures that we have a way to differentiate between nodes with the same value
                heapq.heappush(heap, (node.val, i, node))

        # Continue popping the smallest item from the heap
        while heap:
            val, idx, node = heapq.heappop(heap)
            # Attach the node directly instead of creating a new one
            current.next = node
            current = current.next
            if node.next:
                # Push the next node from the same list into the heap
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next
