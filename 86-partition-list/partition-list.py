# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = l1prev = ListNode(-1)
        l2 = l2prev = ListNode(-1)
        
        while head:
            if head.val < x:
                l1prev.next = head
                l1prev = l1prev.next
            else:
                l2prev.next = head
                l2prev = l2prev.next
            
            head = head.next
        
        # Terminate the second list
        l2prev.next = None
        # Link the end of the first list to the start of the second list
        l1prev.next = l2.next

        return l1.next