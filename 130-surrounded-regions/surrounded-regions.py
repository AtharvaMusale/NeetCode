class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        ROWS, COLS = len(grid),len(grid[0])

        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]!="O":
                return 
            grid[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "O" and r in [0,ROWS-1] or c in [0,COLS-1]:
                    dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="O":
                    grid[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="T":
                    grid[r][c] = "O"




