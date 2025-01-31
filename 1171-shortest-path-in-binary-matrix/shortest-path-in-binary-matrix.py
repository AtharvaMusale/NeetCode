class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0,1)])
        visit = set((0,0))
        directions = [[1,0],[0,1],[-1,0],[0,-1],\
                        [1,1],[1,-1],[-1,1],[-1,-1]]
        while q:
            r, c, length = q.popleft()

            if r<0 or c<0 or r>=N or c>=N or grid[r][c] == 1:
                continue
            if r == N-1 and c == N-1:
                return length
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr,nc) not in visit:
                    q.append((nr,nc,length+1))
                    visit.add((nr,nc))

        return -1
