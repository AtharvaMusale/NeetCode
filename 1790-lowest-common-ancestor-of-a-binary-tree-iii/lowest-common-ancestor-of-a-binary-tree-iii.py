"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Pointers to traverse the tree
        a, b = p, q
        
        # Loop until both pointers meet
        while a != b:
            # Move to the parent node, or to the other node's initial position if reaching the root
            a = a.parent if a else q
            b = b.parent if b else p
        
        # Return the common ancestor
        return a
        # ancestor = set()
        # while p:
        #     ancestor.add(p)
        #     p = p.parent
        
        # while q:
        #     if q in ancestor:
        #         return q
        #     q = q.parent
        



# class Node:
#     def __init__(self,val:int, left:'Node'=None, right:'Node'=None, parent:'Node'=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.parent = parent
# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
#         result = 0
#         ancestor = set()
#         while p:
#             ancestor.add(p)
#             p = p.parent
        
#         while q:
#             if q in ancestor:
#                 return q
#             q = q.parent

#         return None