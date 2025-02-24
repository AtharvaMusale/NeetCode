class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        for crs,pre in prereq:
            hashmap[crs].append(pre)
        
        output = []
        visit,cycle = set(),set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in hashmap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
            

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output