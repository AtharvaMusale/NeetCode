# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val<curr.val and q.val < curr.val:
                curr = curr.left  
            elif p.val>curr.val and q.val>curr.val:
                curr = curr.right
            else:
                return curr


            # def dfs(node):
            #     if node:
            #         if p.val < node.val and q.val < node.val:
            #             return dfs(node.left)
            #         elif p.val > node.val and q.val > node.val:
            #             return dfs(node.right)
            #         else:
            #             return node
            #     return None
            # return dfs(root)

            # curr = root
            # while curr:
                
            #     if p.val<curr.val and q.val<curr.val:
            #         curr = curr.left

            #     elif p.val > curr.val and q.val > curr.val:
            #         curr = curr.right
                
            #     else:
            #         return curr

