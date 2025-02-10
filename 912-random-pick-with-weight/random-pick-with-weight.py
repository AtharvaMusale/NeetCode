import random

class Solution:
    def __init__(self, w):
        self.cum_sum = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.cum_sum.append(current_sum)

    def pickIndex(self):
        # Generate a random number between 1 and the total sum of weights
        u = random.randint(1, self.cum_sum[-1])
        
        # Binary search for the smallest index j where cum_sum[j] >= u
        l, r = 0, len(self.cum_sum) - 1
        while l <= r:
            m = (l + r) // 2
            if self.cum_sum[m] >= u:
                r = m - 1
            else:
                l = m + 1
        return l

# Example of usage
# w = [1, 3, 2]  # Example weights
# obj = Solution(w)
# print(obj.pickIndex())  # Outputs an index, where index 1 has the highest probability of being picked
