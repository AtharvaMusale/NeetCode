class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = {}
        if not root: return res        
        def dfs(node,level):
            if level not in res:
                res[level] = node.val
            if node.right:
                dfs(node.right,level+1)
            if node.left:
                dfs(node.left,level+1)        
        dfs(root,0)        
        return res.values()