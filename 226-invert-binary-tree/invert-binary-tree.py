# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = collections.deque([root])
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            
            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
        
        return root
        
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return None
        
#         queue = collections.deque([root])
#         while queue:
#             current = queue.popleft()

#             current.left, current.right = current.right, current.left

#             while current.left:
#                 queue.append(current.left)
            
#             while current.right:
#                 queue.append(current.right)
            
        
#         return root














        # if root == None:
        #     return None
        
    
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

    