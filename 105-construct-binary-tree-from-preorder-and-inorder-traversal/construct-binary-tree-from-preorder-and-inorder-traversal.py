# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
        


















        # def build ( preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #     if not preorder or not inorder:
        #         return
           
        #     root = TreeNode(preorder[0])
        #     for i, val in enumerate(inorder):
        #         if val == preorder[0]:
        #             inorderIdx = i
        #             break
        #     root.left = build(preorder[1: inorderIdx+1], inorder[ :inorderIdx])
        #     root.right = build(preorder[inorderIdx+1: ], inorder[inorderIdx+1: ])
        #     return root
        # return build(preorder, inorder)
        
    
        