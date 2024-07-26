class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def helper(square):
            r = (square-1)//length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r,c]

        q = deque()
        q.append([1,0])
        visit = set()

        while q:
            square, moves = q.popleft()
            for i in range(1,7):
                newSquare = square+i
                r,c = helper(newSquare)

                if board[r][c] != -1:
                    newSquare = board[r][c]
                if newSquare == length * length:
                    return moves+1
                
                if newSquare not in visit:
                    visit.add(newSquare)
                    q.append([newSquare, moves+1])
        return -1


