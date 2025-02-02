class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if preMap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs,pre in prerequisites:
            if not dfs(crs):
                return False
        return True