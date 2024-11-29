# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, min_val, max_val):
            if not node:
                return True  # Correct base case: An empty node is a valid BST

            if not (min_val < node.val < max_val):
                return False
            
            # Recursively validate the subtrees with updated constraints
            left_is_valid = check(node.left, min_val, node.val)
            right_is_valid = check(node.right, node.val, max_val)
            return left_is_valid and right_is_valid
        
        return check(root, float('-inf'), float('inf'))