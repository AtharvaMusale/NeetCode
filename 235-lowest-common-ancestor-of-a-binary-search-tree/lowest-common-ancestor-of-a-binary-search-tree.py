# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if p.val>root.val and q.val>root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
        
#         elif p.val < root.val and q.val< root.val:
#             return self.lowestCommonAncestor(root.left,p,q)
        
#         else:
#             return root
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # Move to the right subtree if both p and q are greater than root.
            if p.val > root.val and q.val > root.val:
                root = root.right
            # Move to the left subtree if both p and q are lesser than root.
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                # Found the split point or one of p or q is the root.
                return root
