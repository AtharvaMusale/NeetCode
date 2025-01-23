class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         ROWS, COLS = len(matrix), len(matrix[0])

#         for r in range(ROWS-1):
#             for c in range(COLS-1):
#                 if matrix[r][c] != matrix[r+1][c+1]:
#                     return False
                
#         return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        # Function to check if all elements in a diagonal starting from (start_row, start_col) are the same
        def checkDiagonal(start_row, start_col):
            val = matrix[start_row][start_col]
            i, j = start_row, start_col
            while i < rows and j < columns:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1
            return True
        
        # Check all diagonals starting from the first column
        for row in range(rows):
            if not checkDiagonal(row, 0):
                return False
        
        # Check all diagonals starting from the first row (excluding the first element, already checked)
        for col in range(1, columns):
            if not checkDiagonal(0, col):
                return False

        return True
