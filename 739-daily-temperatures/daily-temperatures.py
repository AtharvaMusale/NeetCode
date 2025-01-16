class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [73,74,74,71,69,72,76,73]
        stack = []
        res = [0] * len(temperatures)

        for i,val in enumerate(temperatures):
            while stack and val> stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            
            stack.append((val,i))
        
        return res