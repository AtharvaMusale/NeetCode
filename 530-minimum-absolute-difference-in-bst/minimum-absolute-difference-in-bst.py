# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = float("-inf")
        curr_min = float("inf")
        
        def inorder(node):
            nonlocal prev, curr_min
            if node:
                inorder(node.left)
                if prev != float("-inf"):
                    curr_min = min(curr_min, node.val - prev)
                
                prev = node.val
            
                inorder(node.right)
            
                return curr_min
        curr_min = inorder(root)
        return curr_min