class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = {}
        def dfs(r,c,prev):
            if (r<0 or r==ROWS or c<0 or c == COLS or grid[r][c] <=prev):
                return 0 
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1
            res = max(res, 1+ dfs(r+1,c,grid[r][c]))
            res = max(res, 1+ dfs(r-1,c,grid[r][c]))
            res = max(res, 1+ dfs(r,c+1,grid[r][c]))
            res = max(res, 1+ dfs(r,c-1,grid[r][c]))
            dp[(r,c)] = res
            return res


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        return max(dp.values())






        # n, m = len(matrix), len(matrix[0])
        # ans = 0
        # memo = {}
        # def GetPath(i, j):
        #     if (i, j) in memo : return memo[(i,j)]
        #     ans = 1
        #     for r, c in [(i+1,j),(i-1,j),(i,j+1),(i, j-1)]:
        #         if 0<=r<n and 0<=c<m and matrix[r][c] > matrix[i][j]:
        #             ans = max(ans,1+ GetPath(r,c))
        #     memo[(i,j)] = ans
        #     return ans
        # for r in range(0,n):
        #     for c in range(0, m):
        #         ans = max(ans, GetPath(r,c))

        # return ans
    