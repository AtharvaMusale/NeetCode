class Solution:
    def maximumSwap(self, num: int) -> int:
        swap_i, swap_j = -1, -1
        max_i, max_digit = -1, "0" 
        num = list(str(num))

        for i in reversed(range(len(num))):
            if num[i] > max_digit:
                max_i = i
                max_digit = num[i]
            
            elif num[i] < max_digit:
                swap_i, swap_j = i, max_i

        if swap_i!=-1:
            num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
            
        return int("".join(num))
