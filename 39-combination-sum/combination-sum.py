class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >=len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
        
        dfs(0,[],0)
        return res










# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []

#         def dfs(i,curr,total):
#             if total == target:
#                 res.append(curr.copy())
#                 return 
#             if i>=len(candidates) or total > target:
#                 return 
 
#             curr.append(candidates[i])
#             dfs(i,curr,total+candidates[i])
#             curr.pop()
#             dfs(i+1,curr,total)
        
#         dfs(0,[],0)
#         return res



        # n = len(candidates)
        # self.ans = set()
        # def backtrack(idx, target, curr):
        #     if target == 0:
        #         self.ans.add(tuple(curr))
        #         return
        #     if idx >= n:
        #         return
        #     if target < 0:
        #         return 
        #     pick = backtrack(idx, target-candidates[idx], curr+[candidates[idx]])
        #     notPick = backtrack(idx+1, target, curr)
        #     return
        # backtrack(0, target, [])
        # return self.ans
    

        