class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDiag = set() # r+c
        negDiag = set() # r-c
        col = set()

        board = [["."]*n for row in range(n)]

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtracking(r+1)


                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
            
        backtracking(0)
        return res

            



























# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         board = [["." for i in range(n)] for j in range(n)]
#         ans=[]
#         def isSafe(row, col, b):
#             c, r= col, row
#             while c>=0:
#                 if b[r][c] == "Q":
#                     return False
#                 c-=1
#             c= col
#             while c>=0 and r>=0:
#                 if b[r][c] == "Q":
#                     return False
#                 r-=1
#                 c-=1
#             c, r= col, row
#             while c>=0 and r<n:
#                 if b[r][c] == "Q":
#                     return False
#                 r+=1
#                 c-=1
#             return True
#         def solve(row, col, b):
#             if col == n:
#                 ans.append(["".join(i) for i in b])
#                 return
            
#             for row in range(n):
#                 if(isSafe(row, col, b)):
#                     b[row][col] = "Q"
#                     solve(row, col+1, b)

#                     b[row][col] = "."
            
#         solve(0,0,board)
#         return ans
        