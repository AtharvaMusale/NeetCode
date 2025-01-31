"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {}
        if not head:
            return None

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                oldToNew[curr].next =  oldToNew[curr.next]
            if curr.random:
                oldToNew[curr].random =  oldToNew[curr.random]
            curr = curr.next
    
        return oldToNew[head]