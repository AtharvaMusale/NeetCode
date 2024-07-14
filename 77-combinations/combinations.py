class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i,comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            for s in range(i,n+1):
                comb.append(s)
                dfs(s+1,comb)
                comb.pop()
        dfs(1,[])
        return res