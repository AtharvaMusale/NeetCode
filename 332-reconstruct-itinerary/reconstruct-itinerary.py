# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adj = {src:[] for src, des in tickets}
#         tickets.sort()

#         for src,des in tickets:
#             adj[src].append(des)
        
#         res = ["JFK"]
#         def dfs(src):
#             if len(res) == len(tickets)+1:
#                 return True
            
#             if src not in adj:
#                 return False
            
#             temp = list(adj[src])
#             for i,v in enumerate(adj[src]):
#                 adj[src].append(i)
#                 res.append(v)
#                 if dfs(temp):
#                     return True
                
#                 adj[src].remove(i)
#                 res.pop()
#             return False
#         dfs("JFK")
#         return res


        
        
from collections import defaultdict, deque
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(deque)
        for src, des in sorted(tickets):
            adj[src].append(des)
        
        res = []
        def dfs(src):
            while adj[src]:
                next_dest = adj[src].popleft()
                dfs(next_dest)
            res.append(src)

        dfs("JFK")
        return res[::-1]

# Example usage:
# solution = Solution()
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# print(solution.findItinerary(tickets))  # Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
