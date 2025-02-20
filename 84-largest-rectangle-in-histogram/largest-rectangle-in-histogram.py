class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for ind, h in enumerate(heights):
            start = ind
            while stack and stack[-1][1] > h:
                stackInd, stackHeight = stack.pop()
                maxArea = max(maxArea, stackHeight * (ind-stackInd))
                start = stackInd
            stack.append((start,h))
        
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights)- i))
        return maxArea