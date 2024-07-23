# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         dp = {}
#         def dfs(i,j):
#             if j == len(t):
#                 return 1
#             if i == len(s):
#                 return 0

#             if (i,j) in dp:
#                 return dp[(i,j)]

#             if s[i]==t[j]:
#                 dp[(i,j)] = dfs(i+1,j+1) + dfs(i+i,j)
#             else:
#                 dp[(i,j)] =  dfs(i+i,j)
#             return dp[(i,j)]

#         return dfs(0,0)
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         dp = {}

#         def dfs(i, j):
#             if j == len(t):
#                 return 1
#             if i == len(s):
#                 return 0

#             if (i, j) in dp:
#                 return dp[(i, j)]

#             if s[i] == t[j]:
#                 dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
#             else:
#                 dp[(i, j)] = dfs(i + 1, j)
            
#             return dp[(i, j)]

#         return dfs(0, 0)
            

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0, 0)]

        # dp = {}
        # m, n = len(s), len(t)
        # def findString(i, j):
        #     if (i, j) in dp: return dp[(i, j)]
        #     if j >= n:
        #         return 1 # complted entire t 
        #     if i>=m :
        #         return 0
        #     if s[i] == t[j]:
        #         dp[(i,j)] = findString(i+1, j+1)+ findString(i+1, j) # conside s[i] as match and move ahead to match next char in t or try to find another match to t[j] in s[i+1:]
        #     else:
        #         dp[(i,j)]=  findString(i+1, j)
        #     return dp[(i,j)]
        # return findString(0,0)
        


        