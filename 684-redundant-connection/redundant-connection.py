from typing import List
import collections

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        
        def dfs(s, t):
            stack = [s]
            visit = set()
            while stack:
                node = stack.pop()
                if node == t:
                    return True
                if node not in visit:
                    visit.add(node)
                    stack.extend(graph[node] - visit)
            return False
        
        for u, v in edges:
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)

# Example usage:
# sol = Solution()
# print(sol.findRedundantConnection([[1,2], [1,3], [2,3]]))  # Output: [2, 3]
