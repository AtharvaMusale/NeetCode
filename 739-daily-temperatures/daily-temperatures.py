class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []  # Stack will hold tuples (temperature, index)
        res = [0] * len(t)  # Initialize result list with all 0s

        for i, current_temp in enumerate(t):
            # Check for temperatures that are less than the current temperature
            while stack and stack[-1][0] < current_temp:
                stackTemp, stackInd = stack.pop()  # Pop the temperature and index
                res[stackInd] = i - stackInd  # Calculate the number of days
            stack.append((current_temp, i))  # Push current temperature and index onto stack
        
        return res
