class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        hashmap = defaultdict(list)

        for crs,pre in prereq:
            hashmap[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False

            if hashmap[crs] == []:
                return True
            
            visit.add(crs)

            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            hashmap[crs] = []
            return True
            
         
            
        for crs,pre in prereq:
            if not dfs(crs):
                return False
        return True
        
