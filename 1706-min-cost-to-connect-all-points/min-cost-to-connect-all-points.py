class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {src:[] for src in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1,N):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        res = 0
        visit = set()
        minH = [[0,0]] # Cost , point
        while len(visit) < N:
            cost, i = heapq.heappop(minH)

            if i in visit:
                continue
            
            visit.add(i)
            res+=cost
        
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH,[neiCost,nei])
        return res
                

            

