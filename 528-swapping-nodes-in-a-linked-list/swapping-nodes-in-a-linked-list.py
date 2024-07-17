# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first_k = head
        length = 0
        first_k_node = None
        
        # First pass to find the length of the list and the k-th node from the beginning
        while first_k:
            length += 1
            if length == k:
                first_k_node = first_k
            first_k = first_k.next
        
        # Find the k-th node from the end
        second_k = head
        for _ in range(length - k):
            second_k = second_k.next
        
        # Swap the values of the k-th node from the beginning and the k-th node from the end
        first_k_node.val, second_k.val = second_k.val, first_k_node.val
        
        return head
