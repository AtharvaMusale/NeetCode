# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         second = slow.next
#         prev = slow.next = None

#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp
        
#         first, second = head, prev
#         while second:   
#             tmp1, tmp2 = first.next, second.next
#             first.next = second
#             second.next = tmp1
#             first, second = tmp1, tmp2



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        first = head
        sec = prev
        while sec.next:
            first.next, first =  sec, first.next 
            sec.next, sec = first, sec.next

        return head