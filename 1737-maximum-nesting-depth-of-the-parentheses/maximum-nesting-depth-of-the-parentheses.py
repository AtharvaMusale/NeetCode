# class Solution:
#     def maxDepth(self, s: str) -> int:
#         stack = []
#         count = 0
#         for i in s:
#             if i == "(":
#                 stack.append(i)
#             elif i == ")":
#                 stack.pop()
#             else:
#                 continue
#             count = max(count,len(stack))
#         return count

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_depth = 0
        for i in s:
            if i == "(":
                count += 1
                
            elif i == ")":
                count -= 1
            max_depth = max(max_depth, count)        
        return max_depth
