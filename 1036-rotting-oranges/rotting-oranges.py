class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
            
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh>0:
            length = len(q)
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row in range(ROWS)) and (col in range(COLS)) and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append([row,col])
            time+=1
        return time if fresh == 0 else -1






        # q = deque()
        # fresh = 0
        # time = 0

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             fresh+=1
                
        #         if grid[i][j] == 2:
        #             q.append((i,j))
                
        # directions = [[1,0],[0,1],[-1,0],[0,-1]]

        # while q and fresh>0:
        #     length= len(q)
        #     for i in range(length):
        #         r,c = q.popleft()
        #         for dr, dc in directions:
        #             row = r+dr
        #             col = c+dc
        #             if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
        #                 grid[row][col] = 2
        #                 fresh -= 1
        #                 q.append((row,col))
        #     time+=1
        
        # return time if fresh == 0 else -1
























        # q = []
        # oranges =0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] != 0:
        #             oranges+=1
        #             if grid[i][j] == 2:
        #                 q.append((i, j, 0))
        #                 oranges -=1
        # vis=[]    
        # maxtime = 0   
        # while(q):
        #     row, col, time = q.pop(0)
            
        #     print(row, col, time)
        #     for i, j in ((0,1),(1,0),(0,-1),(-1,0)):
        #         nr, nc = row+i, col+j
        #         if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 1:
        #             grid[nr][nc] = 2
        #             q.append((nr,nc,time+1))
        #             maxtime=max(maxtime, time+1)
        #             oranges -= 1
        # return maxtime if oranges == 0 else -1



