class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ROWS, COLS = len(grid), len(grid[0])
        # visit = set()
        # directions = [[-1,0],[1,0],[0,-1],[0,1]]

        # def bfs(r,c):
        #     q = collections.deque()
        #     visit.add((r,c))
        #     q.append((r,c))

        #     while q:
        #         row,col = q.popleft()
        #         for dr, dc in directions:
        #             nr, nc = row+ dr, col + dc
        #             if not (nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visit or grid[nr][nc] == "0"):
        #                 q.append((nr,nc))
        #                 visit.add((nr,nc))



        # island = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1" and (r,c) not in visit:
        #             bfs(r,c)
        #             island += 1
                    
        
        # return island


        # Using DFS

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        island = 0

        def dfs(r,c):
            if r< 0 or r >= ROWS or c<0 or c >= COLS or (r,c) in visit or grid[r][c] == "0":
                return 

            visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

            return


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    island+=1
                    dfs(r,c)
        
        return island
