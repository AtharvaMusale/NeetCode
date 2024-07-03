class Solution:
    def exist(self, board: List[List[str]], s: str) -> bool:
        m, n = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            if i == len(s):
                return True
            
            if r<0 or c< 0 or r>=m or c>=n or s[i] != board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))
            res =  (dfs(r+1,c,i+1) or
            dfs(r,c+1,i+1) or
            dfs(r-1,c,i+1) or
            dfs(r,c-1,i+1)) 

            path.remove((r,c))
            return res
        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True

        return False



















        # m, n = len(board), len(board[0])
   
        # def find(sInd, i, j, vis):
        #     if sInd == len(s)-1:
        #         print(vis)
        #         return True
        #     vis.append((i, j))
        #     ans = False
        #     for nx, ny in [(i+1, j), (i-1, j), (i,j+1), (i, j-1)]:
        #         if 0<=nx<m and 0<=ny<n and (nx, ny) not in vis and board[nx][ny] == s[sInd+1]:
        #             ans = ans or find(sInd+1, nx, ny, vis)
        #     vis.pop()
        #     return ans
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == s[0] and find(0, i, j,[] ):
        #             return True
        # return False

   
   
   
   
    # if board[i][j] == word[0]
    # if find(0,i, j)
        