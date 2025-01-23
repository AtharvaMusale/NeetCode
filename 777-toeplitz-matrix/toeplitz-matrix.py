class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS-1):
            for c in range(COLS-1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
                
        return True