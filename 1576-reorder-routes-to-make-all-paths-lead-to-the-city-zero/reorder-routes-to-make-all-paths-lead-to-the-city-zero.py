class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Start at city 0
        # Recursively Check for neightbours
        # Count Outgoing Edges
        edges = {(a,b) for a,b in connections}
        neightbours = {city :[] for city in range(n)}
        visit = set()
        count = 0

        for a,b in connections:
            neightbours[a].append(b)
            neightbours[b].append(a)
        
        def dfs(city):
            nonlocal edges, neightbours, visit, count

            for neighbour in neightbours[city]:
                if neighbour in visit:
                    continue
                
                if (neighbour, city) not in edges:
                    count+=1
                
                visit.add(neighbour)
                dfs(neighbour)
        visit.add(0)
        dfs(0)
        return count

