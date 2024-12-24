# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        

        # lh = self.maxDepth(root.left)
        # rh = self.maxDepth(root.right)
    
        # return max(lh,rh) + 1

        q = deque([root])
        depth = 0
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            depth+=1

        return depth
            