# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if len(grid) ==0:
#             return 0 
#         vis = set()
#         island = 0
#         def dfs(i,j):
#             for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
#                 xi, yj = x + i, y + j
#                 if 0<=xi<len(grid) and 0<=yj<len(grid[0]) and grid[i][j] == "1" and (xi,yj) not in vis:
#                     vis.add((xi,yj))
#                     dfs(xi,yj)
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1" and (i,j) not in vis:
#                     island+=1
#                     vis.add((i,j))
#                     dfs(i,j)
#         return island

        # vis = set()
        # island = 0

        # def dfs(i,j):
        #     for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
        #         xi , yi = i + x, j + y
        #         if (0<=xi<len(grid)) and (0<=yi<len(grid[0])) and (grid[xi][yi] == "1") and (xi,yi) not in vis:
                
        #             vis.add((xi,yi))
        #             dfs(xi,yi)

            
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == "1" and (i,j) not in vis:
        #             island+=1
        #             vis.add((i,j))
        #             dfs(i,j)
        
        # return island


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
        









class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        island = 0
        boundary = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(x,y):

            if (x<0 or y<0 or x>=ROWS or y>= COLS or grid[x][y]== "0" or (x,y) in visit):
                return 

            visit.add((x,y))
            
            for i,j in boundary:
                xi = x + i
                yj = y +j

                dfs(xi,yj)
            pass
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in visit:
                    island+=1
                    dfs(i,j)
                
        return island


























