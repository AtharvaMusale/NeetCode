# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        add = 0
        stack = [(root, 0)]

        while stack:
            root, curr_num = stack.pop()
            if root is not None:
                curr_num = curr_num * 10 + root.val

                if root.left is None and root.right is None:
                    add += curr_num
                
                else:
                    stack.append((root.right,curr_num))
                    stack.append((root.left, curr_num))

            
        return add


        