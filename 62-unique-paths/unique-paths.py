class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]

        def dfs(i,j,dp):
            if not (0<=i<m and 0<=j<n):
                return 0

            if i==m-1 and j == n-1:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            ans = dfs(i+1,j,dp) + dfs(i,j+1,dp)
            dp[i][j] = ans
            return ans
        return dfs(0,0,dp) 



















        # dp = [[-1 for _ in range(n)] for r in range(m)]

        # def dfs(i, j, dp):
        #     if not(0<=i<m and 0<=j<n): return 0
        #     if i == m-1 and j == n-1: return 1
        #     if dp[i][j] != -1: return dp[i][j]
        #     ans = dfs(i+1, j, dp) +dfs(i, j+1, dp)
        #     dp[i][j] = ans
        #     return ans
        # return dfs(0,0,dp)