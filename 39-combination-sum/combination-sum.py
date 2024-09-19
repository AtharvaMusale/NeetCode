class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = [] 

        def dfs(i,total):
            if total ==target:
                res.append(subset.copy())
                return
            
            if total>target or i>=len(candidates):
                return 

            # Include the current candidate and stay at the current index
            subset.append(candidates[i])
            dfs(i, total + candidates[i])
            subset.pop()

            # Exclude the current candidate and move to the next index
            dfs(i + 1, total)


        dfs(0,0)
        return res

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       
#         res = []
#         subset = []

#         def dfs(i, total):
#             if total == target:
#                 res.append(subset.copy())
#                 return
            
#             if i>= len(candidates) or total>target:
#                 return
#             subset.append(candidates[i])
#             dfs(i, total+ candidates[i])
#             subset.pop()

#             dfs(i+1, total)
        
#         dfs(0,0)
#         return res