from collections import defaultdict
class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
#         ROWS , COLS = len(board), len(board[0])
#         rows = collections.defaultdict(set)
#         cols = collections.defaultdict(set)
#         grid = collections.defaultdict(set)  
    
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if board[r][c] == ".":
#                     continue
                
#                 if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[(r//3,c//3)]:
#                     return False
                
#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 grid[(r // 3, c // 3)].add(board[r][c])
            
#         return True


        ROWS,COLS = len(grid), len(grid[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        sq = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ".":
                    continue
                
                if grid[r][c] in rows[r] or grid[r][c] in cols[c] or grid[r][c] in sq[(r//3,c//3)]:
                    return False
                
                rows[r].add(grid[r][c])
                cols[c].add(grid[r][c])
                sq[(r//3,c//3)].add(grid[r][c])
                
        return True