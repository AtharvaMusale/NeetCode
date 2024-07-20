class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        atl , pac = set(), set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r,c, visit, prev):
            if r<0 or c<0 or r==ROWS or c == COLS or (r,c) in visit or grid[r][c]<prev:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,grid[r][c])
            dfs(r-1,c,visit,grid[r][c])
            dfs(r,c+1,visit,grid[r][c])
            dfs(r,c-1,visit,grid[r][c])

        
        for c in range(COLS):
            dfs(0,c,pac,grid[0][c])
            dfs(ROWS-1,c,atl,grid[ROWS-1][c])
            
        for r in range(ROWS):
            dfs(r,0,pac,grid[r][0])
            dfs(r,COLS-1,atl,grid[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])

        return res




























        # res = []
        # ROWS, COLS = len(heights), len(heights[0])
        # atl , pac = set(), set()
        # def dfs(r, c, visit, prev):
        #     if r<0 or c < 0 or r ==ROWS or c == COLS or (r,c) in visit or heights[r][c] <prev:
        #         return 
        #     visit.add((r,c))
        #     dfs(r+1, c, visit, heights[r][c])
        #     dfs(r-1, c, visit, heights[r][c])
        #     dfs(r, c+1, visit, heights[r][c])
        #     dfs(r,c-1, visit, heights[r][c])

        # for c in range(COLS):
        #     dfs(0, c, pac, heights[0][c])
        #     dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # for r in range(ROWS):
        #     dfs(r, 0, pac, heights[r][0])
        #     dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if (i,j) in atl and (i,j) in pac:
        #             res.append([i,j])
                
        # return res
                    



































        # ROWS, COLS = len(heights), len(heights[0])
        # pac, atl = set(), set()

        # def dfs(r, c, visit, prevHeight):
        #     if (
        #         (r, c) in visit
        #         or r < 0
        #         or c < 0
        #         or r == ROWS
        #         or c == COLS
        #         or heights[r][c] < prevHeight
        #     ):
        #         return
        #     visit.add((r, c))
        #     dfs(r + 1, c, visit, heights[r][c])
        #     dfs(r - 1, c, visit, heights[r][c])
        #     dfs(r, c + 1, visit, heights[r][c])
        #     dfs(r, c - 1, visit, heights[r][c])

        # for c in range(COLS):
        #     dfs(0, c, pac, heights[0][c])
        #     dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # for r in range(ROWS):
        #     dfs(r, 0, pac, heights[r][0])
        #     dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # res = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r, c) in pac and (r, c) in atl:
        #             res.append([r, c])
        # return res
