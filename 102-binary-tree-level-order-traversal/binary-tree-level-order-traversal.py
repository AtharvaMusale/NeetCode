from collections import deque
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []
        
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                
                # Only add non-null children to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)
        return res
