class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)  # Result array of the same length as temp, initialized with 0s
        stack = []  # Stack to store indices of temp array

        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                index = stack.pop()
                res[index] = i - index  # Calculate the number of days until a warmer temperature
            stack.append(i)  # Push current day's index onto the stack

        return res
