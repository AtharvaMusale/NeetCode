class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        vis =set()

        def dfs(i,j):
            if i<0 or i==rows or j<0 or  j==cols or grid[i][j] == 0 or (i,j) in vis:
                return 0
            vis.add((i,j))
            return 1+ dfs(i-1,j) + dfs(i+1,j) + dfs(i,j+1) + dfs(i,j-1)

        area = 0
        for i in range(rows):
            for j in range(cols):

                area = max(area,dfs(i,j))
        
        return area




# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         visit = set()

#         def dfs(i,j):
#             if i<0 or i==rows or j<0 or j==cols or grid[i][j]==0 or (i,j) in visit:
#                 return 0
            
#             visit.add((i,j))
#             return (1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1))

        

#         area = 0

#         for i in range(rows):
#             for j in range(cols):
#                 area = max(area,dfs(i,j))

#         return area











        # m, n = len(grid), len(grid[0])
        # dp = {}
        # vis = set()
        # def dfs(i, j):
        #     if i<0 or j< 0 or i>=m or j>=n or grid[i][j] != 1 or (i, j) in vis:
        #         return 0
        #     # if (i, j) is dp: 
        #     #     return dp[(i, j)]
        #     vis.add((i, j))
        #     maxArea = 1
        #     for r, c in[(0,1),(1,0),(0,-1),(-1,0)]:
        #         nr, nc = r+i, j+c
        #         maxArea += dfs(nr, nc)
        #     dp[(i, j)] = maxArea
        #     return maxArea
        # maxArea = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1 and grid[i][j] not in vis:
                   
        #             maxArea = max(maxArea, dfs(i, j))
        # return maxArea

                
        