# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         oldtonew = {None : None}

#         curr = head
#         while curr:
#             copy = Node(curr.val)
#             oldtonew[curr] = copy
#             curr= curr.next
        
#         curr = head
#         while curr:
#             copy = oldtonew[curr]
#             copy.next = oldtonew[curr.next]
#             copy.random = oldtonew[curr.random] 
#             curr = curr.next
        
#         return oldtonew[head]


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Interweaving the copied nodes with the original nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        
        # Step 2: Assigning the random pointers to the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next  # Move to the next original node
        
        # Step 3: Restore the original list and extract the copied list
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        
        return copy_head
