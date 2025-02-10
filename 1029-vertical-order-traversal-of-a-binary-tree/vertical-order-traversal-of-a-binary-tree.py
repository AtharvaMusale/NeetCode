# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, x, y):
            if node:
                res.append((x,y,node.val))
                dfs(node.left,x-1,y+1)
                dfs(node.right,x+1,y+1)
        
        dfs(root,0,0)
        res.sort()
        ans =collections.defaultdict(list)
        for x,y,val in res:
            ans[x].append(val)
        return [ans[key] for key in sorted(ans)]
