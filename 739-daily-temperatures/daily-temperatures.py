class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        res = [0] * len(t)

        for ind, val in enumerate(t):
            while stack and stack[-1][0] < val:
                stackVal, stackInd = stack.pop()
                res[stackInd] = ind - stackInd
            
            stack.append((val, ind))

        return res
