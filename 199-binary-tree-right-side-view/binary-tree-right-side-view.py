class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        next_level = deque([root])
        rightside =[]
        while next_level:
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
                
            rightside.append(node.val)
        
        return rightside

        # res = {}
        # if not root: return res        
        # def dfs(node,level):
        #     if level not in res:
        #         res[level] = node.val
        #     if node.right:
        #         dfs(node.right,level+1)
        #     if node.left:
        #         dfs(node.left,level+1)        
        # dfs(root,0)        
        # return res.values()