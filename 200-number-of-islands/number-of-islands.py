# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         island = 0
#         directions = [[-1,0],[1,0],[0,1],[0,-1]]
#         visit = set()

#         if not grid or not grid[0]:  # Checks for an empty grid or empty rows.
#             return 0

#         def bfs(r,c):
#             q = deque()
#             visit.add((r,c))
#             q.append((r,c))

#             while q:
#                 row, col = q.popleft()
#                 for dr,dc in directions:
#                     nr, nc = row + dr, col + dc
#                     if nr<0 or nr >= ROWS or nc<0 or nc>=COLS or (nr,nc) in visit or grid[nr][nc] == "0":
#                         continue 
#                     q.append((nr,nc))
#                     visit.add((nr,nc))


#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1":
#                     bfs(r,c)
#                     island+=1
                
#         return island



from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:  # Correctly checks for an empty grid or empty rows.
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visit = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        visit.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    island += 1
                
        return island
