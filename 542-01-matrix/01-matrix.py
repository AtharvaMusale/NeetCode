class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])

        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    top = mat[i-1][j] if i >0  else (n + m -2)
                    left = mat[i][j-1] if j > 0 else (n+m-2)
                    mat[i][j] = min(top+1, left+1)
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if mat[i][j]!= 0:
                    bot = mat[i+1][j] if i + 1 <n else n+m-2
                    right = mat[i][j+1] if j+1 <m else n+m-2
                    mat[i][j] = min(mat[i][j],bot+1,right+1)
        return mat
