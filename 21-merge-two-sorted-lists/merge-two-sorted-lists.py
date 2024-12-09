# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         curr = dummy
#         while l1 and l2:
#             if l1.val<l2.val:
#                 curr.next = l1
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
            
#             curr = curr.next
        
#         curr.next = l1 if l1 is not None else l2
#         return dummy.next
            


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Create a dummy node to simplify edge cases
        tail = dummy  # This will be the tail of the new list to which we'll add nodes
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1  # Attach the smaller node to the tail
                l1 = l1.next  # Move the pointer in list l1 forward
            else:
                tail.next = l2  # Attach the smaller or equal node to the tail
                l2 = l2.next  # Move the pointer in list l2 forward
            tail = tail.next  # Move the tail pointer forward

        # At the end of the loop, at least one of l1 and l2 is None
        tail.next = l1 if l1 is not None else l2  # Connect the remaining part of the non-empty list
        
        return dummy.next  # The head of the merged list
