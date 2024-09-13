# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         ROW, COL = len(matrix), len(matrix[0])
#         top, bot = 0, ROW-1
#         while top <= bot:
#             row = (top + bot) // 2
#             if target > matrix[row][-1]:
#                 top = row + 1

#             elif target < matrix[row][0]:
#                 bot = row - 1
            
#             else:
#                 break
            
        
#         if not (top <= bot):
#             return False
        

#         row = (top + bot)//2
#         l, r = 0 , COL-1
#         while l<=r:
#             mid = (l+r)//2
#             if target > matrix[row][mid]:
#                 l = mid +1
            
#             elif target < matrix[row][mid]:
#                 r = mid - 1
            
#             else:
#                 return True
        
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search in a "virtual" 1D list of the matrix
        left, right = 0, ROWS * COLS - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // COLS][mid % COLS]  # Map mid to the actual matrix element

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
