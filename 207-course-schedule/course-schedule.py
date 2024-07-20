class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap ={i:[] for i in range(numCourses)}
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

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True








        preMap = {i:[] for i in range(numCourses)}

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
        
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False

        # return True

        # preMap = {i:[] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)
        
        # visit = set()
        # def dfs(crs):

        #     if crs in visit:
        #         return False

        #     if preMap[crs] == []:
        #         return True
            
        #     visit.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
            
        #     visit.remove(crs)
        #     preMap[crs] = []
        #     return True
        
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        
        # return True

























        # if len(prerequisites) == 0: return True
        # indegree=[0] * numCourses
        # starts = []
        # graph = DefaultDict(list)
        # for p in prerequisites:
        #     indegree[p[0]] +=1
        #     graph[p[1]]+=[p[0]]
        # q = []
        # for i in range(len(indegree)):
        #     if indegree[i] == 0:
        #         q.append(i)
        # vis = 0
      
                
        # while len(q)> 0:
        #     top = q.pop(0)
        #     vis+=1
        #     for n in graph[top]:
        #         indegree[n] -=1
        #         if indegree[n] == 0:
        #             q.append(n)
        # return vis == numCourses
