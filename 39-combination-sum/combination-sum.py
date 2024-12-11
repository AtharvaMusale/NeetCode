class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #  distinct, list unique comb, any order, same number can be chosen any no of times

        res = []
        subset = []

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i>=len(nums) or total>target:
                return
            
            curr.append(nums[i])
            backtrack(i, curr, total+ nums[i])
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0,[],0)

        return res
            
