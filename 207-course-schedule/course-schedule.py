class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
     

        preMap = {i: [] for i in range(numCourses)}
        visit = set()      
        for crs, prq in prerequisites:
            preMap[crs].append(prq)
        
        def dfs(crs):

            if crs in visit:
                return False

            elif preMap[crs] == []:
                return True

            
            visit.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visit.remove(crs)
            preMap[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True