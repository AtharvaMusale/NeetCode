class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)


        def is_out_of_bounds(r,c):
            return r<0 or r>=N or c<0 or c >= N 

        #  Precompute Areas
        def dfs(r,c,label):
            if is_out_of_bounds(r,c) or grid[r][c] != 1:
                return 0
            grid[r][c] = label
            size = 1
            nei = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in nei:
                nr = r + dr
                nc = c + dc
                size += dfs(nr,nc,label)
            return size


        def connect(r,c):
            nei = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            visit = set()
            res = 1
            for nr, nc in nei:
                if not is_out_of_bounds(nr,nc) and grid[nr][nc] not in visit:
                    res+= size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return res




        label = 2
        size = defaultdict(int)
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    size[label] = dfs(r,c,label)
                    label+=1
        
        # If grid is already fully occupied by an island, return N*N
        if max(size.values(), default=0) == N * N:
            return N * N


        # 2. Flipping the Water
        res = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    res = max(res, connect(r,c))
        return res