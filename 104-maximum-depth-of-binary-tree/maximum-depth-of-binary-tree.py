# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using Iterative Stack Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        
        if root:
            stack.append([1,root])

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(current_depth,depth)
                stack.append((current_depth+1,  root.left))
                stack.append((current_depth+1, root.right))

        return depth




# Recursive

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         lh = self.maxDepth(root.left)
#         rh = self.maxDepth(root.right)
#         return 1 + max(lh,rh)


