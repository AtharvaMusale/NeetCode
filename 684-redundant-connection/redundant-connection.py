class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        for src, dest in edges:
            hashmap[src].append(dest)
            hashmap[dest].append(src)
        
        visit = [False] * (len(edges) + 1)
        cycleStart = -1
        cycle = set()
        def dfs(node,parent):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for nei in hashmap[node]:
                if nei == parent:
                    continue
                
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1,-1)

        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
            
        return []
            

            