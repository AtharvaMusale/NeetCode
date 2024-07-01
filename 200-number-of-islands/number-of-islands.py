class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vis = set()
        island = 0

        def dfs(i,j):
            for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
                xi , yi = i + x, j + y
                if (0<=xi<len(grid)) and (0<=yi<len(grid[0])) and (grid[xi][yi] == "1") and (xi,yi) not in vis:
                
                    vis.add((xi,yi))
                    dfs(xi,yi)

            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in vis:
                    island+=1
                    vis.add((i,j))
                    dfs(i,j)
        
        return island


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         vis = set()
#         cnt = 0

#         def dfs(i,j):
#             for (x,y) in [(1,0), (0,1), (-1,0), (0,-1)]:
#                 xi, yj = x+i, y+j
#                 if (0<=xi<len(grid) and 0<=yj<len(grid[0])) and grid[xi][yj] =="1" and (xi,yj) not in vis:
#                     if (xi,yj) not in vis:
#                         vis.add((xi,yj))
#                         dfs(xi,yj)


#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1" and (i,j) not in vis:
#                     cnt+=1
#                     vis.add((i,j))
#                     dfs(i,j)
        
#         return cnt














        # vis = set()
        # ones=[]
        # cnt=0
        # rows, cols = len(grid), len(grid[0])
      
        # def dfs(i,j):
        #     for (x, y) in [(0,1), (1,0), (0, -1), (-1,0)]:
        #         xi, yj =x+i, y+j
        #         if (0<=xi<rows and 0<=yj<cols) and grid[xi][yj] == "1" and (xi,yj) not in vis:
        #             vis.add((xi,yj))
        #             dfs(xi,yj)
        #     return


            
        # for i in range(len(grid)):
        #      for j in range(len(grid[0])):
        #          if grid[i][j] == "1" and (i,j) not in vis:
        #             vis.add((i,j))
        #             cnt+=1
        #             dfs(i,j)
        # return cnt
        