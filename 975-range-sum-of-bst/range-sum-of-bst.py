# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        if low <= root.val <= high:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        elif low <= root.val:
            return self.rangeSumBST(root.left, low, high)
        elif root.val <= high:
            return self.rangeSumBST(root.right, low, high)
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         def dfs(node):
#             nonlocal ans
#             if node:
#                 if node.val<=high and node.val>=low:
#                     ans+=node.val
#                 if low<node.val:
#                     dfs(node.left)
#                 if node.val<high:
#                     dfs(node.right)
#         ans = 0
#         dfs(root)
#         return ans
        