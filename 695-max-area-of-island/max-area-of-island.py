class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def area(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == 0:
                return 0

            visit.add((r, c))
            return (1 +
                    area(r + 1, c) +
                    area(r - 1, c) +
                    area(r, c + 1) +
                    area(r, c - 1))

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    current_area = area(r, c)
                    max_area = max(max_area, current_area)

        return max_area
