# class Solution:
#     def dailyTemperatures(self, t: List[int]) -> List[int]:
#         stack = []
#         res = [0] * len(t)

#         for ind, val in enumerate(t):
#             while stack and stack[-1][0] < val:
#                 stackVal, stackInd = stack.pop()
#                 res[stackInd] = ind - stackInd
            
#             stack.append((val, ind))

#         return res


class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        answer = [0] * n
        stack = []  # This will store indices of t in decreasing order

        for i, temp in enumerate(t):
            # Check if the current temperature is warmer than the one at the top of the stack
            while stack and t[stack[-1]] < temp:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index  # Calculate the number of days
            stack.append(i)  # Push the current index onto the stack
        
        return answer
