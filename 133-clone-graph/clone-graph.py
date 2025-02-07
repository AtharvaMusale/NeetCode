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
        seen = {}
        if not node:
            return None

        def dfs(node):
            copy = Node(node.val)
            seen[copy.val] = copy
            for i in node.neighbors:
                if i.val in seen:
                    copy.neighbors.append(seen[i.val])
                else:
                    copy.neighbors.append(dfs(i))
            return copy
            
        return dfs(node)