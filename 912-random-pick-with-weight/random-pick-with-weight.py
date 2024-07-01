import random

class Solution:
    def __init__(self, w):
        self.prefix_sum = []
        self.w = w
        self.sum = 0
        for wt in w:
            self.sum += wt
            self.prefix_sum.append(self.sum)

    def pickIndex(self):
        target = self.sum * random.random()
        print(target)
        return self.search(target)

    def search(self, num):
        low, high, ans = 0, len(self.prefix_sum) - 1, None

        while low <= high:
            mid = low + (high - low) // 2
            if num < self.prefix_sum[mid]:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

# Example usage:
# w = [3, 17, 18, 25]
# obj = Solution(w)
# param_1 = obj.pick_index()
# print(param_1)
