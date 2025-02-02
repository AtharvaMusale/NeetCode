class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            for c in range(r,n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for i in range(n):
            matrix[i].reverse()