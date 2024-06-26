class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         col = collections.defaultdict(set)
#         row = collections.defaultdict(set)
#         squares = collections.defaultdict(set)

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
                
#                 if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in squares[r//3,c//3]:
#                     return False
                
#                 row[r].add(board[r][c])
#                 col[c].add(board[r][c])
#                 squares[(r//3,c//3)].add(board[r][c])
            
#         return True

                




















# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for row in board:
#             if not is_valid_row(row):
#                 return False
# # Check columns
#         for j in range(9):
#             column = [board[i][j] for i in range(9)]
#             if not is_valid_row(column):
#                 return False

#         for i in range(0, 9, 3):
#             for j in range(0, 9, 3):
#                 sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
#                 if not is_valid_row(sub_box):
#                     return False

#         return True

# def is_valid_row(row):
#     row_arr = [False] * 9
#     for num in row:
#         if num != ".":
#             idx = int(num) - 1
#             if row_arr[idx]:
#                 return False
#             row_arr[idx] = True
#     return True






