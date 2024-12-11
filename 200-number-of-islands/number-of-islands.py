class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # horiz, vertically, edges surounded by water -  assume

        ROWS, COLS = len(grid), len(grid[0])
        # direct = [[-1,0],[1,0],[0,1],[0,-1]]
        island = 0
        # visit = set()
        def dfs(r,c):
            if r<0 or r >=ROWS or c<0 or c>=COLS or grid[r][c] == "0":
                return 

            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island+=1
        
        return island


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         visit = set()

#         def dfs(r, c):
#             # Boundary check and check if it is water or already visited
#             if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == "0":
#                 return

#             visit.add((r, c))
#             # Recursively call dfs in all four directions
#             dfs(r + 1, c)
#             dfs(r - 1, c)
#             dfs(r, c + 1)
#             dfs(r, c - 1)

#         island = 0
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     dfs(r, c)
#                     island += 1

#         return island
