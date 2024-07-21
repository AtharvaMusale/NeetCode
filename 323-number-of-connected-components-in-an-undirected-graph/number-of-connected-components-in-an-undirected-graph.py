from typing import List

class Solution:
    def dfs(self, adj_list: List[List[int]], visited: List[int], start_node: int):
        visited[start_node] = 1
        
        for neighbor in adj_list[start_node]:
            if visited[neighbor] == 0:
                self.dfs(adj_list, visited, neighbor)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visited = [0] * n
        
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        for i in range(n):
            if visited[i] == 0:
                components += 1
                self.dfs(adj_list, visited, i)
        
        return components
