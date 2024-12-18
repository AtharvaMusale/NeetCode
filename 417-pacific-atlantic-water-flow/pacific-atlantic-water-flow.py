class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        res = []


        def dfs(r,c, visit, prevHeight):
            if r < 0 or r == ROWS or c<0 or c == COLS or (r,c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        res = []

        # def dfs(r,c,visit,prevH):
        #     if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in visit or heights[r][c] < prevH:
        #         return 
        #     visit.add((r,c))
        #     dfs(r+1,c,visit, prevH)
        #     dfs(r-1,c,visit, prevH)
        #     dfs(r,c+1,visit, prevH)
        #     dfs(r,c-1,visit, prevH)


        # for c in range(COLS):
        #     dfs(0,c,pac,heights[0][c])
        #     dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        # for r in range(ROWS):
        #     dfs(r,0,pac,heights[r][0])
        #     dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r,c) in pac and (r,c) in atl:
        #             res.append([r,c])
        
        # return res