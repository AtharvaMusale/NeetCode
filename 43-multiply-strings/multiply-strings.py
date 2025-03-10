# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         if num1 == "0" or num2 == "0":
#             return "0"
        
#         m, n = len(num1), len(num2)
#         result = (m + n) * [0]


#         for i in range(m):
#             for j in range(n):
#                 result[i + j] += int(num1[i]) * int(num2[j])
#                 result[i + j + 1] = result[i+j] // 10
#                 result[i+j] %= 10
        
#         while len(result)>1 and result[-1] == 0:
#             result.pop()
#         result.reverse()

#         return "".join(map(str,result))

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Prepare the result array.
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Reverse both numbers to ease the multiplication.
        num1, num2 = num1[::-1], num2[::-1]
        
        # Multiply each digit and add to the result.
        for i in range(m):
            for j in range(n):
                result[i + j] += int(num1[i]) * int(num2[j])
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        # Skip leading zeros and convert result to string.
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result.reverse()
        
        return ''.join(map(str, result))
