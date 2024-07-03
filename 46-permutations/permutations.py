class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums)== 1:
            return [nums[:]]    
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res



# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         if len(nums)== 1:
#             return [nums[:]]     
#         for i in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)
#             for perm in perms:
#                 perm.append(n)
#             res.extend(perms)
#             nums.append(n)
#         return res

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         if len(nums)== 1:
#             return [nums[:]]    
#         for i in range(len(nums)):
#             n = nums.pop(0)
#             perms = self.permute(nums)
#             for perm in perms:
#                 perm.append(n)
#             res.extend(perms)
#             nums.append(n)
#         return res










        # class Solution:
#     def __init__(self):
#         self.result = []
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         vis = set()
#         curr = []

#         self.solve(curr, vis, nums)

#         return self.result

#     def solve(self, curr, vis, nums):
#         if len(curr) == len(nums):
#             self.result.append(curr.copy())
#             return
        
#         for i in range(len(nums)):
#             if i not in vis:
#                 curr.append(nums[i])
#                 vis.add(i)
#                 self.solve(curr, vis, nums)
#                 curr.pop()
#                 vis.remove(i)
        

