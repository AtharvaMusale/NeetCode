class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addRooms(r,c):
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or grid[r][c]==-1:
                return 
            
            visit.add((r,c))
            q.append([r,c])
            



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
                
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                
                addRooms(r+1,c)
                addRooms(r-1,c)
                addRooms(r,c+1)
                addRooms(r,c-1)
            dist+=1




# from collections import deque
# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         Do not return anything, modify rooms in-place instead.
#         """
#         rows, cols = len(rooms), len(rooms[0])
#         q = deque()
#         visit = set()

#         def addRooms(r,c):
#             if r<0 or r==rows or c<0 or c==cols or (r,c) in visit or rooms[r][c] == -1:
#                 return
            
#             visit.add((r,c))
#             q.append([r,c])

#         for i in range(rows):
#             for j in range(cols):
#                 if rooms[i][j] == 0:
#                     q.append([i,j])
#                     visit.add((i,j))
            
#         dist = 0
#         while q:
#             for i in range(len(q)):
#                 r,c = q.popleft()
#                 rooms[r][c] = dist
#                 addRooms(r+1,c)
#                 addRooms(r-1,c)
#                 addRooms(r,c-1)
#                 addRooms(r,c+1)
#             dist+=1


# from collections import deque
# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> None:
#         """
#         Do not return anything, modify rooms in-place instead.
#         """
#         rows, cols = len(rooms), len(rooms[0])
#         q = deque()
#         visit = set()

#         def addRoom(r,c):
#             if r<0 or r==rows or c<0 or c==cols or (r,c) in visit or rooms[r][c]==-1:
#                 return 
            
#             visit.add((r,c))
#             q.append([r,c])

#         for i in range(rows):
#             for j in range(cols):
#                 if rooms[i][j] == 0:
#                     q.append([i,j])
#                     visit.add((i,j))


#         dist = 0
#         while q:
#             for i in range(len(q)):
#                 r,c = q.popleft()
#                 rooms[r][c] = dist
#                 addRoom(r+1,c)
#                 addRoom(r-1,c)
#                 addRoom(r,c+1)
#                 addRoom(r,c-1)
#             dist += 1
