class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix),  len(matrix[0])
        l, r = 0, m*n -1

        while l<=r:
            mid = (l+r)//2
            row, col = mid // n, mid % n
            
            if matrix[row][col] == target:
                return True
            
            elif target < matrix[row][col]:
                r = mid-1
            
            else:
                l = mid+1
            
        return False


        # m, n = len(matrix), len(matrix[0])

        # lo , hi = 0, m*n -1

        # while lo <= hi:
        #     mid = lo+(hi-lo)//2
        #     row, col = mid//n, mid%n
            
        #     if matrix[row][col] == target:
        #         return True
        #     elif  target < matrix[row][col]:
        #         hi = mid-1
        #     else:
        #         lo = mid +1
        # return False

