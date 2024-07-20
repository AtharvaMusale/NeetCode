# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        res = []
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if level:
                res.append(level)
        
        return res















        # res = []
        # q = collections.deque([root])
        # while q:
        #     level =[]
        #     for i in range(len(q)):
        #         curr = q.popleft()
        #         if curr:
        #             level.append(curr.val)
        #             q.append(curr.left)
        #             q.append(curr.right)
        #     if level:
        #         res.append(level)
        # return res
        # res = []
        # queue = collections.deque()
        # queue.append(root)
        
        # while queue:
        #     level = []
        #     for i in range(len(queue)):
        #         curr = queue.popleft()
        #         if curr:
        #             level.append(curr.val)
        #             queue.append(curr.left)
        #             queue.append(curr.right)
        #     if level:
        #         res.append(level)
            
        # return res























# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
        
#         queue = collections.deque()
#         queue.append(root)

#         while queue:
#             level = []
#             for i in range(len(queue)):
#                 curr = queue.popleft()
#                 if curr:
#                     level.append(curr.val)
#                     queue.append(curr.left)
#                     queue.append(curr.right)
#             if level:
#                 res.append(level)
#         return res