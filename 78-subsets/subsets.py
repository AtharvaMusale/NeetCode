class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def backtracking(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtracking(i+1)

            subset.pop()
            backtracking(i+1)
        backtracking(0)
        return res

        
        




# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         curr = []
#         def dfs(i):
#             if i>=len(nums):
#                 res.append(curr.copy())
#                 return 
            
#             # For Left condtion of including the element:
#             curr.append(nums[i])
#             dfs(i+1)
        
#             # For the right side condition of not including the element:
#             curr.pop()
#             dfs(i+1)
        
#         dfs(0)
#         return res






























        # n = len(nums)
        # self.ans=set()
        # self.ans.add(tuple([]))
        # def backtrack(temp, i):              
        #     self.ans.add(tuple(temp))
        #     if i == n-1 :
        #         return 
        #     for j in range(i+1, n):
        #         backtrack(temp+[nums[j]], j)
        #     return
        # for j in range(0, n):
        #     backtrack([nums[j]], j)
        # return sorted(self.ans)

        