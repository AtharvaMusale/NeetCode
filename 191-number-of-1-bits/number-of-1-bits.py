from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # Clear the least significant '1' bit
            count += 1
        return count
