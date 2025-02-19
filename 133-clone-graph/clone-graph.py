"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        oldToNew = {}
        copy = Node(node.val)
        oldToNew[node] = copy
    
        q = deque([node])
        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in oldToNew:
                    copyNei = Node(nei.val)
                    oldToNew[nei] = copyNei
                    q.append(nei)
                oldToNew[curr].neighbors.append(oldToNew[nei])
        return oldToNew[node]