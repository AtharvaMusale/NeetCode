class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 empty, 1 orange 2 rotten
        ROWS, COLS = len(grid), len(grid[0])
        # direction = 
        q = collections.deque()

        time = 0    
        fresh = 0

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        while q and fresh>0:
            n = len(q)
            for i in range(n):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = r+dr, c+dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:

                        fresh-=1
                        q.append((row,col))
                        grid[row][col] = 2
                    
            time+=1
        return time if fresh==0 else -1

