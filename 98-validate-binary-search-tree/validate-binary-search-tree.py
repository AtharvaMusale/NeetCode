# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def validate(node,low = math.inf,high = math.inf):
#             if not node:
#                 return True
            
#             if node.val<=low or node.val >= high:
#                 return False
            
#             return validate(node.right,node.val,high) and validate(node.left,low,node.val)
#         return validate(root)

        # def isValid(node):
        #     if node is None:
        #         return True, float("inf"), -float("inf")
            
        #     lbst, lmin, lmax = isValid(node.left)
        #     rbst, rmin, rmax = isValid(node.right)

        #     if lbst and rbst and lmax<node.val<rmin:
        #         return True, min(lmin,node.val), max(rmax,node.val)
        #     return False, 0, 0
        # ans, _, _ = isValid(root)
    
        # return ans

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return validate(node.right, node.val, high) and validate(node.left, low, node.val)
        
        return validate(root)
