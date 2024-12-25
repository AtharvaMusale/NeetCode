# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.res = 0

#         def dfs(curr):
#             if not curr:
#                 return 0

#             lh = dfs(curr.left)
#             rh = dfs(curr.right)

#             self.res = max(self.res, lh+rh)
        
#             return 1 + max(lh,rh)
    
#         dfs(root)
#         return self.res
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(curr):
            if not curr:
                return 0

            # Recursively get the depth of the left and right subtrees
            lh = dfs(curr.left)
            rh = dfs(curr.right)

            # Update the result with the maximum diameter found
            self.res = max(self.res, lh + rh)

            # Return the depth of the current node
            return 1 + max(lh, rh)
        
        dfs(root)
        return self.res
