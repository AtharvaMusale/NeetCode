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
        
        q = deque([root])
        while q:
            current = q.popleft()
            current.left, current.right = current.right, current.left

            if current.left:
                q.append(current.left)
            
            if current.right:
                q.append(current.right)
            
        return root
        # if not root:
        #     return None
        
        # q = collections.deque([root])
        # while q:
     
        #         current = q.popleft()
        #         current.left, current.right = current.right, current.left

        #         if current.left:
        #             q.append(current.left)
                
        #         if current.right:
        #             q.append(current.right)
        # return root
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is not None:
#             root.left, root.right = root.right, root.left
#             self.invertTree(root.left)
#             self.invertTree(root.right)
#             return root
        
#         else:
#             return None














        # if root == None:
        #     return None
        
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        # if root == None:
        #     return None
        
    
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

    