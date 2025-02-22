class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, curr):
        
            if i == len(nums):
                res.append(curr[:])
                return 
    
            # Recursive Exploration
            curr.append(nums[i])

            dfs(i+1, curr)

            # Check feasibility
            curr.pop()
            dfs(i+1,curr)

        dfs(0,[])
        return res
