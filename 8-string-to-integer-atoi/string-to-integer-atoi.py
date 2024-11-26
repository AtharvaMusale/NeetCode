class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result = 0
        index = 0
        n = len(s)
        sign = 1

        # Discard leading whitespaces
        while index < n and s[index] == ' ':
            index += 1

        # Check if the next character is a sign
        if index < n and (s[index] == '+' or s[index] == '-'):
            sign = 1 if s[index] == '+' else -1
            index += 1

        # Convert number and avoid overflow
        while index < n and s[index].isdigit():
            digit = int(s[index])
            # Check overflow and underflow conditions
            if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = 10 * result + digit
            index += 1

        return sign * result
