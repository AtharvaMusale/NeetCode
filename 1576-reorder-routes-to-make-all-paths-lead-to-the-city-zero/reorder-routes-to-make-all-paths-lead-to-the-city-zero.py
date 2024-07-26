# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         # Start at city 0
#         # Recursively Check for neightbours
#         # Count Outgoing Edges
#         edges = {(a,b) for a,b in connections}
#         neightbours = {city :[] for city in range(n)}
#         visit = set()
#         count = 0

#         for a,b in connections:
#             neightbours[a].append(b)
#             neightbours[b].append(a)
        
#         def dfs(city):
#             nonlocal edges, neightbours, visit, count

#             for neighbour in neightbours[city]:
#                 if neighbour in visit:
#                     continue
                
#                 if (neighbour, city) not in edges:
#                     count+=1
                
#                 visit.add(neighbour)
#                 dfs(neighbour)
#         visit.add(0)
#         dfs(0)
#         return count

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Create a set of edges for quick lookup
        edges = {(a, b) for a, b in connections}
        # Create an adjacency list for the graph
        neighbours = [[] for _ in range(n)]
        
        for a, b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        visit = set([0])  # Start by visiting city 0
        count = 0
        
        def dfs(city):
            nonlocal count
            
            for neighbour in neighbours[city]:
                if neighbour not in visit:
                    if (neighbour, city) not in edges:
                        count += 1
                    visit.add(neighbour)
                    dfs(neighbour)
        
        dfs(0)
        return count
