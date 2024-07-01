
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        n1 , n2 = len(self.nums), len(vec.nums)
        res = 0
        if n1!=n2:
            return 0

        for i in range(len(self.nums)):
            if self.nums[i] !=0 and vec.nums[i]!=0:
                res += self.nums[i] * vec.nums[i]
        
        return res



# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         n1,n2 = len(self.nums),len(vec.nums)
#         result = 0
#         if n1!=n2:
#             return 0
#         for i in range(len(self.nums)):
#             if self.nums[i] !=0 and vec.nums[i]!=0:
#                 result += self.nums[i] * vec.nums[i]
        
#         return result
